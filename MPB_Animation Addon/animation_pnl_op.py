import bpy

from bpy.props import BoolProperty, PointerProperty
from bpy.types import Operator, PropertyGroup
from bpy.utils import register_class

class AnimProps(PropertyGroup):
    choose_video : BoolProperty(
        name = ""
    )

class SetAnimationCoordinates(Operator):
    """
    По третьей кнопке из меню:
        - Запускает скрипт трекинга, который выдает в результате csv файл с координатами
        - Двигает точки модели в соответствии с координатами в каждом кадре
        - Показывает процесс выполнения процедуры
        - После выполнения - сообщение об окончании
    """
    bl_idname = "anim.set_anim_coords"
    bl_label = "Set Animation Keys"
    
    def execute(self, context):
        """Do something with the selected file(s)."""
        print("-----------SetAnimationCoordinates DONE-------------")
        return {"FINISHED"}


if __name__ == "__main__":
    register_class(AnimProps)
    register_class(SetAnimationCoordinates)    
    bpy.types.Object.anim = PointerProperty(type = AnimProps)