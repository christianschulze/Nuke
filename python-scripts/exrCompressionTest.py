#### Function to test EXR file Compression scheme...
import os, nuke
def exrCompressionTest():
        compressList = ['None', 'RLE', 'ZIP', 'ZIP 16 lines', 'PIZ', 'PXR24', 'B44', 'B44A']
        try:
                n = nuke.selectedNode()
                if nuke.selectedNode().Class()!='Read' or nuke.selectedNode() == "" :
                        nuke.message('No Read node selected.')
                elif os.path.splitext(nuke.filename(nuke.selectedNode()))[-1]!=".exr" :
                        nuke.message('Selected Read is not an EXR')
                else:
                        file = nuke.filename(n, nuke.REPLACE)
                        fd = open(file, 'rb')
                        header = fd.read(4096)
                        index = header.find('compression')
                        comp =ord(header[(index+28):(index+29)])
                        compressMethod = compressList[comp]
                        print compressMethod
                        nuke.message('EXR compression is %s' %(compressMethod))

        except ValueError:
                nuke.message('Please select a Read node...')

exrCompressionTest()
