
############################# PULL MEDIA #############################
# pull media from remote to local at intervals
# check /proc/SERVERPID/fd, if there are /usr/local/movies/remote/media be opened, pull it,
#
# [root@VOD-VSS-5 fd]# ps axf | grep Video
# 14163 pts/1    S+     0:00          \_ grep Video
#  6712 ?        Ss     0:00 /usr/local/sbin/VideoStreamingServer
#  6713 ?        Sl     6:48  \_ /usr/local/sbin/VideoStreamingServer
#
# [root@VOD-VSS-5 run]# pwd
# /var/run
# [root@VOD-VSS-5 run]# cat VideoStreamingServer.pid
# 6712
# 6713
#
# [root@VOD-VSS-5 fd]# pwd
# /proc/6713/fd
# [root@VOD-VSS-5 fd]# ls -l
# total 0
# lrwx------ 1 root root 64 May 19 10:23 0 -> /dev/null
# lrwx------ 1 root root 64 May 19 10:23 1 -> /dev/null
# lrwx------ 1 root root 64 May 19 10:23 10 -> socket:[21835]
# lr-x------ 1 root root 64 May 19 10:23 100 -> /usr/local/movies/remote/41223t1205181800.tsx
# lrwx------ 1 root root 64 May 19 10:23 101 -> socket:[2524852]
# lrwx------ 1 root root 64 May 19 10:23 102 -> socket:[2524385]
# lrwx------ 1 root root 64 May 19 10:23 103 -> socket:[2511508]
# lr-x------ 1 root root 64 May 19 10:23 104 -> /usr/local/movies/remote/41238t1205162226.ts
# lr-x------ 1 root root 64 May 19 10:23 105 -> /usr/local/movies/remote/41238t1205162226.tsx
# lrwx------ 1 root root 64 May 19 10:23 106 -> socket:[2511510]
# lr-x------ 1 root root 64 May 19 10:23 107 -> /usr/local/movies/remote/41222t1205180635.ts
# lr-x------ 1 root root 64 May 19 10:23 108 -> /usr/local/movies/remote/41222t1205180635.tsx
# lrwx------ 1 root root 64 May 19 10:23 109 -> socket:[2524387]
# lrwx------ 1 root root 64 May 19 10:23 11 -> socket:[21836]
# lrwx------ 1 root root 64 May 19 10:23 110 -> socket:[2526236]
# lr-x------ 1 root root 64 May 19 10:23 111 -> /usr/local/movies/remote/41234t1205190732.ts
# lr-x------ 1 root root 64 May 19 10:23 112 -> /usr/local/movies/remote/41234t1205190732.tsx
# lrwx------ 1 root root 64 May 19 10:23 113 -> socket:[2526238]
# lrwx------ 1 root root 64 May 19 10:23 114 -> socket:[2525279]
# lr-x------ 1 root root 64 May 19 10:23 115 -> /usr/local/movies/remote/41223t1205181800.ts
# lr-x------ 1 root root 64 May 19 10:23 116 -> /usr/local/movies/remote/41223t1205181800.tsx
# lrwx------ 1 root root 64 May 19 10:23 117 -> socket:[2525281]
# lrwx------ 1 root root 64 May 19 10:23 118 -> socket:[2526620]
# lrwx------ 1 root root 64 May 19 10:23 119 -> socket:[2526508]
# lrwx------ 1 root root 64 May 19 10:23 12 -> socket:[21837]
# lr-x------ 1 root root 64 May 19 10:23 120 -> /usr/local/movies/remote/41217t1205181900.ts
# lr-x------ 1 root root 64 May 19 10:23 121 -> /usr/local/movies/remote/41217t1205181900.tsx
# lrwx------ 1 root root 64 May 19 10:23 122 -> socket:[2526622]
# lrwx------ 1 root root 64 May 19 10:23 123 -> socket:[2526857]
# lr-x------ 1 root root 64 May 19 10:23 124 -> /usr/local/movies/remote/41238t1205171605.ts
# lr-x------ 1 root root 64 May 19 10:23 125 -> /usr/local/movies/remote/41238t1205171605.tsx
# lrwx------ 1 root root 64 May 19 10:23 126 -> socket:[2526859]
# lrwx------ 1 root root 64 May 19 10:23 127 -> socket:[2493001]
# lr-x------ 1 root root 64 May 19 10:23 128 -> /usr/local/movies/remote/41223t1205181800.ts
# lr-x------ 1 root root 64 May 19 10:23 129 -> /usr/local/movies/remote/41223t1205181800.tsx
# lrwx------ 1 root root 64 May 19 10:23 13 -> socket:[21996]
# lrwx------ 1 root root 64 May 19 10:23 130 -> socket:[2493003]
# lrwx------ 1 root root 64 May 19 10:23 14 -> socket:[21997]
# lrwx------ 1 root root 64 May 19 10:23 15 -> /var/streaming/logs/StreamingServer.log
# lrwx------ 1 root root 64 May 19 10:23 16 -> /var/streaming/logs/mp3_access.log
# lrwx------ 1 root root 64 May 19 10:23 17 -> socket:[22004]
# lrwx------ 1 root root 64 May 19 10:23 18 -> socket:[22005]
# lrwx------ 1 root root 64 May 19 10:23 19 -> socket:[22006]
# lrwx------ 1 root root 64 May 19 10:23 2 -> /dev/null
# lrwx------ 1 root root 64 May 19 10:23 20 -> socket:[22007]
# lrwx------ 1 root root 64 May 19 10:23 21 -> socket:[22008]
# lrwx------ 1 root root 64 May 19 10:23 22 -> socket:[22009]
# lrwx------ 1 root root 64 May 19 10:23 23 -> socket:[22010]
# lrwx------ 1 root root 64 May 19 10:23 24 -> socket:[22011]
# lrwx------ 1 root root 64 May 19 10:23 25 -> socket:[22012]
# lrwx------ 1 root root 64 May 19 10:23 26 -> socket:[22013]
# lrwx------ 1 root root 64 May 19 10:23 27 -> socket:[22014]
# lrwx------ 1 root root 64 May 19 10:23 28 -> socket:[22015]
# lrwx------ 1 root root 64 May 19 10:23 29 -> socket:[22016]
# lr-x------ 1 root root 64 May 19 10:23 3 -> eventpoll:[21828]
# lrwx------ 1 root root 64 May 19 10:23 30 -> socket:[22017]
# lrwx------ 1 root root 64 May 19 10:23 31 -> socket:[2526065]
# lr-x------ 1 root root 64 May 19 10:23 32 -> /usr/local/movies/remote/41237t1205171953.ts
# lr-x------ 1 root root 64 May 19 10:23 33 -> /usr/local/movies/remote/41237t1205171953.tsx
# lrwx------ 1 root root 64 May 19 10:23 34 -> socket:[2526067]
# lrwx------ 1 root root 64 May 19 10:23 35 -> socket:[2523780]
# lr-x------ 1 root root 64 May 19 10:23 36 -> /usr/local/movies/remote/41234t1205172213.ts
# lr-x------ 1 root root 64 May 19 10:23 37 -> /usr/local/movies/remote/41234t1205172213.tsx
# lrwx------ 1 root root 64 May 19 10:23 38 -> socket:[2523782]
# lrwx------ 1 root root 64 May 19 10:23 39 -> socket:[2525992]
# lrwx------ 1 root root 64 May 19 10:23 4 -> socket:[21829]
# lrwx------ 1 root root 64 May 19 10:23 40 -> socket:[2523449]
# lr-x------ 1 root root 64 May 19 10:23 41 -> /usr/local/movies/remote/41223t1205180055.ts
# lr-x------ 1 root root 64 May 19 10:23 42 -> /usr/local/movies/remote/41223t1205180055.tsx
# lrwx------ 1 root root 64 May 19 10:23 43 -> socket:[2527004]
# lr-x------ 1 root root 64 May 19 10:23 44 -> /usr/local/movies/remote/41237t1205170644.ts
# lr-x------ 1 root root 64 May 19 10:23 45 -> /usr/local/movies/remote/41237t1205170644.tsx
# lrwx------ 1 root root 64 May 19 10:23 46 -> socket:[2527005]
# lrwx------ 1 root root 64 May 19 10:23 47 -> socket:[2525212]
# lr-x------ 1 root root 64 May 19 10:23 48 -> /usr/local/movies/remote/41243t1205171017.ts
# lr-x------ 1 root root 64 May 19 10:23 49 -> /usr/local/movies/remote/41243t1205171017.tsx
# lrwx------ 1 root root 64 May 19 10:23 5 -> socket:[21830]
# lrwx------ 1 root root 64 May 19 10:23 50 -> socket:[2525214]
# lr-x------ 1 root root 64 May 19 10:23 51 -> /usr/local/movies/remote/41223t1205160855.ts
# lr-x------ 1 root root 64 May 19 10:23 52 -> /usr/local/movies/remote/41223t1205160855.tsx
# lrwx------ 1 root root 64 May 19 10:23 53 -> socket:[2523451]
# lrwx------ 1 root root 64 May 19 10:23 54 -> socket:[2522891]
# lrwx------ 1 root root 64 May 19 10:23 55 -> socket:[2515753]
# lr-x------ 1 root root 64 May 19 10:23 56 -> /usr/local/movies/remote/41223t1205172325.ts
# lr-x------ 1 root root 64 May 19 10:23 57 -> /usr/local/movies/remote/41223t1205172325.tsx
# lrwx------ 1 root root 64 May 19 10:23 58 -> socket:[2515755]
# lrwx------ 1 root root 64 May 19 10:23 59 -> socket:[2525994]
# lrwx------ 1 root root 64 May 19 10:23 6 -> socket:[21831]
# lrwx------ 1 root root 64 May 19 10:23 60 -> socket:[2527028]
# lr-x------ 1 root root 64 May 19 10:23 61 -> /usr/local/movies/remote/41223t1205170335.ts
# lr-x------ 1 root root 64 May 19 10:23 62 -> /usr/local/movies/remote/41223t1205170335.tsx
# lr-x------ 1 root root 64 May 19 10:23 63 -> /usr/local/movies/remote/41232t1205161235.ts
# lr-x------ 1 root root 64 May 19 10:23 64 -> /usr/local/movies/remote/41232t1205161235.tsx
# lrwx------ 1 root root 64 May 19 10:23 65 -> socket:[2522893]
# lrwx------ 1 root root 64 May 19 10:23 66 -> socket:[2523093]
# lrwx------ 1 root root 64 May 19 10:23 67 -> socket:[2527030]
# lrwx------ 1 root root 64 May 19 10:23 68 -> socket:[2524606]
# lrwx------ 1 root root 64 May 19 10:23 69 -> socket:[2525270]
# lr-x------ 1 root root 64 May 19 10:23 70 -> /usr/local/movies/remote/41228t1205180632.ts
# lr-x------ 1 root root 64 May 19 10:23 71 -> /usr/local/movies/remote/41218t1205160508.ts
# lr-x------ 1 root root 64 May 19 10:23 72 -> /usr/local/movies/remote/41218t1205160508.tsx
# lrwx------ 1 root root 64 May 19 10:23 73 -> socket:[2523095]
# lr-x------ 1 root root 64 May 19 10:23 74 -> /usr/local/movies/remote/41228t1205180632.tsx
# lrwx------ 1 root root 64 May 19 10:23 75 -> socket:[2526198]
# lr-x------ 1 root root 64 May 19 10:23 76 -> /usr/local/movies/remote/41233t1205171930.ts
# lr-x------ 1 root root 64 May 19 10:23 77 -> /usr/local/movies/remote/41233t1205171930.tsx
# lrwx------ 1 root root 64 May 19 10:23 78 -> socket:[2526200]
# lrwx------ 1 root root 64 May 19 10:23 79 -> socket:[2525272]
# lrwx------ 1 root root 64 May 19 10:23 8 -> /var/streaming/logs/Error.log
# lr-x------ 1 root root 64 May 19 10:23 80 -> /usr/local/movies/remote/41223t1205170745.ts
# lr-x------ 1 root root 64 May 19 10:23 81 -> /usr/local/movies/remote/41223t1205170745.tsx
# lrwx------ 1 root root 64 May 19 10:23 82 -> socket:[2524608]
# lrwx------ 1 root root 64 May 19 10:23 83 -> socket:[2526452]
# lr-x------ 1 root root 64 May 19 10:23 84 -> /usr/local/movies/remote/41237t1205170644.ts
# lr-x------ 1 root root 64 May 19 10:23 85 -> /usr/local/movies/remote/41237t1205170644.tsx
# lrwx------ 1 root root 64 May 19 10:23 86 -> socket:[2526454]
# lrwx------ 1 root root 64 May 19 10:23 87 -> socket:[2526506]
# lr-x------ 1 root root 64 May 19 10:23 88 -> /usr/local/movies/remote/41234t1205181150.ts
# lr-x------ 1 root root 64 May 19 10:23 89 -> /usr/local/movies/remote/41234t1205181150.tsx
# lrwx------ 1 root root 64 May 19 10:23 9 -> socket:[21834]
# lrwx------ 1 root root 64 May 19 10:23 90 -> socket:[2524848]
# lrwx------ 1 root root 64 May 19 10:23 91 -> socket:[2527007]
# lr-x------ 1 root root 64 May 19 10:23 92 -> /usr/local/movies/remote/41234t1205190825.ts
# lr-x------ 1 root root 64 May 19 10:23 93 -> /usr/local/movies/remote/41234t1205190825.tsx
# lrwx------ 1 root root 64 May 19 10:23 94 -> socket:[2527011]
# lrwx------ 1 root root 64 May 19 10:23 95 -> socket:[2515713]
# lr-x------ 1 root root 64 May 19 10:23 96 -> /usr/local/movies/remote/41238t1205171605.ts
# lr-x------ 1 root root 64 May 19 10:23 97 -> /usr/local/movies/remote/41238t1205171605.tsx
# lrwx------ 1 root root 64 May 19 10:23 98 -> socket:[2515715]
# lr-x------ 1 root root 64 May 19 10:23 99 -> /usr/local/movies/remote/41223t1205181800.ts
#
########################## REMOVE MEDIA ###############################
# remove "old" movies at midnight.
# old VOD is the media have not been access for many days.
# old recorded tv program is the media recorded 5 days ago 

import os
import glob
import fileinput
import string
import logging
import shutil

LOCAL = "/usr/local/movies/"
PULLD = "/usr/local/movies/pulld/"
REMOTE = "/usr/local/movies/remote"

def getvssprocpath ():
        procpath = []
        for l in fileinput.input ("/var/run/VideoStreamingServer.pid"):
                procpath.append ("/proc/%s/fd" % l.strip ())
        return procpath

if __name__ == '__main__':
        logging.basicConfig (format='%(asctime)s %(message)s', filename='/var/log/pull.log',level=logging.DEBUG)
        logger = logging.getLogger ()
        procpath = getvssprocpath ()
        for path in procpath:
                # check remot open medias
                remotemedia = glob.glob ("%s/*" % path)
                for f in remotemedia:
                        if string.find (os.path.realpath (f), REMOTE) == 0:
                                if glob.glob ("%s%s" % (LOCAL, (os.path.realpath (f)[25:]))):
                                        # the media exist in local storage, bypass
                                        continue
                                if glob.glob ("%s%s" % (PULLD, (os.path.realpath (f)[25:]))):
                                        # have pulled to pulld, wait move to local
                                        continue
                                shutil.copy (os.path.realpath (f), PULLD)
                                logger.info("pull %s" % os.path.realpath (f))

                # move from pulld to /usr/local/movies
                pullmedia = glob.glob ("%s*" % PULLD)
                for f in pullmedia:
                        shutil.move (f, LOCAL)
