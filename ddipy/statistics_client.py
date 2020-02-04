import requests


class StatisticsClient:
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                             "Chrome/54.0.2840.99 Safari/537.36"}
    getStatisticsOrganismsUrl = "https://www.omicsdi.org:443/ws/statistics/organisms"
    getStatisticsTissuesUrl = "https://www.omicsdi.org:443/ws/statistics/tissues"
    getStatisticsOmicsUrl = "https://www.omicsdi.org:443/ws/statistics/omics"
    getStatisticsVersionUrl = "https://www.omicsdi.org:443/ws/statistics/version"
    getStatisticsDiseasesUrl = "https://www.omicsdi.org:443/ws/statistics/diseases"
    getStatisticsDomainsUrl = "https://www.omicsdi.org:443/ws/statistics/domains"
    getStatisticsOmicsByYearUrl = "https://www.omicsdi.org:443/ws/statistics/omicsByYear"
    getStatisticsGeneralUrl = "https://www.omicsdi.org:443/ws/statistics/general"

    def __init__(self):
        pass

    def get_statistics_organisms(self, size):
        res = requests.get(self.getStatisticsOrganismsUrl, params={
            "size": size
        }, headers=self.headers)
        return res

    def get_statistics_tissues(self, size):
        res = requests.get(self.getStatisticsTissuesUrl, params={
            "size": size
        }, headers=self.headers)
        return res

    def get_statistics_omics(self):
        res = requests.get(self.getStatisticsOmicsUrl, headers=self.headers)
        return res

    def get_statistics_version(self):
        res = requests.get(self.getStatisticsVersionUrl, headers=self.headers)
        return res

    def get_statistics_diseases(self, size):
        res = requests.get(self.getStatisticsDiseasesUrl, params={
            "size": size
        }, headers=self.headers)
        return res

    def get_statistics_domains(self):
        res = requests.get(self.getStatisticsDomainsUrl, headers=self.headers)
        return res

    def get_statistics_omics_by_year(self):
        res = requests.get(self.getStatisticsOmicsByYearUrl, headers=self.headers)
        return res

    def get_statistics_general(self):
        res = requests.get(self.getStatisticsGeneralUrl, headers=self.headers)
        return res



