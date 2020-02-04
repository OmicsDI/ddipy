import requests


class TermClient:
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                             "Chrome/54.0.2840.99 Safari/537.36"}
    getTermByPatternUrl = "https://www.omicsdi.org:443/ws/term/getTermByPattern"
    getFrequentlyTermListUrl = "https://www.omicsdi.org:443/ws/term/frequentlyTerm/list"

    def __init__(self):
        pass

    def get_term_by_pattern(self, q, size):
        res = requests.get(self.getTermByPatternUrl, params={
            "q": q,
            "size": size
        }, headers=self.headers)
        return res

    def get_term_frequently_term_list(self, size, domain, field):
        res = requests.get(self.getFrequentlyTermListUrl, params={
            "size": size,
            "domain": domain,
            "field": field
        }, headers=self.headers)
        return res
