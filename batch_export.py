# exports each selected object into its own file

bl_idname = "batch_export"

import bpy
import os
from __main__ import *

#----------------
#exportpath
#savelocation
#saverotation
#savescale

#resetlocation
#resetrotation
#resetscale

#exportpath = os.path.dirname(bpy.data.filepath)
#----------------


# export to blend file location
basedir = bpy.context.scene.inreal_tools.export_path
basedir = bpy.path.abspath(basedir)

loc = bpy.context.scene.inreal_tools.reset_location
rot = bpy.context.scene.inreal_tools.reset_rotation
sca = bpy.context.scene.inreal_tools.reset_scale


if not basedir:
    raise Exception("Blend file is not saved")

scene = bpy.context.scene

obj_active = scene.objects.active
selection = bpy.context.selected_objects

bpy.ops.object.select_all(action='DESELECT')

for obj in selection:

    obj.select = True
    
    #####save original transforms
    savelocation=(obj.location.x, obj.location.y, obj.location.z)
    saverotation=(obj.rotation_euler.x, obj.rotation_euler.y, obj.rotation_euler.z)
    savescale=(obj.scale.x, obj.scale.y, obj.scale.x)
    
    # some exporters only use the active object
    scene.objects.active = obj

    name = bpy.path.clean_name(obj.name)
    fn = os.path.join(basedir, name)
    #------------------------------------
    #*****duplicate object and convert to mesh*****
    #------------------------------------
    bpy.ops.object.duplicate_move(OBJECT_OT_duplicate={"linked":False, "mode":'TRANSLATION'}, TRANSFORM_OT_translate={"value":(0, 0, 0), "constraint_axis":(False, False, False), "constraint_orientation":'GLOBAL', "mirror":False, "proportional":'DISABLED', "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "texture_space":False, "remove_on_cancel":False, "release_confirm":False, "use_accurate":False})
    bpy.ops.object.convert(target='MESH')
    #------------------------------------
    #*****clear transforms for export*****
    #------------------------------------
    if loc==True:
        bpy.ops.object.location_clear(clear_delta=False)
    if rot==True:
        bpy.ops.object.rotation_clear(clear_delta=False)
    if sca==True:
        bpy.ops.object.scale_clear(clear_delta=False)
    #------------------------------------

    bpy.ops.export_scene.fbx(filepath=fn + ".fbx", use_selection=True)

    ## Can be used for multiple formats
    # bpy.ops.export_scene.x3d(filepath=fn + ".x3d", use_selection=True)

    #------------------------------------
    #*****set transforms to original transforms*****
    #------------------------------------
    obj.location=(savelocation)
    obj.rotation_euler=(saverotation)
    obj.scale=(savescale)
    
    print(obj.location)
    print(obj.rotation_euler)
    print(obj.scale)
    
    #------------------------------------
    #*****delete dublicated object*****
    #------------------------------------
    bpy.ops.object.delete(use_global=False)


    obj.select = False

    print("written:", fn)


scene.objects.active = obj_active

for obj in selection:
    obj.select = True
    
    


