from rest_framework import status
from .service import msg_error_status

def get_status_error(error):
    if "Errors" in error:
        if error['Errors'] == msg_error_status:
            return status.HTTP_404_NOT_FOUND
    return status.HTTP_400_BAD_REQUEST

