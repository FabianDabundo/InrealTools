import bpy
from __main__ import *

scene = bpy.context.scene

save_cursor = scene.cursor_location[0], scene.cursor_location[1], scene.cursor_location[2]
save_area = bpy.context.area.type


#-------------------------------------------------------
#*****set origin*****
#-------------------------------------------------------

bpy.context.area.type = 'VIEW_3D'

bpy.ops.view3d.snap_cursor_to_selected()
bpy.ops.object.editmode_toggle()
bpy.ops.object.origin_set(type='ORIGIN_CURSOR')
bpy.ops.object.editmode_toggle()

scene.cursor_location = save_cursor
bpy.context.area.type = save_area