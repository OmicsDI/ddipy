import requests

from ddipy.verify_utils import VerifyUtils


class PublicationClient:
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                             "Chrome/54.0.2840.99 Safari/537.36"}
    listUrl = "https://www.omicsdi.org/ws/publication/list"

    def __init__(self):
        pass

    def get_list(self, acc):
        if not acc:
            return VerifyUtils.empty_param_error("acc")
        res = requests.get(self.listUrl, params={"acc": acc}, headers=self.headers)
        return res

