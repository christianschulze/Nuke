import nuke

prefs = nuke.toNode('preferences')
grid_width = prefs['GridWidth'].getValue()
grid_height = prefs['GridHeight'].getValue()

def resize_to_grid():
    n = nuke.thisNode();
    k = nuke.thisKnob();
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

nuke.addKnobChanged(resize_to_grid, nodeClass = 'BackdropNode')
