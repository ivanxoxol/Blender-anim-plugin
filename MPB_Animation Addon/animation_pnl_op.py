import bpy

from bpy.types import Operator
from . choose_model_pnl_op import model_path
from . choose_video_pnl_op import video_path

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
        print("-----------SetAnimationCoordinates DONE-------------")
        return {"FINISHED"}
