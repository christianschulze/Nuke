for n in nuke.allNodes():
    if n.Class() == 'Read' or n.Class() == 'ReadGeo2' or n.Class() == 'Camera2' or n.Class() == 'Axis2':
        print n['file'].value()
