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

        for i in range(33):
            bpy.ops.mesh.primitive_cube_add()
            cube = bpy.context.selected_objects[0]
            cube.name = 'Cube.' + '0' * (3 - len(str(i))) + str(i)
            x = randint(-10,10)
            y = randint(-10,10)
            z = randint(-10,10)
            cube.location = (x, y, z)

        # 2 blocks of clearing animation data
        context = bpy.context
        for ob in context.selected_objects:
            ob.animation_data_clear()

        # for j in range(33):
        #     obj_name = 'Cube.' + '0' * (3 - len(str(j))) + str(j)
        #     bpy.data.objects[obj_name].animation_data_clear()

        bpy.ops.object.all_coord()

        print("-----------SetAnimationCoordinates DONE-------------")
        return {"FINISHED"}
