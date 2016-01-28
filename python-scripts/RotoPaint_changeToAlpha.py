import nuke.rotopaint as rp

def traverse(root):
    for element in root:
        if type(element) == rp.Layer:
            print 'traversing layer ' + element.name
            traverse(element)
        elif type(element) == rp.Stroke:
            print 'changing stroke ' + element.name + ' to color'
            attrs = element.getAttributes()
            attrs.set(attrs.kSourceAttribute, 0)
        else:
            print 'skipping ' + element.name

for node in nuke.selectedNodes():
    if node.Class() == 'RotoPaint':
        print 'processing node ' + node.name()
        knob = node['curves']
        root = knob.rootLayer
        traverse(root)
