# src/exception.py
class CustomException(Exception):
    def __init__(self, message, error_detail=None):
        super().__init__(message)
        self.error_detail = error_detail

