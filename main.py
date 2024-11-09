import yaml
import logging
from src.camera.camera_interface import CameraInterface
from src.preprocessing.image_processor import ImageProcessor
from src.detection.lane_detector import LaneDetector
from src.tracking.lane_tracker import LaneTracker
from src.integration.vehicle_interface import VehicleInterface
from src.utils.logger import setup_logger

def load_config(config_path):
    """Load YAML configuration file."""
    with open(config_path, 'r') as f:
        return yaml.safe_load(f)

def main():
    # Load configuration
    config = load_config("config/production.yml")

    # Setup logger
    logger = setup_logger("LaneDetectionSystem", config['system']['log_file'])
    logger.info("Initializing Lane Detection System...")

    # Initialize system components
    camera = CameraInterface(config['camera'])
    processor = ImageProcessor(config['preprocessing'])
    detector = LaneDetector(config['detection'])
    tracker = LaneTracker(config['tracking'])
    vehicle_interface = VehicleInterface()

    try:
        logger.info("Starting frame processing loop.")
        while True:
            # Capture frame
            frame = camera.get_frame()

            # Preprocess frame
            processed = processor.preprocess(frame)

            # Detect lanes
            left_fit, right_fit = detector.detect_lanes(processed)

            # Track lanes over time
            smoothed_left, smoothed_right = tracker.update(left_fit, right_fit)

            # Send lane data to vehicle interface
            vehicle_interface.send_lane_data({'left': smoothed_left, 'right': smoothed_right})

            # Log the results
            logger.info(f"Processed frame: Left Lane: {smoothed_left}, Right Lane: {smoothed_right}")

    except Exception as e:
        logger.error(f"System encountered an error: {e}", exc_info=True)

    finally:
        # Release camera resources
        camera.release()
        logger.info("Lane Detection System shutting down.")

if __name__ == "__main__":
    main()