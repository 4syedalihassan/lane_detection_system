# src/utils/data_logger.py
import cv2
import os

class DataLogger:
    def __init__(self, log_dir):
        os.makedirs(log_dir, exist_ok=True)
        self.log_dir = log_dir

    def save_frame(self, frame, name="frame.jpg"):
        cv2.imwrite(os.path.join(self.log_dir, name), frame)
