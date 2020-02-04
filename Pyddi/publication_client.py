import requests

from models.request.publication.PublicationList import PublicationList


class PublicationClient:
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                             "Chrome/54.0.2840.99 Safari/537.36"}
    listUrl = "https://www.omicsdi.org:443/ws/publication/list"

    def __init__(self):
        pass

    def get_list(self, acc):
        res = requests.get(self.listUrl, params={"acc": acc}, headers=self.headers)
        return res

