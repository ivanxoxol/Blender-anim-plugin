import bpy
import os
from bpy.props import BoolProperty, StringProperty
from bpy_extras.io_utils import ImportHelper
from bpy.types import Operator
from random import randint

class ANIM_OT_ChooseModelFile(Operator, ImportHelper):
    """
    By the second button from the menu:
        - Opens explorer
        - User selects a file
        - Confirms the selection (if no file is selected, the operator takes the stock model)
        - After selection, displays the file name on the button, imports the model
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
        """Add Model of the human just for fun and generate Cubes-Point Armature"""

        model_name, extension = os.path.splitext(self.filepath)
        model_path = self.filepath

        if extension == '.obj' or extension == '.mtl':
            bpy.ops.import_scene.obj(filepath=model_path, axis_forward='-Z', axis_up='Y', filter_glob="*.obj;*.mtl")
        elif extension == '.fbx':
            bpy.ops.import_scene.fbx(filepath=model_path, axis_forward='-Z', axis_up='Y', filter_glob="*.fbx")
        elif extension == '.x3d' or extension == '.wrl':
            bpy.ops.import_scene.x3d(filepath=model_path, axis_forward='-Z', axis_up='Y', filter_glob="*.x3d;*.wrl")

        for i in range(33):
            bpy.ops.mesh.primitive_cube_add()
            cube = bpy.context.selected_objects[0]
            cube.name = 'Cube.' + '0' * (3 - len(str(i))) + str(i)
            x = randint(-10,10)
            y = randint(-10,10)
            z = randint(-10,10)
            cube.location = (x, y, z)

        return {"FINISHED"}
