maxRes = 50
space = 10

node = nuke.selectedNode()
w = node.width()
h = node.height()

hasAlpha = 'rgba.alpha' in node.channels()

factor = max(w, h) / maxRes
xRes = w / factor
yRes = h / factor

startX = node.xpos() + 100
startY = node.ypos()

for y in range(1, yRes):
    for x in range(1, xRes):
        xPos = x * factor
        yPos = y * factor

        a = 1
        if hasAlpha:
            a = node.sample('alpha', xPos, yPos, factor, factor)
        if a > 0:
            r = node.sample('red', xPos, yPos, factor, factor)
            g = node.sample('green', xPos, yPos, factor, factor)
            b = node.sample('blue', xPos, yPos, factor, factor)
            r = nuke.expr('to_sRGB(%s)' % r)
            g = nuke.expr('to_sRGB(%s)' % g)
            b = nuke.expr('to_sRGB(%s)' % b)
            a = 255
            c = int('%02x%02x%02x%02x' % (r, g, b, a), 16)

            dot = nuke.nodes.Dot(tile_color = c, hide_input = True)
            dot.setXYpos(startX + x * space, startY - y * space)
