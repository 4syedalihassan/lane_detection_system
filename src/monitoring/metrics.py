# monitoring/metrics.py
class PerformanceMonitor:
    def __init__(self):
        self.metrics = {
            'fps': [],
            'detection_confidence': [],
            'processing_time': []
        }
    
    def update_metrics(self, frame_metrics):
        for key, value in frame_metrics.items():
            self.metrics[key].append(value)
    
    def get_statistics(self):
        return {
            key: np.mean(values[-100:])
            for key, values in self.metrics.items()
        }