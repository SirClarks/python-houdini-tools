# python-houdini-tools
A very simple quick and dirty collection of python snippets I've found useful myself

**Last tested in version: Houdini 18.0.532**

## kc_cachebackup
Creates a backup of the current hipfile when running a sop filecache. Place the file anywhere you'd like and call it in the pre-render script `exec(open('file/path/here').read())` 

![Image of pre-render script location](https://i.imgur.com/KHeAcA3.png)

By default the new file should be created in same directory as your bgeos under `/backup/$OS_backup.hip`

## kc_ropgeobackup.py and kc_mantrabackup.py
Are functionally the same as the **kc_cachebackup** just adjusted for mantra and geometry rops. Just point at the scripts using `exec(open('file/path/here').read())` in the pre-render/postrender wherever you need it.

These also work with the ROP Geometery Output and ROP Mantra Render in TOPs.
