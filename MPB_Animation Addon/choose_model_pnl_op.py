import bpy
import os
from bpy.props import BoolProperty, StringProperty
from bpy_extras.io_utils import ImportHelper
from bpy.types import Operator

class ANIM_OT_ChooseModelFile(Operator, ImportHelper):
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

        model_name, extension = os.path.splitext(self.filepath)
        model_path = self.filepath

        if extension == '.obj' or extension == '.mtl':
            bpy.ops.import_scene.obj(filepath=model_path, axis_forward='-Z', axis_up='Y', filter_glob="*.obj;*.mtl")
        elif extension == '.fbx':
            bpy.ops.import_scene.fbx(filepath=model_path, axis_forward='-Z', axis_up='Y', filter_glob="*.fbx")
        elif extension == '.x3d' or extension == '.wrl':
            bpy.ops.import_scene.x3d(filepath=model_path, axis_forward='-Z', axis_up='Y', filter_glob="*.x3d;*.wrl")

        return {"FINISHED"}
