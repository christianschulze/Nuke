# code copied and adapted from https://pastebin.com/4vmAmARU by Throb

import nuke
import math


def create_camera_from_vray_exr(node):
    '''
    Create a camera node based on VRay metadata.
    This works specifically on VRay data coming from maya.
    '''

    mDat = node.metadata()
    reqFields = ['exr/camera%s' % i for i in ('FocalLength', 'Aperture', 'Transform')]
    if mDat is None or not set(reqFields).issubset(mDat):
        nuke.critical('No metadata for camera found! Please select a read node with EXR metadata from VRay!')
        return

    nuke.message("Creating a camera node based on VRay metadata. This works specifically on VRay data coming from Maya!\n\nIf you get both focal and aperture as they are in the metadata, there's no guarantee your Nuke camera will have the same FOV as the one that rendered the scene (because the render could have been fit to horizontal, to vertical, etc). Nuke always fits to the horizontal aperture. If you set the horizontal aperture as it is in the metadata, then you should use the FOV in the metadata to figure out the correct focal length for Nuke's camera. Or, you could keep the focal as is in the metadata, and change the horizontal_aperture instead. I'll go with the former here. Set the haperture knob as per the metadata, and derive the focal length from the FOV.")

    first = node.firstFrame()
    last = node.lastFrame()
    ret = nuke.getFramesAndViews('Create Camera from Metadata', '%s-%s' % (first, last))
    if ret is None:
        return
    fRange = nuke.FrameRange(ret[0])
    
    cam = nuke.createNode('Camera2')
    cam['useMatrix'].setValue(False)
    
    for k in ('focal', 'haperture', 'vaperture', 'translate', 'rotate'):
        cam[k].setAnimated()
    
    task = nuke.ProgressTask('Baking camera from meta data in %s' % node.name())
    
    for curTask, frame in enumerate(fRange):
        if task.isCancelled():
            break
        task.setMessage('processing frame %s' % frame)
        
        hap = node.metadata('exr/cameraAperture', frame) # get horizontal aperture
        fov = node.metadata('exr/cameraFov', frame) # get camera FOV
        
        focal = float(hap) / (2.0 * math.tan(math.radians(fov) * 0.5)) # convert the fov and aperture into focal length

        width = node.metadata('input/width', frame)
        height = node.metadata('input/height', frame)
        aspect = float(width) / float(height) # calulate aspect ratio from width and height
        vap = float(hap) / aspect # calculate vertical aperture from aspect ratio
        
        cam['focal'].setValueAt(float(focal), frame)
        cam['haperture'].setValueAt(float(hap), frame)
        cam['vaperture'].setValueAt(float(vap), frame)
        
        matrixCamera = node.metadata('exr/cameraTransform', frame) # get camera transform data
        
        # create a matrix to shove the original data into 
        matrixCreated = nuke.math.Matrix4()
        
        for k,v in enumerate(matrixCamera):
            matrixCreated[k] = v
        
        matrixCreated.rotateX(math.radians(-90)) # this is needed for VRay, it's a counter clockwise rotation
        translate = matrixCreated.transform(nuke.math.Vector3(0,0,0))  # get a vector that represents the camera translation   
        rotate = matrixCreated.rotationsZXY() # give us xyz rotations from cam matrix (must be converted to degrees)
    
        cam['translate'].setValueAt(float(translate.x), frame, 0)
        cam['translate'].setValueAt(float(translate.y), frame, 1)
        cam['translate'].setValueAt(float(translate.z), frame, 2)
        cam['rotate'].setValueAt(float(math.degrees(rotate[0])), frame, 0)
        cam['rotate'].setValueAt(float(math.degrees(rotate[1])), frame, 1)
        cam['rotate'].setValueAt(float(math.degrees(rotate[2])), frame, 2)
    
        task.setProgress(int(float(curTask) / fRange.frames() * 100))
