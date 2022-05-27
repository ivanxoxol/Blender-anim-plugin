"""
This module opens the video and uses mediapipe to create a csv file with landmarks coordinates
to be used in blender.
"""

import bpy
from bpy.types import Operator
import cv2
import numpy as np
import mediapipe as mp
import csv
from pathlib import Path

class ANIM_OT_VideoProcessing(Operator):
    """ ??????????????? """

    bl_idname = "file.video_processing"
    bl_label = "Make CSV File"

    def execute(self, context):
        smooth_fact = 0.9

        mp_drawing = mp.solutions.drawing_utils
        mp_holistic = mp.solutions.holistic

        # Get video path
        video_path = Path('D:/MY/VisualStudioCode Projects/BLENDER-TERM-PROJECT/Blender-anim-plugin/video/acrobatics.mp4')
        cap = cv2.VideoCapture(str(video_path))

        fps = int(cap.get(cv2.CAP_PROP_FPS))

        # Make csv file profile
        num_coords = 33
        landmarks = ["fps"]
        for val in range(1, num_coords + 1):
            landmarks += [  'x{}'.format(val),
                            'y{}'.format(val),
                            'z{}'.format(val)   ]

        csv_path = Path.cwd().parents[0] / "Blender-anim-plugin" / "data" / "coords.csv"

        with open(csv_path, mode='w', newline='') as f:
            csv_writer = csv.writer(f, delimiter=',',
                                    quotechar='"',
                                    quoting=csv.QUOTE_MINIMAL)
            csv_writer.writerow(landmarks)

        # Make detections using mediapipe holistic mode
        with mp_holistic.Holistic(  min_detection_confidence=0.5,
                                    min_tracking_confidence=0.5   ) as holistic:
            i = 0
            while cap.isOpened():

                # Check the video stream
                ret, frame = cap.read()
                if not ret:
                    print("Ignoring empty camera frame.")
                    break

                # Get results
                image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                image.flags.writeable = False

                results = holistic.process(image)

                image.flags.writeable = True
                image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

                # Pose Detections
                mp_drawing.draw_landmarks(image, results.pose_landmarks,
                                            mp_holistic.POSE_CONNECTIONS,
                                            mp_drawing.DrawingSpec( color=(166, 83, 147),
                                                                    thickness=2,
                                                                    circle_radius=4 ),
                                            mp_drawing.DrawingSpec( color=(92, 28, 78),
                                                                    thickness=2,
                                                                    circle_radius=2 ))

                # Export coordinates
                h, w, c = frame.shape

                try:
                    pose = results.pose_landmarks.landmark
                except AttributeError:
                    continue

                i += 1
                pose_row = [fps]
                pose_row += list(np.array([[int(w / 10 - (landmark.x * w) / 10),
                                            int(h / 10 - (landmark.y * h) / 10),
                                            int(c / 10 - (landmark.z * c) / 10)]
                                                            for landmark in pose]).flatten())
                if i == 1:
                    pose_row_before = pose_row.copy()
                else:
                    for j in range(1, len(pose_row), 3):
                        pose_row[j] = int(smooth_fact * pose_row[j] + (1 - smooth_fact) * pose_row_before[j])
                    pose_row_before = pose_row.copy()

                with open(csv_path, mode='a', newline='') as f:
                    csv_writer = csv.writer(f, delimiter=',',
                                            quotechar='"',
                                            quoting=csv.QUOTE_MINIMAL)
                    csv_writer.writerow(pose_row)

                # Show video processing in window
                cv2.imshow('video processing', image)

                if cv2.waitKey(5) & 0xFF == ord('q'):
                    break

        cap.release()
        cv2.destroyAllWindows()

        return {"FINISHED"}
