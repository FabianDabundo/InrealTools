bl_info = {
    "name": "Inreal Tools",
    "author": "Fabian D'Abundo",
    #"version": (0,1),
    #"blender": (2, 75, 0),
    "location": "View3D > Tool Shelf > Inreal Tools",
    "description": "Unreal Engine 4 Tools",
    #"warning": "",
    #"wiki_url": "",
    "category": "Export",
    }


import bpy, math, os
from bpy.props import (StringProperty, PointerProperty,)
from bpy.types import (Panel, Operator, AddonPreferences, PropertyGroup,)

script_file = os.path.realpath(__file__)
directory = os.path.dirname(script_file)

#-------------------------------------------------------
#*****class for setting up the export path*****
#-------------------------------------------------------
class ExportGroup(PropertyGroup):
    export_path = StringProperty(name="", description="Path To Directory", default="//", maxlen=1024, subtype='DIR_PATH')
    reset_location = bpy.props.BoolProperty(name="", description="Reset Location", default=False)
    reset_rotation = bpy.props.BoolProperty(name="", description="Reset Rotation", default=False)
    reset_scale = bpy.props.BoolProperty(name="", description="Reset Scale", default=False)


#-------------------------------------------------------
#*****class panel objectmode*****
#-------------------------------------------------------
class InrealToolPanelObject(Panel):
    """Custom Panel For Inreal Tools Objectmode"""
    bl_idname = "inreal"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_label = 'Inreal Tools'
    bl_context = 'objectmode'
    bl_category = 'Inreal Tools'
    
    #my_exportpath = bpy.props.StringProperty()
    #my_savetxt = bpy.props.BoolProperty(name="Save Txt File", default=False)
    
    

    def draw(self, context):
        layout=self.layout
        scn = context.scene              
        
        layout.label(text="Copy Transforms To Clipboard:")
        layout.operator('ue4.copytransforms', text='Copy', icon='COPYDOWN')
        
        layout.label(text="Batch Export:")
        
        col = layout.box().column(align=True)
        row = col.row(align=True)
        col.prop(scn.inreal_tools, "export_path", text="")
        #print(scn.inreal_tools.export_path)
        
        col.prop(scn.inreal_tools, "reset_location", text="Reset Location")
        col.prop(scn.inreal_tools, "reset_rotation", text="Reset Rotation")
        col.prop(scn.inreal_tools, "reset_scale", text="Reset Scale")
        
        col.operator('export.batch', text='Export', icon='EXPORT')

#-------------------------------------------------------
#*****class panel editmode*****
#-------------------------------------------------------
class InrealToolPanelEdit(Panel):
    """Custom Panel For Inreal Tools Objectmode"""
    bl_idname = "inreal_edit"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_label = 'Inreal Tools'
    bl_context = 'mesh_edit'
    bl_category = 'Inreal Tools'

    def draw(self, context):
        layout = self.layout
        scn = context.scene
        
        layout.label(text="Set Origin To Selection")
        layout.operator('set.origin', text='Set', icon='SPACE2')
		
#-------------------------------------------------------
#*****class for setting the origin of an object*****
#-------------------------------------------------------
class SetOrigin(Operator):
	bl_idname = 'set.origin'
	bl_label = 'Set Origin To Selection'
	
	def execute(self, context):
		filename = os.path.join(os.path.dirname(script_file), "set_origin.py")
		exec(compile(open(filename).read(), filename, 'exec'))
		return {'FINISHED'}
		
#-------------------------------------------------------
#*****class for copy transforms*****
#-------------------------------------------------------
class CopyTransforms(Operator):
    bl_idname = 'ue4.copytransforms'
    bl_label = 'Copy Transforms To UE4'
    
    def execute(self, context):
		#filename = os.path.realpath(__file__)
        filename = os.path.join(os.path.dirname(script_file), "ue4_copy_transforms_to_clipboard.py")
        #filename = os.path.join(os.path.dirname(bpy.data.filepath), "ue4_copy_transforms_to_clipboard.py")   
        exec(compile(open(filename).read(), filename, 'exec'))
        return {'FINISHED'}


#-------------------------------------------------------
#*****class for batch export*****
#-------------------------------------------------------
class BatchExport(Operator):
    bl_idname = 'export.batch'
    bl_label = 'Batch Export'
    
    def execute(self, context):
        #filename = os.path.realpath(__file__)
        filename = os.path.join(os.path.dirname(script_file), "batch_export.py")
        #filename = os.path.join(os.path.dirname(bpy.data.filepath), "batch_export.py")   
        exec(compile(open(filename).read(), filename, 'exec'))
        return {'FINISHED'}
    

#-------------------------------------------------------
#*****register classes*****
#-------------------------------------------------------
#register
def register():
    #bpy.utils.register_class(InrealToolPanel)
    
    #bpy.utils.register_class(ExportGroup)
    bpy.utils.register_module(__name__)
    bpy.types.Scene.inreal_tools = PointerProperty(type=ExportGroup)
            
    #bpy.utils.register_class(CopyTransforms)
    #bpy.utils.register_class(BatchExport)
#unregister
def unregister():
    #bpy.utils.unregister_class(InrealToolPanel)
    
    #bpy.utils.unregister_class(ExportGroup)
    bpy.utils.unregister_module(__name__)
    del bpy.types.Scene.inreal_tools    
    
    #bpy.utils.unregister_class(CopyTransforms)
    #bpy.utils.unregister_class(BatchExport)
#need to run script in text editor
if __name__=='__main__':
   register()
