import pytest
import numpy as np
from src.detection.lane_detector import LaneDetector

def test_lane_detection():
    config = {'detection': {'some_param': 1}}
    detector = LaneDetector(config)
    binary_image = np.zeros((720, 1280), dtype=np.uint8)

    left_fit, right_fit = detector.detect_lanes(binary_image)
    assert left_fit is None
    assert right_fit is None