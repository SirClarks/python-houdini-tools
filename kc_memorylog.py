# just copy paste this into a python node and place after your dopnet/importfield
# this is a very quick and dirty script to log memory in a text file, just change
# the path variable to where you need it to go. Default is $HIP/log/log.txt
# works best in conjunction with the clear log shelf tool

import hou

node = hou.pwd()
geo = node.geometry()

memory = hou.hscript('memory')
frame = hou.frame()

# change path here if needed
path = "$HIP/log/log.txt"

# write to file here
file = f=open("%s" % path, "a+")
file.write("{} {}\r\n".format(frame, memory))
file.close()

# import psutil
# special note, if you're running Ubuntu 18.04+ psutil should be installed by
# default, otherwise you can get it via pip. It's got some nice printouts and
# you could log your system memory as well. I've noticed that my houdini memory
# usuage doesn't always seem to line up with what system monitor is saying
