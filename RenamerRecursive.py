import tkMessageBox
import os
import Tkinter
import tkFileDialog
from AdjNounAdj import *

teekay = Tkinter.Tk()
teekay.withdraw()

file_paths = tkFileDialog.askdirectory()
if tkMessageBox.askyesno("You sure?", "Recursively rename all files in " + file_paths + "?"):
    for root, dirs, files in os.walk(file_paths):
        for filename in files:
            print "orig", root + os.sep + filename
            print "new", root + os.sep + random_name() + os.path.splitext(filename)[1]
            os.rename(root + os.sep + filename, root + os.sep + random_name() + os.path.splitext(filename)[1])

