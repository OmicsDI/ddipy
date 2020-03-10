import requests

from ddipy import constants
from ddipy.ddi_utils import VerifyUtils


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
            return VerifyUtils.empty_param_error("dbName")

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
            return VerifyUtils.empty_param_error("luceneName")
        res = requests.get(constants.DB_NAME_URL, params={
            "luceneName": lucene_name
        }, headers=constants.HEADERS)
        return res
