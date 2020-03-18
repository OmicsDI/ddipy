import requests

from ddipy import constants
from ddipy.commons import StatRecord, DomainStats, StatOmicsRecord
from ddipy.ddi_utils import BadRequest


class StatisticsClient:

    def __init__(self):
        pass

    @staticmethod
    def get_statistics_organisms(size=20):
        res = requests.get(constants.STATISTICS_URL + "/organisms", params={
            "size": size
        }, headers=constants.HEADERS)
        if res.status_code != 200:
            raise BadRequest("The request size {} thrown connection error".format(size), res.status_code, payload=None)
        stat_records = []
        if res.json():
            for stat_record_json in res.json():
                stat_record = StatRecord.get_object_from_json(stat_record_json)
                stat_records.append(stat_record)

        return stat_records

    @staticmethod
    def get_statistics_tissues(size=20):
        res = requests.get(constants.STATISTICS_URL + "/tissues", params={
            "size": size
        }, headers=constants.HEADERS)
        stat_records = []
        if res.json():
            for stat_record_json in res.json():
                stat_record = StatRecord.get_object_from_json(stat_record_json)
                stat_records.append(stat_record)

        return stat_records

    @staticmethod
    def get_statistics_omics():
        res = requests.get(constants.STATISTICS_URL + "/omics", headers=constants.HEADERS)
        stat_records = []
        if res.json():
            for stat_record_json in res.json():
                stat_record = StatRecord.get_object_from_json(stat_record_json)
                stat_records.append(stat_record)

        return stat_records

    @staticmethod
    def get_statistics_diseases(size=20):
        res = requests.get(constants.STATISTICS_URL + "/diseases", params={
            "size": size
        }, headers=constants.HEADERS)
        stat_records = []
        if res.json():
            for stat_record_json in res.json():
                stat_record = StatRecord.get_object_from_json(stat_record_json)
                stat_records.append(stat_record)

        return stat_records

    @staticmethod
    def get_statistics_domains():
        res = requests.get(constants.STATISTICS_URL + "/domains", headers=constants.HEADERS)
        domain_statuses = []
        if res.json():
            for domain_stats_json in res.json():
                domain_stats = DomainStats.get_object_from_json(domain_stats_json)
                domain_statuses.append(domain_stats)
        return domain_statuses

    @staticmethod
    def get_statistics_omics_by_year():
        res = requests.get(constants.STATISTICS_URL + "/omicsByYear", headers=constants.HEADERS)
        omics_by_years = []
        if res.json():
            for omics_by_year_json in res.json():
                omics_by_year = StatOmicsRecord.get_object_from_json(omics_by_year_json)
                omics_by_years.append(omics_by_year)
        return omics_by_years



