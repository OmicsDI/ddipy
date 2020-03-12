from unittest import TestCase

from ddipy.seo_client import SeoClient


class TestSeoClient(TestCase):

    def test_seo_home(self):
        client = SeoClient()
        res = client.get_seo_home()

    def test_seo_search(self):
        client = SeoClient()
        res = client.get_seo_search()

    def test_seo_search(self):
        client = SeoClient()
        res = client.get_seo_api()

    def test_seo_database(self):
        client = SeoClient()
        res = client.get_seo_database()

    def test_seo_dataset(self):
        client = SeoClient()
        res = client.get_seo_dataset("PXD000210", "pride")

    def test_seo_about(self):
        client = SeoClient()
        res = client.get_seo_about()