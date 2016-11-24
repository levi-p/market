from __future__ import print_function
import os, sys
from PIL import Image
def g():

  h=['/home/levi/Pictures/mw/networky.png']
  for infile in h:#sys.argv[1:]:
    f, e = os.path.splitext(infile)


    outfile = f + ".jpg"
    if infile != outfile:
        try:
            Image.open(infile).save(outfile)
            print("success!", outfile)
        except Exception,e:
            print("cannot convert",+ str(e), infile)

size = (128, 128)
def gg():
    h=['/home/levi/Pictures/mw/networky.png']
    for infile in h:#sys.argv[1:]:
        outfile = os.path.splitext(infile)[0] + ".thumbnail"
        if infile != outfile:
            try:
                im = Image.open(infile)
                im.thumbnail(size)
                im.save(outfile, "JPEG")
                print("success!", outfile)
            except IOError:
                print("cannot create thumbnail for", infile)

def gg2():
    h=['/home/levi/Pictures/mw/placeh.jpg']
    for infile in h:#sys.argv[1:]:
        outfile = os.path.splitext(infile)[0] + ".thumb"
        if infile != outfile:
            try:
                im = Image.open(infile)
                im.resize((100,100))
                im.save('outfile', "JPEG")
                print("success!", outfile)
            except IOError:
                print("cannot create thumbnail for", infile)
