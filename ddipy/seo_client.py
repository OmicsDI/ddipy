import requests

from ddipy import constants
from ddipy.ddi_utils import VerifyUtils, BadRequest


class SeoClient:

    def __init__(self):
        pass

    @staticmethod
    def get_seo_home():
        res = requests.get(constants.SEO_URL_HOME, headers=constants.HEADERS)
        if res.status_code != 200:
            raise BadRequest("The request thrown connection error", res.status_code, payload=None)
        return res

    @staticmethod
    def get_seo_search():
        res = requests.get(constants.SEO_SEARCH_URL, headers=constants.HEADERS)
        if res.status_code != 200:
            raise BadRequest("The request thrown connection error", res.status_code, payload=None)
        return res

    @staticmethod
    def get_seo_api():
        res = requests.get(constants.SEO_API_URL, headers=constants.HEADERS)
        if res.status_code != 200:
            raise BadRequest("The request thrown connection error", res.status_code, payload=None)
        return res

    @staticmethod
    def get_seo_schema(acc, domain):
        if not acc:
            return VerifyUtils.empty_param_error("acc")

        if not domain:
            return VerifyUtils.empty_param_error("domain")

        res = requests.get(constants.SEO_SCHEMA_URL + "/" + domain + "/" + acc, headers=constants.HEADERS)

        return res

    @staticmethod
    def get_seo_database():
        res = requests.get(constants.SEO_DATABASE_URL, headers=constants.HEADERS)
        if res.status_code != 200:
            raise BadRequest("The request thrown connection error", res.status_code, payload=None)
        return res

    @staticmethod
    def get_seo_dataset(domain, acc):
        if not acc:
            return VerifyUtils.empty_param_error("acc")

        if not domain:
            return VerifyUtils.empty_param_error("domain")

        res = requests.get(constants.SEO_DATASET_URL + "/" + domain + "/" + acc, headers=constants.HEADERS)

        if res.status_code != 200:
            raise BadRequest("The request accession {} and database {} thrown connection error", res.status_code, payload=None)
        return res

    @staticmethod
    def get_seo_about():
        res = requests.get(constants.SEO_ABOUT_URL, headers=constants.HEADERS)
        if res.status_code != 200:
            raise BadRequest("The request thrown connection error", res.status_code, payload=None)
        return res
