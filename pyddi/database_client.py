import requests


class DatabaseClient:
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                             "Chrome/54.0.2840.99 Safari/537.36"}
    baseDatabaseUrl = "https://www.omicsdi.org:443/ws/database"
    getDatabaseAllUrl = "https://www.omicsdi.org:443/ws/database/all"
    getDatabasePicbytesUrl = "https://www.omicsdi.org:443/ws/database/db/picturebyte"

    def __init__(self):
        pass

    def get_database_pic(self, database_name):
        res = requests.get(self.baseDatabaseUrl + "/" + database_name + "/picture",  headers=self.headers)
        return res

    def get_database_all(self):
        res = requests.get(self.getDatabaseAllUrl,  headers=self.headers)
        return res

    def get_database_db_picturebyte(self):
        res = requests.get(self.getDatabasePicbytesUrl, headers=self.headers)
        return res
