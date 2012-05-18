
import fileinput
import re
import socket

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

for l in fileinput.input ("vss.log"):
        if re.match ("^#", l):
                continue

        r = re.compile ("\S+ \/(\S+\.ts)")
        sendrequest (r.search (l).group (1))
                
