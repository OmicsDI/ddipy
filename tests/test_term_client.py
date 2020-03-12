from unittest import TestCase

from ddipy.term_client import TermClient


class TestTermClient(TestCase):

    def test_get_term_by_pattern(self):
        client = TermClient()
        res = client.get_term_by_pattern("hom", 10)
        assert res.status_code == 200

    def test_get_frequently_term_list(self):
        client = TermClient()

        res = client.get_term_frequently_term_list("pride", "description", 20)
        assert res.status_code == 200