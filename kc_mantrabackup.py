# Simple script to save a backup of the file used to create a rop output 
# from either ROP Geometry Output TOP node or regular /out/ one.
# place in a file anywhere needed and it can be executed with
# exec(open('file_path_here').read()) inside the Pre-Render Script section
# also don't forget to dropdown Hscript to python
import hou

# necessary for creation of intermittent directories
import os

node = hou.pwd()

# edit filepath using vm_picture parm
currentfilepath = hou.hipFile.path()
filepath = node.evalParm('vm_picture')
filepath = filepath.split('/')
del filepath[-1]

seperator = '/'
filepath = seperator.join(filepath) + '/'

# check if file path doesn't exists, make if not
if not os.path.exists(filepath):
    os.makedirs(filepath)

# save file path as name of filecache node similar to $OS opname(".")
filepath += 'backup/' + str(node) + '_backup.hip'
hou.hipFile.save(file_name=filepath, save_to_recent_files=False)

# return back to original filename due to switching over from hipFile.save
hou.hipFile.setName(currentfilepath)
