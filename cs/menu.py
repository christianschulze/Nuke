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
nuke.knobDefault('Read.label', '[lindex [value format] end]\n[value first]-[value last]')
nuke.knobDefault('TimeOffset.label', '[value time_offset]')
nuke.knobDefault('Retime.shutter', '{1/speed}')
nuke.knobDefault('Card.rows', '2')
nuke.knobDefault('Card.columns', '2')
nuke.knobDefault('OFlow.input.first', '{input.first_frame}')
nuke.knobDefault('OFlow.input.last', '{input.last_frame}')
nuke.knobDefault('Kronos.input.first', '{input.first_frame}')
nuke.knobDefault('Kronos.input.last', '{input.last_frame}')
nuke.knobDefault('Shuffle.label', '[value in]')

def switch_color():
    if nuke.thisNode().knob('which').getValue() > 0 and not nuke.thisNode().knob('disable').getValue():
        nuke.thisNode().knob('tile_color').setValue(0x00ff00ff)
    else:
        nuke.thisNode().knob('tile_color').setValue(0xff0000ff)
nuke.addKnobChanged(switch_color, nodeClass='Switch')

# Menu
toolbar = nuke.menu('Nodes')
filterMenu = toolbar.findItem('Filter')
colorMenu = toolbar.findItem('Color')

erode = filterMenu.findItem('Erode (filter)')
filterMenu.addCommand(erode.name(), erode.script(), 'e', erode.icon())

filterMenu.addCommand('AlphaBlur', 'nuke.createNode("Blur", "channels alpha")', 'shift+b', "Blur.png")
colorMenu.addCommand('AlphaGrade', 'nuke.createNode("Grade", "channels alpha white_clamp 1")', 'shift+g', "Grade.png")

toolbar.addCommand('Transform/Reformat', 'nuke.createNode("Reformat")', 'ctrl+r')

toolbar.addMenu('cs', icon='cs.png')

# Gizmos
toolbar.addCommand('cs/CS_HeatDistortion', 'nuke.createNode("CS_HeatDistortion")')
toolbar.addCommand('cs/CS_ColorPicker', 'nuke.createNode("CS_ColorPicker")')
toolbar.addCommand('cs/CS_DistanceBetween', 'nuke.createNode("CS_DistanceBetween")')
toolbar.addCommand('cs/CS_MapValue', 'nuke.createNode("CS_MapValue")')
toolbar.addCommand('cs/CS_Haze', 'nuke.createNode("CS_Haze")')
toolbar.addCommand('cs/CS_Ghost', 'nuke.createNode("CS_Ghost")')
toolbar.addCommand('cs/CS_ChromaticAbberation', 'nuke.createNode("CS_ChromaticAbberation")')
toolbar.addCommand('cs/CS_RoughenEdges', 'nuke.createNode("CS_RoughenEdges")')
toolbar.addCommand('cs/CS_Backdrop', 'nuke.nodes.BackdropNode(label = \'<center><img src="cs.png">\', tile_color = ' + str(int('99000000', 16)) + ')')
# color is hex to int with alpha (rgba): #cc000000 = 3422552064

# Scripts

