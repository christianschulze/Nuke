#!/usr/bin/env python
#
#----------------------------------------------------------------
# Name: PathReplace.py
# Version: 1.0
# Purpose: Search and replace paths in all file reading nodes
#
# Author: Christian Schulze
# Email: mail@christian-schulze.eu
#
# Created: 2011/08/15
# Copyright (C) 2011 Christian Schulze
#----------------------------------------------------------------


import nukescripts
import os.path

if nuke.env["gui"]:
    class PathReplace( nukescripts.PythonPanel ):
        def __init__( self ):
            nukescripts.PythonPanel.__init__( self, "Path Replace" )
            self.search = nuke.File_Knob( "search", "Search:" )
            self.addKnob( self.search )
            self.replace = nuke.File_Knob( "replace", "Replace:" )
            self.addKnob( self.replace )

        def replacePath( self ):
            search = os.path.normpath( self.search.value() ).lower()
            replace = os.path.normpath( self.replace.value() )
            
            for n in nuke.allNodes():
                if n.Class() == 'Read' \
                   or n.Class() == 'Write' \
                   or n.Class() == 'Camera2' \
                   or n.Class() == 'ReadGeo' \
                   or n.Class() == 'ReadGeo2':
                    if n:
                        npath = os.path.normpath( n.knob( 'file' ).value() ).lower()
                        newpath = npath.replace( search , replace )
                        if newpath != npath:
                            newpath = newpath.replace( "\\" , "/" )
                            n.knob( 'file' ).setValue( newpath )
                            print 'Replaced path in node \"' + n.name() + "\""

        def showModalDialog( self ):
            result = nukescripts.PythonPanel.showModalDialog( self )
            if result:
                self.replacePath()


    PathReplace().showModalDialog()
