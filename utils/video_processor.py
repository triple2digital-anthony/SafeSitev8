import cv2
import numpy as np
import torch
from PIL import Image
import os

def load_model():
    # Load a pre-trained model (e.g., YOLOv5)
    model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)
    return model

def process_video(video_path, model):
    cap = cv2.VideoCapture(video_path)
    frames = []
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        # Convert frame to PIL Image
        img = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        # Perform detection
        results = model(img)
        # Draw bounding boxes
        frame = np.squeeze(results.render())
        frames.append(frame)
    cap.release()
    return frames 

print("Current working directory:", os.getcwd())
print("Contents of utils directory:", os.listdir('utils'))