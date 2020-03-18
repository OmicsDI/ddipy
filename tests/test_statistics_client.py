from unittest import TestCase

from ddipy.statistics_client import StatisticsClient


class TestStatisticsClient(TestCase):

    def test_get_statistics_organisms(self):
        client = StatisticsClient()
        res = client.get_statistics_organisms(20)
        assert len(res) > 0

    def test_get_statistics_tissues(self):
        client = StatisticsClient()
        res = client.get_statistics_tissues(20)
        assert len(res) > 0

    def test_get_statistics_omics(self):
        client = StatisticsClient()
        res = client.get_statistics_omics()
        assert len(res) > 0

    def test_get_statistics_diseases(self):
        client = StatisticsClient()
        res = client.get_statistics_diseases(20)
        assert len(res) > 0

    def test_get_statistics_domains(self):
        client = StatisticsClient()
        res = client.get_statistics_domains()
        assert len(res) > 0

    def test_get_statistics_omics_by_year(self):
        client = StatisticsClient()
        res = client.get_statistics_omics_by_year()
        assert len(res) > 0
