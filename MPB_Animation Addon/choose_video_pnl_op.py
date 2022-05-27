import bpy

from bpy.props import BoolProperty, StringProperty
from bpy_extras.io_utils import ImportHelper
from bpy.types import Operator 

class ANIM_OT_ChooseVideoFile(Operator, ImportHelper):
    """
    По первой кнопке из меню:
        - Открывает проводник
        - Пользователь выбирает файл
        - Подтверждает выбор (если файл не выбран, оператор настаивает на выборе)
        - После выбора отображает название файла на кнопке, сохраняет путь в переменную
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
        """Do something with the selected file(s)."""

        video_path = self.filepath
        bpy.ops.file.video_processing()

        return {"FINISHED"}
