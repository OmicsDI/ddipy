import requests

from ddipy import constants
from ddipy.constants import MISSING_PARAMETER
from ddipy.ddi_utils import VerifyUtils, BadRequest


class EnrichmentClient:

    def __init__(self):
        pass

    @staticmethod
    def get_synonyms_for_dataset(accession, database):
        if not accession:
            raise BadRequest("missing parameter accession", MISSING_PARAMETER, payload=None)

        if not database:
            raise BadRequest("missing parameter database", MISSING_PARAMETER, payload=None)

        res = requests.get(constants.SYNONYMS_URL, params={
            "accession": accession,
            "database": database
        }, headers=constants.HEADERS)
        return res

    @staticmethod
    def get_reanalysis():
        res = requests.get(constants.REANALYSIS_URL, headers=constants.HEADERS)
        return res

    @staticmethod
    def get_enrichment_info(accession, database):
        if not accession:
            raise BadRequest("missing parameter accession", MISSING_PARAMETER, payload=None)

        if not database:
            raise BadRequest("missing parameter database", MISSING_PARAMETER, payload=None)

        res = requests.get(constants.ENRICHMENT_INFO_URL, params={
            "accession": accession,
            "database": database
        }, headers=constants.HEADERS)
        return res

    @staticmethod
    def get_similar_datasets_by_biological_data(accession, database):
        if not accession:
            raise BadRequest("missing parameter accession", MISSING_PARAMETER, payload=None)

        if not database:
            raise BadRequest("missing parameter database", MISSING_PARAMETER, payload=None)

        res = requests.get(constants.SIMILAR_DATASETS_BIOLOGY_URL, params={
            "accession": accession,
            "database": database
        }, headers=constants.HEADERS)
        return res

    @staticmethod
    def get_similarity_info(accession, database, threshold):
        if not accession:
            raise BadRequest("missing parameter accession", MISSING_PARAMETER, payload=None)

        if not database:
            raise BadRequest("missing parameter database", MISSING_PARAMETER, payload=None)

        if not threshold:
            raise BadRequest("missing parameter threshold", MISSING_PARAMETER, payload=None)
        res = requests.get(constants.SIMILAR_INFO_URL, params={
            "accession": accession,
            "database": database,
            "threshold": threshold
        }, headers=constants.HEADERS)
        return res
