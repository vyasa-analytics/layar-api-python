# layar_api.OntologyTermApi

All URIs are relative to *BASE_PATH*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ontology_term_get**](OntologyTermApi.md#ontology_term_get) | **GET** /ontologyTerm | search for ontology terms
[**ontology_term_id_delete**](OntologyTermApi.md#ontology_term_id_delete) | **DELETE** /ontologyTerm/{id} | delete
[**ontology_term_id_get**](OntologyTermApi.md#ontology_term_id_get) | **GET** /ontologyTerm/{id} | ontologyTerm details
[**ontology_term_id_put**](OntologyTermApi.md#ontology_term_id_put) | **PUT** /ontologyTerm/{id} | update
[**ontology_term_post**](OntologyTermApi.md#ontology_term_post) | **POST** /ontologyTerm | save a new ontology term
[**ontology_term_search_post**](OntologyTermApi.md#ontology_term_search_post) | **POST** /ontologyTerm/search | search for ontologyTerms

# **ontology_term_get**
> list[OntologyTerm] ontology_term_get(q=q, rows=rows, start=start, sort=sort, order=order, from_date=from_date, to_date=to_date, db_ids=db_ids, document_ids=document_ids, id_paths=id_paths, include_obsolete=include_obsolete, name_paths=name_paths, path_traversal=path_traversal, terms=terms)

search for ontology terms

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
    # search for ontology terms
    api_response = api_instance.ontology_term_get(q=q, rows=rows, start=start, sort=sort, order=order, from_date=from_date, to_date=to_date, db_ids=db_ids, document_ids=document_ids, id_paths=id_paths, include_obsolete=include_obsolete, name_paths=name_paths, path_traversal=path_traversal, terms=terms)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OntologyTermApi->ontology_term_get: %s\n" % e)
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

# **ontology_term_id_delete**
> ontology_term_id_delete(id)

delete

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
    # delete
    api_instance.ontology_term_id_delete(id)
except ApiException as e:
    print("Exception when calling OntologyTermApi->ontology_term_id_delete: %s\n" % e)
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

# **ontology_term_id_get**
> OntologyTerm ontology_term_id_get(id)

ontologyTerm details

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
    # ontologyTerm details
    api_response = api_instance.ontology_term_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OntologyTermApi->ontology_term_id_get: %s\n" % e)
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

# **ontology_term_id_put**
> OntologyTerm ontology_term_id_put(body, id)

update

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
    # update
    api_response = api_instance.ontology_term_id_put(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OntologyTermApi->ontology_term_id_put: %s\n" % e)
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

# **ontology_term_post**
> OntologyTerm ontology_term_post(body)

save a new ontology term

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
    # save a new ontology term
    api_response = api_instance.ontology_term_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OntologyTermApi->ontology_term_post: %s\n" % e)
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

# **ontology_term_search_post**
> list[OntologyTerm] ontology_term_search_post(body=body)

search for ontologyTerms

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
    # search for ontologyTerms
    api_response = api_instance.ontology_term_search_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OntologyTermApi->ontology_term_search_post: %s\n" % e)
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

