import json

from ddipy.constants import BAD_DATASET_OBJECT
from ddipy.ddi_utils import BadRequest

PUBLICATION_DATE = 'publication'
SUBMISSION_DATE = 'submission'
UPDATE_DATE = 'update'

CITATION_COUNT = 'citationCount'
REANALYSIS_COUNT = 'reanalysisCount'
SEARCH_COUNT = 'searchCount'
VIEW_COUNT = 'viewCount'
CONNECTION_COUNT = "connectionsCount"
DOWNLOAD_COUNT = "downloadCount"

CITATION_SCALED_COUNT = "citationsCountScaled"
CONNECTIONS_SCALED_COUNT = "connectionsCountScaled"
REANALYSIS_SCALED_COUNT = "reanalysisCountScaled"
VIEW_SCALED_COUNT = "viewsCountScaled"
DOWNLOAD_SCALED_COUNT = "downloadCountScaled"


class DatasetSummary():

    def __init__(self, accession: str, database: str, title: str, description: str, dates: dict, scores: dict, keywords: list, omics_type: list ) -> None:
        super().__init__()
        self.accession = accession
        self.database = database
        self.title = title
        self.description = description
        self.dates = dates
        self.scores = scores
        self.keywords = keywords
        self.omics_type = omics_type


class Dataset(DatasetSummary):

    def __init__(self, accession: str, database: str, title: str, description: str, dates: dict, scores: dict, keywords: list, omics_type: list, cross_references: dict) -> None:
        super().__init__(accession, database, title, description, dates, scores, keywords, omics_type)
        self.cross_references = cross_references

    @staticmethod
    def get_object_from_json(json_object: json):

        accession = None
        database = None
        title = None
        description = None

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

        scores = {}
        if 'scores' in json_object:
            old_scores = json_object['scores']
        else:
            old_scores = json_object

        if 'citationCount' in old_scores:
            scores[CITATION_COUNT] = old_scores['citationCount']
        if 'reanalysisCount' in old_scores:
            scores[REANALYSIS_COUNT] = old_scores['reanalysisCount']
        if 'searchCount' in old_scores:
            scores[SEARCH_COUNT] = old_scores['searchCount']
        if 'viewCount' in json_object['scores']:
            scores[VIEW_COUNT] = old_scores['viewCount']

        cross_references = {}
        if 'cross_references' in json_object:
            cross_references = json_object['cross_references']

        keywords = []
        if 'keywords' in json_object:
            keywords = json_object['keywords']
        elif 'additional' in json_object and 'submitter_keywords' in json_object['additional']:
            keywords = json_object['additional']['submitter_keywords']

        omics_type = []
        if 'omicsType' in json_object:
           omics_type = json_object['omicsType']
        elif 'additional' in json_object and 'omics_type' in json_object['additional']:
            omics_type = json_object['additional']['omics_type']

        dataset = Dataset(accession, database, title, description, dates, scores, keywords, omics_type, cross_references)
        return dataset
