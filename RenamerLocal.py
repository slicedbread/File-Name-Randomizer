__author__ = 'Ian'

import os
from AdjNounAdj import *

file_paths = os.listdir(os.curdir)

for filePath in file_paths:
    #this if is vital if you dont want it to rename itself
    if filePath != "RenamerLocal.py":
        print "\n\nfilePath", filePath
        fileExtension = os.path.splitext(filePath)[1]
        name = os.path.splitext(filePath)[0]

        print "name,ext", name, fileExtension
        print "random name", random_name()

        #todo add exception handling for repeat names
        newFile = random_name() + fileExtension
        os.rename(filePath, newFile)