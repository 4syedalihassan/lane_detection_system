from src.preprocessing.image_processor import ImageProcessor
from src.detection.lane_detector import LaneDetector
from src.tracking.lane_tracker import LaneTracker

class LaneDetectionSystem:
    def __init__(self, config, camera):
        self.camera = camera
        self.processor = ImageProcessor(config['preprocessing'])
        self.detector = LaneDetector(config['detection'])
        self.tracker = LaneTracker(config['tracking'])

    def process_frame(self):
        frame = self.camera.get_frame()
        processed = self.processor.preprocess(frame)
        left_fit, right_fit = self.detector.detect_lanes(processed)
        return self.tracker.update(left_fit, right_fit)