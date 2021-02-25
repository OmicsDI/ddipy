[ddipy](https://github.com/OmicsDI/ddipy)
======

An [Python package](https://github.com/OmicsDI/ddipy) to obtain data from the Omics Discovery Index ([OmicsDI](http://www.omicsdi.org). It uses the RESTful Web Services at [OmicsDI WS](http://www.omicsdi.org/ws/) for that purpose.

### Installation

we need to install `ddipy`:  

```
pip install ddipy
```

### Examples  

This example shows how retrieve details of one dataset by using the Python package ddipy.

```python
from ddipy.dataset_client import DatasetClient
    
if __name__ == '__main__':
   client = DatasetClient()
   res = client.get_dataset_details("pride", "PXD000210", False)
   
```
        
This example shows a search for all the datasets for human.

```python
from ddipy.dataset_client import DatasetClient
    
if __name__ == '__main__':
   client = DatasetClient()
   res = client.search("cancer human", "publication_date", "ascending")
   
```

This example shows a search for all the datasets for cancer human and loop over the pagination

```python
from ddipy.dataset_client import DatasetClient
    
if __name__ == '__main__':
   client = DatasetClient()
   res = client.search("cancer human", "publication_date", "ascending", 1200, 30, 20)
   
```

This example is a query to retrieve all the datasets that reported the UniProt protein P21399 as identified.

```python
from ddipy.dataset_client import DatasetClient

if __name__ == '__main__':
    client = DatasetClient()
    res = client.search("UNIPROT:P21399")
    
```

This example is a query to find all the datasets where the gene ENSG00000147251 is reported as differentially expressed.

```python
from ddipy.dataset_client import DatasetClient

if __name__ == '__main__':
    client = DatasetClient()
    res = client.search("ENSEMBL:ENSG00000147251")
    
```

This example is a query to retrieve all databases recorded in OmicsDI

```python
from ddipy.dataset_client import DatabaseClient

if __name__ == '__main__':
   client = DatabaseClient()
   res = client.get_database_all()
```


This example is retrieving JSON+LD for dataset page

```python
from ddipy.dataset_client import SeoClient

if __name__ == '__main__':
    client = SeoClient()
    res = client.get_seo_dataset("pride", "PXD000210")
```

This example is  retriveing JSON+LD for home page

```python
from ddipy.dataset_client import SeoClient

if __name__ == '__main__':
    client = SeoClient()
    res = client.get_seo_home()
```

This example is a query for statistics about the number of datasets per Tissue

```python
from ddipy.dataset_client import StatisticsClient

if __name__ == '__main__':
    client = StatisticsClient()
    res = client.get_statistics_tissues(20)
```

This example is a query for statistics about the number of datasets per dieases

```python
from ddipy.dataset_client import StatisticsClient

if __name__ == '__main__':
    client = StatisticsClient()
    res = client.get_statistics_diseases(20)
```

This example for searching dictionary terms

```python
from ddipy.dataset_client import TermClient

if __name__ == '__main__':
    client = TermClient()
    res = client.get_term_by_pattern("hom", 10)
```

This example for retrieving frequently terms from the repo

```python
from ddipy.dataset_client import TermClient

if __name__ == '__main__':
    client = TermClient()
    res = client.get_term_by_pattern("pride", "description", 20)
```


Find out about us in our GitHub profiles:

[Yasset Perez-Riverol](https://github.com/ypriverol)  
[Pan Xu](https://github.com/hll3939092)


### CLI for downloading files

When ddipy is installed correctly it should be available on your path through the command `omicsdi`. This command line interface makes it possible to list all the data links and download the data itself related to an accession number. The tool has one mandatory parameter 'accession number' and several options:

```
omicsdi_fetcher [OPTIONS] ACC_NUMBER
```

| Option           | Type | Description                                                                                                  |
|------------------|------|--------------------------------------------------------------------------------------------------------------|
|   --version      | FLAG | Show the version and exit.                                                                                   |
|   -d, --download | FLAG | Use this flag to download the files in the current directory or a specified output directory                 |
|   -v, --verbose  | FLAG | Use this flag to print identifiers and file extension along with the urls                                    |
|   -i, --input    | LIST | This option allows you to download the a selection of the files based on comma separated list of identifiers |
|   -o, --output   | PATH | Output directory when downloading files (default: CWD)                                                       |
|   -h, --help     | FLAG | Show this message and exit.                                                                                  |

#### Examples

- A microarray dataset with ftp links:
    ```
    omicsdi E-MTAB-5612
    ```
- Downloading the microarray dataset with ftp links:
    ```
    omicsdi E-MTAB-5612 -d
    ```
- A BioModels dataset with https links and exposing identifiers for each file link:
    ```
    omicsdi BIOMD0000000048 -v
    ```

- Downloading a selection of the files belonging to an accession number based on a list of identifiers as input:
    ```
    omicsdi BIOMD0000000048 -d -i "8b52492888, d3144265ac"
    ```
