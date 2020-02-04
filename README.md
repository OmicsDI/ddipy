[ddiPy](https://github.com/OmicsDI/Pyddi)
======

An [Python package](https://github.com/OmicsDI/Pyddi) to obtain data from the Omics Discovery Index ([OmicsDI](http://www.omicsdi.org). It uses its RESTful Web Services at [OmicsDI WS](http://www.omicsdi.org/ws/) for that purpose.  

Currently, the following domain entities are supported:  


### Installation  

we need to install `ddipy`:  

    pip install ddipy

### Examples  

This exmaple shows how retrieve details of one dataset by using the Python-package ddipy. 

    from ddipy.dataset_client import DatasetClient

    if __name__ == '__main__':
        client = DatasetClient()
        res = client.get_dataset_from_domain_and_accession("pride", "PXD000210", False)
        print(res.text)

Find out about us in our GitHub profiles:  

[Yasset Perez-Riverol](https://github.com/ypriverol)  
[Pan Xu](https://github.com/hll3939092)

