from unittest import TestCase

from ddipy.dataset_client import DatasetClient
from ddipy.ddi_utils import BadRequest


class TestDatasetClient(TestCase):

    def test_get_dataset_details(self):
        """
        check the details for one dataset.
        :return:
        """
        client = DatasetClient()
        dataset = client.get_dataset_details("pride", "PXD000210", False)

        assert dataset['accession'] == "PXD000210"
        assert len(dataset['description']) == 2227

        try:
            dataset = client.get_dataset_details("PXD@£", "pride")
        except BadRequest as err:
            assert err.status == 500





