from unittest import TestCase

from ddipy.constants import MISSING_PARAMETER
from ddipy.ddi_utils import BadRequest
from ddipy.seo_client import SeoClient


class TestSeoClient(TestCase):

    def test_seo_home(self):
        client = SeoClient()
        res = client.get_seo_home()
        assert res.status_code == 200

    def test_seo_search(self):
        client = SeoClient()
        res = client.get_seo_search()
        assert res.status_code == 200

    def test_seo_search(self):
        client = SeoClient()
        res = client.get_seo_api()
        assert res.status_code == 200

    def test_seo_database(self):
        client = SeoClient()
        res = client.get_seo_database()
        assert res.status_code == 200

    def test_seo_dataset(self):
        client = SeoClient()
        res = client.get_seo_dataset("pride", "PXD000210")
        assert res.status_code ==200
        try:
            res = client.get_seo_dataset("pride", "PXDqqqqqqqq")
        except BadRequest as err:
            assert err.status == 500

        try:
            res = client.get_seo_dataset(None, "PXDqqqqqqqq")
        except BadRequest as err:
            assert err.status == MISSING_PARAMETER

    def test_seo_about(self):
        client = SeoClient()
        res = client.get_seo_about()
        assert res.status_code == 200
