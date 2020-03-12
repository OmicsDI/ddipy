import requests

from ddipy import constants
from ddipy.ddi_utils import VerifyUtils


class TermClient:

    def __init__(self):
        pass

    @staticmethod
    def get_term_by_pattern(q="hom", size=10):
        res = requests.get(constants.TERM_BY_PATTERN_URL, params={
            "q": q,
            "size": size
        }, headers=constants.HEADERS)
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
        return res
