# tests/test_system.py
def test_complete_pipeline():
    # Initialize components
    camera = CameraInterface()
    processor = ImageProcessor(config)
    detector = LaneDetector(config)
    tracker = LaneTracker(config)
    
    # Process frame
    frame = camera.get_frame()
    processed = processor.preprocess(frame)
    left_fit, right_fit = detector.detect_lanes(processed)
    tracked_left, tracked_right = tracker.update(left_fit, right_fit)
    
    # Validate results
    assert validate_system_output(tracked_left, tracked_right)