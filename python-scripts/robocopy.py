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
            if '\#' in filepath or '%' in filepath: # it's possibly a sequence
                filepath = os.path.dirname(filepath) # convert to folder path
            if filepath[1] != ':': # no drive letter, so we assume relative paths
                project_dir = nuke.Root()['project_directory'].value()
                if not project_dir.endswith('/'):
                    project_dir += '/'
                filepath = project_dir + filepath
            if os.path.exists(filepath):
                pathlist.append(filepath) # save the path to the path list
            else:
                print "path doesn't exist: " + filepath

pathlist = sorted(set(pathlist)) # sort the path list alphabetically

destination = nuke.getFilename('Destination folder', pattern = '*/')

def copy():
    task = nuke.ProgressTask('Copying all inputs...') # create a progress bar
    progIncr = 100.0 / len(pathlist) # calculate the increment for the progress
    for i, src in enumerate(pathlist):
        (src_drive, src_tail) = os.path.splitdrive(src)
        dst = os.path.join(destination, src_tail.lstrip('/\\')) # change just the drive letter for the destination to preserve the folder structure
        src = os.path.normpath(src)
        dst = os.path.normpath(dst)
        print 'copying ' + src + ' to ' + dst
        cmd_src = src
        cmd_dst = dst
        cmd_file = '*.*'
        if os.path.isfile(src):
            cmd_src = os.path.dirname(src)
            cmd_dst = os.path.dirname(dst)
            cmd_file = os.path.basename(src)
        cmd = ['robocopy', cmd_src, cmd_dst, cmd_file, '/R:0'] # command line
        proc = subprocess.Popen(cmd, stdout = subprocess.PIPE) # start the command line process
        task.setProgress(int(i * progIncr)) # update the progress
        task.setMessage(os.path.basename(src)) # inform about the item that is currently copied

        while proc.poll() is None: # wait for the copy process to finish for the current folder
            for line in proc.stdout:
                print line
            if task.isCancelled():
                return

        if i == len(pathlist) - 1:
            print 'finished robocopy'

if destination != None:
    threading.Thread(target = copy).start() # start copy in a separate thread so the UI is still responsive and the progress bar is updated
