
import bpy
import re

def copy_constraints(a, b):
    # copy constraints from a to b
    for c in a.constraints:
        nc = b.constraints.new(c.type)
        for prop in dir(c): # lol
            try:
                value = getattr(c, prop)
                setattr(nc, prop, value) # lmao
            except:
                pass
            
def replace_dupligroups(a, b):
    # replace dupligroups a with dupligroup b
    ga = bpy.data.groups[a]
    gb = bpy.data.groups[b]
    
    for obj in bpy.data.objects:
        if obj.dupli_group == ga:
            obj.dupli_group = gb
            
def rename(r, s):
    # rename objects using regex
    # e.g. rename(r'(\w+)Marker(.*)', r'\1\2')
    regex = re.compile(r)
    for obj in bpy.data.objects:
        obj.name = regex.sub(regex, s, obj.name)
        
def select(objs, value):
    for obj in objs: obj.select = value
            
def egg_export(path):
    # export all objects in group 'Export' to path
    settings = bpy.context.scene.yabee_settings
    try:
        bpy.ops.object.mode_set(mode='OBJECT', toggle=False)
    except RuntimeError:
        pass
    select(bpy.data.objects, False)
    objs = bpy.data.groups["Export"].objects
    select(objs, True)
    settings.opt_pview = False
    bpy.ops.export.panda3d_egg(filepath=path)
    select(objs, False)

def link_groups(path):
    # link all groups in .blend file
    with bpy.data.libraries.load(path, link=True) as (data_src, data_dst):
        data_dst.groups = data_src.groups
        #self.report({'INFO'}, 'linked {} groups'.format(len(data_src.groups)))

def link_my_stuff():
    # could be an operator?
    paths = [
        r"C:\Users\alcor_000\Projects\my_panda_game\art\models\levels\markers\markers.blend",
        r"C:\Users\alcor_000\Projects\my_panda_game\art\models\scenery\chest.blend",
        r"C:\Users\alcor_000\Projects\my_panda_game\art\models\scenery\coin.blend",
        r"C:\Users\alcor_000\Projects\my_panda_game\art\models\scenery\crate.blend",
        r"C:\Users\alcor_000\Projects\my_panda_game\art\models\scenery\sign.blend",
        r"C:\Users\alcor_000\Projects\my_panda_game\art\models\scenery\switch.blend",
        r"C:\Users\alcor_000\Projects\my_panda_game\art\models\vehicles\tank\tank.blend",
        r"C:\Users\alcor_000\Projects\my_panda_game\art\models\vehicles\ship\ship.blend",
        r"C:\Users\alcor_000\Projects\my_panda_game\art\models\vehicles\plane\plane.blend",
        r"C:\Users\alcor_000\Projects\my_panda_game\art\models\vehicles\car\car.blend",
        r"C:\Users\alcor_000\Projects\my_panda_game\art\models\accessories\pike.blend",
        r"C:\Users\alcor_000\Projects\my_panda_game\art\models\accessories\rlauncher.blend"
    ]
    for path in paths:
        link_groups(path)
    