import bpy

from bpy.types import Panel

class ANIM_PT_ObjectTrackingPanel(Panel):
    bl_label = "Object Tracking Animation"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Tracking"
    
    def draw(self, context):
        layout = self.layout
        col = layout.column()
        col.operator("file.choose_video_file", text="add video")
        col = layout.column()
        col.operator("file.choose_model_file", text="add model")
        col = layout.column()
        col.operator("anim.set_anim_coords", text="run tracking")

