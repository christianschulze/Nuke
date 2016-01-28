import os.path
import subprocess
import threading


pathlist = []
pathlist.append(nuke.root().name()) # add nuke script to path list

for n in nuke.allNodes():
    k = n.knob('file') # get the file knob
    if n.Class() == 'Write' and not n['reading'].getValue(): continue # skip paths from Write nodes that don't read
    isdisabled = n.knob('disable')
    if isdisabled is not None and isdisabled.getValue(): continue # skip nodes that are disabled
    if len(n.dependent()) == 0: continue # skip nodes that are not connected to other nodes in any way
    if k is not None:
        filepath = k.getValue() # get the path from the file knob
        if filepath is not '':
            pathlist.append(filepath) # save the path to the path list

pathlist = sorted(set(pathlist)) # sort the path list alphabetically

destination = nuke.getFilename('Destination folder', pattern = '*/')

def copy():
    task = nuke.ProgressTask('Copying all input folders...') # create a progress bar
    progIncr = 100.0 / len(pathlist) # calculate the increment for the progress
    for i, p in enumerate(pathlist):
        src = os.path.dirname(p) # copy whole directories of the input files
        (src_drive, src_tail) = os.path.splitdrive(src)
        dst = os.path.join(destination, src_tail.lstrip('/\\')) # change just the drive letter for the destination to preserve the folder structure
        src = os.path.normpath(src)
        dst = os.path.normpath(dst)
        print 'copying ' + src + ' to ' + dst
        cmd = ['robocopy', src, dst, '/R:0'] # command line
        proc = subprocess.Popen(cmd, stderr = subprocess.PIPE) # start the command line process
        task.setProgress(int(i * progIncr)) # update the progress
        task.setMessage(os.path.basename(src)) # inform about the folder that is currently copied

        while proc.poll() is None: # wait for the copy process to finish for the current folder
            for line in proc.stderr:
                print line
            if task.isCancelled():
                return

if destination != None:
    threading.Thread(target = copy).start() # start copy in a separate thread so the UI is still responsive and the progress bar is updated
