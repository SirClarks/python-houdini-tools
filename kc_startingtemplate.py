# Simple script to generate a starting template of network boxes
# Just copy & paste this into a shelf tool

import hou
n = hou.node('/obj')
# n = hou.pwd()

# globals
default_size = (8,3.25)
default_color = hou.Color(.5,.5,.5)

# asset box
asset_size = (4,3.25)
asset_color = default_color
asset_position = (4.2,0)
asset_box = n.createNetworkBox("assets")
asset_box.setComment("Assets")
asset_box.setSize(asset_size)
asset_box.setColor(asset_color)
asset_box.setPosition(asset_position)

# scene box
scene_size = default_size
scene_color = default_color
scene_position = (-4,0)
scene_box = n.createNetworkBox("scene")
scene_box.setComment("Scene")
scene_box.setSize(scene_size)
scene_box.setColor(scene_color)
scene_box.setPosition(scene_position)

# geoprep box
geo_size = default_size
geo_color = default_color
geo_position = (-4,-3.8)
geo_box = n.createNetworkBox("geoprep")
geo_box.setComment("Geo Prep")
geo_box.setSize(geo_size)
geo_box.setColor(geo_color)
geo_box.setPosition(geo_position)

# sim box
sim_size = default_size
sim_color = default_color
sim_position = (-4,-7.6)
sim_box = n.createNetworkBox("sim")
sim_box.setComment("Sim")
sim_box.setSize(sim_size)
sim_box.setColor(sim_color)
sim_box.setPosition(sim_position)

# render box
render_size = default_size
render_color = default_color
render_position = (-4,-11.4)
render_box = n.createNetworkBox("render")
render_box.setComment("Render")
render_box.setSize(render_size)
render_box.setColor(render_color)
render_box.setPosition(render_position)

# added popup in an attempt to prevent multiple repetitve clicks on tool.
hou.ui.displayMessage('Starting Template Created')
