import bpy

from bpy.types import Panel
from bpy.utils import register_class

class ANIM_PT_ObjectTrackingPanel(Panel):
    bl_label = "Object Tracking Animation"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Tracking"
    
    def draw(self, context):
        layout = self.layout
        props = context.object.anim
        col = layout.column()
        col.operator("file.choose_video_file")
        col = layout.column()
        col.operator("file.choose_model_file")
        col = layout.column()
        col.operator("anim.set_anim_coords")

if __name__ == "__main__":
    register_class(ANIM_PT_ObjectTrackingPanel)
