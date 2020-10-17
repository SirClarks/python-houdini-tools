# python-houdini-tools
A very simple quick and dirty collection of python snippets I've found useful myself

### Last tested in version: Houdini 18.0.532

# kc_cachebackup
Creates a backup of the current hipfile when running a sop filecache. Place the file anywhere you'd like and call it in the pre-render script `exec(open('file/path/here').read())` 

![Image of pre-render script location](https://drive.google.com/uc?export=view&id=1KNsFZQXUcTeIGuAscgIbLGFNZGMu8Hn9)

By default the new file should be created in same directory as your bgeos under `/backup/$OS_backup.hip`

# kc_ropgeobackup.py and kc_mantrabackup.py
Are functionally the same as the **kc_cachebackup** just adjusted for mantra and geometry rops. Just point at the scripts using `exec(open('file/path/here').read())` in the pre-render/postrender wherever you need it.

These also work with the ROP Geometery Output and ROP Mantra Render in TOPs.

# kc_memorylog 
This quick script is used to log memory usage of houdini every time it's cooked. It's best used along with [clear log shelf tool](https://github.com/SirClarks/python-houdini-tools/blob/master/shelf/kc_logclear.py), which will simply clean out the log. Just copy & paste the script into a python node and place wherever needed for example after a dopimport:

![Image of an example of the logger use](https://drive.google.com/uc?export=view&id=1EllO6nFwO-6atQp_ndYsoWWvseYvlcv9)

By default it'll be saved under: `$HIP/log/log.txt` 

The output will look like this, you could also just open it up in a text editor as well:

![Image of log.txt output](https://drive.google.com/uc?export=view&id=1ArdARBAL679CS2oKQc57VyxxxsWjHXCc)

# kc_startingtemplate
This script can be pasted into a shelf tool to easily create a "starting template" of network boxes reminicent of the one I've used at work. Feel free to change the size and colors of each individual element.

![Image of template shelftool](https://drive.google.com/uc?export=view&id=1n54SB0OAsjQmKeS-YG9wwMSIotfxlZ43)

# kc_flipbook
Not necessarily the most useful, but if you're environment is setup correctly, and you'd like to save a few clicks. This script can be pasted into a shelf tool to create a flipbook using the frame range and save it to disk at the location specified by a $FLIPBOOK environment variable, which must be set in the project either via the "Project Settings" or a more custom setup, like for example using an edited *houdini_setup_bash* file on linux. Alternatively simply edit the line containing `flippath = hou.getenv("FLIPBOOK")` to whichever static path you'd like. 
