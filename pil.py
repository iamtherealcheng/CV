'''from distutils import filelist
from PIL import Image
import os


for infile in filelist:
    outfile = os.path.splitext(infile)[0]+"png"
    if infile != outfile:
        try:
            Image.open(infile).save(outfile)
        except IOError:
            print "cannot convert", infile
import os
def get_imlist(path):
""" Returns a list of filenames for all jpg images in a directory. """

return [os.path.join(path,f) for f in os.listdir(path) if f.endswith('.png')]'''

#pil_im.thumbnail((1920,1920)) size of image setting

'''
from PIL import Image
import os
pil_im =    Image.open('a.png')
box = (100,100,400,400)
trai tren phai duoi
#region = pil_im.crop(box)
#crop image
region = pil_im.transpose(Image.ROTATE_90)
#quay hinh anh
#pil_im.paste(region,box)
#sau khi doan cat duoc xoay no se dat ve ban dau
#width, height = pil_im.size

region.show()
cu phap show nay giup in ra hinh anh vua xu ly'''