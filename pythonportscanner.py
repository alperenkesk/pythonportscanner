#!/usr/bin/env python
import socket

remoteServer    = raw_input("IP Adresi Giriniz: ")
remoteServerIP  = socket.gethostbyname(remoteServer)

print "IP Adresi Taraniyor", remoteServerIP

try:
    for port in range(1,9999):  
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((remoteServerIP, port))
        if result == 0:
            print "Port:", port , "\t" "Open"
        sock.close()

except KeyboardInterrupt:
    print "Hoscakal..."
    sys.exit()
