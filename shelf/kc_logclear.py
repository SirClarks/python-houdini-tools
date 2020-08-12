# Simply create a new shelf tool
# then copy paste this into a shelf tool script tab.
# This is meant to work alongside the kc_memorylog.py

import hou
hip= hou.getenv("HIP")
path = "{}/log/log.txt".format(hip)
open("{}".format(path), 'w').close()
hou.ui.displayMessage('Log should have cleared')
