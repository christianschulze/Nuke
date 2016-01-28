import sys, os

root = "/Volumes/BOB_HD_02/NEW_MATERIAL/LOGO"

#WITH SUBFOLDERS
for dirname, dirnames, filenames in os.walk(root):
    for filename in filenames:
        if not ".png" in filename:
            continue
        newfilename = filename.replace("#-", "")
        
        filepath = os.path.join(dirname, filename)
        newfilepath = os.path.join(dirname, newfilename)
        
        if filepath != newfilepath:
            os.rename(filepath, newfilepath)
            print 'renamed "' + filename + '" to "' + newfilename + '"'
