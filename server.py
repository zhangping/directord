
import logging
import sys
from daemon import *
from director import *

class Server (Daemon):
        def run (self):
                # Create the server
                HOST, PORT = "localhost", 554
                theserver = SocketServer.TCPServer ((HOST, PORT), Director)

                # Activate the server
                theserver.serve_forever () 

if __name__ == "__main__":

        logging.basicConfig(filename='/var/log/director.log',
                format='%(asctime)s - %(module)s.%(funcName)s - %(levelname)s - %(message)s',
                level=logging.DEBUG)

        service = Server ("/var/run/director.pid")
        if len(sys.argv) == 2:
                if 'start' == sys.argv[1]:
                        sys.argv[1] = '8080'
                        service.start()
                elif 'stop' == sys.argv[1]:
                        service.stop()
                elif 'restart' == sys.argv[1]:
                        service.restart()
                else:
                        print "Unknown command"
                        sys.exit(2)
                sys.exit(0)

