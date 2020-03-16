
HEADERS = {"User-Agent": "ddipy/0.0.3"}
WS_URL = "https://www.omicsdi.org/ws/"
DATASET_URL = WS_URL + "/dataset"
MERGE_URL = DATASET_URL + "/merge"
DATASET_PAGE_URL = DATASET_URL + "/getDatasetPage"
UNMERGE_URL = DATASET_URL + "/unmerge"
MERGE_CANDIDATE_URL = DATASET_URL + "/getMergeCandidates"
MULTIOMICS_MERGE_URL = DATASET_URL + "/multiomicsMerge"
ALL_MERGE_URL = DATASET_URL + "/getAllmerged"
DATASET_BY_URL_URL = DATASET_URL + "/getDatasetByUrl"
ALL_URL = DATASET_URL + "/getAll"
MERGE_CANDIDATE_COUNT_URL = DATASET_URL + "/getMergeCandidateCount"
SKIP_MERGE_URL = DATASET_URL + "/skipMerge"
DB_DATABASE_COUNT_URL = DATASET_URL + "/getDbDatasetCount"
SEARCH_URL = DATASET_URL + "/search"
LATEST_URL = DATASET_URL + "/latest"
GET_URL = DATASET_URL + "/get"
SIMILAR_BY_PUBMED_URL = DATASET_URL + "/getSimilarByPubmed"
BATCH_URL = DATASET_URL + "/batch"
MOST_ACCESSED_DATASETS = DATASET_URL + "/mostAccessed"
FILE_LINKS_URL = DATASET_URL + "/getFileLinks"
SIMILAR_URL = DATASET_URL + "/getSimilar"

DBLUCENCE_URL = WS_URL + "/dblucene"
SAVE_MAPPING_URL = DBLUCENCE_URL + "/saveMapping"
LUCENE_NAME_URL = DBLUCENCE_URL + "/getLuceneName"
MAPPINGS_URL = DBLUCENCE_URL + "/getAllMappings"
DB_NAME_URL = DBLUCENCE_URL + "/getDbName"

ENRICHMENT_URL = WS_URL + "/enrichment"
SYNONYMS_URL = ENRICHMENT_URL + "/getSynonymsForDataset"
REANALYSIS_URL = ENRICHMENT_URL + "/getSynonymsForDataset"
ENRICHMENT_INFO_URL = ENRICHMENT_URL + "/getEnrichmentInfo"
SIMILAR_DATASETS_BIOLOGY_URL = ENRICHMENT_URL + "/getSimilarDatasetsByBiologicalData"
SIMILAR_INFO_URL = ENRICHMENT_URL + "/getSimilarityInfo"

FEEDBACK_URL = WS_URL + "/feedback"
FEEDBACK_INFO_URL = FEEDBACK_URL + "/saveFeedback"
ALL_FEEDBACK_URL = FEEDBACK_URL + "/getAllFeedbacks"
FEEDBACK_BY_STATUS_URL = FEEDBACK_URL + "/getFeedbackByStatus"
LIST_URL = FEEDBACK_URL + "/publication/list"
SEO_URL = WS_URL + "/seo"
SEO_URL_HOME = SEO_URL + "/home"
SEO_SEARCH_URL = SEO_URL + "/search"
SEO_API_URL = SEO_URL + "/api"
SEO_SCHEMA_URL = SEO_URL + "/schema"
SEO_DATABASE_URL = SEO_URL + "/database"
SEO_DATASET_URL = SEO_URL + "/dataset"
SEO_ABOUT_URL = SEO_URL + "/about"
STATISTICS_URL = WS_URL + "/statistics/"

TERM_URL = WS_URL + "/term"
TERM_BY_PATTERN_URL = TERM_URL + "/getTermByPattern"
FREQUENTLY_TERM_URL = TERM_URL + "/frequentlyTerm/list"
DATABASE_URL = WS_URL + "/database"
DATABASE_ALL_URL = DATABASE_URL + "/all"
DATABASE_PICTURE_URL = DATABASE_URL + "/db/picturebyte"


DATA_NOT_FOUND = 801
BAD_DATASET_OBJECT = 802
MISSING_PARAMETER = 803



