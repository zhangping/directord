
import logging
import sys
from daemon import *
from evserver import *

class Server (Daemon):
        def run (self):
                # Create the server
                HOST, PORT = "192.168.1.13", 554
                theserver = EvServer ((HOST, PORT))

                # Activate the server
                theserver.start () 

if __name__ == "__main__":

        logging.basicConfig (filename='/var/log/directord.log',
                format='%(asctime)s - %(module)s.%(funcName)s - %(levelname)s - %(message)s',
                level=logging.DEBUG)

        service = Server ("/var/run/directord.pid")
        if len(sys.argv) == 2:
                if 'start' == sys.argv[1]:
                        service.start()
                elif 'stop' == sys.argv[1]:
                        service.stop()
                elif 'restart' == sys.argv[1]:
                        service.restart()
                else:
                        print "Unknown command"
                        sys.exit(2)
                sys.exit(0)

