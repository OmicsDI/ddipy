class VerifyUtils:

    @staticmethod
    def empty_param_error(param_name):
        return {"error": param_name + " is missing"}


class BadRequest(Exception):
    """Custom exception class to be thrown when local error occurs."""

    def __init__(self, message, status=400, payload=None):
        self.message = message
        self.status = status
        self.payload = payload
