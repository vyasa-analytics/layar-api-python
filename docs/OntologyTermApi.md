# layar_api.OntologyTermApi

All URIs are relative to *BASE_PATH*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_term**](OntologyTermApi.md#create_term) | **POST** /layar/ontologyTerm | Create a new ontology term
[**delete_term**](OntologyTermApi.md#delete_term) | **DELETE** /layar/ontologyTerm/{id} | Delete an ontology term
[**get_term**](OntologyTermApi.md#get_term) | **GET** /layar/ontologyTerm/{id} | Get ontology term details
[**layar_ontology_term_get**](OntologyTermApi.md#layar_ontology_term_get) | **GET** /layar/ontologyTerm | Search for ontology terms
[**search_term**](OntologyTermApi.md#search_term) | **POST** /layar/ontologyTerm/search | 
[**update_term**](OntologyTermApi.md#update_term) | **PUT** /layar/ontologyTerm/{id} | Update ontology term details

# **create_term**
> OntologyTerm create_term(body)

Create a new ontology term

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
api_instance = layar_api.OntologyTermApi(layar_api.ApiClient(configuration))
body = layar_api.OntologyTerm() # OntologyTerm | 

try:
    # Create a new ontology term
    api_response = api_instance.create_term(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OntologyTermApi->create_term: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**OntologyTerm**](OntologyTerm.md)|  | 

### Return type

[**OntologyTerm**](OntologyTerm.md)

### Authorization

[oAuth2ClientCredentials](../README.md#oAuth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_term**
> delete_term(id)

Delete an ontology term

Remove a specified Ontology Term object from your Layar instance.

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
api_instance = layar_api.OntologyTermApi(layar_api.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Delete an ontology term
    api_instance.delete_term(id)
except ApiException as e:
    print("Exception when calling OntologyTermApi->delete_term: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[oAuth2ClientCredentials](../README.md#oAuth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_term**
> OntologyTerm get_term(id)

Get ontology term details

Get information provided in a specific Ontology Term object.

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
api_instance = layar_api.OntologyTermApi(layar_api.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Get ontology term details
    api_response = api_instance.get_term(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OntologyTermApi->get_term: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**OntologyTerm**](OntologyTerm.md)

### Authorization

[oAuth2ClientCredentials](../README.md#oAuth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **layar_ontology_term_get**
> list[OntologyTerm] layar_ontology_term_get(q=q, rows=rows, start=start, sort=sort, order=order, from_date=from_date, to_date=to_date, db_ids=db_ids, document_ids=document_ids, id_paths=id_paths, include_obsolete=include_obsolete, name_paths=name_paths, path_traversal=path_traversal, terms=terms)

Search for ontology terms

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
api_instance = layar_api.OntologyTermApi(layar_api.ApiClient(configuration))
q = 'q_example' # str | the query string to search for (optional)
rows = 56 # int | the number of rows to return (optional)
start = 56 # int | the start offset for the row (optional)
sort = 'sort_example' # str | sort results by the given property (optional)
order = 'order_example' # str | what order to return sorted results (optional)
from_date = '2013-10-20' # date | beginning of date range to return (optional)
to_date = '2013-10-20' # date | end of date range to return (optional)
db_ids = ['db_ids_example'] # list[str] | limit results to terms with specific IDs (optional)
document_ids = ['document_ids_example'] # list[str] | limit results to terms from specific documents (optional)
id_paths = ['id_paths_example'] # list[str] | limit results to terms with specific ID paths (optional)
include_obsolete = true # bool | include obsolte terms in the results (optional)
name_paths = ['name_paths_example'] # list[str] | limit results to terms with specific name paths (optional)
path_traversal = 'path_traversal_example' # str | limit results based on a specific traversal strategy when restricting by idPath or namePath (optional)
terms = ['terms_example'] # list[str] | limit results to terms matching the supplied terms (in either name or synonym) (optional)

try:
    # Search for ontology terms
    api_response = api_instance.layar_ontology_term_get(q=q, rows=rows, start=start, sort=sort, order=order, from_date=from_date, to_date=to_date, db_ids=db_ids, document_ids=document_ids, id_paths=id_paths, include_obsolete=include_obsolete, name_paths=name_paths, path_traversal=path_traversal, terms=terms)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OntologyTermApi->layar_ontology_term_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **str**| the query string to search for | [optional] 
 **rows** | **int**| the number of rows to return | [optional] 
 **start** | **int**| the start offset for the row | [optional] 
 **sort** | **str**| sort results by the given property | [optional] 
 **order** | **str**| what order to return sorted results | [optional] 
 **from_date** | **date**| beginning of date range to return | [optional] 
 **to_date** | **date**| end of date range to return | [optional] 
 **db_ids** | [**list[str]**](str.md)| limit results to terms with specific IDs | [optional] 
 **document_ids** | [**list[str]**](str.md)| limit results to terms from specific documents | [optional] 
 **id_paths** | [**list[str]**](str.md)| limit results to terms with specific ID paths | [optional] 
 **include_obsolete** | **bool**| include obsolte terms in the results | [optional] 
 **name_paths** | [**list[str]**](str.md)| limit results to terms with specific name paths | [optional] 
 **path_traversal** | **str**| limit results based on a specific traversal strategy when restricting by idPath or namePath | [optional] 
 **terms** | [**list[str]**](str.md)| limit results to terms matching the supplied terms (in either name or synonym) | [optional] 

### Return type

[**list[OntologyTerm]**](OntologyTerm.md)

### Authorization

[oAuth2ClientCredentials](../README.md#oAuth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_term**
> list[OntologyTerm] search_term(body=body)



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
api_instance = layar_api.OntologyTermApi(layar_api.ApiClient(configuration))
body = layar_api.OntologySearchCommand() # OntologySearchCommand |  (optional)

try:
    api_response = api_instance.search_term(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OntologyTermApi->search_term: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**OntologySearchCommand**](OntologySearchCommand.md)|  | [optional] 

### Return type

[**list[OntologyTerm]**](OntologyTerm.md)

### Authorization

[oAuth2ClientCredentials](../README.md#oAuth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_term**
> OntologyTerm update_term(body, id)

Update ontology term details

Modify the information provided for a specific Ontology Term object.

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
api_instance = layar_api.OntologyTermApi(layar_api.ApiClient(configuration))
body = layar_api.OntologyTerm() # OntologyTerm | 
id = 'id_example' # str | 

try:
    # Update ontology term details
    api_response = api_instance.update_term(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OntologyTermApi->update_term: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**OntologyTerm**](OntologyTerm.md)|  | 
 **id** | **str**|  | 

### Return type

[**OntologyTerm**](OntologyTerm.md)

### Authorization

[oAuth2ClientCredentials](../README.md#oAuth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

