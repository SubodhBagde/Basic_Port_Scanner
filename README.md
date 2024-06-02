# Basic_Port_Scanner

> Identifies open ports in the target system.

I developed this basic port scanner using concept of networking and python programming.

A port scanner is basically a network tool which is used to identify open ports in the target system.
This project is made by integrating the concept of networking and python programming.
Important libraries:
1) Socket: Socket library is used to create network sockets and perform port scanning.
2) Threading: Threading library is used to increase the verbosity of the code, that is it will scan multiple ports at a time thereby increasing the efficiency of the code.
3) Sys: Sys library is used to access system specific parameters and functions. It is also used to pass command-line arguments to the scripts.

Note: This code accepts command line arguments therefore you will need to run this code on terminal. The IP address which is used here is of my metasploitable machine which is by default vulnerable therefore there are some ports open in this machine. If you will enter your PC/laptop's IP address then there are chances it will not show any ports open because of the firewalls and the anti-virus installed on our device.



```
import socket
import sys
import time
import threading
from datetime import datetime

print("Python Port Scanner")
start_time = time.time()
if(len(sys.argv)) == 4:
    target = socket.gethostbyname(sys.argv[1])
else:
    print("Invalid amount of arguements.")
    print("Syntax: {Target IP address} Start_Port End_Port")
    sys.exit()

start_port = int(sys.argv[2])
end_port = int(sys.argv[3])
threads = []
print("-" * 50)
print("Scanning Target: "+target)
print("Time Started: "+str(datetime.now()))
print("-" * 50)

try:
    def scan_port(port):
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        result = s.connect_ex((target,port))
        socket.setdefaulttimeout(1)
        if result == 0:
            print(f"Port {port} is open")
        s.close()
    for port in range(start_port,end_port+1):
            thread = threading.Thread(target = scan_port, args = (port,))
            thread.start()
            threads.append(thread)
    for thread in threads:
        thread.join()
           
except KeyboardInterrupt:
     print("\nExiting Program.")
     sys.exit()
except socket.gaierror:
     print("Hostname could not be resolved.")
     sys.exit()
end_time = time.time()
print("Time Elapsed: ",end_time-start_time,"sec")
print("-" * 50)

```
Here is the output of this program: 

![Screenshot 2023-07-21 143510](https://github.com/SubodhBagde/Basic_Port_Scanner/assets/136182792/5611016c-423f-4814-a2f2-f08c6af47388)
