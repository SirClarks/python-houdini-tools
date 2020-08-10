import hou
hip= hou.getenv("HIP")
path = "{}/log/log.txt".format(hip)
open("{}".format(path), 'w').close()
hou.ui.displayMessage('Log should have cleared')
