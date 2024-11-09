import cv2
import numpy as np

class ImageProcessor:
    def __init__(self, config):
        self.config = config

    def preprocess(self, frame):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        blurred = cv2.GaussianBlur(gray, (5, 5), 0)
        enhanced = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8)).apply(blurred)
        return self.perspective_transform(enhanced)

    def perspective_transform(self, img):
        M = cv2.getPerspectiveTransform(
            np.float32(self.config['perspective_src']),
            np.float32(self.config['perspective_dst'])
        )
        return cv2.warpPerspective(img, M, (img.shape[1], img.shape[0]))
