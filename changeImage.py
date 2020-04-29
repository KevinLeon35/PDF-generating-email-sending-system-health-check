#!/usr/bin/env python3
import os, sys
from PIL import Image
srcfolder="/home/student-04-f312d8e8e665/supplier-data/images"
destfolder="/home/student-04-f312d8e8e665/supplier-data/images"
for infile in os.listdir(srcfolder):
    if ".tiff" not in infile:
        continue
    else:
        print(infile)
        fullpath = os.path.join(srcfolder,infile)
        file,extension = os.path.splitext(infile)
        newfile = file + ".jpeg"
        outimg = os.path.join(destfolder,newfile)
        print(outimg)
        img = Image.open(fullpath)
        newimg = img.resize((600,400)).convert('RGB')
        newimg.save(outimg,'JPEG')
