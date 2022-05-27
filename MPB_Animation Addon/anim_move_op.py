import bpy
import csv
from bpy.types import Operator
from bpy.utils import register_class
from pathlib import Path


class ANIM_OT_Move_obj(Operator):
    """
    The Move_obj class performs the function of an object movement operator.
    Inherited from the Operator class in Blender.
    Methods: execute — the main method
    """
    
    bl_idname = 'object.all_coord'
    bl_label = 'Storing Coordinates'
            
    def execute(self, context):
        """
        The arguments "self" and "context" are accepted as input
        The method takes coordinates from the file "coords.csv"
        Error handler: IndexError — if there are no more coordinates for the object, just continue
        """

        csv_path = Path.cwd().parents[0] / "Blender-anim-plugin" / "data" / "coords.csv"

        with open(csv_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            all_point = []
            for row in reader:
                if row[0] in 'fps':
                    continue
                fps_rate = int(row[0])
                row.pop(0)
                point = []
                for i in range(0, len(row), 3):
                    point.append([int(row[i]), int(row[i + 2]), int(row[i + 1])])
                all_point.append(point.copy())
        
        for fr in range(len(all_point)):
            for j in range(33):
                obj_name = 'Cube.' + '0' * (3 - len(str(j))) + str(j)
                for i in range(3):
                    bpy.data.objects[obj_name].location[i] = all_point[fr][j][i]
                bpy.data.objects[obj_name].keyframe_insert(data_path="location", frame=fr)
        
        return {'FINISHED'}
