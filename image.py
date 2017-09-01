
from os.path import join, basename, dirname
from os import listdir, getcwd
from PIL import Image

def get_images():
    path = getcwd()
    images = []
    for fn in listdir(path):
        if fn.endswith('.png'):
            images.append(fn)
    return images

def resize(height, width):
    for image in get_images():
        img = Image.open(image)
        img = img.resize((height, width), Image.ANTIALIAS)
        img.save(image) 

def crop(input, height, width, k):
    # (tile?)
    # todo should be divide x y times
    img = Image.open(input)
    imgwidth, imgheight = img.size
    for i in range(0,imgheight,height):
        for j in range(0,imgwidth,width):
            box = (j, i, j+width, i+height)
            a = img.crop(box)
            a.save("IMG-{}.png".format(k))
            k +=1
            
def greyscale_to_alpha(path):
    img = Image.open(path, 'r')
    l = img.split()[0]

    rgbimg = Image.new("RGBA", img.size)
    rgbimg.paste(img)
    rgbimg.putalpha(l)
    out = join(dirname(path), "alpha", basename(path))
    rgbimg.save(out)
    
def rgba_to_rgb(input, output):
    img = Image.open(input)
    img.load() # required for img.split()

    background = Image.new("RGB", img.size, (255, 255, 255))
    background.paste(img, mask=img.split()[3])

    background.save(output, 'PNG')