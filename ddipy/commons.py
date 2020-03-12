import json

from ddipy.constants import BAD_DATASET_OBJECT
from ddipy.ddi_utils import BadRequest

PUBLICATION_DATE = 'publication'
SUBMISSION_DATE  = 'submission'
UPDATE_DATE      = 'update'

class DatasetSummary():

    def __init__(self, accession: str, database: str, title: str, description: str, dates: dict) -> None:
        super().__init__()
        self.accession = accession
        self.database = database
        self.title = title
        self.description = description
        self.dates = dates


class Dataset(DatasetSummary):

    def __init__(self, accession: str, database: str, title: str , description: str, dates: dict) -> None:
        super().__init__(accession, database, title, description, dates)

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
        dates = {}
        if 'dates' in json_object:
            if 'publication' in json_object['dates']:
                dates[PUBLICATION_DATE] = json_object['dates']['publication']
            if 'submission' in json_object['dates']:
                dates[SUBMISSION_DATE] = json_object['dates']['submission']
        if 'publicationDate' in json_object:
            dates[PUBLICATION_DATE] = json_object['dates']['publication']

        dataset = Dataset(accession, database, title, description, dates)
        return dataset
