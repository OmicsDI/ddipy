import json

from ddipy.constants import BAD_DATASET_OBJECT
from ddipy.ddi_utils import BadRequest


class DatasetSummary():

    def __init__(self, accession: str, database: str, title: str, description: str) -> None:
        super().__init__()
        self.accession = accession
        self.database = database
        self.title = title
        self.description = description


class Dataset(DatasetSummary):

    def __init__(self, accession: str, database: str, title: str , description: str) -> None:
        super().__init__(accession, database, title ,description)

    @staticmethod
    def get_object_from_json(json_object: json):
        accession = None
        database = None
        if 'accession' in json_object:
            accession = json_object['accession']
        elif 'id' in json_object:
            accession = json_object['id']

        if 'database' in json_object:
            database = json_object['database']
        elif 'source' in json_object:
            database = json_object['source']

        if 'title' in json_object:
            title = json_object['title']
        elif 'name' in json_object:
            title = json_object['name']

        if 'description' in json_object:
            description = json_object['description']

        if accession is None or database is None:
            raise BadRequest("The present dataset do not contains accession or database {}".format(json_object),
                             BAD_DATASET_OBJECT,
                             None)
        dataset = Dataset(accession, database, title, description)
        return dataset
