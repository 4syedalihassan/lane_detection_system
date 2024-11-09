# src/utils/error_handler.py
class ErrorHandler:
    def __init__(self, logger):
        self.logger = logger

    def handle(self, error):
        self.logger.error(f"Error occurred: {error}")
        # Add recovery mechanisms here
