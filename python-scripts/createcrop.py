def createcrop():
    for n in nuke.selectedNodes():
        n['selected'].setValue(False)
    n = nuke.thisNode()
    n.input(0)['selected'].setValue(True)
    c = nuke.createNode("Crop", inpanel = False)
    #c.setInput(0, n.input(0))
    c['box'].fromScript(n['autocropdata'].toScript())
    n.setInput(0, None)

#nuke.execute(nuke.selectedNode(), 1, 1)

#WIP
#c = nuke.toNode('CurveTool1')
#for n in nuke.selectedNodes():
#    c.setInput(0, n)
#    nuke.execute(c, 1, 1)