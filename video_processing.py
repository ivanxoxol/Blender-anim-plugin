import cv2
import numpy as np
import pathlib
from pathlib import Path

video_path = Path(pathlib.Path.cwd(), "video", "acrobatics.mp4")
cap = cv2.VideoCapture(str(video_path))

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
fps = float(cap.get(cv2.CAP_PROP_FPS))
w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
out = cv2.VideoWriter('output.mp4', fourcc, fps, (w,h))

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    out.write(frame)

    cv2.imshow('video feed', frame)
    cv2.imshow('gray feed', gray)    

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()