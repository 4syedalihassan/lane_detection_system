# src/camera/camera_interface.py
import cv2

class CameraInterface:
    def __init__(self, config):
        self.camera = cv2.VideoCapture(config['id'])
        self.camera.set(cv2.CAP_PROP_FRAME_WIDTH, config['width'])
        self.camera.set(cv2.CAP_PROP_FRAME_HEIGHT, config['height'])
        self.camera.set(cv2.CAP_PROP_FPS, config['fps'])

    def get_frame(self):
        ret, frame = self.camera.read()
        if not ret:
            raise RuntimeError("Failed to capture frame from camera")
        return frame

    def release(self):
        self.camera.release()