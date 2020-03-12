from unittest import TestCase

from ddipy.database_client import DatabaseClient


class TestDatabaseClient(TestCase):

    def test_get_database_all(self):
        client = DatabaseClient()
        res = client.get_database_all()
        assert len(res) > 0
