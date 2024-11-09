# Lane Detection System

A robust, real-time lane detection system designed for autonomous vehicles and advanced driver-assistance systems (ADAS). This system uses computer vision and machine learning techniques to accurately detect, track, and visualize lane markings on the road.

## Features

- **Real-time Lane Detection**: Detects lane lines in video streams with high accuracy.
- **Lane Tracking**: Smoothens lane detection across frames using historical data.
- **Modular Design**: Easily extend or customize preprocessing, detection, and tracking.
- **Hardware Acceleration**: Supports GPU for high-performance processing.
- **Vehicle Integration**: Communicates with a vehicle's control system via CAN bus.

---

## Table of Contents

1. [Installation](#installation)
2. [Usage](#usage)
3. [Configuration](#configuration)
4. [Directory Structure](#directory-structure)
5. [Development](#development)
6. [Testing](#testing)
7. [License](#license)

---

## Installation

### Prerequisites
- Python 3.9+
- OpenCV 4.5+
- PyTorch 1.9+ (with GPU support for NVIDIA GPUs)
- A compatible camera (e.g., USB camera, webcam)

### Setup Instructions
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/lane-detection-system.git
   cd lane-detection-system
   ```

2. Create and activate a virtual environment:
   ```bash
   python3 -m venv lane_detection_env
   source lane_detection_env/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Configure the system:
   Edit the `config/production.yml` file to match your camera and system specifications.

5. Run the system:
   ```bash
   python main.py
   ```

---

## Usage

### Real-Time Lane Detection
The system processes live video feed from the camera and detects lane lines in real-time. Detected lanes are smoothed using tracking and sent to the vehicle's control system.

### Debug Mode
Enable debug mode in the configuration file to visualize frames with detected lanes overlayed:
```yaml
system:
  debug_mode: true
```

### Saving Processed Data
To save frames or lane data for debugging, set `save_data` to `true` in the configuration.

---

## Configuration

The system uses a YAML configuration file located at `config/production.yml`. Key sections include:

- **Camera Settings**: Resolution, FPS, and camera ID.
- **Preprocessing Parameters**: Gaussian blur kernel size, CLAHE settings, and perspective transformation points.
- **Detection Parameters**: Sliding window settings, thresholds, and validation rules.
- **Tracking Settings**: History size and thresholds for smoothing.
- **System Options**: GPU toggle, logging level, debug mode, and data saving options.

Example configuration:
```yaml
camera:
  id: 0
  width: 1920
  height: 1080
  fps: 30

preprocessing:
  blur_kernel_size: 5
  clahe_clip_limit: 2.0
  perspective_src: [[590, 450], [690, 450], [1080, 720], [200, 720]]
  perspective_dst: [[320, 0], [960, 0], [960, 720], [320, 720]]

system:
  gpu_enabled: true
  log_level: INFO
  debug_mode: false
  save_data: false
```

---

## Directory Structure

```plaintext
lane-detection-system/
├── src/                         # Source code
│   ├── preprocessing/           # Preprocessing modules
│   ├── detection/               # Lane detection algorithms
│   ├── tracking/                # Tracking modules
│   ├── integration/             # Vehicle integration
│   ├── visualization/           # Visualization tools
│   └── utils/                   # Utility scripts
├── tests/                       # Unit and system tests
├── config/                      # Configuration files
├── docs/                        # Documentation and diagrams
├── logs/                        # Log files
├── data/                        # Sample data for testing and training
├── main.py                      # Entry point for the application
├── requirements.txt             # Python dependencies
└── README.md                    # Project overview and instructions
```

---

## Development

### Adding Features
1. Add new modules to the relevant subdirectories under `src/`.
2. Follow the existing modular design for consistency.
3. Update the configuration file if new parameters are required.

### Profiling
Use the built-in profiler to identify bottlenecks:
```python
from src.utils.profiler import profile_function
profile_function(system.process_frame, frame)
```

---

## Testing

The system includes unit and integration tests under the `tests/` directory.

### Run All Tests
```bash
pytest tests/
```

### Add New Tests
1. Write new test cases in the `tests/` directory.
2. Use mock data to validate new features.

Example test:
```python
def test_lane_detection():
    detector = LaneDetector(config)
    result = detector.detect_lanes(mock_binary_image)
    assert result['left'] is not None
    assert result['right'] is not None
```

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Contributing

Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a feature branch (`git checkout -b feature/new-feature`).
3. Commit your changes (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature/new-feature`).
5. Open a pull request.

---

## Acknowledgments

This project is inspired by advancements in autonomous vehicle technologies and the open-source community.

---

Feel free to update the repository link, license, or acknowledgments as needed. Would you like help drafting a contribution guide or issue templates for GitHub?
