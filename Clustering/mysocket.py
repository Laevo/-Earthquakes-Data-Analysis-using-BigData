#!/usr/bin/env python

import socket
import time
import os
import csv
from nvd3 import lineChart

# create a socket object
serversocket = socket.socket(
                socket.AF_INET, socket.SOCK_STREAM)

TCP_IP = ''
TCP_PORT = 7789

# b
serversocket.bind((TCP_IP, TCP_PORT))
print "Binding Complete"
# queue up to 5 requests
serversocket.listen(10)
print "Listening"
while True:
    # establish a connection
    clientsocket,addr = serversocket.accept()
    hor = clientsocket.recv(1024)
    dep = clientsocket.recv(1024)
    num_clusters = clientsocket.recv(1024)
    command = "python /home/ubuntu/clstr/makeclstr.py "+ hor+ " "+ dep+" " + num_clusters
    os.system(command)
#    with open('/var/www/html/clstr/static/clusterview.html', 'r') as f:
#        data = f.read()
    data = "Done"
    clientsocket.sendall(data)
#    clientsocket.sendall("Done")
    print "Close"
