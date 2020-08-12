# Simple script to save a backup of the file used when running a filecache sop
# place this file anywhere on your system and it can be executed with
# exec(open('file_path_here').read()) inside the Pre-Render Script section
# also don't forget to set the dropdown Hscript to python
import hou

# necessary for creation of intermittent directories
import os

# Special note, since running the file cache, this node is actually the
# ROP Geometery Output found inside the filecache otl, the parent is the
# interactive filecache node itself
node = hou.pwd()
parent = node.parent()

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

# save file path as name of filecache node similar to $OS opname(".")
filepath += 'backup/' + str(parent) + '_backup.hip'
hou.hipFile.save(file_name=filepath, save_to_recent_files=False)

# return back to original filename due to switching over from hipFile.save
hou.hipFile.setName(currentfilepath)
