import requests

from ddipy.verify_utils import VerifyUtils


class SeoClient:
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                             "Chrome/54.0.2840.99 Safari/537.36"}
    seoHomeUrl = "https://www.omicsdi.org/ws/seo/home"
    seoSearchUrl = "https://www.omicsdi.org/ws/seo/search"
    seoApiUrl = "https://www.omicsdi.org/ws/seo/api"
    seoSchemaUrl = "https://www.omicsdi.org/ws/seo/schema"
    seoDatabaseUrl = "https://www.omicsdi.org/ws/seo/database"
    seoDatasetUrl = "https://www.omicsdi.org/ws/seo/dataset"
    seoAboutUrl = "https://www.omicsdi.org/ws/seo/about"

    def __init__(self):
        pass

    def get_seo_home(self):
        res = requests.get(self.seoHomeUrl, headers=self.headers)
        return res

    def get_seo_search(self):
        res = requests.get(self.seoSearchUrl, headers=self.headers)
        return res

    def get_seo_api(self):
        res = requests.get(self.seoApiUrl, headers=self.headers)
        return res

    def get_seo_schema(self, acc, domain):
        if acc:
            return VerifyUtils.empty_param_error("acc")

        if domain:
            return VerifyUtils.empty_param_error("domain")

        res = requests.get(self.seoSchemaUrl + "/" + domain + "/" + acc, headers=self.headers)
        return res

    def get_seo_database(self):
        res = requests.get(self.seoDatabaseUrl, headers=self.headers)
        return res

    def get_seo_dataset(self, domain, acc):
        if acc:
            return VerifyUtils.empty_param_error("acc")

        if domain:
            return VerifyUtils.empty_param_error("domain")

        res = requests.get(self.seoDatasetUrl + "/" + domain + "/" + acc, headers=self.headers)
        return res

    def get_seo_about(self):
        res = requests.get(self.seoAboutUrl, headers=self.headers)
        return res

