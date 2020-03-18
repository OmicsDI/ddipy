from unittest import TestCase

from ddipy.constants import DATA_NOT_FOUND, MISSING_PARAMETER
from ddipy.ddi_utils import BadRequest
from ddipy.term_client import TermClient


class TestTermClient(TestCase):

    def test_get_term_by_pattern(self):
        client = TermClient()
        res = client.get_term_by_pattern("hom", 10)
        assert res.total_count > 0
        assert len(res.items) > 0

        try:
            res = client.get_term_by_pattern("$@", 10)
        except BadRequest as err:
            assert err.status == DATA_NOT_FOUND

    def test_get_frequently_term_list(self):
        client = TermClient()

        res = client.get_term_frequently_term_list("pride", "description", 20)
        assert len(res)

        try:
            res = client.get_term_frequently_term_list("konkon", "description", 20)
        except BadRequest as err:
            assert err.status == DATA_NOT_FOUND

        try:
            res = client.get_term_frequently_term_list(None, "description", 20)
        except BadRequest as err:
            assert err.status == MISSING_PARAMETER
