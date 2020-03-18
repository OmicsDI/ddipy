import requests

from ddipy import constants
from ddipy.commons import DictWord, Term
from ddipy.constants import DATA_NOT_FOUND, MISSING_PARAMETER
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
        return DictWord.get_object_from_json(res.json())

    @staticmethod
    def get_term_frequently_term_list(domain, field, size=20):
        if not domain:
            raise BadRequest("missing parameter domain", MISSING_PARAMETER, payload=None)

        if not field:
            raise BadRequest("missing parameter field", MISSING_PARAMETER, payload=None)

        res = requests.get(constants.FREQUENTLY_TERM_URL, params={
            "size": size,
            "domain": domain,
            "field": field
        }, headers=constants.HEADERS)

        if res.status_code != 200:
            raise BadRequest("The request domain {} and field {} and size {} thrown connection error".format(domain, field, size), res.status_code, payload=None)

        terms = []
        if res.json():
            for term_json in res.json():
                term = Term.get_object_from_json(term_json)
                terms.append(term)

        return terms
