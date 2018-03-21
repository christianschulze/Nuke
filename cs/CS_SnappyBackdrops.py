import nuke

prefs = nuke.toNode('preferences')
grid_width = prefs['GridWidth'].getValue()
grid_height = prefs['GridHeight'].getValue()

def resize_to_grid():
    n = nuke.thisNode()
    k = nuke.thisKnob()
    if knob_to_grid(k, 'bdwidth', grid_width) or knob_to_grid(k, 'bdheight', grid_height):
        nuke.autoplaceSnap(n)

def knob_to_grid(knob, knob_name, grid_value):
    if knob.name() == knob_name:
        value = knob.getValue()
        base = 2 * grid_value
        new_value = int(base * round(float(value) / base))
        knob.setValue(new_value)
        return True
    return False

def resizeBackdrop():
    selNodes = nuke.selectedNodes()
    if not selNodes:
        return nuke.nodes.BackdropNode()

    # Calculate bounds for the backdrop node.
    bdX = min([node.xpos() for node in selNodes])
    bdY = min([node.ypos() for node in selNodes])
    bdW = max([node.xpos() + node.screenWidth() for node in selNodes]) - bdX
    bdH = max([node.ypos() + node.screenHeight() for node in selNodes]) - bdY

    headroom = 4 * grid_height
    bdX -= grid_width * 0.5
    bdY -= grid_height * 0.5 + headroom
    bdW += grid_width * 1.0
    bdH += grid_height * 1.0 + headroom

    # create the backdrop
    n = nuke.nodes.BackdropNode(xpos = bdX, ypos = bdY, bdwidth = bdW, bdheight = bdH, note_font_size = 42)

    # revert to previous selection
    n['selected'].setValue(False)
    for node in selNodes:
        node['selected'].setValue(True)

# add the resize to grid callback
nuke.addKnobChanged(resize_to_grid, nodeClass = 'BackdropNode')

# overwrite the backdrop creation command
toolbar = nuke.menu('Nodes')
otherMenu = toolbar.findItem('Other')
otherMenu.addCommand('Backdrop', 'CS_SnappyBackdrops.resizeBackdrop()', 'alt+b', icon = "Backdrop.png")
