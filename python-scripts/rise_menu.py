toolbar = nuke.menu('Nodes')
filterMenu = toolbar.findItem('Filter')

erode = filterMenu.findItem('Erode (filter)')
filterMenu.addCommand(erode.name(), erode.script(), 'e', erode.icon())

blur = filterMenu.findItem('Blur')
filterMenu.addCommand('AlphaBlur', 'blur = ' + blur.script() + '\nblur["channels"].setValue("alpha")', 'Shift+B', blur.icon())

##nuke.knobDefault("RotoPaint.toolbox", '''brush {
##{ clone opc .1 bs 10}
##{ brush opc .5 }
##}''')
##
##DEFAULTS
##toolbox {selectAll {
##  { selectAll str 1 ssx 1 ssy 1 sf 1 }
##  { createBezier str 1 ssx 1 ssy 1 sf 1 sb 1 }
##  { createBezierCusped str 1 ssx 1 ssy 1 sf 1 sb 1 }
##  { createBSpline str 1 ssx 1 ssy 1 sf 1 sb 1 }
##  { createEllipse str 1 ssx 1 ssy 1 sf 1 sb 1 }
##  { createRectangle str 1 ssx 1 ssy 1 sf 1 sb 1 }
##  { createRectangleCusped str 1 ssx 1 ssy 1 sf 1 sb 1 }
##  { brush str 1 ssx 1 ssy 1 sf 1 sb 1 }
##  { eraser src 2 str 1 ssx 1 ssy 1 sf 1 sb 1 }
##  { clone src 1 str 1 ssx 1 ssy 1 sf 1 sb 1 }
##  { reveal src 3 str 1 ssx 1 ssy 1 sf 1 sb 1 }
##  { dodge src 1 str 1 ssx 1 ssy 1 sf 1 sb 1 }
##  { burn src 1 str 1 ssx 1 ssy 1 sf 1 sb 1 }
##  { blur src 1 str 1 ssx 1 ssy 1 sf 1 sb 1 }
##  { sharpen src 1 str 1 ssx 1 ssy 1 sf 1 sb 1 }
##  { smear src 1 str 1 ssx 1 ssy 1 sf 1 sb 1 }
##} }
