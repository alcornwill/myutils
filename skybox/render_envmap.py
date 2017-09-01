
import bpy
from sys import argv
from myutils.blender import egg_export
from os.path import join, basename

etex = argv[-1]
out = "C:\\Users\\alcor_000\\Desktop\\"
image_out = join(out, 'skybox.png')
egg_out = join(out, 'skybox.egg')

class NotFoundError(Exception):
    pass

def find_image(path):
    for img in bpy.data.images:
        if img.name == basename(path):
            return img
    raise NotFoundError('image "{}" not found'.format(path))
    
def get_context_override():
    for area in bpy.context.screen.areas:
        if area.type == 'PROPERTIES':
            override = bpy.context.copy()
            override['area'] = area
            override['texture'] = bpy.data.textures['Envmap']
            for space in area.spaces:
                if space.type == 'PROPERTIES':
                    space.context = 'TEXTURE'
                    space.texture_context = 'MATERIAL'
                    override['space_data'] = space
                    return override
            
cube = bpy.data.objects['Cube']
envmap = bpy.data.materials['Envmap']
skybox = bpy.data.materials['Skybox']
envmap_tex = bpy.data.textures['Envmap']
skybox_tex = bpy.data.textures['Skybox']
sky = bpy.data.textures['Sky']

# set equitangular texture as sky
bpy.ops.image.open(filepath=etex)
img = find_image(etex)
sky.image = img

# render scene and save envmap
bpy.ops.render.render()
override = get_context_override()
bpy.ops.texture.envmap_save(override, filepath=image_out)

# export skybox egg
bpy.ops.image.open(filepath=image_out)
img = find_image(image_out)
skybox_tex.image = img
cube.material_slots[0].material = skybox

egg_export(egg_out)
