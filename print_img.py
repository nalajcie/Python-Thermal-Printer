#!/usr/bin/python

from Adafruit_Thermal import *
import sys
from PIL import Image, ImageOps

max_width = 384
#max_height = 512

printer = Adafruit_Thermal(timeout=5)

# give usage and exit if no arguments
if len(sys.argv) == 1:
    print 'Usage:', sys.argv[0], \
           'image1 [image2] [...]'
    exit(1)

# print all of the images!
for i in sys.argv[1:]:
    im = Image.open(i)

    im = im.transpose(Image.ROTATE_90)#.transpose(Image.FLIP_TOP_BOTTOM)

    if im.size[0] > max_width:
        newsize = (max_width, int(float(im.size[1]) / (float(im.size[0]) / max_width)))
        im = im.resize(newsize, Image.ANTIALIAS)

    # PIL algorithm: convert to greyscale then convert to mono with dithering
    im = im.convert('1')


    im.save("p.jpg", "jpeg")
    printer.printImage(im, False)
    printer.feed(2)

