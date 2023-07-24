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


