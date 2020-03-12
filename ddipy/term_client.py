import requests

from ddipy import constants
from ddipy.constants import DATA_NOT_FOUND
from ddipy.ddi_utils import VerifyUtils, BadRequest


class TermClient:

    def __init__(self):
        pass

    @staticmethod
    def get_term_by_pattern(q="hom", size=10):
        res = requests.get(constants.TERM_BY_PATTERN_URL, params={
            "q": q,
            "size": size
        }, headers=constants.HEADERS)
        if res.status_code != 200:
            raise BadRequest("The request query {} and size {} thrown connection error".format(q, size), res.status_code, payload=None)
        if res.status_code == 200 and res.json()["total_count"] ==0:
            raise BadRequest("The request found nothing in server", DATA_NOT_FOUND, payload=None)
        return res

    @staticmethod
    def get_term_frequently_term_list(domain, field, size=20):
        if not domain:
            return VerifyUtils.empty_param_error("domain")

        if not field:
            return VerifyUtils.empty_param_error("field")

        res = requests.get(constants.FREQUENTLY_TERM_URL, params={
            "size": size,
            "domain": domain,
            "field": field
        }, headers=constants.HEADERS)

        if res.status_code != 200:
            raise BadRequest("The request domain {} and field {} and size {} thrown connection error".format(domain, field, size), res.status_code, payload=None)
        if res.status_code == 200 and len(res.json()) == 0:
            raise BadRequest("The request found nothing in server", DATA_NOT_FOUND, payload=None)
        return res
