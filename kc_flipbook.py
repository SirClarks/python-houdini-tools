# Simple script to generate flipbook and save to disk.
# Just copy & paste this into a shelf tool

import hou
import os

cur_desktop = hou.ui.curDesktop()
scene = cur_desktop.paneTabOfType(hou.paneTabType.SceneViewer)

# Copy the viewer's current flipbook settings
flipbook_options = scene.flipbookSettings().stash()

# get range
range = hou.playbar.playbackRange()

# set resolution
resolution = (1280,720)

# output path edit this
# path = "~/FX/UTILITY/$F4.jpg"

# use this path if you've set a $FLIPBOOK env veriable
flippath = hou.getenv("FLIPBOOK")
path = flippath + "$F.jpg"

# Change the settings however you need
# (for example, set the frame range and output filename)
flipbook_options.frameRange( (int(range[0]), int(range[1])) )
flipbook_options.output(path)
#flipbook_options.resolution((1920,1080))
flipbook_options.resolution((int(resolution[0]),int(resolution[1])))
flipbook_options.cropOutMaskOverlay(1)

# Generate the flipbook using the modified settings
scene.flipbook(scene.curViewport(), flipbook_options)
