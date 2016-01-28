#!/usr/bin/env python
#
#----------------------------------------------------------------
# Name: BakeScript.py
# Version: 1.0
# Purpose: Bake all Gizmos, Groups and Precomps into the script.
# Might be helpful to submit a script to a render farm without
# dependencies.
#
# Author: Christian Schulze
# Email: chris@christian-schulze.eu
#
# Created: 2015/03/31
# Copyright (C) 2015 Christian Schulze
#----------------------------------------------------------------


import os
import nuke
import nukescripts


def main():
	baked = '_baked'
	(base, ext) = os.path.splitext(nuke.scriptName())
	if base.endswith(baked):
	    newfile = base + ext
	else:
	    newfile = base + baked + ext

	nukescripts.misc.clear_selection_recursive()
	for n in nuke.allNodes():
	    if n.Class() in ('Precomp', 'Group', 'Gizmo'):
	        n.expand()
	        nukescripts.misc.clear_selection_recursive()

#	for n in nuke.allNodes():
#	    if n.Class() == 'Write':
#	    	n['file'].setValue(n['file'].evaluate().strip())

	nuke.scriptSaveAs(filename = newfile, overwrite = 1)

if  __name__ == '__main__':
    main()