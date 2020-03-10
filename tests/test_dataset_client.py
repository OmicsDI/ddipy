from unittest import TestCase

from ddipy.dataset_client import DatasetClient


class TestDatasetClient(TestCase):
    def test_get_dataset_details(self):
        client = DatasetClient()
        dataset = client.get("PXD000210", "pride")
        assert dataset['id'] == "PXD000210"
