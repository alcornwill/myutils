
from subprocess import call
from os.path import abspath, join

def create_skybox(path):
    # hmm always render to equitangular or util for render envmap anywhere?
    # takes equitangular image, renders cubemap texture, save UV mapped skybox.egg
    path = abspath(path)
    root = "C:\\Users\\alcor_000\\Projects\\my_panda_game\\myutils"
    filepath = join(root, 'skybox\\skybox.blend')
    script = join(root, 'skybox\\render_envmap.py')
    call("blender {} -b -P {} -- {}".format(filepath, script, path))