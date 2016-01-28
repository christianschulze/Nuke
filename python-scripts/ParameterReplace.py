#!/usr/bin/env python
#
#----------------------------------------------------------------
# Name: ParameterReplace.py
# Version: 1.0
# Purpose: Modify one parameter of similar named nodes
#
# Author: Christian Schulze
# Email: mail@christian-schulze.eu
#
# Created: 2011/07/19
# Copyright (C) 2011 Christian Schulze
#----------------------------------------------------------------


import nukescripts

if nuke.env["gui"]:
    class ParameterReplace( nukescripts.PythonPanel ):
        def __init__( self ):
            nukescripts.PythonPanel.__init__( self, "Parameter Replace" )
            self.nodenames = nuke.String_Knob( "nodenames", "Node Names:" )
            self.nodenames.setValue( 'Transform' )
            self.addKnob( self.nodenames )
            self.parameter = nuke.String_Knob( "parameter", "Parameter:" )
            self.parameter.setValue( 'scale' )
            self.addKnob( self.parameter )
            self.istart = nuke.Int_Knob( "istart", "Index Start:" )
            self.istart.setValue( 1 )
            self.addKnob( self.istart )
            self.iend = nuke.Int_Knob( "iend", "Index End:" )
            self.iend.setValue( 10 )
            self.addKnob( self.iend )
            self.xfactor = nuke.Double_Knob( "xfactor", "Factor X:" )
            self.xfactor.setValue( 1 )
            self.xfactor.setRange( -10 , 10 )
            self.addKnob( self.xfactor )
            self.yfactor = nuke.Double_Knob( "yfactor", "Factor Y:" )
            self.yfactor.setValue( 1 )
            self.yfactor.setRange( -10 , 10 )
            self.addKnob( self.yfactor )
            self.xadd = nuke.Double_Knob( "xadd", "Add X:" )
            self.xadd.setValue( 0 )
            self.xadd.setRange( -100 , 100 )
            self.addKnob( self.xadd )
            self.yadd = nuke.Double_Knob( "yadd", "Add Y:" )
            self.yadd.setValue( 0 )
            self.yadd.setRange( -100 , 100 )
            self.addKnob( self.yadd )

        def replace( self ):
            nodenames = self.nodenames.value()
            parameter = self.parameter.value()
            istart = self.istart.value()
            iend = self.iend.value()
            xfactor = self.xfactor.value()
            yfactor = self.yfactor.value()
            xadd = self.xadd.value()
            yadd = self.yadd.value()

            for i in range( istart , iend + 1 ):
                inode = nuke.toNode( nodenames + str(i) )
                if inode:
                    iparamx = inode.knob( parameter ).getValue( 0 )
                    iparamy = inode.knob( parameter ).getValue( 1 )
                    if iparamx == iparamy and xfactor == yfactor and xadd == yadd: #only one scale value
                        inode.knob( parameter ).setValue( iparamx * xfactor + xadd )
                    else: #separate values for x and y
                        inode.knob( parameter ).setValue( iparamx * xfactor + xadd , 0 )
                        inode.knob( parameter ).setValue( iparamy * yfactor + yadd , 1 )

        def showModalDialog( self ):
            result = nukescripts.PythonPanel.showModalDialog( self )
            if result:
                self.replace()


    ParameterReplace().showModalDialog()
