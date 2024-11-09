# src/system/async_processor.py
import threading

class AsyncProcessor:
    def __init__(self, processing_function):
        self.processing_function = processing_function
        self.lock = threading.Lock()

    def process_async(self, data):
        thread = threading.Thread(target=self.processing_function, args=(data,))
        thread.start()
