 https://iperf.fr/iperf-doc.php

 # default 
 - iperf3 -s
 - iperf3 -c <IP address of server>

 # UDP Tests
    # Client Node setup
    # -c tells the client what server to connect to on the far side
    # -n will send 100Gigabytes of data
    # -R instead of client sending traffic, this reverses the flow so the server sends and client receives
    # -u send the traffic over UDP
    # -b Max bandwidth set at 500Mbps
- iperf3 -c 169.254.141.36 -n 100G -R -u -b 500M
    # One node needs to be set as the server
    # -B (binds) or listens on the IP address given
    # -s tells iperf3 to start up a server
- iperf3 -B 169.254.141.36 -s