
import SocketServer

class Director (SocketServer.BaseRequestHandler):
        """
        The RequestHandler class for our server.

        It is instantiated once per connection to the server, and must
        override the handle() method to implement communication to the
        client.
        """

        def handle(self):
                # self.request is the TCP socket connected to the client
                self.data = self.request.recv(1024).strip()
                print self.data

                # just send back the same data, but upper-cased
                self.request.sendall(self.data.upper())


