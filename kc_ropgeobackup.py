# Simple script to save a backup of the file used when running a geometry rop
# place this file anywhere on your system and it can be executed with
# exec(open('file_path_here').read()) inside the Pre-Render Script section
# also don't forget to set the dropdown Hscript to python
import hou

# necessary for creation of intermittent directories
import os

node = hou.pwd()

# edit filepath using sopoutput parm
currentfilepath = hou.hipFile.path()
filepath = node.evalParm('sopoutput')
filepath = filepath.split('/')
del filepath[-1]

seperator = '/'
filepath = seperator.join(filepath) + '/'

# check if file path doesn't exists, make if not
if not os.path.exists(filepath):
    os.makedirs(filepath)

# save file path as name of node similar to $OS opname(".")
filepath += 'backup/' + str(node) + '_backup.hip'
hou.hipFile.save(file_name=filepath, save_to_recent_files=False)

# return back to original filename due to switching over from hipFile.save
hou.hipFile.setName(currentfilepath)
