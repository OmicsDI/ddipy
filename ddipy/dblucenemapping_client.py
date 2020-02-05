import requests

from ddipy.verify_utils import VerifyUtils


class DbLuceneMappingClient:
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                             "Chrome/54.0.2840.99 Safari/537.36"}
    saveMappingUrl = "https://www.omicsdi.org/ws/dblucene/saveMapping"
    getLuceneNameUrl = "https://www.omicsdi.org/ws/dblucene/getLuceneName"
    getAllMappingsUrl = "https://www.omicsdi.org/ws/dblucene/getAllMappings"
    getDbNameUrl = "https://www.omicsdi.org/ws/dblucene/getDbName"

    def __init__(self):
        pass

    def save_mapping(self, _id, db_url, logo_path, db_name, lucene_name, description, display_name):
        res = requests.put(self.saveMappingUrl, params={
            "id": _id,
            "dbUrl": db_url,
            "logoPath": logo_path,
            "dbName": db_name,
            "luceneName": lucene_name,
            "description": description,
            "displayName": display_name
        }, headers=self.headers)
        return res

    def get_lucene_name(self, db_name):
        if not db_name:
            return VerifyUtils.empty_param_error("dbName")

        res = requests.get(self.getLuceneNameUrl, params={
            "dbName": db_name
        }, headers=self.headers)
        return res

    def get_all_mappings(self):
        res = requests.get(self.getAllMappingsUrl, headers=self.headers)
        return res

    def get_db_name(self, lucene_name):
        if not lucene_name:
            return VerifyUtils.empty_param_error("luceneName")
        res = requests.get(self.getDbNameUrl, params={
            "luceneName": lucene_name
        }, headers=self.headers)
        return res
