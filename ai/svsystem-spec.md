# AV Equipment Management System — Technical Specification

## 1. System Overview

A hybrid cloud/on-premises system for remotely managing audio-visual equipment across ~140 meeting rooms in a multi-floor building. Engineers can monitor device status, perform power cycles, schedule firmware upgrades, and view meeting room schedules from a centralized dashboard.

### 1.1 Scope

- **Rooms**: ~140 meeting rooms across multiple buildings/floors
- **Devices per room**: ~7 (WattBox, Atlona, Neat Bar, Neat Pad, Shure microphones, Scheduler panel, PoE switch port mapping)
- **Total managed endpoints**: ~980+ AV devices + N Cisco switches
- **Users**: Engineering/IT staff (authenticated via SSO/OIDC)

### 1.2 Key Capabilities

1. **Real-time device status monitoring** — online/offline, firmware version, errors
2. **Remote power cycling** — WattBox outlets, Cisco PoE ports
3. **Firmware management** — version tracking, scheduled upgrades, bulk operations
4. **Meeting awareness** — current/next meeting from Exchange, room utilization
5. **Action queue** — async execution of reboot, upgrade, power cycle with audit trail
6. **Floor map visualization** — hierarchical building/floor/room view with status indicators
7. **Bulk operations** — mass power cycle, upgrade scheduling across rooms/floors

---

## 2. Architecture

### 2.1 High-Level Architecture

```
┌──────────────────────────────────────────────────────────────┐
│                      CLOUD LAYER                              │
│  ┌────────────┐  ┌───────────┐  ┌──────────┐  ┌───────────┐ │
│  │ Svelte UI  │  │ Go API    │  │ Postgres │  │ Redis     │ │
│  │ (Dashboard)│←→│ Server    │←→│          │←→│ (PubSub)  │ │
│  └────────────┘  └───────────┘  └──────────┘  └─────┬─────┘ │
└──────────────────────────────────────────────────────┼───────┘
                                                       │ WSS
┌──────────────────────────────────────────────────────┼───────┐
│                  ON-PREM GATEWAY AGENT(S)              │       │
│  ┌────────────────────────────────────────────┐       │       │
│  │              Go Gateway Agent              │       │       │
│  │  ┌──────────┐ ┌─────────┐ ┌───────────┐  │       │       │
│  │  │ WattBox  │ │ Atlona  │ │ Shure     │  │       │       │
│  │  │ Driver   │ │ Driver  │ │ Driver    │  │       │       │
│  │  └──────────┘ └─────────┘ └───────────┘  │       │       │
│  │  ┌────────────────────────────────────┐   │       │       │
│  │  │ Neat Driver (Pulse Cloud + Local)  │   │       │       │
│  │  └────────────────────────────────────┘   │       │       │
│  │  ┌────────────────────────────────────┐   │       │       │
│  │  │ Cisco PoE Driver (Direct + CC)     │   │       │       │
│  │  └────────────────────────────────────┘   │       │       │
│  │  ┌────────────────────────────────────┐   │       │       │
│  │  │ MS Graph API Client (Exchange)     │   │       │       │
│  │  └────────────────────────────────────┘   │       │       │
│  └────────────────────────────────────────────┘       │       │
└───────────────────────────────────────────────────────┘       │
```

### 2.2 Component Responsibilities

| Component | Location | Technology | Responsibility |
|---|---|---|---|
| **Go API Server** | Cloud | Go 1.22+, chi router | REST API, auth, business logic, WebSocket hub |
| **Svelte Dashboard** | Cloud (served by API) | Svelte 5, TypeScript, Tailwind | Admin UI, real-time updates, floor maps |
| **PostgreSQL** | Cloud | PostgreSQL 16 | Persistent data store |
| **Redis** | Cloud | Redis 7 | Pub/Sub for real-time events, caching |
| **Gateway Agent** | On-prem | Go 1.22+ | Device communication, polling, action execution |
| **Device Drivers** | On-prem (in gateway) | Go packages | Protocol-specific communication with each device type |

### 2.3 Communication Patterns

- **Gateway ↔ Cloud**: Persistent WebSocket connection. Gateway pushes status updates, action results. Cloud sends action commands, config changes.
- **Cloud ↔ Svelte UI**: WebSocket for real-time status. REST API for CRUD operations.
- **Gateway ↔ Devices**: Direct network connections (HTTP, Telnet, SSH, REST, TCP) on the local AV network.
- **Gateway ↔ Cloud APIs**: HTTPS outbound to Neat Pulse, MS Graph, Catalyst Center.

---

## 3. Device Driver Specifications

### 3.1 SnapAV WattBox

**Protocols**: HTTP (primary), SSH, Telnet (fallback)

**Capabilities**:
- Per-outlet power cycle (on/off with configurable delay)
- Outlet status (on/off, energy consumption)
- Device health (uptime, firmware, network status)
- Sensor data (if WattBox model has sensors)

**HTTP Endpoints** (typical WattBox REST):
- `GET /restapi/feedback.xml` — Full device state (outlets, sensors, firmware)
- `POST /restapi/setoutlet.xml` — Control individual outlets
- `GET /restapi/status.xml` — Device status

**SSH/Telnet**: Fallback for models without full REST API. Command-based interface for outlet control.

**Driver Interface**:
```go
type WattBoxDriver struct {
    ip       string
    username string
    password string
    protocol string // "http", "ssh", "telnet"
}

func (d *WattBoxDriver) GetStatus(ctx context.Context) (*DeviceStatus, error)
func (d *WattBoxDriver) PowerCycleOutlet(ctx context.Context, outlet int, delaySec int) error
func (d *WattBoxDriver) SetOutlet(ctx context.Context, outlet int, on bool) error
func (d *WattBoxDriver) GetFirmwareVersion(ctx context.Context) (string, error)
```

### 3.2 Atlona Switcher

**Protocols**: Telnet (port 23), SSH, HTTP (WebGUI), JSON over WebSockets (newer OME-series)

**Capabilities**:
- Input/output routing (switch sources)
- Display power control (via RS-232 passthrough, CEC, or IP)
- EDID management
- Device power on/off
- Firmware update
- System status

**Telnet/SSH Command Format**: Text-based, carriage-return terminated. Commands vary by model. Example:
- `Input1` — Switch to input 1
- `PowerOn` / `PowerOff` — Device power
- `DispOn` / `DispOff` — Display power control
- `sta` — Status query

**JSON over WebSockets** (OME-series):
- Structured commands via WebSocket connection
- API methods documented in Atlona Velocity SDK

**Driver Interface**:
```go
type AtlonaDriver struct {
    ip       string
    port     int
    model    string // e.g., "AT-UHD-CLSO-601", "AT-OME-CS31-SA-HDBT"
    protocol string // "telnet", "ssh", "websocket"
    conn     net.Conn
}

func (d *AtlonaDriver) GetStatus(ctx context.Context) (*DeviceStatus, error)
func (d *AtlonaDriver) SwitchInput(ctx context.Context, input int) error
func (d *AtlonaDriver) PowerOn(ctx context.Context) error
func (d *AtlonaDriver) PowerOff(ctx context.Context) error
func (d *AtlonaDriver) ControlDisplay(ctx context.Context, cmd string) error
func (d *AtlonaDriver) GetFirmwareVersion(ctx context.Context) (string, error)
func (d *AtlonaDriver) GetEDID(ctx context.Context) ([]byte, error)
```

### 3.3 Neat Devices (Bar, Pad, Board, Frame, Center)

**Primary**: Neat Pulse Cloud REST API (`https://api.pulse.neat.no/v1`)
**Fallback**: Local IP access (HTTP, when enabled on device)

**Device Type Registry**:

| Type | API Model | Key Settings | Reboot via Pulse | Local IP Fallback |
|---|---|---|---|---|
| Neat Bar / Bar 2 | `bar` | Camera framing, audio, display output | `POST /endpoints/{id}/reboot` | Limited |
| Neat Bar Pro | `bar_pro` | Same as Bar + additional camera settings | Yes | Limited |
| Neat Pad | `pad` | Scheduler display, room info | Yes | Yes |
| Neat Board / Board 50 | `board` | Touch settings, display | Yes | Yes |
| Neat Board Pro | `board_pro` | Same as Board + advanced | Yes | Yes |
| Neat Frame | `frame` | Display mode (personal/hotdesk/virtual) | Yes | Yes |
| Neat Center | `center` | Compute unit settings | Yes | Limited |

**Neat Pulse API Endpoints** (Bearer token auth):
- `GET /v1/orgs/{orgid}/endpoints` — List all endpoints
- `GET /v1/orgs/{orgid}/endpoints/{id}` — Get endpoint details
- `POST /v1/orgs/{orgid}/endpoints/{id}/reboot` — Reboot device
- `POST /v1/orgs/{orgid}/endpoints/{id}/config` — Apply config
- `POST /v1/orgs/{orgid}/endpoints/{id}/config/remote_access` — Enable local IP access
- `GET /v1/orgs/{orgid}/endpoints/{id}/sensorData` — Sensor data (temp, air quality, people count)
- `GET /v1/orgs/{orgid}/firmwareUpdates/endpoints/{id}` — Firmware update status
- `POST /v1/orgs/{orgid}/firmwareUpdates/endpoints/{id}` — Trigger firmware update
- `POST /v1/orgs/{orgid}/endpoints/{id}/factoryReset` — Factory reset
- `GET /v1/orgs/{orgid}/rooms` — List rooms
- `GET /v1/orgs/{orgid}/rooms/{id}/sensorData` — Room-level sensor data

**Local IP Access** (when enabled):
- HTTP web interface on device IP
- Limited compared to Pulse API — basic health, reboot trigger

**Driver Interface**:
```go
type NeatDriver struct {
    pulseClient    *PulseClient    // Cloud API client
    localIP        string          // Fallback local IP
    localEnabled   bool            // Whether local access is enabled
    deviceType     string          // "bar", "pad", "board", "frame", "center"
    endpointID     string          // Neat Pulse endpoint ID
    orgID          string          // Neat Pulse org ID
}

func (d *NeatDriver) GetStatus(ctx context.Context) (*DeviceStatus, error)
func (d *NeatDriver) Reboot(ctx context.Context) error
func (d *NeatDriver) GetSensorData(ctx context.Context) (*SensorData, error)
func (d *NeatDriver) ApplyConfig(ctx context.Context, config *DeviceConfig) error
func (d *NeatDriver) UpdateFirmware(ctx context.Context) error
func (d *NeatDriver) GetFirmwareVersion(ctx context.Context) (string, error)
func (d *NeatDriver) FactoryReset(ctx context.Context) error
func (d *NeatDriver) EnableLocalAccess(ctx context.Context) error
```

### 3.4 Shure Audio (MXA, P300, etc.)

**Protocols**: REST API (System API Server), TCP port 2202 (3rd-party control strings), SNMP (port 161)

**Capabilities**:
- Firmware update
- DSP configuration (AEC, EQ, gating, mixing)
- Preset management
- Diagnostics (signal levels, clipping, temperature)
- Network status
- NTP sync

**REST API** (System API Server):
- Requires Shure System API Server installed on a local machine
- RESTful endpoints for all device operations
- JSON payloads

**TCP Port 2202** (control strings):
- Text-based command protocol
- Used for real-time control and monitoring
- Commands vary by device model

**SNMP** (port 161):
- Standard MIB for monitoring
- Firmware version, uptime, network status
- Alerts/traps for fault conditions

**Driver Interface**:
```go
type ShureDriver struct {
    ip         string
    model      string // "MXA710", "P300", "MXA920", etc.
    apiServer  string // System API Server URL
    tcpPort    int    // 2202 for control strings
    snmpCommunity string
}

func (d *ShureDriver) GetStatus(ctx context.Context) (*DeviceStatus, error)
func (d *ShureDriver) GetDiagnostics(ctx context.Context) (*Diagnostics, error)
func (d *ShureDriver) UpdateFirmware(ctx context.Context) error
func (d *ShureDriver) GetFirmwareVersion(ctx context.Context) (string, error)
func (d *ShureDriver) ApplyPreset(ctx context.Context, presetID string) error
func (d *ShureDriver) GetSignalLevels(ctx context.Context) ([]SignalLevel, error)
func (d *ShureDriver) Reboot(ctx context.Context) error
```

### 3.5 Cisco PoE Switch Driver

**Primary**: Direct to switch via RESTCONF, NETCONF, or SSH CLI
**Fallback**: Catalyst Center REST API

**Capabilities**:
- PoE port status (admin/oper state, power allocated/consumed)
- PoE port power cycle (shutdown → wait → no shutdown)
- Interface status
- Device health (CPU, memory, uptime)
- Power budget monitoring

#### 3.5.1 Direct Switch Access

**RESTCONF** (HTTPS, requires `restconf` + `ip http secure-server` configured):
```
GET  /restconf/data/Cisco-IOS-XE-native:native/interface/GigabitEthernet=1%2F0%2F5
GET  /restconf/data/Cisco-IOS-XE-native:native/interface/GigabitEthernet=1%2F0%2F5/Cisco-IOS-XE-power:power
PATCH /restconf/data/Cisco-IOS-XE-native:native/interface/GigabitEthernet=1%2F0%2F5/config
  {"shutdown": true}
```

**NETCONF** (SSH port 830, requires `netconf-yang` configured):
```xml
<!-- Get interface config -->
<rpc message-id="1">
  <get-config>
    <source><running/></source>
    <filter>
      <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
        <interface><GigabitEthernet><name>1/0/5</name></GigabitEthernet></interface>
      </native>
    </filter>
  </get-config>
</rpc>

<!-- Shutdown port -->
<rpc message-id="2">
  <edit-config>
    <target><running/></target>
    <config>
      <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
        <interface>
          <GigabitEthernet>
            <name>1/0/5</name>
            <shutdown/>
          </GigabitEthernet>
        </interface>
      </native>
    </config>
  </edit-config>
</rpc>
```

**SSH CLI** (fallback, requires enable credentials):
```
enable
configure terminal
interface GigabitEthernet1/0/5
shutdown
end
-- wait --
configure terminal
interface GigabitEthernet1/0/5
no shutdown
end
```

#### 3.5.2 Catalyst Center API (Fallback)

**Base URL**: `https://<catalyst-center-host>/dna/intent/api/v1`

**Key Endpoints**:
- `GET /network-device` — List all managed devices
- `GET /network-device/{uuid}/poe` — PoE summary for device
- `GET /network-device/{uuid}/interface/poe-detail?interfaceNameList=GigabitEthernet1/0/5` — PoE details per port
- `POST /network-device/{uuid}/command-runner` — Run CLI commands (for shutdown/no shutdown)

**Note**: Catalyst Center does not have a native "toggle PoE on port" API endpoint. PoE port control is done via Command Runner (CLI injection) or via device-level NETCONF through Catalyst Center.

**Driver Interface**:
```go
type CiscoDriver struct {
    switchIP        string
    method          string // "restconf", "netconf", "ssh", "catalyst_center"
    username        string
    password        string
    enablePassword  string // for SSH CLI
    catalystCenter  *CatalystCenterClient // optional fallback
    switchUUID      string // Catalyst Center device UUID
}

func (d *CiscoDriver) GetPoEPortStatus(ctx context.Context, iface string) (*PoEPortStatus, error)
func (d *CiscoDriver) PowerCyclePort(ctx context.Context, iface string, waitSec int) error
func (d *CiscoDriver) DisablePort(ctx context.Context, iface string) error
func (d *CiscoDriver) EnablePort(ctx context.Context, iface string) error
func (d *CiscoDriver) GetSwitchStatus(ctx context.Context) (*DeviceStatus, error)
func (d *CiscoDriver) GetPowerBudget(ctx context.Context) (*PowerBudget, error)
```

### 3.6 MS Graph API (Exchange Room Scheduling)

**Protocol**: Microsoft Graph REST API (HTTPS)
**Auth**: OAuth 2.0 (client credentials or delegated)

**Capabilities**:
- Room calendar for each meeting room
- Current meeting info (organizer, subject, time)
- Next scheduled meeting
- Room availability

**Key Endpoints**:
```
GET /users/{room-email}/calendarview?startDateTime=...&endDateTime=...
GET /users/{room-email}/calendar/getSchedule
POST /users/{room-email}/calendar/getSchedule
```

**Driver Interface**:
```go
type ExchangeDriver struct {
    tenantID     string
    clientID     string
    clientSecret string
}

func (d *ExchangeDriver) GetRoomSchedule(ctx context.Context, roomEmail string, start, end time.Time) ([]MeetingEvent, error)
func (d *ExchangeDriver) GetCurrentMeeting(ctx context.Context, roomEmail string) (*MeetingEvent, error)
func (d *ExchangeDriver) GetNextMeeting(ctx context.Context, roomEmail string) (*MeetingEvent, error)
```

---

## 4. Database Schema

### 4.1 Core Tables

```sql
-- Hierarchical location model
CREATE TABLE buildings (
    id          UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name        TEXT NOT NULL,
    address     TEXT,
    timezone    TEXT NOT NULL DEFAULT 'UTC',
    created_at  TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at  TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE TABLE floors (
    id          UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    building_id UUID NOT NULL REFERENCES buildings(id) ON DELETE CASCADE,
    name        TEXT NOT NULL,
    floor_order INT NOT NULL DEFAULT 0,
    created_at  TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at  TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    UNIQUE(building_id, name)
);

CREATE TABLE rooms (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    floor_id        UUID NOT NULL REFERENCES floors(id) ON DELETE CASCADE,
    name            TEXT NOT NULL,
    display_name    TEXT,
    room_number     TEXT,
    capacity        INT,
    exchange_email  TEXT,
    neat_pulse_room_id TEXT,
    switch_id       UUID,
    notes           TEXT,
    created_at      TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at      TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    UNIQUE(floor_id, name)
);

-- Device registry
CREATE TABLE devices (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    room_id         UUID NOT NULL REFERENCES rooms(id) ON DELETE CASCADE,
    device_type     TEXT NOT NULL,
    model           TEXT,
    hostname        TEXT,
    ip_address      INET,
    mac_address     MACADDR,
    firmware_version TEXT,
    target_firmware TEXT,
    serial_number   TEXT,
    config          JSONB,
    status          TEXT NOT NULL DEFAULT 'unknown',
    last_seen       TIMESTAMPTZ,
    created_at      TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at      TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

-- Cisco switch port to room mapping
CREATE TABLE switch_ports (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    switch_id       UUID NOT NULL REFERENCES devices(id) ON DELETE CASCADE,
    interface_name  TEXT NOT NULL,
    room_id         UUID NOT NULL REFERENCES rooms(id) ON DELETE CASCADE,
    poe_enabled     BOOLEAN NOT NULL DEFAULT true,
    poe_class       TEXT,
    description     TEXT,
    created_at      TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at      TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    UNIQUE(switch_id, interface_name)
);

-- Real-time device status
CREATE TABLE device_status (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    device_id       UUID NOT NULL REFERENCES devices(id) ON DELETE CASCADE,
    status          TEXT NOT NULL,
    uptime          INTERVAL,
    cpu_usage       FLOAT,
    memory_usage    FLOAT,
    temperature     FLOAT,
    error_message   TEXT,
    outlets         JSONB,
    sensor_data     JSONB,
    poe_status      JSONB,
    last_polled     TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    created_at      TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at      TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    UNIQUE(device_id)
);

-- Action queue
CREATE TABLE actions (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    device_id       UUID NOT NULL REFERENCES devices(id) ON DELETE CASCADE,
    action_type     TEXT NOT NULL,
    status          TEXT NOT NULL DEFAULT 'pending',
    parameters      JSONB,
    result          JSONB,
    created_by      UUID REFERENCES users(id),
    created_at      TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    started_at      TIMESTAMPTZ,
    completed_at    TIMESTAMPTZ,
    error_message   TEXT
);

-- Audit log
CREATE TABLE audit_logs (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    actor_id        UUID REFERENCES users(id),
    actor_name      TEXT,
    action          TEXT NOT NULL,
    target_type     TEXT,
    target_id       UUID,
    details         JSONB,
    ip_address      INET,
    created_at      TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

-- Meeting events (cached from Exchange)
CREATE TABLE meeting_events (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    room_id         UUID NOT NULL REFERENCES rooms(id) ON DELETE CASCADE,
    exchange_id     TEXT NOT NULL,
    subject         TEXT,
    organizer       TEXT,
    organizer_email TEXT,
    start_time      TIMESTAMPTZ NOT NULL,
    end_time        TIMESTAMPTZ NOT NULL,
    status          TEXT NOT NULL DEFAULT 'confirmed',
    is_current      BOOLEAN NOT NULL DEFAULT false,
    synced_at       TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

-- Firmware version registry
CREATE TABLE firmware_versions (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    device_type     TEXT NOT NULL,
    model           TEXT NOT NULL,
    version         TEXT NOT NULL,
    release_date    DATE,
    release_notes   TEXT,
    is_stable       BOOLEAN NOT NULL DEFAULT true,
    is_target       BOOLEAN NOT NULL DEFAULT false,
    created_at      TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    UNIQUE(device_type, model, version)
);

-- User accounts (linked to SSO)
CREATE TABLE users (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    email           TEXT NOT NULL UNIQUE,
    name            TEXT NOT NULL,
    role            TEXT NOT NULL DEFAULT 'engineer',
    sso_provider    TEXT,
    sso_subject     TEXT,
    is_active       BOOLEAN NOT NULL DEFAULT true,
    last_login      TIMESTAMPTZ,
    created_at      TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at      TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

-- Gateway agent registration
CREATE TABLE gateways (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name            TEXT NOT NULL,
    hostname        TEXT,
    ip_address      INET,
    version         TEXT,
    status          TEXT NOT NULL DEFAULT 'offline',
    last_heartbeat  TIMESTAMPTZ,
    created_at      TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at      TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

-- Indexes
CREATE INDEX idx_devices_room ON devices(room_id);
CREATE INDEX idx_devices_type ON devices(device_type);
CREATE INDEX idx_devices_status ON devices(status);
CREATE INDEX idx_device_status_device ON device_status(device_id);
CREATE INDEX idx_device_status_last_polled ON device_status(last_polled);
CREATE INDEX idx_actions_device ON actions(device_id);
CREATE INDEX idx_actions_status ON actions(status);
CREATE INDEX idx_actions_created ON actions(created_at);
CREATE INDEX idx_audit_logs_created ON audit_logs(created_at);
CREATE INDEX idx_audit_logs_target ON audit_logs(target_type, target_id);
CREATE INDEX idx_meeting_events_room ON meeting_events(room_id);
CREATE INDEX idx_meeting_events_time ON meeting_events(start_time, end_time);
CREATE INDEX idx_switch_ports_switch ON switch_ports(switch_id);
CREATE INDEX idx_switch_ports_room ON switch_ports(room_id);
```

---

## 5. API Endpoints

### 5.1 Public API (Authenticated)

#### Buildings & Rooms
```
GET    /api/v1/buildings              — List all buildings
GET    /api/v1/buildings/{id}         — Get building details
GET    /api/v1/buildings/{id}/floors  — List floors in building
GET    /api/v1/floors/{id}/rooms      — List rooms on floor
GET    /api/v1/rooms                  — List all rooms (with filters)
GET    /api/v1/rooms/{id}             — Get room details with all devices
GET    /api/v1/rooms/{id}/status      — Get real-time room status (all devices)
POST   /api/v1/rooms/import           — Import rooms/devices from spreadsheet
```

#### Devices
```
GET    /api/v1/devices                — List all devices (with filters)
GET    /api/v1/devices/{id}           — Get device details
GET    /api/v1/devices/{id}/status    — Get real-time device status
POST   /api/v1/devices/{id}/actions   — Queue an action on a device
GET    /api/v1/devices/{id}/actions   — List actions for a device
GET    /api/v1/devices/{id}/history   — Get device status history
```

#### Actions
```
GET    /api/v1/actions                — List all actions (with filters)
GET    /api/v1/actions/{id}           — Get action details
POST   /api/v1/actions/{id}/cancel    — Cancel a pending action
POST   /api/v1/actions/bulk           — Queue bulk actions across devices
```

#### Meetings
```
GET    /api/v1/rooms/{id}/meetings    — Get current/next meetings
GET    /api/v1/meetings/current       — Get all rooms with active meetings
GET    /api/v1/meetings/timeline      — Meeting timeline for a building/floor
POST   /api/v1/meetings/sync          — Trigger calendar sync
```

#### Firmware
```
GET    /api/v1/firmware               — List known firmware versions
GET    /api/v1/firmware/outdated      — List devices with outdated firmware
POST   /api/v1/firmware/upgrade       — Queue firmware upgrade (single or bulk)
```

#### Cisco Switches
```
GET    /api/v1/switches               — List all managed Cisco switches
GET    /api/v1/switches/{id}          — Get switch details
GET    /api/v1/switches/{id}/ports    — List switch ports with room mapping
GET    /api/v1/switches/{id}/ports/{iface}/poe  — Get PoE status for port
POST   /api/v1/switches/{id}/ports/{iface}/power-cycle  — Power cycle PoE port
```

#### System
```
GET    /api/v1/health                 — System health check
GET    /api/v1/gateways               — List gateway agents
GET    /api/v1/gateways/{id}/status   — Gateway status
GET    /api/v1/audit-logs             — Query audit logs
WS     /ws                            — WebSocket for real-time updates
```

### 5.2 Gateway Internal API (via WebSocket)

**Cloud → Gateway**:
```json
{ "type": "action", "action_id": "...", "device_id": "...", "action_type": "power_cycle", "parameters": { "outlet": 1 } }
{ "type": "status_request", "device_ids": ["..."] }
{ "type": "config_update", "device_id": "...", "config": { ... } }
```

**Gateway → Cloud**:
```json
{ "type": "status_update", "device_id": "...", "status": { ... }, "timestamp": "..." }
{ "type": "action_result", "action_id": "...", "status": "completed", "result": { ... } }
{ "type": "heartbeat", "gateway_id": "...", "timestamp": "..." }
```

---

## 6. Gateway Agent Architecture

### 6.1 Structure
```
gateway/
├── cmd/agent/
│   └── main.go
├── internal/
│   ├── agent/
│   │   ├── agent.go
│   │   └── config.go
│   ├── drivers/
│   │   ├── driver.go           # Driver interface
│   │   ├── wattbox/
│   │   ├── atlona/
│   │   ├── neat/
│   │   ├── shure/
│   │   └── cisco/
│   ├── poller/
│   │   ├── poller.go
│   │   └── queue.go
│   ├── sync/
│   │   └── websocket.go
│   └── exchange/
│       └── client.go
├── config.yaml
└── go.mod
```

### 6.2 Polling Strategy

| Device Type | Poll Interval | Reason |
|---|---|---|
| WattBox | 60s | Outlet state rarely changes |
| Atlona | 60s | Input routing changes infrequently |
| Neat | 30s | Sensor data, meeting status |
| Shure | 60s | Audio levels, diagnostics |
| Cisco Switch | 120s | PoE status, power budget |
| Exchange Calendar | 300s | Meeting schedule changes |

### 6.3 Action Execution Flow

```
Cloud queues action → WebSocket push to gateway → Action queue → Execute → Report result → Update DB
```

1. Action created in cloud DB with status `pending`
2. Cloud sends action to gateway via WebSocket
3. Gateway acknowledges, sets status `running`
4. Gateway executes action using appropriate driver
5. Gateway reports result to cloud
6. Cloud updates action status to `completed` or `failed`
7. Audit log entry created

---

## 7. Svelte Dashboard

### 7.1 Page Structure

```
/                           — Dashboard overview
/buildings                  — Building list
/buildings/{id}             — Building floor map view
/floors/{id}                — Floor view with room grid
/rooms/{id}                 — Room detail (all devices, meeting info, actions)
/devices/{id}               — Device detail
/actions                    — Action queue & history
/actions/{id}               — Action detail
/meetings                   — Meeting timeline view
/firmware                   — Firmware management
/switches                   — Cisco switch management
/settings                   — System configuration
/audit                      — Audit log viewer
```

### 7.2 Key Components

- **FloorMapView** — SVG floor plan with color-coded room status indicators
- **RoomCard** — Compact room status: name, current meeting, device health dots
- **DevicePanel** — Device detail: status, firmware, controls, history
- **ActionQueue** — Real-time action list with status indicators
- **MeetingTimeline** — Visual timeline of room usage
- **BulkOpsModal** — Select multiple rooms/devices, queue bulk action
- **AlertBanner** — System-wide alerts (offline devices, failed actions)

---

## 8. Security

### 8.1 Authentication

- **Cloud API**: OIDC/OAuth 2.0 (Azure AD, Okta, or Google)
- **Gateway Agent**: Mutual TLS or pre-shared token for WebSocket
- **Neat Pulse**: Bearer token (API key from Neat Pulse account)
- **MS Graph**: OAuth 2.0 client credentials flow
- **Catalyst Center**: OAuth 2.0 token

### 8.2 Credential Storage

- Device credentials stored encrypted with AES-256 in PostgreSQL
- Encryption key via environment variable or KMS
- Never logged or transmitted in plaintext

### 8.3 RBAC

| Role | Permissions |
|---|---|
| **Admin** | Full access, user management, system config |
| **Engineer** | View all, execute actions, manage devices |
| **Viewer** | Read-only access to status and meetings |

---

## 9. Deployment

### 9.1 Cloud Components (Docker Compose)

```yaml
services:
  api:
    image: av-manager/api:latest
    ports: ["8080:8080"]
    environment:
      - DATABASE_URL=postgres://...
      - REDIS_URL=redis://...
      - OIDC_ISSUER=...
      - OIDC_CLIENT_ID=...

  postgres:
    image: postgres:16
    volumes: ["pgdata:/var/lib/postgresql/data"]

  redis:
    image: redis:7

  web:
    image: av-manager/web:latest
```

### 9.2 Gateway Agent

- Binary distribution (Linux amd64/arm64)
- Systemd service on on-prem server
- Configuration via YAML file or environment variables
- Auto-reconnect on network disruption
- Local SQLite cache for offline operation

---

## 10. Spreadsheet Import Format

```csv
Building,Floor,Room,RoomDisplayName,Capacity,ExchangeEmail,DeviceType,DeviceModel,IPAddress,MACAddress,SerialNumber,SwitchIP,SwitchPort,NeatPulseEndpointID,Notes
HQ,1,Room 101,Innovation Lab,12,room101@company.com,WattBox,WB-08-15,10.1.1.10,,,,,,,
HQ,1,Room 101,Innovation Lab,12,room101@company.com,Atlona,AT-UHD-CLSO-601,10.1.1.11,,,,,,,
HQ,1,Room 101,Innovation Lab,12,room101@company.com,Neat Bar,Neat Bar,,11:22:33:44:55:66,ABC123,,,,neat-endpoint-uuid,
HQ,1,Room 101,Innovation Lab,12,room101@company.com,Neat Pad,Neat Pad,,22:33:44:55:66:77,DEF456,,,,neat-endpoint-uuid2,
HQ,1,Room 101,Innovation Lab,12,room101@company.com,Shure,MXA710,10.1.1.12,,,,,,,
HQ,1,Room 101,Innovation Lab,12,room101@company.com,Cisco Switch,C9300-48P,10.1.0.1,,,,10.1.0.1,GigabitEthernet1/0/1,,,
```

---

## 11. Implementation Phases

| Phase | Duration | Deliverables |
|---|---|---|
| **1: Foundation** | Weeks 1-2 | DB schema, Go API skeleton, gateway skeleton, Svelte shell, SSO skeleton |
| **2: Device Drivers** | Weeks 3-5 | All 5 device drivers (WattBox, Atlona, Neat, Shure, Cisco) + driver registry |
| **3: Polling & Status** | Weeks 5-6 | Polling scheduler, status aggregation, real-time push, room status cards |
| **4: MS Graph** | Week 7 | Exchange calendar sync, meeting awareness, timeline component |
| **5: Action System** | Weeks 7-8 | Action queue, power cycle, reboot, audit trail |
| **6: Dashboard UI** | Weeks 8-10 | Floor map, room detail, device detail, real-time updates, alerts |
| **7: Firmware & Bulk Ops** | Weeks 10-11 | Firmware registry, upgrade scheduling, bulk ops, spreadsheet import |
| **8: Production** | Weeks 11-12 | RBAC, rate limiting, Docker compose, docs, load testing |

---

## 12. Non-Functional Requirements

| Requirement | Target |
|---|---|
| Device poll latency | < 5s per device |
| Dashboard load time | < 2s for full building |
| Action execution | < 30s for power cycle, < 10min for firmware |
| WebSocket reconnect | < 5s on disconnect |
| Gateway offline resilience | Cache status locally, sync on reconnect |
| Concurrent users | 50+ engineers |
| Device count | 1000+ devices across 140 rooms |
| Data retention | 90 days audit logs, 30 days status history |

---

## 13. Future Enhancements

- Automated troubleshooting — Run diagnostic scripts on failing devices
- Predictive maintenance — Alert before failures based on patterns
- Integration with ITSM — Auto-create tickets for device failures
- Room scheduling optimization — Suggest room reassignments based on AV health
- Energy management — Power down unused rooms based on calendar
- Voice control — Alexa/Google Home integration for room controls
- Mobile app — React Native companion app for on-the-go management
