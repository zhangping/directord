# -*- coding: utf-8 -

# This file - route.py, is part of directord.

import re

def dispatchvod (medianame):
        return "192.168.1.13"

def route (medianame):
        if re.match ("^VOD\S+", medianame): # VOD find
                return dispatchvod (medianame)

        if re.match ("^1234\S+", medianame): # CCTV-1 find
                return "192.168.1.15"

        return None

if __name__ == "__main__":
        medianame = "VODC2011011613583204.ts"
        print "%s ---> %s" % (medianame, route (medianame))
        medianame = "1234VODC2011011613583204.ts"
        print "%s ---> %s" % (medianame, route (medianame))
