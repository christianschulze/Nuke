import sys, os, fileinput

root = "/Volumes/RAID_03/130411_1309_PayPal_ThePayPalDifference/4_workfiles/NUKE/NIGHTSOUT/"
versionTCL = "\[python\ \{nuke.root()\['name'].value().rsplit('_v',1)\[1].replace('.nk','')\}]"

for dirname, dirnames, filenames in os.walk(root):
    for filename in filenames:
        if not ".nk" in filename:
            continue
        filepath = os.path.join(dirname, filename)
        print filepath
        for line in fileinput.input(filepath, inplace=1):
            if "_####.dpx" in line or "_####.png" in line:
                line = line.replace("_v01", "_v" + versionTCL)
            if "colorspace linear" in line or 'colorspace "linear"' in line:
                line = line.replace("linear", "Cineon" + versionTCL)
            sys.stdout.write(line)
