import requests

from ddipy import constants
from ddipy.verify_utils import VerifyUtils


class PublicationClient:

    def __init__(self):
        pass

    @staticmethod
    def get_list(acc):
        if not acc:
            return VerifyUtils.empty_param_error("acc")
        res = requests.get(constants.LIST_URL, params={"acc": acc}, headers=constants.HEADERS)
        return res
