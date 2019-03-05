import nuke

prefs = nuke.toNode('preferences')
grid_width = prefs['GridWidth'].getValue()
grid_height = prefs['GridHeight'].getValue()


def snap_knob_to_grid(knob, grid_value):
    value = knob.getValue()
    base = 2 * grid_value
    new_value = int(base * round(float(value) / base))
    knob.setValue(new_value)

def resize_knob_to_grid(knob):
    snap = False
    if knob.name() == 'bdwidth':
        snap_knob_to_grid(knob, grid_width)
        snap = True
    if knob.name() == 'bdheight':
        snap_knob_to_grid(knob, grid_height)
        snap = True
    if snap:
        nuke.autoplaceSnap(knob.node())

def resize_knob_to_grid_callback():
    knob = nuke.thisKnob()
    resize_knob_to_grid(knob)

def create_snappy_backdrop():
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
    bdW += grid_width * 1.5
    bdH += grid_height * 1.5 + headroom

    # create the backdrop
    n = nuke.nodes.BackdropNode(xpos = bdX, ypos = bdY, bdwidth = bdW, bdheight = bdH, note_font_size = 42)

    # revert to previous selection
    n['selected'].setValue(False)
    for node in selNodes:
        node['selected'].setValue(True)

def snap_all_backdrops():
    backdrops = nuke.allNodes('BackdropNode')
    for backdrop in backdrops:
        resize_knob_to_grid(backdrop.knob('bdwidth'))
        resize_knob_to_grid(backdrop.knob('bdheight'))

# add the resize to grid callback
nuke.addKnobChanged(resize_knob_to_grid_callback, nodeClass = 'BackdropNode')

# overwrite the backdrop creation command
toolbar = nuke.menu('Nodes')
otherMenu = toolbar.findItem('Other')
otherMenu.addCommand('Backdrop', 'CS_SnappyBackdrops.create_snappy_backdrop()', 'alt+b', icon = "Backdrop.png")
