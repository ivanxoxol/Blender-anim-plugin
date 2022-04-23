import cv2
import numpy as np
import mediapipe as mp
import pathlib
from pathlib import Path

mp_drawing = mp.solutions.drawing_utils
mp_holistic = mp.solutions.holistic

video_path = Path(pathlib.Path.cwd(), "video", "acrobatics.mp4")
cap = cv2.VideoCapture(str(video_path))

fps = float(cap.get(cv2.CAP_PROP_FPS))
w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

with mp_holistic.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5) as holistic:
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
        results = holistic.process(image)
        print(type(results.face_landmarks))
        # face_landmarks, pose_landmarks, 
        # left_hand_landmarks, right_hand_landmarks

        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        # 1. Draw face landmarks
        mp_drawing.draw_landmarks(image, results.face_landmarks, 
                                mp_holistic.FACE_CONNECTIONS, 
                                mp_drawing.DrawingSpec(color=(20,143,209), thickness=2, circle_radius=1),
                                mp_drawing.DrawingSpec(color=(7,95,143), thickness=2, circle_radius=2)
                                )
        # 2. Right hand
        mp_drawing.draw_landmarks(image, results.right_hand_landmarks, mp_holistic.HAND_CONNECTIONS, 
                                mp_drawing.DrawingSpec(color=(70,177,137), thickness=2, circle_radius=4),
                                mp_drawing.DrawingSpec(color=(38,110,84), thickness=2, circle_radius=2)
                                )
        # 3. Left Hand
        mp_drawing.draw_landmarks(image, results.left_hand_landmarks, mp_holistic.HAND_CONNECTIONS, 
                                mp_drawing.DrawingSpec(color=(70,177,137), thickness=2, circle_radius=4),
                                mp_drawing.DrawingSpec(color=(38,110,84), thickness=2, circle_radius=2)
                                )
        # 4. Pose Detections
        mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_holistic.POSE_CONNECTIONS, 
                                mp_drawing.DrawingSpec(color=(166,83,147), thickness=2, circle_radius=4),
                                mp_drawing.DrawingSpec(color=(92,28,78), thickness=2, circle_radius=2)
                                )
        cv2.imshow('video processing', image)

        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()