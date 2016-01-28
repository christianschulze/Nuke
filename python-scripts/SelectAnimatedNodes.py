#!/usr/bin/env python
#
#----------------------------------------------------------------
# Name: SelectAnimatedNodes.py
# Version: 1.0
# Purpose: Make it easier to find all animated nodes in a comp
#
# Author: Christian Schulze
# Email: chris@christian-schulze.eu
#
# Created: 2015/01/29
# Copyright (C) 2015 Christian Schulze
#----------------------------------------------------------------


import nuke


def main():
    only_selected = nuke.ask("Consider only selected nodes? Select No to consider all nodes.")
    with_expression = nuke.ask("Include nodes with expression?")

    if only_selected:
        nodes = nuke.selectedNodes()
    else:
        nodes = nuke.root().nodes() # all nodes

    for node in nodes:
        node['selected'].setValue(False) # make sure no node is selected at the beginning
        for knob in node.allKnobs():
            if knob.isAnimated():
                if with_expression or not knob.hasExpression():
                    node['selected'].setValue(True)
                    if knob.hasExpression():
                        print node.name() + " is animated with expression"
                    else:
                        print node.name() + " is animated"
                    break

if  __name__ == '__main__':
    main()