import requests

from ddipy import constants
from ddipy.commons import StructuredDataGraph, StructuredData
from ddipy.constants import MISSING_PARAMETER
from ddipy.ddi_utils import VerifyUtils, BadRequest


class SeoClient:

    def __init__(self):
        pass

    @staticmethod
    def get_seo_home():
        res = requests.get(constants.SEO_URL_HOME, headers=constants.HEADERS)
        if res.status_code != 200:
            raise BadRequest("The request thrown connection error", res.status_code, payload=None)
        return StructuredDataGraph.get_object_from_json(res.json())

    @staticmethod
    def get_seo_search():
        res = requests.get(constants.SEO_SEARCH_URL, headers=constants.HEADERS)
        if res.status_code != 200:
            raise BadRequest("The request thrown connection error", res.status_code, payload=None)
        return StructuredData.get_object_from_json(res.json())

    @staticmethod
    def get_seo_api():
        res = requests.get(constants.SEO_API_URL, headers=constants.HEADERS)
        if res.status_code != 200:
            raise BadRequest("The request thrown connection error", res.status_code, payload=None)
        return StructuredData.get_object_from_json(res.json())

    @staticmethod
    def get_seo_schema(acc, domain):
        if not acc:
            raise BadRequest("missing parameter acc", MISSING_PARAMETER, payload=None)

        if not domain:
            raise BadRequest("missing parameter domain", MISSING_PARAMETER, payload=None)

        res = requests.get(constants.SEO_SCHEMA_URL + "/" + domain + "/" + acc, headers=constants.HEADERS)

        return res

    @staticmethod
    def get_seo_database():
        res = requests.get(constants.SEO_DATABASE_URL, headers=constants.HEADERS)
        if res.status_code != 200:
            raise BadRequest("The request thrown connection error", res.status_code, payload=None)
        return StructuredData.get_object_from_json(res.json())

    @staticmethod
    def get_seo_dataset(domain, acc):
        if not acc:
            raise BadRequest("missing parameter acc", MISSING_PARAMETER, payload=None)

        if not domain:
            raise BadRequest("missing parameter domain", MISSING_PARAMETER, payload=None)

        res = requests.get(constants.SEO_DATASET_URL + "/" + domain + "/" + acc, headers=constants.HEADERS)

        if res.status_code != 200:
            raise BadRequest("The request accession {} and database {} thrown connection error", res.status_code, payload=None)
        return StructuredData.get_object_from_json(res.json())

    @staticmethod
    def get_seo_about():
        res = requests.get(constants.SEO_ABOUT_URL, headers=constants.HEADERS)
        if res.status_code != 200:
            raise BadRequest("The request thrown connection error", res.status_code, payload=None)
        return StructuredData.get_object_from_json(res.json())
