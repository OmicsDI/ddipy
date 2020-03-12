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

    def test_search(self):

        client = DatasetClient()

        res = client.search("cancer human", "publication_date", "ascending")
        try:


    def test_batch(self):
        client = DatasetClient()

        res = client.batch("PXD000210", 'pride')
        assert res.status_code == 200
        assert res.json()["datasets"][0]["id"] == "PXD000210"

    def test_latest(self):
        client = DatasetClient()

        res = client.latest(20)
        assert res.status_code == 200
        assert res.json()["count"] > 0

    def test_most_accessed(self):
        client = DatasetClient()

        res = client.most_accessed(20)
        assert res.status_code == 200
        assert res.json()["count"] == 20

    def test_get_file_links(self):
        client = DatasetClient()

        res = client.get_file_links("PXD000210", "pride")
        assert res.status_code == 200
        assert len(res.json()) > 0

    def test_get_similar(self):
        client = DatasetClient()

        res = client.get_similar("PXD000210", "pride")
        assert res.status_code == 200

    def test_get_similar_by_pubmed(self):
        client = DatasetClient()

        res = client.get_similar_by_pubmed("16585740")
        assert res.status_code == 200
