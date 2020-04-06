import socket
import sys
import subprocess
from threading import Thread
import time

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 5000      # The port used by the server
while 1:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.connect((HOST, PORT))
        except:
            time.sleep(1)
            continue

        while 1:
            msg = bytes(input("Enter message: ")+'\n','utf8')
            s.sendall(msg)
            data = s.recv(1024).decode("utf-8")
            print(data)
            if "249" in data:
                print('He left, you can stay here alone now if you want... I guess?')
