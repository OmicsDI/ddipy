from unittest import TestCase

from ddipy.database_client import DatabaseClient
from ddipy.ddi_utils import BadRequest


class TestDatabaseClient(TestCase):

    def test_get_database_all(self):
        client = DatabaseClient()
        try:
            res = client.get_database_all()
            assert len(res) > 0
        except BadRequest as arr:
            assert arr.status == 500
