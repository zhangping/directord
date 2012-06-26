
import os
import sys
import glob
import logging
import logging.handlers
import shutil
import time

LOCAL = "/usr/local/movies/"
PUSHD = "/usr/local/movies/pushd/"
REMOTE = "/usr/local/movies/remote/"

# vss 1 -> 10.49.34.67 (41214, 41215, 41216, 41217, 41218, 41219, 41238, 41239, 41240, 41241, 41242, 41243)
#chs = ["41243", "41238", "41218"] 

# vss 2 -> 10.49.34.68 (41232, 41233, 41234, 41235, 41236, 41237, 41238, 41239, 41240, 41241, 41242, 41243)
#chs = ["41238", "41234", "41233"]

# vss 3 -> 10.49.34.69 (41226, 41227, 41228, 41229, 41230, 41231, 41232, 41233, 41234, 41235, 41236, 41237)
#chs = ["41234", "41233", "41230"]

# vss 4 -> 10.49.34.70 (41220, 41221, 41222, 41223, 41224, 41225, 41226, 41227, 41228, 41229, 41230, 41231)
#chs = ["41223", "41222", "41230"] 

# vss 5 -> 10.49.34.71 (41214, 41215, 41216, 41217, 41218, 41219, 41220, 41221, 41222, 41223, 41224, 41225)
chs = ["41223", "41222", "41218"] 

def GetLogger():
        logger = logging.getLogger()
        # 1M log file, back count 10
        handler = logging.handlers.RotatingFileHandler("/var/log/push.log", 'a', 1024000, 10)
        formatter = logging.Formatter('[%(asctime)s %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.setLevel(logging.DEBUG)
        return logger

if __name__ == "__main__":
        logger = GetLogger ()
        if os.path.exists("/var/run/push"):
                logger.info("A push instance is working, exit...")
                sys.exit(0)
        else:
                logger.info("Start pushing...")
                os.system("touch /var/run/push")
        for c in chs:
                #recorde file pattern 41224t1205281040.ts
                p = "%s%st??????????.*" % (REMOTE, c)
                fs = glob.glob (p)
                for f in fs:
                        if glob.glob ("%s%s" % (LOCAL, (f[25:]))):
                                # the media exist in local storage, bypass
                                continue
                        else:
                                logger.info ("push %s" % f)
                                r = open (f,  'r')
                                w = open ("%s%s" % (PUSHD, f[25:]), 'w')
                                b = r.read (1024*1024)
                                while not (b == ""): # 2M
                                        w.write (b)
                                        w.flush()
                                        time.sleep (0.05)
                                        b = r.read (1024*1024)
                                        if (b == ""): # push a file be coping into storage? reopen and read more.
                                                time.sleep(5)
                                                logger.info("read 0, reopen and seek to %d" % w.tell())
                                                r.close()
                                                r = open(f, 'r')
                                                r.seek(w.tell())
                                                b = r.read(1024*1024)
                                r.close ()
                                w.close ()
                                os.system ("mv %s%s %s" % (PUSHD, f[25:], LOCAL))

        os.system("rm /var/run/push")
