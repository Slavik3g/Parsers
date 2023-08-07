from fastapi import HTTPException
from starlette import status


class InvalidPositionIdException(HTTPException):
    def __init__(self):
        super().__init__(status_code=status.HTTP_404_NOT_FOUND,
                         detail="Bad ID")


class DefaultServerException(HTTPException):
    def __init__(self):
        super().__init__(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                         detail="Something unusual happened on the server")
