
import fileinput
import re
import socket
import glob
import time
import random

SERVER = '192.168.1.13'    # The directord server
PORT = 554

DescribeRequest = (
"DESCRIBE rtsp://%s/%s RTSP/1.0\r\n"
"CSeq: 896\r\n"
"User-Agent: Directord load tool\r\n"
"Accept: application/sdp\r\n\r\n"
)

def sendrequest (medianame):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((SERVER, PORT))
        request = DescribeRequest % (SERVER, medianame)
        print "Request {}".format (request)
        s.sendall(request)
        data = s.recv(1024)
        s.close()
        print 'Received', data

def loadtest (filename):
        for l in fileinput.input (filename):
                if re.match ("^#", l):
                        continue

                r = re.compile ("\S+ \/(\S+\.ts)")
                sendrequest (r.search (l).group (1))
                time.sleep (random.choice((0.01, 0.012, 0.013, 0.001, 0.015, 0.05, 0.024, 0.19, 0.0081, 0.04)))
                
fs = glob.glob ("Streaming*.log")
while True:
        print "another circle"
        for f in fs:
                loadtest(f)
