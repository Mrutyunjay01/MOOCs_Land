# -*- coding: utf-8 -*-

import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # set up the connections

mysock.connect(('data.pr4e.org', 80))  # set of the host and port

cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\n\n'.encode()

mysock.send(cmd)

while True:
    
    data = mysock.recv(512) # limit upto 512 characters
    print(data.decode())
    if len(data):
        break
    
    print(data.decode())
    
mysock.close() # close the connection

