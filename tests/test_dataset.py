from unittest import TestCase

from ddipy.commons import Dataset
from ddipy.dataset_client import DatasetClient


class TestDataset(TestCase):

    def test_get_object_from_json(self):
        client = DatasetClient()
        dataset = client.get_dataset_details("pride", "PXD000210")

        # dataset = Dataset.get_object_from_json(object_json)
        assert dataset.accession == "PXD000210"
        assert dataset.title == "Proteome analysis by charge state-selective separation of peptides: a multidimensional approach"

        assert len(dataset.dates) > 0
        assert len(dataset.scores) > 0
        assert len(dataset.cross_references) > 0
        assert len(dataset.keywords) > 0
        assert len(dataset.organisms) > 0
        assert len(dataset.get_posttranslational_modifications()) == 7

        assert len(dataset.get_diseases()) == 0

        assert len(dataset.get_tissues()) == 0

        dataset_transcriptomics = client.get_dataset_details("arrayexpress-repository", "E-TABM-555")
        # dataset_transcriptomics = Dataset.get_object_from_json(object_json)

        assert dataset_transcriptomics.accession == "E-TABM-555"
        assert dataset_transcriptomics.title == "Transcription profiling of rat to investigate technical and biological variability on the Agilent platform"

        assert len(dataset_transcriptomics.dates) > 0
        assert len(dataset_transcriptomics.scores) > 0
        assert len(dataset_transcriptomics.cross_references) > 0
        assert len(dataset_transcriptomics.keywords) > 0
        assert len(dataset_transcriptomics.organisms) > 0
        assert len(dataset_transcriptomics.get_posttranslational_modifications()) == 0

        assert len(dataset_transcriptomics.get_diseases()) == 0

        assert len(dataset_transcriptomics.get_tissues()) == 4


