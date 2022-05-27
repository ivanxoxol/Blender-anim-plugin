# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

bl_info = {
    "name" : "MPB Animation",
    "author" : "Ivan & Kirill",
    "description" : "Animation from your motion video",
    "blender" : (3, 2, 0),
    "version" : (0, 0, 1),
    "location" : "View3D",
    "warning" : "",
    "category" : "Object"
}

import bpy
from bpy.utils import register_class, unregister_class
from . animation_pnl_op import ANIM_OT_SetAnimationCoordinates
from . choose_model_pnl_op import ANIM_OT_ChooseModelFile
from . choose_video_pnl_op import ANIM_OT_ChooseVideoFile
from . menu_pnl import ANIM_PT_ObjectTrackingPanel
from . anim_move_op import ANIM_OT_Move_obj

classes = (
    ANIM_OT_Move_obj, 
    ANIM_OT_SetAnimationCoordinates,
    ANIM_OT_ChooseModelFile,
    ANIM_OT_ChooseVideoFile,
    ANIM_PT_ObjectTrackingPanel
)

def register():
    for cl in classes:
        register_class(cl)

def unregister():
    for cl in reversed(classes):
        unregister_class(cl)
        
if __name__ == "__main__":
    register()
