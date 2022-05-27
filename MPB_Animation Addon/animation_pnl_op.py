import bpy

from bpy.types import Operator
from random import randint

class ANIM_OT_SetAnimationCoordinates(Operator):
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

        for j in range(33):
            obj_name = 'Cube.' + '0' * (3 - len(str(j))) + str(j)
            bpy.data.objects[obj_name].animation_data_clear()

        bpy.ops.object.all_coord()

        print("-----------SetAnimationCoordinates DONE-------------")
        return {"FINISHED"}
