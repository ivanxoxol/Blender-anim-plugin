import bpy
import csv
from bpy.types import Operator
from bpy.utils import register_class


class Move_obj(Operator):
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

        with open('coords.csv', newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            all_point = []
            frame_of_end = 0
            for row in reader:
                frame_of_end += 1
                if row[0] in 'fps':
                    continue
                fps_rate = int(row[0])
                row.pop(0)
                point = []
                for i in range(0, len(row), 3):
                    point.append([int(row[i]), int(row[i + 2]), int(row[i + 1])])
                all_point.append(point.copy())
        
        bpy.data.scenes["Scene"].frame_end = frame_of_end
        now_current = bpy.context.scene.frame_current
        bpy.context.scene.render.fps = fps_rate
        
        for j in range(33):
            obj_name = 'Cube.' + '0' * (3 - len(str(j))) + str(j)
            for i in range(3):
                try:
                    bpy.data.objects[obj_name].location[i] = all_point[now_current][j][i]
                    bpy.data.objects[obj_name].keyframe_insert(data_path="location", frame=now_current)
                except IndexError:
                    continue
                
        if now_current == frame_of_end:
            bpy.app.handlers.frame_change_pre.clear()
        
        return {'FINISHED'}


if __name__ == '__main__':    
    register_class(Move_obj)

    for j in range(33):
        obj_name = 'Cube.' + '0' * (3 - len(str(j))) + str(j)
        bpy.data.objects[obj_name].animation_data_clear()
        
    bpy.app.handlers.frame_change_pre.append(Move_obj.execute)