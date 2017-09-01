
from os import listdir, getcwd, makedirs
from os.path import splitext, join, basename, abspath, exists
from subprocess import Popen
from argparse import ArgumentParser

processes = []
        
def mkdir(path):
    if path == "":
        return
    if not exists(path):
        makedirs(path)
        
def filename(path):
    b = basename(path)
    fn, ext = splitext(b)
    if fn == '':
        return None
    return fn
        
def wait_processes():
    for p in processes:
        stdout, stderr = p.communicate()
    processes.clear()

def cmd(cmd_str, cwd=None):
    if cwd:
        p = Popen(cmd_str, cwd=cwd)
    else:
        p = Popen(cmd_str)
    processes.append(p)

def make_recolors(input, gradients, output):
    input = abspath(input)
    gradients = abspath(gradients)
    output = abspath(output)
    mkdir(output)
    iname = filename(input)
    for gradient in listdir(gradients):
        gpath = join(gradients, gradient)
        gname = filename(gradient)
        out_name = "{}_{}.png".format(iname, gname)
        cmd("magick convert {input} -alpha copy -channel A {gradient} -channel RGB -interpolate NearestNeighbor -clut {output}".format(
                input=input,
                gradient=gpath,
                output=out_name),
            cwd=output)
    wait_processes()
    
if __name__ == "__main__":
    parser = ArgumentParser(description="Recolor image with set of gradients")
    parser.add_argument('-i', '--input', help="input image file")
    parser.add_argument('-g', '--gradients', help="folder containing gradients")
    parser.add_argument('-o', '--output', help="output folder")
    # todo -v --verbose

    args = parser.parse_args()
    make_recolors(**vars(args))
    