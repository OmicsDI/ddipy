import requests


class EnrichmentClient:
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                             "Chrome/54.0.2840.99 Safari/537.36"}
    getSynonymsForDatasetUrl = "https://www.omicsdi.org:443/ws/enrichment/getSynonymsForDataset"
    getReanalysisUrl = "https://www.omicsdi.org:443/ws/enrichment/getSynonymsForDataset"
    getEnrichmentInfoUrl = "https://www.omicsdi.org:443/ws/enrichment/getEnrichmentInfo"
    getSimilarDatasetsByBiologicalDataUrl = "https://www.omicsdi.org:443/ws/enrichment" \
                                            "/getSimilarDatasetsByBiologicalData "
    getSimilarityInfoUrl = "https://www.omicsdi.org:443/ws/enrichment/getSimilarityInfo"

    def __init__(self):
        pass

    def get_synonyms_for_dataset(self, accession, database):
        res = requests.get(self.getSynonymsForDatasetUrl, params={
            "accession": accession,
            "database": database
        }, headers=self.headers)
        return res

    def get_reanalysis(self):
        res = requests.get(self.getReanalysisUrl, headers=self.headers)
        return res

    def get_enrichment_info(self, accession, database):
        res = requests.get(self.getEnrichmentInfoUrl, params={
            "accession": accession,
            "database": database
        }, headers=self.headers)
        return res

    def get_similar_datasets_by_biological_data(self, accession, database):
        res = requests.get(self.getSimilarDatasetsByBiologicalDataUrl, params={
            "accession": accession,
            "database": database
        }, headers=self.headers)
        return res

    def get_similarity_info(self, accession, database, threshold):
        res = requests.get(self.getSimilarityInfoUrl, params={
            "accession": accession,
            "database": database,
            "threshold": threshold
        }, headers=self.headers)
        return res
