# Hurl

## Windows Installation
- [Requires Visual C++ Redistributable Version](https://aka.ms/vs/17/release/vc_redist.x64.exe)
- Download and install Visual C++

```powershell
winget install hurl
```

## Cargo Install
```
cargo install hurl
```

## Basic command
```bash
hurl test.hurl 

hurl test.hurl —-test
```

## Hurl File

### Basic Example with 'test'
>This checks that there is a 200 returned
```bash
#test.hurl
GET http://httpbin.org
HTTP 200
```

### Authentication with headers
>adds in authentication via HTTP headers
```bash
#test-auth.hurl
GET http://httpbing.org
X-HTTP-API-USER: user
X-HTTP-API-TOKEN: token
```

### Basic auth
```bash
GET http://httpbing.org
[BasicAuth]
bob: secret
```
### Using variables for sensitive items

```bash
hurl ./ --variable user=user token=token
hurl ./ --variables-file hurl.env

export HURL_user=user
export HURL_token=token
```

```bash
#hurl.evn
user=user
token=token
```

```bash
#test-auth.hurl
GET http://httpbing.org
X-HTTP-API-USER: {{user}}
X-HTTP-API-TOKEN: {{token}}
```

```bash
GET http://httpbing.org
[BasicAuth]
{{user}}: {{secret}}
```
```
 
# Resources
- [Hurl](https://hurl.dev/#whats-hurl)
