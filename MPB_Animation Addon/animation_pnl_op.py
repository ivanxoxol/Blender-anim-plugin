import bpy
from bpy.types import Operator

class ANIM_OT_SetAnimationCoordinates(Operator):
    """
    By the third button from the menu:
        - Runs a tracking script that produces a csv file with coordinates as a result
        - Moves the points of the model according to the coordinates in each frame
        - Shows the progress of the procedure
        - After completion - a message about the end
    """

    bl_idname = "anim.set_anim_coords"
    bl_label = "Set Animation Keys"
    
    def execute(self, context):
        """Add Cubes and run Set Animation Coordinates Operator"""

        for j in range(33):
            obj_name = 'Cube.' + '0' * (3 - len(str(j))) + str(j)
            bpy.data.objects[obj_name].animation_data_clear()

        bpy.ops.object.all_coord()

        return {"FINISHED"}
