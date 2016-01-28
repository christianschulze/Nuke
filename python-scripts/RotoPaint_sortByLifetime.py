import nuke.rotopaint as rp

for node in nuke.selectedNodes():
    if node.Class() == 'RotoPaint':
        curvesKnob = node['curves']
        rootLayer = curvesKnob.rootLayer
        i = 0
        while i < len(rootLayer):
            element = rootLayer[i]
            i += 1
            if type(element) == rp.Layer:
                print 'skipping layer ' + element.name
            else:
                attrs = element.getAttributes()
                lt_from = attrs.getValue(0, 'ltm')
                lt_to = attrs.getValue(0, 'ltn')
                layername = 'f'
                if lt_from == lt_to:
                    layername += str(int(lt_from))
                else:
                    layername += str(int(lt_from)) + '_' + str(int(lt_to))
                layer = curvesKnob.toElement(layername)
                if layer == None:
                    print 'creating new layer ' + layername
                    layer = rp.Layer(curvesKnob)
                    layer.name = layername
                    rootLayer.append(layer)
                print 'moving element ' + element.name + ' layer ' + layername
                layer.append(element)
                i -= 1
