import bpy
import math
import csv

ar = bpy.context.active_object

def animate():
    with open('coords.csv', newline='', encoding='utf-8') as csvfile:
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
        bn = 0
        for bone in ar.pose.bones:
            for i in range(3):
                bone.location[i] = all_point[fr][bn][i]
            bone.keyframe_insert(data_path="location", frame=fr)
            bn += 1


def delete_keys():
    context = bpy.context
    for ob in context.selected_objects:
        ob.animation_data_clear()
        
    
if __name__ == "__main__":
    delete_keys()
    animate()