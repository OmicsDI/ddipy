import requests

from ddipy import constants
from ddipy.constants import MISSING_PARAMETER
from ddipy.ddi_utils import VerifyUtils, BadRequest


class DbLuceneMappingClient:

    def __init__(self):
        pass

    @staticmethod
    def save_mapping(_id, db_url, logo_path, db_name, lucene_name, description, display_name):
        res = requests.put(constants.SAVE_MAPPING_URL, params={
            "id": _id,
            "dbUrl": db_url,
            "logoPath": logo_path,
            "dbName": db_name,
            "luceneName": lucene_name,
            "description": description,
            "displayName": display_name
        }, headers=constants.HEADERS)
        return res

    @staticmethod
    def get_lucene_name(db_name):
        if not db_name:
            raise BadRequest("missing parameter db_name", MISSING_PARAMETER, payload=None)

        res = requests.get(constants.LUCENE_NAME_URL, params={
            "dbName": db_name
        }, headers=constants.HEADERS)
        return res

    @staticmethod
    def get_all_mappings():
        res = requests.get(constants.MAPPINGS_URL, headers=constants.HEADERS)
        return res

    @staticmethod
    def get_db_name(lucene_name):
        if not lucene_name:
            raise BadRequest("missing parameter lucene_name", MISSING_PARAMETER, payload=None)
        res = requests.get(constants.DB_NAME_URL, params={
            "luceneName": lucene_name
        }, headers=constants.HEADERS)
        return res
