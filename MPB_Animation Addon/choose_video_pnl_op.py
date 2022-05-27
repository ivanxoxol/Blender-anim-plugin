import bpy
from bpy.props import BoolProperty, StringProperty
from bpy_extras.io_utils import ImportHelper
from bpy.types import Operator 


class ANIM_OT_ChooseVideoFile(Operator, ImportHelper):
    """
    On the first button from the menu:
        - Opens explorer
        - User selects a file
        - Confirms selection (if file is not selected, operator insists on selection)
        - After selection, displays the file name on the button, saves the path to a variable
    """
    bl_idname = "file.choose_video_file"
    bl_label = "Choose Video File"
    
    filter_glob: StringProperty(
        default='*.mp4;*.mov;*.avi;*.mkv;*.wmv;',
        options={'HIDDEN'}
    )
    
    some_boolean: BoolProperty(
        name='Do a thing',
        description='Do a thing with the file you\'ve selected',
        default=True,
    )
    
    def execute(self, context):
        """Add Video path and Run Video Processing"""

        video_path = self.filepath
        bpy.ops.file.video_processing()

        return {"FINISHED"}
