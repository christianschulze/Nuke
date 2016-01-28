# /Applications/Nuke7.0v4/Nuke7.0v4.app/Nuke7.0v4 -t /Volumes/RAID_03/130411_1309_PayPal_ThePayPalDifference/4_workfiles/NUKE/initialSetup.py

import nuke, sys, os

root = "/Volumes/RAID_03/130411_1309_PayPal_ThePayPalDifference/4_workfiles/NUKE/NIGHTSOUT/"

def runScript(filepath):
    nuke.scriptOpen(filepath)
    r3d = nuke.toNode('Read1')
    r3d.setXYpos(730, -451)
    nuke.toNode('HieroData').setXYpos(730, -359)
    jpg = nuke.toNode('Read2')
    if jpg != None:
        print "has no jpg-read"
        jpg.setXYpos(840, -457)
        nuke.toNode('HieroData1').setXYpos(840, -353)
        first = jpg.knob('first').getValue()
        last = jpg.knob('last').getValue()
        proxy = jpg.knob('file').getValue()
        r3d.knob('first').setValue(first)
        r3d.knob('origfirst').setValue(first)
        r3d.knob('last').setValue(last)
        r3d.knob('origlast').setValue(last)
        r3d.knob('proxy').setValue(proxy)

    nuke.toNode('AddTimeCode1').setXYpos(730, 135)
    nuke.toNode('ModifyMetaData1').setXYpos(730, 159)
    nuke.toNode('Reformat1').setXYpos(730, 183)
    nuke.toNode('Reformat2').setXYpos(840, 183)
    nuke.toNode('Write_preview').setXYpos(730, 217)
    nuke.toNode('Write_master').setXYpos(840, 217)

    nuke.toNode('AddTimeCode1').connectInput(0, nuke.toNode('HieroData'))

    viewer = None
    for n in nuke.allNodes():
        if n.Class() == 'Viewer':
            viewer = n
    if viewer == None:
        print "has no viewer"
        viewer = nuke.createNode("Viewer")
    viewer.setXYpos(730, 263)
    viewer.connectInput(0, nuke.toNode('Write_preview'))
    
    nuke.root().knob('proxy_type').setValue('scale')
    #nuke.scriptSaveAs(filepath.replace(".nk", "_test.nk"), 1)
    nuke.scriptSaveAs(filepath, 1)
    nuke.scriptExit()

filecount = 1
for dirname, dirnames, filenames in os.walk(root):
    for filename in filenames:
        if not filename.endswith(".nk"):
            continue
        filepath = os.path.join(dirname, filename)
        print str(filecount) + ") editing file:"
        print filepath
        runScript(filepath)
        print str(filecount) + ") done!\n"
        filecount += 1
