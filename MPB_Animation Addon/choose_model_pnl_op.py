import bpy
import os

from bpy.props import BoolProperty, StringProperty
from bpy_extras.io_utils import ImportHelper
from bpy.types import Operator
from bpy.utils import register_class

class ChooseModelFile(Operator, ImportHelper):
    """
    По второй кнопке из меню:
        - Открывает проводник
        - Пользователь выбирает файл
        - Подтверждает выбор (если файл не выбран, оператор берет стоковую модель)
        - После выбора отображает название файла на кнопке, импортирует модель
    """
    bl_idname = "file.choose_model_file"
    bl_label = "Choose Model File"
    
    filter_glob: StringProperty(
        default='*.blend;*.stl;*.fbx;*.obj;*.dae',
        options={'HIDDEN'}
    )
    
    some_boolean: BoolProperty(
        name='Do a thing',
        description='Do a thing with the file you\'ve selected',
        default=True,
    )
    
    def execute(self, context):
        """Do something with the selected file(s)."""

        filename, extension = os.path.splitext(self.filepath)
        
        print('Selected file:', self.filepath)
        print('File name:', filename)
        print('File extension:', extension)
        print('Some Boolean:', self.some_boolean)
        
        return {"FINISHED"}

if __name__ == "__main__":
    register_class(ChooseModelFile)