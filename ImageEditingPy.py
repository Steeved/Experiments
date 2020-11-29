#
# This script uses Pillow image processing lib 
# Installation https://pillow.readthedocs.io/en/stable/installation.html : 
#    python -m pip install --upgrade pip
#    python -m pip install --upgrade Pillow
#
# Draw function:
# f(x) = x^2/5 -2x + 5

from PIL import Image, ImageDraw

im= Image.new("RGB", (128, 128), "#ffffff")

dra w = ImageDraw.Draw(im)
draw.line([(0,im.size[1]/2), (im.size[0], im.size[1]/2)], fill=128)
draw.line([(im.size[0]/2, 0), (im.size[0]/2, im.size[1])], fill=128)


for p in range (-1000, 1000) :
    x = p/10
    
    y = (x ** 2) / 5 - 2 * x + 5
    draw.point((x+im.size[0]/2, -y+im.size[1]/2), fill=120)
    
im.show()