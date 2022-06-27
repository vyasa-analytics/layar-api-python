# layar_api.OntologyApi

All URIs are relative to *BASE_PATH*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_table_ontology**](OntologyApi.md#create_table_ontology) | **POST** /layar/sourceDocument/{id}/createOntology | Create an ontology from a table

# **create_table_ontology**
> SourceDocument create_table_ontology(id, name=name, id2=id2, label=label, synonyms=synonyms, properties=properties, delimeter=delimeter)

Create an ontology from a table

### Example
```python
from __future__ import print_function
import time
import layar_api
from layar_api.rest import ApiException
from pprint import pprint

# configure oauth access token for authorization
configuration = layar_api.Configuration()
configuration.host = 'HOST_NAME'
configuration.access_token = configuration.fetch_access_token('CLIENT_ID', 'CLIENT_SECRET')

# create an instance of the api class
api_instance = layar_api.OntologyApi(layar_api.ApiClient(configuration))
id = 'id_example' # str | The Layar ID for the table to be converted
name = 'name_example' # str |  (optional)
id2 = 'id_example' # str |  (optional)
label = 'label_example' # str |  (optional)
synonyms = ['synonyms_example'] # list[str] |  (optional)
properties = ['properties_example'] # list[str] |  (optional)
delimeter = 'delimeter_example' # str |  (optional)

try:
    # Create an ontology from a table
    api_response = api_instance.create_table_ontology(id, name=name, id2=id2, label=label, synonyms=synonyms, properties=properties, delimeter=delimeter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OntologyApi->create_table_ontology: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The Layar ID for the table to be converted | 
 **name** | **str**|  | [optional] 
 **id2** | **str**|  | [optional] 
 **label** | **str**|  | [optional] 
 **synonyms** | [**list[str]**](str.md)|  | [optional] 
 **properties** | [**list[str]**](str.md)|  | [optional] 
 **delimeter** | **str**|  | [optional] 

### Return type

[**SourceDocument**](SourceDocument.md)

### Authorization

[oAuth2ClientCredentials](../README.md#oAuth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

