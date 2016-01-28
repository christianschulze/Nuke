import os
import os.path
import shutil

path = 'C:\\Users\christian.schulze\\Desktop\\test'

#shutil.rmtree( path )
os.mkdir( path )

for i in range(0, 256):
    name = hex(i)[2:]
    if len(name) < 2:
        name = "0" + name
    os.mkdir( os.path.join( path, name ) )
    for i in range(0, 16):
        name2 = hex(i)[2:]
        os.mkdir( os.path.join( path, name, name2 ) )
