# python-houdini-tools
A very simple quick and dirty collection of python snippets

## kc_cachebackup
Creates a backup of the current hipfile when running a sop filecache. Place the file anywhere you'd like and call it in the pre-render script `exec(open('file/path/here').read())` 

![Image of pre-render script location](https://i.imgur.com/KHeAcA3.png)

By default the new file should be created in same directory as your bgeos under `/backup/$OS_backup.hip`
