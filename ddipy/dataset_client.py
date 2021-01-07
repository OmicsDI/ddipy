import requests

from ddipy import constants
from ddipy.commons import Dataset, DataSetResult, BatchDataset
from ddipy.constants import DATA_NOT_FOUND, HEADERS, MISSING_PARAMETER
from ddipy.ddi_utils import VerifyUtils, BadRequest


class DatasetClient:

    def __init__(self):
        pass

    @staticmethod
    def merge(similar_arr, accession, database, source_url, name, access_token):
        similar_list = []
        for similar in similar_arr:
            temp_dict = {}
            temp_dict.update(accession=similar.accession)
            temp_dict.update(database=similar.database)
            temp_dict.update(sourceUrl=similar.sourceUrl)
            temp_dict.update(name=similar.name)
            similar_list.append(temp_dict)

        request_params = {
            "similars": similar_list,
            "accession": accession,
            "database": database,
            "sourceUrl": source_url,
            "name": name
        }
        tokened_header = HEADERS.copy()
        tokened_header["x-auth-token"] =  access_token
        res = requests.post(constants.MERGE_URL, params=request_params, headers=tokened_header)
        return res

    @staticmethod
    def get_dataset_page(start=0, size=20):
        res = requests.get(constants.DATASET_PAGE_URL, params={
            "start": start,
            "size": size
        }, headers=constants.HEADERS)
        return res

    # todo
    @staticmethod
    def unmerge(merge_candidates, access_token):

        tokened_header = HEADERS.copy()
        tokened_header["x-auth-token"] = access_token

        res = requests.post(constants.UNMERGE_URL, params=merge_candidates, headers=tokened_header)
        return res

    @staticmethod
    def get_merge_candidates(start, size, access_token):
        tokened_header = HEADERS.copy()
        tokened_header["x-auth-token"] = access_token
        res = requests.get(constants.MERGE_CANDIDATE_URL, params={
            "start": start,
            "size": size
        }, headers=tokened_header)
        return res

    @staticmethod
    def multiomics_merge(similar_arr, accession, database, source_url, name, access_token):
        similar_list = []
        for similar in similar_arr:
            temp_dict = {}
            temp_dict.update(accession=similar.accession)
            temp_dict.update(database=similar.database)
            temp_dict.update(sourceUrl=similar.sourceUrl)
            temp_dict.update(name=similar.name)
            similar_list.append(temp_dict)

        request_params = {
            "similars": similar_list,
            "accession": accession,
            "database": database,
            "sourceUrl": source_url,
            "name": name
        }
        tokened_header = HEADERS.copy()
        tokened_header["x-auth-token"] = access_token
        res = requests.post(constants.MULTIOMICS_MERGE_URL, params=request_params, headers=tokened_header)
        return res

    @staticmethod
    def get_allmerged(access_token):
        tokened_header = HEADERS.copy()
        tokened_header["x-auth-token"] = access_token
        res = requests.get(constants.ALL_MERGE_URL, headers=tokened_header)
        return res

    @staticmethod
    def get_dataset_by_url(url):

        if not url:
            raise BadRequest("missing parameter url", MISSING_PARAMETER, payload=None)

        res = requests.post(constants.DATASET_URL + "/getDatasetByUrl", params={
            "url": url
        }, headers=constants.HEADERS)
        return res

    @staticmethod
    def get_all():
        res = requests.get(constants.ALL_URL, headers=constants.HEADERS)
        return res

    @staticmethod
    def get_merge_candidate_count(access_token):
        tokened_header = HEADERS.copy()
        tokened_header["x-auth-token"] = access_token

        res = requests.get(constants.MERGE_CANDIDATE_COUNT_URL, headers=tokened_header)
        return res

    @staticmethod
    def skip_merge(similar_arr, accession, database, source_url, name, access_token):
        similar_list = []
        for similar in similar_arr:
            temp_dict = {}
            temp_dict.update(accession=similar.accession)
            temp_dict.update(database=similar.database)
            temp_dict.update(sourceUrl=similar.sourceUrl)
            temp_dict.update(name=similar.name)
            similar_list.append(temp_dict)

        request_params = {
            "similars": similar_list,
            "accession": accession,
            "database": database,
            "sourceUrl": source_url,
            "name": name
        }
        tokened_header = HEADERS.copy()
        tokened_header["x-auth-token"] = access_token

        res = requests.post(constants.SKIP_MERGE_URL, params=request_params, headers=tokened_header)
        return res

    @staticmethod
    def get_dataset_details(database, accession):
        if not database:
            raise BadRequest("missing parameter database", MISSING_PARAMETER, payload=None)

        if not accession:
            raise BadRequest("missing parameter accession", MISSING_PARAMETER, payload=None)

        res = requests.get(constants.DATASET_URL + "/" + database + "/" + accession, headers=constants.HEADERS)

        if res.status_code != 200:
            raise BadRequest("The request dataset accession {} and database {} thrown connection error".format(accession, database), res.status_code, payload=None)

        dataset = Dataset.get_object_from_json(res.json())

        return dataset

    @staticmethod
    def get_dataset_files(database, accession, position):
        if not database:
            raise BadRequest("missing parameter database", MISSING_PARAMETER, payload=None)

        if not accession:
            raise BadRequest("missing parameter accession", MISSING_PARAMETER, payload=None)

        if not position:
            raise BadRequest("missing parameter position", MISSING_PARAMETER, payload=None)

        res = requests.get(constants.DATASET_URL + "/" + database + "/" + accession + "/files",
                           params={
                               "position": position
                           },
                           headers=constants.HEADERS)
        file_links = []
        if res.json():
            for file_link in res.json():
                file_links.append(file_link)
        return file_links

    @staticmethod
    def get_db_dataset_count():
        res = requests.get(constants.DB_DATABASE_COUNT_URL, headers=constants.HEADERS)
        return res

    @staticmethod
    def search(query, sortfield=None, order=None, start=0, size=20, face_count=20):
        params = {
            "start": start,
            "size": size,
            "faceCount": face_count
        }
        if not query:
            raise BadRequest("missing parameter query", MISSING_PARAMETER, payload=None)
        else:
            params.update(query=query)
        if sortfield:
            params.update(sortfield=sortfield)
        if order:
            params.update(order=order)

        res = requests.get(constants.SEARCH_URL, params=params, headers=constants.HEADERS)
        if res.status_code != 200:
            raise BadRequest("The request query {} and sortfield {} and order {} thrown connection error".format(query, sortfield, order), res.status_code, payload=None)

        return DataSetResult.get_object_from_json(res.json())

    @staticmethod
    def latest(size=20):
        res = requests.get(constants.LATEST_URL, params={
            "size": size
        }, headers=constants.HEADERS)

        if res.status_code != 200:
            raise BadRequest("The request thrown connection error", res.status_code, payload=None)
        return DataSetResult.get_object_from_json(res.json())

    @staticmethod
    def get(acc, database):
        if not acc:
            raise BadRequest("missing parameter acc", MISSING_PARAMETER, payload=None)

        if not database:
            raise BadRequest("missing parameter database", MISSING_PARAMETER, payload=None)

        res = requests.get(constants.GET_URL, params={
            "accession": acc,
            "database": database
        }, headers=constants.HEADERS)
        return res.json()

    @staticmethod
    def get_similar_by_pubmed(pubmed):
        if not pubmed:
            raise BadRequest("missing parameter pubmed", MISSING_PARAMETER, payload=None)

        res = requests.get(constants.DATASET_URL + "/getSimilarByPubmed", params={
            "pubmed": pubmed
        }, headers=constants.HEADERS)

        if res.status_code != 200:
            raise BadRequest("The request pubmed {} thrown connection error".format(pubmed), res.status_code, payload=None)
        datasets = []
        for i in res.json():
            dataset = Dataset.get_object_from_json(i)
            datasets.append(dataset)
        return datasets

    @staticmethod
    def batch(acc, database):
        if not acc:
            raise BadRequest("missing parameter acc", MISSING_PARAMETER, payload=None)

        if not database:
            raise BadRequest("missing parameter database", MISSING_PARAMETER, payload=None)

        res = requests.get(constants.BATCH_URL, params={
            "accession": acc,
            "database": database
        }, headers=constants.HEADERS)

        if res.status_code != 200:
            raise BadRequest("The request accession {} and database {} thrown connection error".format(acc, database), res.status_code, payload=None)
        return BatchDataset.get_object_from_json(res.json())

    @staticmethod
    def most_accessed(size=20):
        res = requests.get(constants.MOST_ACCESSED_DATASETS, params={
            "size": size
        }, headers=constants.HEADERS)

        if res.status_code != 200:
            raise BadRequest("The request thrown connection error", res.status_code, payload=None)

        return DataSetResult.get_object_from_json(res.json())

    @staticmethod
    def get_file_links(accession, database):
        if not accession:
            raise BadRequest("missing parameter accession", MISSING_PARAMETER, payload=None)

        if not database:
            raise BadRequest("missing parameter database", MISSING_PARAMETER, payload=None)

        res = requests.get(constants.FILE_LINKS_URL, params={
            "accession": accession,
            "database": database
        }, headers=constants.HEADERS)

        if res.status_code != 200:
            raise BadRequest("The request accession {} and database {} thrown connection error".format(accession, database), res.status_code, payload=None)

        file_links = []
        if res.json():
            for file_link in res.json():
                file_links.append(file_link)
        return file_links

    @staticmethod
    def get_similar(accession, database):
        if not accession:
            raise BadRequest("missing parameter accession", MISSING_PARAMETER, payload=None)

        if not database:
            raise BadRequest("missing parameter database", MISSING_PARAMETER, payload=None)

        res = requests.get(constants.SIMILAR_URL, params={
            "accession": accession,
            "database": database
        }, headers=constants.HEADERS)

        if res.status_code != 200:
            raise BadRequest("The request accession {} and database {} thrown connection error".format(accession, database), res.status_code, payload=None)
        return DataSetResult.get_object_from_json(res.json())

