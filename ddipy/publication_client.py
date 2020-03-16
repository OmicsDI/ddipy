import requests

from ddipy import constants
from ddipy.constants import MISSING_PARAMETER
from ddipy.ddi_utils import BadRequest


class PublicationClient:

    def __init__(self):
        pass

    @staticmethod
    def get_list(acc):
        if not acc:
            raise BadRequest("missing parameter acc", MISSING_PARAMETER, payload=None)
        res = requests.get(constants.LIST_URL, params={"acc": acc}, headers=constants.HEADERS)
        return res
