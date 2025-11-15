import sys
from networksecurity.logging import logger

class NetworkSecurityException(Exception):
    """Base class for all network security exceptions."""
    
    def __init__(self, error_message, error_details: sys):
        super().__init__(error_message)
        self.error_message = str(error_message)

        # Extract traceback details
        _, _, exc_tb = error_details.exc_info()
        self.lineno = exc_tb.tb_lineno
        self.file_name = exc_tb.tb_frame.f_code.co_filename

    def __str__(self):
        return (
            f"Error occurred in python script [{self.file_name}] "
            f"on line [{self.lineno}] "
            f"with message: {self.error_message}"
        )

