import socket
import signal
import weakref
import errno
import logging
import pyev
from rtspparser import *
from route import *

MethodNotAllowed = (
"RTSP/1.0 405 Method Not Allowed\r\n"
"CSeq: %d\r\n\r\n"
)

MethodOptions = (
"RTSP/1.0 200 OK\r\n"
"CSeq: %d\r\n"
"Public: DESCRIBE\r\n\r\n"
)

MethodRedirect = (
"RTSP/1.0 302 Found\r\n"
"Server: Directord/1.0\r\n"
"CSeq: %d\r\n"
"Connection: Close\r\n"
"Location: %s\r\n\r\n"
)

FileNotFound = (
"RTSP/1.0 404 Not Found\r\n"
"Server: Directord/1.0\r\n"
"Cseq: %d\r\n"
"Connection: Close\r\n\r\n"
)

STOPSIGNALS = (signal.SIGINT, signal.SIGTERM)
NONBLOCKING = (errno.EAGAIN, errno.EWOULDBLOCK)
logger = logging.getLogger ()
accesslogger = logging.getLogger ('access')

class Connection(object):

        def __init__(self, sock, address, loop):
                self.sock = sock
                self.address = address
                self.sock.setblocking(0)
                self.buf = ""
                self.watcher = pyev.Io(self.sock._sock, pyev.EV_READ, loop, self.io_cb)
                self.watcher.start()
                logger.debug("{0}: ready".format(self))

        def reset(self, events):
                self.watcher.stop()
                self.watcher.set(self.sock, events)
                self.watcher.start()

        def handle_error(self, msg, level=logging.ERROR, exc_info=True):
                logger.log(level, "{0}: {1} --> closing".format(self, msg), exc_info=exc_info)
                self.close()

        def handle_read(self):
                try:
                        buf = self.sock.recv(1024)
                except socket.error as err:
                        if err.args[0] not in NONBLOCKING:
                                self.handle_error("error reading from {0}".format(self.sock))
                if buf:
                        logger.debug ("Got request {}".format (buf))
                        self.buf += buf
                        self.reset(pyev.EV_READ | pyev.EV_WRITE)
                else:
                        self.handle_error("connection closed by peer", logging.DEBUG, False)

        def handle_write(self):
                try:
                        if (self.buf.find("\r\n\r\n") >= 0): # whole request received
                                logger.debug ("whole request got: %s" % self.buf)
                                request = RtspParser (self.buf)
                                if request.error:
                                        logger.warning ("Bad request: {}".format (self.buf))
                                        response = MethodNotAllowed % request.get_CSeq ()
                                        self.sock.send (response)
                                        self.close ()
                                else:
                                        if request.get_method () == "DESCRIBE":
                                                logger.debug ("It is a DESCRIBE request")
                                                destination = route (request.get_medianame ())
                                                if destination is None:
                                                        logger.warning ("File not found : %s" % request.get_url ())
                                                        response = FileNotFound % request.get_CSeq ()
                                                        self.sock.send (response)
                                                        self.close ()
                                                else:
                                                        accesslogger.info ("%s %s" % (request.get_medianame (), destination))
                                                        location = "rtsp://%s/%s" % (destination, request.get_medianame ())
                                                        response = MethodRedirect % (request.get_CSeq (), location)
                                                        self.sock.send (response)
                                                        self.buf = self.buf[len(self.buf):]
                                        elif request.get_method () == "OPTIONS":
                                                logger.debug ("It is a OPTIONS request")
                                                response = MethodOptions % request.get_CSeq ()
                                                self.sock.send (response)
                                                self.buf = self.buf[len(self.buf):]
                                if not self.buf:
                                        self.reset(pyev.EV_READ)
                        else: # should read more
                                self.reset(pyev.EV_READ)
                except socket.error as err:
                        if err.args[0] not in NONBLOCKING:
                                self.handle_error("error writing to {0}".format(self.sock))

        def io_cb(self, watcher, revents):
                if revents & pyev.EV_READ:
                        self.handle_read()
                else:
                        self.handle_write()

        def close(self):
                self.sock.close()
                self.watcher.stop()
                self.watcher = None
                logger.debug("{0}: closed".format(self))

class EvServer(object):

        def __init__(self, address):
                self.sock = socket.socket()
                self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                self.sock.bind(address)
                self.sock.setblocking(0)
                self.address = self.sock.getsockname()
                self.loop = pyev.default_loop()
                self.watchers = [pyev.Signal(sig, self.loop, self.signal_cb) for sig in STOPSIGNALS]
                self.watchers.append(pyev.Io(self.sock._sock, pyev.EV_READ, self.loop, self.io_cb))
                self.conns = weakref.WeakValueDictionary()

        def handle_error(self, msg, level=logging.ERROR, exc_info=True):
                logger.log(level, "{0}: {1} --> stopping".format(self, msg), exc_info=exc_info)
                self.stop()

        def signal_cb(self, watcher, revents):
                self.stop()

        def io_cb(self, watcher, revents):
                try:
                        while True:
                                try:
                                        sock, address = self.sock.accept()
                                except socket.error as err:
                                        if err.args[0] in NONBLOCKING:
                                                break
                                        else:
                                                raise
                                else:
                                        self.conns[address] = Connection(sock, address, self.loop)
                except Exception:
                        self.handle_error("error accepting a connection")

        def start(self):
                self.sock.listen(socket.SOMAXCONN)
                for watcher in self.watchers:
                        watcher.start()
                logger.debug("{0}: started on {0.address}".format(self))
                self.loop.start()

        def stop(self):
                self.loop.stop(pyev.EVBREAK_ALL)
                self.sock.close()
                while self.watchers:
                        self.watchers.pop().stop()
                for conn in self.conns.values():
                        conn.close()
                logger.debug("{0}: stopped".format(self))


if __name__ == "__main__":
        server = EvServer(("192.168.1.13", 554))
        server.start()
