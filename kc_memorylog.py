node = hou.pwd()
geo = node.geometry()

# just copy paste this into a python node and place after your dopnet/importfield
# this is a very quick and dirty script to log memory in a text file, just change 
# the path variable to where you need it to go. Default is $HIP/log/log.txt
# works best in conjunction with the clear log shelf tool

memory = hou.hscript('memory')
frame = hou.frame()

# change path here if needed
path = "$HIP/log/log.txt"

# write to file here
file = f=open("%s" % path, "a+")
file.write("{} {}\r\n".format(frame, memory))
file.close()
