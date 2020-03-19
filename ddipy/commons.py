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

    def __init__(self, accession: str, database: str, title: str, description: str, dates: dict, scores: dict,
                 keywords: list, omics_type: list, organisms: list) -> None:
        super().__init__()
        self.accession = accession
        self.database = database
        self.title = title
        self.description = description
        self.dates = dates
        self.scores = scores
        self.keywords = keywords
        self.omics_type = omics_type
        self.organisms = organisms


class Dataset(DatasetSummary):

    def __init__(self, accession: str, database: str, title: str, description: str, dates: dict, scores: dict,
                 keywords: list, omics_type: list, organisms: list, cross_references: dict, files: list,
                 additional: dict) -> None:
        super().__init__(accession, database, title, description, dates, scores, keywords, omics_type, organisms)
        self.cross_references = cross_references
        self.files = files
        self.additional = additional

    def get_return_additional_property(self, additional_property: str):
        property_values = []
        if self.additional is not None and additional_property in self.additional:
            property_values = [x for x in self.additional[additional_property] if x not in ['Not Available']]
        return property_values

    def get_posttranslational_modifications(self):
        """
        Return the PTMs for proteomics experiments. If no PTMs are annotated, return an empty List
        :return: List of Post-translational modifications
        """
        return self.get_return_additional_property("modification")

    def get_diseases(self):
        """
        Return the Diseases for dataset. If not disease are annotated, return an empty List
        :return:
        """
        return self.get_return_additional_property("disease")

    def get_tissues(self):
        """
        Return the tissues for a dataset. If not tissue is annotated, return an empty list
        :return:
        """
        return self.get_return_additional_property("tissue")

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
                if json_object['dates']['publication']:
                    dates[PUBLICATION_DATE] = json_object['dates']['publication']
            if 'submission' in json_object['dates']:
                if json_object['dates']['submission']:
                    dates[SUBMISSION_DATE] = json_object['dates']['submission']
        if 'publicationDate' in json_object:
            if json_object['publicationDate']:
                dates[PUBLICATION_DATE] = json_object['publicationDate']

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
        if 'viewCount' in old_scores:
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

        files = []
        if 'file_versions' in json_object:
            files = json_object['file_versions']

        organisms = []
        if 'organisms' in json_object:
            if json_object['organisms']:
                for organism in json_object['organisms']:
                    organisms.append(organism['name'])
        elif 'additional' in json_object and 'species' in json_object['additional']:
            organisms = json_object['additional']['species']

        additional = {}
        if 'additional' in json_object:
            if json_object['additional']:
                additional = json_object['additional']

        dataset = Dataset(accession, database, title, description, dates, scores, keywords, omics_type, organisms,
                          cross_references, files, additional)
        return dataset


class DataSetResult():
    def __init__(self, dataset_array: list, facet_array: list, count: int):
        self.datasets = dataset_array
        self.facets = facet_array
        self.count = count

    @staticmethod
    def get_object_from_json(json_object: json):

        dataset_list = []
        datasets_json = json_object["datasets"]
        if datasets_json:
            for dataset_json in datasets_json:
                dataset = Dataset.get_object_from_json(dataset_json)
                dataset_list.append(dataset)

        facets_list = []
        facets_json = json_object["facets"]
        if facets_json:
            for facet_json in facets_json:
                facets = Facet.get_object_from_json(facet_json)
                facets_list.append(facets)

        count = json_object["count"]
        return DataSetResult(dataset_list, facets_list, count)


class Facet():
    def __init__(self, facet_values: list, label: str, total: int, _id: str):
        self.facet_values = facet_values
        self.label = label
        self.total = total
        self.id = _id

    @staticmethod
    def get_object_from_json(json_object: json):
        facet_values = []

        facet_values_json = json_object["facetValues"]
        if facet_values_json:
            for facet_value_json in facet_values_json:
                facet_value = FacetValue.get_object_from_json(facet_value_json)
                facet_values.append(facet_value)

        label = json_object["label"]
        total = json_object["total"]
        id = json_object["id"]

        return Facet(facet_values, label, total, id)


class FacetValue():
    def __init__(self, label: str, count: str, value: str):
        self.label = label
        self.count = count
        self.value = value

    @staticmethod
    def get_object_from_json(json_object: json):
        label = json_object["label"]
        count = json_object["count"]
        value = json_object["value"]
        facet_value = FacetValue(label, count, value)
        return facet_value


class BatchDataset():
    def __init__(self, failure: list, datasets: list):
        self.failure = failure
        self.datasets = datasets

    @staticmethod
    def get_object_from_json(json_object: json):
        failures = []
        failures_json = json_object["failure"]
        if failures_json:
            for failure_json in failures_json:
                failure = Failure.get_object_from_json(failure_json)
                failures.append(failure)

        datasets = []
        datasets_json = json_object["datasets"]
        if datasets_json:
            for dataset_json in datasets_json:
                dataset = Dataset.get_object_from_json(dataset_json)
                datasets.append(dataset)
        return BatchDataset(failures, datasets)


class Failure():
    def __init__(self, database: str, accession: str, name: str, source_url: str):
        self.database = database
        self.accession = accession
        self.name = name
        self.source_url = source_url

    @staticmethod
    def get_object_from_json(json_object: json):
        database = json_object["database"]
        accession = json_object["accession"]
        name = json_object["name"]
        source_url = json_object["sourceUrl"]
        return Failure(database, accession, name, source_url)


class FileLink():
    def __init__(self, file_link: str):
        self.file_link = file_link


class DatabaseDetail():
    def __init__(self, repository: str, orcidName: str, urlTemplate: str, accessionPrefix: list, title: str,
                 imgAlt: str, sourceUrl: str, description: str, domain: str, image: list, icon: str, source: str,
                 databaseName: str):
        self.repository = repository
        self.orcid_name = orcidName
        self.url_template = urlTemplate
        self.accession_prefix = accessionPrefix
        self.title = title
        self.img_alt = imgAlt
        self.source_url = sourceUrl
        self.description = description
        self.domain = domain
        self.image = image
        self.icon = icon
        self.source = source
        self.database_name = databaseName

    @staticmethod
    def get_object_from_json(json_object: json):
        repository = json_object["repository"]
        orcid_name = json_object["orcidName"]
        url_template = json_object["urlTemplate"]
        accession_prefix = json_object["accessionPrefix"]
        title = json_object["title"]
        img_alt = json_object["imgAlt"]
        source_url = json_object["sourceUrl"]
        description = json_object["description"]
        domain = json_object["domain"]
        image = json_object["image"]
        icon = json_object["icon"]
        source = json_object["source"]
        database_name = json_object["databaseName"]
        database_detail = DatabaseDetail(repository, orcid_name, url_template, accession_prefix, title, img_alt,
                                         source_url, description, domain, image, icon, source, database_name)

        return database_detail


class Term():
    def __init__(self, frequent: str, label: str):
        self.frequent = frequent
        self.label = label

    @staticmethod
    def get_object_from_json(json_object: json):
        frequent = json_object["frequent"]
        label = json_object["label"]
        return Term(frequent, label)


class Item():
    def __init__(self, name: str):
        self.name = name

    @staticmethod
    def get_object_from_json(json_object: json):
        name = json_object["name"]
        return Item(name)


class DictWord():
    def __init__(self, total_count: int, items: list):
        self.total_count = total_count
        self.items = items

    @staticmethod
    def get_object_from_json(json_object: json):
        total_count = json_object["total_count"]
        items_json = json_object["items"]
        items = []
        if items_json:
            for item_json in items_json:
                item = Item.get_object_from_json(item_json)
                items.append(item)
        return DictWord(total_count, items)


# Seo
class StructuredDataAction():
    def __init__(self, query_input: str, type: str, target: str):
        self.query_input = query_input
        self.type = type
        self.target = target

    @staticmethod
    def get_object_from_json(json_object: json):
        query_input = json_object["query-input"]
        type = json_object["@type"]
        target = json_object["target"]
        return StructuredDataAction(query_input, type, target)


class StructuredDataAuthor():
    def __init__(self, name: str, type: str):
        self.name = name
        self.type = type

    @staticmethod
    def get_object_from_json(json_object: json):
        name = json_object["name"]
        type = json_object["@type"]
        return StructuredDataAuthor(name, type)


class StructuredDataCitation():
    def __init__(self, author: StructuredDataAuthor, publisher: StructuredDataAuthor, name: str, type: str, url: str):
        self.author = author
        self.publisher = publisher
        self.name = name
        self.type = type
        self.url = url

    @staticmethod
    def get_object_from_json(json_object: json):
        author_json = json_object["author"]
        author = None
        if author_json:
            author = StructuredDataAuthor.get_object_from_json(author_json)

        publisher_json = json_object["publisher"]
        publisher = None
        if publisher_json:
            publisher = StructuredDataAuthor.get_object_from_json(publisher_json)

        name = json_object["name"]
        type = json_object["@type"]
        url = json_object["url"]
        return StructuredDataCitation(author, publisher, name, type, url)


class StructuredDataImage():
    def __init__(self, author: str, content_url: str, content_location: str, type: str):
        self.author = author
        self.contentUrl = content_url
        self.contentLocation = content_location
        self.type = type

    @staticmethod
    def get_object_from_json(json_object: json):
        author = json_object["author"]
        content_url = json_object["contentUrl"]
        content_location = json_object["contentLocation"]
        _type = json_object["@type"]
        return StructuredDataImage(author, content_url, content_location, _type)


class StructuredData():
    def __init__(self, logo: str, alternate_name: str,
                 potential_action: StructuredDataAction, variable_measured: str, same_as: str, creator: list,
                 citation: StructuredDataCitation, email: str, keywords: str,
                 primary_image_of_page: StructuredDataImage,
                 description: str, image: str, name: str, context: str, type: str, url: str):
        self.logo = logo
        self.alternateName = alternate_name
        self.potentialAction = potential_action
        self.variableMeasured = variable_measured
        self.sameAs = same_as
        self.creator = creator
        self.citation = citation
        self.email = email
        self.keywords = keywords
        self.primaryImageOfPage = primary_image_of_page
        self.description = description
        self.image = image
        self.name = name
        self.context = context
        self.type = type
        self.url = url

    @staticmethod
    def get_object_from_json(json_object: json):
        logo = json_object["logo"]
        alternate_name = json_object["alternateName"]
        potential_action_json = json_object["potentialAction"]
        potential_action = None
        if potential_action_json:
            potential_action = StructuredDataAction.get_object_from_json(potential_action_json)

        variable_measured = json_object["variableMeasured"]
        same_as = json_object["sameAs"]
        creators_json = json_object["creator"]
        creators = []
        if creators_json:
            for creator_json in creators_json:
                creator = StructuredDataAuthor.get_object_from_json(creator_json)
                creators.append(creator)

        citation_json = json_object["citation"]
        citation = None
        if citation_json:
            citation = StructuredDataCitation.get_object_from_json(citation_json)

        email = json_object["email"]
        keywords = json_object["keywords"]
        primary_image_of_page_json = json_object["primaryImageOfPage"]
        primary_image_of_page = None
        if primary_image_of_page_json:
            primary_image_of_page = StructuredDataImage.get_object_from_json(primary_image_of_page_json)

        description = json_object["description"]
        image = json_object["image"]
        name = json_object["name"]
        context = json_object["@context"]
        type = json_object["@type"]
        url = json_object["url"]

        return StructuredData(logo, alternate_name, potential_action, variable_measured, same_as, creators, citation,
                              email, keywords, primary_image_of_page, description, image, name, context, type, url)


class StructuredDataGraph():
    def __init__(self, graph: list):
        self.graph = graph

    @staticmethod
    def get_object_from_json(json_object: json):
        graphs_json = json_object["@graph"]
        graphs = []
        if graphs_json:
            for graph_json in graphs_json:
                if graph_json:
                    graph = StructuredData.get_object_from_json(graph_json)
                    graphs.append(graph)
        return StructuredDataGraph(graphs)


# Statistics
class StatRecord():
    def __init__(self, label: str, name: str, value: str, _id: str):
        self.label = label
        self.name = name
        self.value = value
        self.id = _id

    @staticmethod
    def get_object_from_json(json_object: json):
        label = json_object["label"]
        name = json_object["name"]
        value = json_object["value"]
        _id = json_object["id"]
        return StatRecord(label, name, value, _id)


class DomainStats():
    def __init__(self, domain: StatRecord, subdomains: list):
        self.domain = domain
        self.subdomains = subdomains

    @staticmethod
    def get_object_from_json(json_object: json):
        domain_json = json_object["domain"]
        domain = StatRecord.get_object_from_json(domain_json)
        subdomain = []
        if json_object["subdomains"]:
            subdomain = json_object["subdomains"]
        return DomainStats(domain, subdomain)


class StatOmicsRecord():
    def __init__(self, proteomics: str, transcriptomics: str, genomics: str, metabolomics: str, year: str):
        self.proteomics = proteomics
        self.transcriptomics = transcriptomics
        self.genomics = genomics
        self.metabolomics = metabolomics
        self.year = year

    @staticmethod
    def get_object_from_json(json_object: json):
        proteomics = json_object["proteomics"]
        transcriptomics = json_object["transcriptomics"]
        genomics = json_object["genomics"]
        metabolomics = json_object["metabolomics"]
        year = json_object["year"]
        return StatOmicsRecord(proteomics, transcriptomics, genomics, metabolomics, year)

