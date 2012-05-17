# -*- coding: utf-8 -

# This file - rtspparser.py, is part of directord.
# url must be : rtsp://host/medianame?parameter, medianmae must be *.ts

import string
import re
import logging

logger = logging.getLogger ()

class RtspParser (object):
        """
        RTSP Request parser
        """
        def __init__ (self, request):
                self.error = False
                self.errstr = ""
                self.method = ""
                self.url = ""
                self.medianame = ""
                self.host = ""
                self.CSeq = None
                self.parse (request)

        def get_method (self):
                return self.method

        def get_url (self):
                return self.url

        def get_CSeq (self):
                return self.CSeq

        def get_host (self):
                return self.host

        def get_medianame (self):
                return self.medianame

        def parse (self, buf):
                a = re.split ("\r\n", buf)
                if a[0].find ("DESCRIBE") == 0:
                        self.method = "DESCRIBE"
                        for s in a:
                                if s.find ("DESCRIBE") == 0:
                                        try:
                                                r = re.compile ("DESCRIBE (\S+) RTSP/1.0")
                                                self.url = r.search (s).group (1)
                                                r = re.compile ("rtsp://(\S+)/(\S+\.ts)")
                                                self.host = r.search (self.url).group (1)
                                                self.medianame = r.search (self.url).group (2)
                                        except:
                                                self.errstr = "parse error"
                                                self.error = True # invalid url
                                                return -1
                                elif s.find ("CSeq") == 0:
                                        try:
                                                r = re.compile ("CSeq:.(\d+)")
                                                self.CSeq = string.atoi (r.search (s).group (1))
                                        except:
                                                self.errstr = "parse error"
                                                self.error = True
                                                return -1
                        return 0
                elif a[0].find ("OPTIONS") ==0:
                        self.method = "OPTIONS"
                        for s in a:
                                if s.find ("CSeq") == 0:
                                        try:
                                                r = re.compile ("CSeq:.(\d+)")
                                                self.CSeq = string.atoi (r.search (s).group (1))
                                        except:
                                                self.errstr = "parse error"
                                                self.error = True
                                                return -1
                        return 0
                else: # unsupported method
                        self.errstr = "not a valid request"
                        logger.debug ("bad request {}".format(self.errstr))
                        self.error = True # unsupported method
                        return -1

if __name__ == "__main__":
        request = "DESCRIBE rtsp://192.168.1.13/x.ts RTSP/1.0\r\nCSeq: 13\r\nUser-Agent: LibVLC/2.0.1 (LIVE555 Streaming Media v2011.12.23)\r\nAccept: application/sdp\r\n"
        #request = "OPTIONS rtsp://192.168.1.13/x.ts RTSP/1.0\r\nCSeq: 2\r\nUser-Agent: LibVLC/2.0.1 (LIVE555 Streaming Media v2011.12.23)"
        #request = "DESCRIBE rtsp://192.168.1.13/VODC2011011613583204.ts?ServiceGroup=1 RTSP/1.0\r\nCSeq: 3\r\nUser-Agent: LibVLC/2.0.1 (LIVE555 Streaming Media v2011.12.23)\r\nAccept: application/sdp\r\n\r\n"
        rtsp = RtspParser (request)
        if rtsp.error:
                print "Error: {}".format(rtsp.errstr)
        else:
                print "url: %s" % rtsp.get_url ()
                print "CSeq: %d" % rtsp.get_CSeq ()
                print "host: %s" % rtsp.get_host ()
                print "medianame: %s" % rtsp.get_medianame ()
