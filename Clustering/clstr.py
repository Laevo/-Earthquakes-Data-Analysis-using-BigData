#!usr/bin/env python
import time
import os
import csv
import socket
import subprocess
from flask import Flask, Response, request
app = Flask(__name__)

@app.route('/')
def welcome():
    return app.send_static_file('index.html')


@app.route('/plot', methods=['GET', 'POST'])
def plot():
    if request.method == 'POST':
        hor = str(request.form['hor'])
        dep = str(request.form['dep'])
        cluster = str(request.form['cluster'])
        start_time = time.time()
        host = ''
        port = 7789

        page = socket_connection(host, port, hor, dep, cluster)
        print("--- %s seconds ---" % (time.time() - start_time))
        return app.send_static_file('clusterview.html')

def socket_connection(host_ip,port, hor, dep, cluster):
        try:
                s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        except socket.error:
                sys.exit()

        s.connect((host_ip,port))
        try:
                s.sendall(hor)
                s.sendall(dep)
                s.sendall(cluster)
        except socket.error:
                sys.exit()
        print "Execute"
        data = s.recv(98988)
#        print data
#        indexfile = open("/var/www/html/clstr/static/clusterview.html", "r")
#        clusterScatter = indexfile.read()
        return data


if __name__ == "__main__":
    app.run(debug=True)

