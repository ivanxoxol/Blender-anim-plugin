import cv2
import numpy as np
import mediapipe as mp
import pathlib
from pathlib import Path
import csv
import os

mp_drawing = mp.solutions.drawing_utils
mp_holistic = mp.solutions.holistic

# Get video path
video_path = Path(pathlib.Path.cwd(), "video", "acrobatics.mp4")
cap = cv2.VideoCapture(str(video_path))

# Make csv file profile
num_coords = 33
landmarks = []
for val in range(1, num_coords+1):
    landmarks += [  'x{}'.format(val), 
                    'y{}'.format(val), 
                    'z{}'.format(val), 
                    'v{}'.format(val)   ]
with open('coords.csv', mode='w', newline='') as f:
    csv_writer = csv.writer(f, delimiter=',', 
                            quotechar='"', 
                            quoting=csv.QUOTE_MINIMAL)
    csv_writer.writerow(landmarks)

# Make detections using mediapipe holistic mode
with mp_holistic.Holistic(
                    min_detection_confidence=0.5,
                    min_tracking_confidence=0.5     ) as holistic:
    
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
                                mp_drawing.DrawingSpec(color=(166,83,147), 
                                                        thickness=2, 
                                                        circle_radius=4),
                                mp_drawing.DrawingSpec(color=(92,28,78), 
                                                        thickness=2, 
                                                        circle_radius=2))
        
        # Export coordinates
        try:
            pose = results.pose_landmarks.landmark
            pose_row = list(np.array([[landmark.x, 
                                        landmark.y, 
                                        landmark.z, 
                                        landmark.visibility] 
                                    for landmark in pose]).flatten())
            
            with open('coords.csv', mode='a', newline='') as f:
                csv_writer = csv.writer(f, delimiter=',', 
                                        quotechar='"', 
                                        quoting=csv.QUOTE_MINIMAL)
                csv_writer.writerow(pose_row) 
        except:
            pass
        
        # Show video processing in window
        cv2.imshow('video processing', image)

        if cv2.waitKey(5) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()