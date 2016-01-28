import nuke.rotopaint as rp

inPoint = nuke.root()['first_frame'].getValue()
outPoint = nuke.root()['last_frame'].getValue()

def traverse(root):
    for element in root:
        if type(element) == rp.Layer:
            print 'traversing layer ' + element.name
            traverse(element)
        elif type(element) == rp.Shape:
            attrs = element.getAttributes()
            for frame in range(inPoint, outPoint + 1):
                feather = attrs.getValue(0, attrs.kFeatherXAttribute)
                if abs(feather) > 2:
                    print element.name + ' (f' + str(frame) + '): ' + str(feather)
                    element.setFlag(rp.FlagType.eSelectedFlag, True)
        else:
            print 'skipping ' + element.name

for node in nuke.selectedNodes():
    if node.Class() == 'RotoPaint' or node.Class() == 'Roto':
        print 'processing node ' + node.name()
        knob = node['curves']
        root = knob.rootLayer
        traverse(root)
    else:
        print 'no RotoPaint or Roto: ' + node.name()
