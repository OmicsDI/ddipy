import requests

from ddipy import constants


class StatisticsClient:

    def __init__(self):
        pass

    @staticmethod
    def get_statistics_organisms(size=20):
        res = requests.get(constants.STATISTICS_URL + "/organisms", params={
            "size": size
        }, headers=constants.HEADERS)
        return res

    @staticmethod
    def get_statistics_tissues(size=20):
        res = requests.get(constants.STATISTICS_URL + "/tissues", params={
            "size": size
        }, headers=constants.HEADERS)
        return res

    @staticmethod
    def get_statistics_omics():
        res = requests.get(constants.STATISTICS_URL + "/omics", headers=constants.HEADERS)
        return res

    @staticmethod
    def get_statistics_diseases(size=20):
        res = requests.get(constants.STATISTICS_URL + "/diseases", params={
            "size": size
        }, headers=constants.HEADERS)
        return res

    @staticmethod
    def get_statistics_domains():
        res = requests.get(constants.STATISTICS_URL + "/domains", headers=constants.HEADERS)
        return res

    @staticmethod
    def get_statistics_omics_by_year():
        res = requests.get(constants.STATISTICS_URL + "/omicsByYear", headers=constants.HEADERS)
        return res



