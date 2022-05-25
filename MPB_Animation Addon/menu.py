import bpy
import os

from bpy.props import BoolProperty, StringProperty, PointerProperty
from bpy_extras.io_utils import ImportHelper
from bpy.types import Operator, Panel, PropertyGroup
from bpy.utils import register_class, unregister_class

class AnimProps(PropertyGroup):
    choose_video : BoolProperty(
        name = "Choose Video"
    )
    

class ChooseVideoFile(Operator, ImportHelper):
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

        filename, extension = os.path.splitext(self.filepath)
        
        print('Selected file:', self.filepath)
        print('File name:', filename)
        print('File extension:', extension)
        print('Some Boolean:', self.some_boolean)
        
        return {"FINISHED"}


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

class ANIM_PT_ObjectTrackingPanel(Panel):
    bl_label = "Object Tracking Animation"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Tracking"
    
    def draw(self, context):
        layout = self.layout
        props = context.object.anim
        col = layout.column()
        col.operator("file.choose_video_file")
        col = layout.column()
        col.operator("file.choose_model_file")
        col = layout.column()
        col.operator("anim.set_anim_coords")

classes = [
    AnimProps,
    ChooseVideoFile,
    ChooseModelFile,
    SetAnimationCoordinates,
    ANIM_PT_ObjectTrackingPanel
]

def register():
    for cl in classes:
        register_class(cl)
    bpy.types.Object.anim = PointerProperty(type = AnimProps)

def unregister():
    for cl in reversed(classes):
        register_class(cl)
        
if __name__ == "__main__":
    register()