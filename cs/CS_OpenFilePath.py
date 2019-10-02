import os.path
import platform
import subprocess
import nuke

def open_file_knob_of_selected_node():
    try:
        node = nuke.selectedNode()
        open_file_knob(node)
    except ValueError:
        nuke.message("No Node selected.")

def open_file_knob(node):
    file = node['file'].evaluate()
    if os.path.isfile(file):
        # print "opening: " + file
        open_path(file, True)
    else:
        dir = os.path.dirname(file)
        if os.path.isdir(dir):
            # print "opening: " + dir
            open_path(dir, False)
        else:
            nuke.message("Path does not exist.")

def open_path(path, is_select):
    if platform.system() == "Windows":
        if is_select:
            subprocess.Popen(["explorer", "/select,", os.path.normpath(path)])
        else:
            subprocess.Popen(["explorer", os.path.normpath(path)])
    elif platform.system() == "Darwin":
        if is_select:
            subprocess.Popen(["open", "-R", path])
        else:
            subprocess.Popen(["open", path])
    else:
        subprocess.Popen(["xdg-open", path])
