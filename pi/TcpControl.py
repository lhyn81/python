import socket
import time
import sys
import struct
#RPi's IP
SERVER_IP = "192.168.1.1"
SERVER_PORT = 2222

print("Starting socket: TCP...")
server_addr = (SERVER_IP, SERVER_PORT)
socket_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
while True:
    try:
        print("Connecting to server @ %s:%d..." %(SERVER_IP, SERVER_PORT))
        socket_tcp.connect(server_addr)
        break
    except Exception:
        print("Can't connect to server,try it latter!")
        time.sleep(1)
        continue
print("Please input gogo or stop to turn on/off the motor!")
while True:
    try:
        cmd=input()
        if cmd=='a':
            data1 = struct.pack('1B',255)
            data2 = struct.pack('1B',4)
            data3 = struct.pack('1B',0)
            data4 = struct.pack('1B',0)
            data5 = struct.pack('1B',255)
            socket_tcp.send(data1)
            socket_tcp.send(data2)
            socket_tcp.send(data3)
            socket_tcp.send(data4)
            socket_tcp.send(data5)
        elif cmd=='b':
            data1 = struct.pack('1B',255)
            data2 = struct.pack('1B',4)
            data3 = struct.pack('1B',1)
            data4 = struct.pack('1B',0)
            data5 = struct.pack('1B',255)
            socket_tcp.send(data1)
            socket_tcp.send(data2)
            socket_tcp.send(data3)
            socket_tcp.send(data4)
            socket_tcp.send(data5)    
        #data = socket_tcp.recv(512).decode()
        #if not data:
        #    break
        #print(data)
    except e:
        print(e.message)
        socket_tcp.close()
        socket_tcp=None
        sys.exit(1)
