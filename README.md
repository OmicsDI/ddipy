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
   print(res.text)
```
        
This example shows a search for all the datasets for human.

```python
from ddipy.dataset_client import DatasetClient
    
if __name__ == '__main__':
   client = DatasetClient()
   res = client.search("human")
   print(res.text)
```

This example is a query to retrieve all the datasets that reported the UniProt protein P21399 as identified.

```python
from ddipy.dataset_client import DatasetClient

if __name__ == '__main__':
    client = DatasetClient()
    res = client.search("UNIPROT:P21399")
    print(res.text)
```

This example is a query to find all the datasets where the gene ENSG00000147251 is reported as differentially expressed.

```python
from ddipy.dataset_client import DatasetClient

if __name__ == '__main__':
    client = DatasetClient()
    res = client.search("ENSEMBL:ENSG00000147251")
    print(res.text)
```
        
The normal result of any client should be an original response from [requests](https://pypi.org/project/requests/).
when missing some of required parameters, the result shoud be like:

```python
  {
     error: parameter is missing
  }

```

Find out about us in our GitHub profiles:

[Yasset Perez-Riverol](https://github.com/ypriverol)  
[Pan Xu](https://github.com/hll3939092)

