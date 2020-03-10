import requests

from ddipy import constants
from ddipy.constants import DATA_NOT_FOUND
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
        tokened_header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, "
                                        "like Gecko) "
                                        "Chrome/54.0.2840.99 Safari/537.36",
                          "x-auth-token": access_token}
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
        tokened_header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, "
                                        "like Gecko) "
                                        "Chrome/54.0.2840.99 Safari/537.36",
                          "x-auth-token": access_token}
        res = requests.post(constants.UNMERGE_URL, params=merge_candidates, headers=tokened_header)
        return res

    @staticmethod
    def get_merge_candidates(start, size, access_token):
        tokened_header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, "
                                        "like Gecko) "
                                        "Chrome/54.0.2840.99 Safari/537.36",
                          "x-auth-token": access_token}
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
        tokened_header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, "
                                        "like Gecko) "
                                        "Chrome/54.0.2840.99 Safari/537.36",
                          "x-auth-token": access_token}
        res = requests.post(constants.MULTIOMICS_MERGE_URL, params=request_params, headers=tokened_header)
        return res

    @staticmethod
    def get_allmerged(access_token):
        tokened_header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, "
                                        "like Gecko) "
                                        "Chrome/54.0.2840.99 Safari/537.36",
                          "x-auth-token": access_token}
        res = requests.get(constants.ALL_MERGE_URL, headers=tokened_header)
        return res

    @staticmethod
    def get_dataset_by_url(url):

        if not url:
            return VerifyUtils.empty_param_error("url")

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
        tokened_header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, "
                                        "like Gecko) "
                                        "Chrome/54.0.2840.99 Safari/537.36",
                          "x-auth-token": access_token}
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
        tokened_header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, "
                                        "like Gecko) "
                                        "Chrome/54.0.2840.99 Safari/537.36",
                          "x-auth-token": access_token}
        res = requests.post(constants.SKIP_MERGE_URL, params=request_params, headers=tokened_header)
        return res

    @staticmethod
    def get_dataset_details(domain, accession, debug=False):
        if not domain:
            return VerifyUtils.empty_param_error("domain")

        if not accession:
            return VerifyUtils.empty_param_error("accession")

        res = requests.get(constants.DATASET_URL + "/" + domain + "/" + accession, params={
            "debug": debug
        }, headers=constants.HEADERS)

        if res.status_code != 200:
            raise BadRequest("The request dataset accession {} and database {} thrown connection error".format(accession, domain), res.status_code, payload= None)
        elif res.status_code == 200 and res.json()['accession'] == "None":
            raise BadRequest( "The request dataset accession {} and database {} was not found in the server".format(accession, domain), DATA_NOT_FOUND, payload=None)
        return res.json()

    @staticmethod
    def get_dataset_files(domain, accession, position):
        if not domain:
            return VerifyUtils.empty_param_error("domain")

        if not accession:
            return VerifyUtils.empty_param_error("accession")

        if not position:
            return VerifyUtils.empty_param_error("position")

        res = requests.get(constants.DATASET_URL + "/" + domain + "/" + accession + "/files",
                           params={
                               "position": position
                           },
                           headers=constants.HEADERS)
        return res

    @staticmethod
    def get_db_dataset_count():
        res = requests.get(constants.DB_DATABASE_COUNT_URL, headers=constants.HEADERS)
        return res

    @staticmethod
    def search(query="", sortfield="", order="", start=0, size=20, face_count=20):
        params = {
            "start": start,
            "size": size,
            "faceCount": face_count
        }
        print(query)
        if not query:
            return VerifyUtils.empty_param_error("query")
        else:
            params.update(query=query)
        if not query:
            return VerifyUtils.empty_param_error("sortfield")
        else:
            params.update(sortfield=sortfield)
        if not query:
            return VerifyUtils.empty_param_error("order")
        else:
            params.update(order=order)

        res = requests.get(constants.SEARCH_URL, params=params, headers=constants.HEADERS)
        return res

    @staticmethod
    def latest(size=20):
        res = requests.get(constants.LATEST_URL, params={
            "size": size
        }, headers=constants.HEADERS)
        return res

    @staticmethod
    def get(acc, database):
        if not acc:
            return VerifyUtils.empty_param_error("acc")

        if not database:
            return VerifyUtils.empty_param_error("database")

        res = requests.get(constants.GET_URL, params={
            "acc": acc,
            "database": database
        }, headers=constants.HEADERS)
        return res.json()

    @staticmethod
    def get_similar_by_pubmed(pubmed):
        if not pubmed:
            return VerifyUtils.empty_param_error("pubmed")

        res = requests.get(constants.DATASET_URL + "/getSimilarByPubmed", params={
            "pubmed": pubmed
        }, headers=constants.HEADERS)
        return res

    @staticmethod
    def batch(acc, database):
        if not acc:
            return VerifyUtils.empty_param_error("acc")

        if not database:
            return VerifyUtils.empty_param_error("database")

        res = requests.get(constants.BATCH_URL, params={
            "acc": acc,
            "database": database
        }, headers=constants.HEADERS)
        return res

    @staticmethod
    def most_accessed(size=20):
        res = requests.get(constants.MOST_ACCESSED_DATASETS, params={
            "size": size
        }, headers=constants.HEADERS)
        return res

    @staticmethod
    def get_file_links(acc, database):
        if not acc:
            return VerifyUtils.empty_param_error("acc")

        if not database:
            return VerifyUtils.empty_param_error("database")

        res = requests.get(constants.FILE_LINKS_URL, params={
            "acc": acc,
            "database": database
        }, headers=constants.HEADERS)
        return res

    @staticmethod
    def get_similar(acc, database):
        if not acc:
            return VerifyUtils.empty_param_error("acc")

        if not database:
            return VerifyUtils.empty_param_error("database")

        res = requests.get(constants.SIMILAR_URL, params={
            "acc": acc,
            "database": database
        }, headers=constants.HEADERS)
        return res


if __name__ == '__main__':
    client = DatasetClient()
    res = client.search("human")
    print(res)
