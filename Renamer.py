__author__ = 'Ian'

import os
import Tkinter
import tkFileDialog
from AdjNounAdj import *

root = Tkinter.Tk()
root.withdraw()

file_paths = tkFileDialog.askopenfilenames()

for filePath in file_paths:
    fileExtension = os.path.splitext(filePath)[1]
    nameStart = filePath.rfind("/")+1
    fileName = filePath[nameStart:nameStart+len(fileExtension)]
    directory = filePath[:nameStart]

    print directory, fileName, fileExtension
    print random_name()

    #todo add exception handling for repeat names
    newFile = directory + random_name() + fileExtension
    os.rename(filePath, newFile)