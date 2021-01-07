from unittest import TestCase

from ddipy.constants import DATA_NOT_FOUND, MISSING_PARAMETER
from ddipy.dataset_client import DatasetClient
from ddipy.ddi_utils import BadRequest


class TestDatasetClient(TestCase):

    def test_get_dataset_details(self):
        """
        check the details for one dataset.
        :return:
        """
        client = DatasetClient()
        dataset = client.get_dataset_details("pride", "PXD000210")

        assert dataset.accession == "PXD000210"
        assert len(dataset.description) == 2227

        try:
            dataset = client.get_dataset_details("PXD@£", "pride")
        except BadRequest as err:
            assert err.status == 404

        try:
            dataset = client.get_dataset_details(None, "pride")
        except BadRequest as err:
            assert err.status == MISSING_PARAMETER

    def test_search(self):

        client = DatasetClient()
        res = client.search("cancer human", "publication_date", "ascending")

        assert len(res.datasets) > 0

        assert res.count > 0

        res_other_pages = client.search("cancer human", "publication_date", "ascending", 1200, 30, 20)

        assert res_other_pages.count > 0
        assert len(res_other_pages.datasets) == 30

        try:
            dataset = client.search("j9j9j9j9@£", "publication_date", "ascending")
        except BadRequest as err:
            assert err.status == DATA_NOT_FOUND

        try:
            dataset = client.search(None, "publication_date", "ascending")
        except BadRequest as err:
            assert err.status == MISSING_PARAMETER

    def test_batch(self):
        client = DatasetClient()

        res = client.batch("PXD000210", 'pride')

        assert len(res.failure) == 0
        assert res.datasets[0].accession == "PXD000210"

        try:
            client.batch("gulugulu11", "momomomomo")
        except BadRequest as err:
            assert err.status == DATA_NOT_FOUND

        try:
            client.batch(None, "momomomomo")
        except BadRequest as err:
            assert err.status == MISSING_PARAMETER

    def test_latest(self):
        client = DatasetClient()

        res = client.latest(20)

        assert res.count > 0
        assert len(res.datasets) > 0

        try:
            client.latest(0)
        except BadRequest as err:
            assert err.status == DATA_NOT_FOUND

    def test_most_accessed(self):
        client = DatasetClient()

        res = client.most_accessed(20)

        assert res.count > 0
        assert len(res.datasets) > 0

        try:
            res = client.most_accessed(0)
        except BadRequest as err:
            assert err.status == 500

    def test_get_file_links(self):
        client = DatasetClient()

        res = client.get_file_links("PXD000210", "pride")

        assert len(res) > 0

        try:
            res = client.get_file_links("aaa", "pride")
        except BadRequest as err:
            assert err.status == DATA_NOT_FOUND

        try:
            res = client.get_file_links(None, "pride")
        except BadRequest as err:
            assert err.status == MISSING_PARAMETER

    def test_get_similar(self):
        client = DatasetClient()

        res = client.get_similar("PXD000210", "pride")
        assert res.count > 0
        assert len(res.datasets)

        try:
            res = client.get_similar("aaaa", "pride")
        except BadRequest as err:
            assert err.status == 500

        try:
            res = client.get_similar(None, "pride")
        except BadRequest as err:
            assert err.status == MISSING_PARAMETER

    def test_get_similar_by_pubmed(self):
        client = DatasetClient()

        res = client.get_similar_by_pubmed("16585740")
        assert len(res)

        try:
            res = client.get_similar_by_pubmed("qq9q9")
        except BadRequest as err:
            assert err.status == DATA_NOT_FOUND

        try:
            res = client.get_similar_by_pubmed(None)
        except BadRequest as err:
            assert err.status == MISSING_PARAMETER
