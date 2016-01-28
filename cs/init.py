import CS_SnappyBackdrops

# Defaults
nuke.knobDefault('Root.format','HD_1080')
nuke.knobDefault('Root.fps','25')
#nuke.knobDefault('Roto.output', 'alpha')
nuke.knobDefault('Invert.channels', 'alpha')
nuke.knobDefault('CornerPin2D.from1', '0 0')
nuke.knobDefault('CornerPin2D.from2', '{width} 0')
nuke.knobDefault('CornerPin2D.from3', '{width} {height}')
nuke.knobDefault('CornerPin2D.from4', '0 {height}')
nuke.knobDefault('TimeOffset.label', '[value time_offset]')
nuke.knobDefault('Card.rows', '2')
nuke.knobDefault('Card.columns', '2')

#label = '[if {[value which]>0 && ![value disable]} {return "[knob this.tile_color 0x00ff00ff]"} else {return "[knob this.tile_color 0xff0000ff]"}]'
#nuke.knobDefault('Switch.label', label)

def switch_color():
    if nuke.thisNode().knob('which').getValue() > 0 and not nuke.thisNode().knob('disable').getValue():
        nuke.thisNode().knob('tile_color').setValue(0x00ff00ff)
    else:
        nuke.thisNode().knob('tile_color').setValue(0xff0000ff)
nuke.addKnobChanged(switch_color, nodeClass='Switch')

def create_write_dir():
    file = nuke.filename(nuke.thisNode())
    dir = os.path.dirname(file)
    osdir = nuke.callbacks.filenameFilter(dir)
    try:
        os.makedirs(osdir)
        return
    except:
        return
nuke.addBeforeRender(create_write_dir)
