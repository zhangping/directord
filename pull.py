
# pull movie from remote to local at intervals
# check /var/streaming/logs/StreamingServer.log, if there are new media being accessed, pull it,
# new media means it is not in locale storage.
#
# remove "old" movies at midnight.
# old VOD is the media have not been access for many days.
# old recorded tv program is the media recorded 5 days ago 
