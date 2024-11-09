import numpy as np
from collections import deque

class LaneTracker:
    def __init__(self, config):
        self.history = {'left': deque(maxlen=config['history_size']),
                        'right': deque(maxlen=config['history_size'])}

    def update(self, left_fit, right_fit):
        if left_fit: self.history['left'].append(left_fit)
        if right_fit: self.history['right'].append(right_fit)
        return (np.mean(self.history['left'], axis=0) if self.history['left'] else None,
                np.mean(self.history['right'], axis=0) if self.history['right'] else None)