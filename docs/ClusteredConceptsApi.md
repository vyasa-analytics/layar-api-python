# layar_api.ClusteredConceptsApi

All URIs are relative to *BASE_PATH*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get**](ClusteredConceptsApi.md#get) | **GET** /clusteredConcepts/{id} | clustered concept details
[**get_concepts**](ClusteredConceptsApi.md#get_concepts) | **GET** /clusteredConcepts/{clusteredQueryId}/{clusterId}/concepts | concepts
[**get_graph**](ClusteredConceptsApi.md#get_graph) | **GET** /clusteredConcepts/{clusteredQueryId}/graph | graph
[**get_relationships**](ClusteredConceptsApi.md#get_relationships) | **GET** /clusteredConcepts/{clusteredQueryId}/relationships | relationships

# **get**
> ClusteredConcepts get(id)

clustered concept details

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
api_instance = layar_api.ClusteredConceptsApi(layar_api.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # clustered concept details
    api_response = api_instance.get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusteredConceptsApi->get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**ClusteredConcepts**](ClusteredConcepts.md)

### Authorization

[oAuth2ClientCredentials](../README.md#oAuth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_concepts**
> list[Concept] get_concepts(clustered_query_id, cluster_id, rows=rows, start=start, sort=sort, order=order)

concepts

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
api_instance = layar_api.ClusteredConceptsApi(layar_api.ApiClient(configuration))
clustered_query_id = 'clustered_query_id_example' # str | 
cluster_id = 'cluster_id_example' # str | 
rows = 56 # int | the number of rows to return (optional)
start = 56 # int | the start offset for the row (optional)
sort = 'sort_example' # str | sort results by the given property (optional)
order = 'order_example' # str | what order to return sorted results (optional)

try:
    # concepts
    api_response = api_instance.get_concepts(clustered_query_id, cluster_id, rows=rows, start=start, sort=sort, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusteredConceptsApi->get_concepts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **clustered_query_id** | **str**|  | 
 **cluster_id** | **str**|  | 
 **rows** | **int**| the number of rows to return | [optional] 
 **start** | **int**| the start offset for the row | [optional] 
 **sort** | **str**| sort results by the given property | [optional] 
 **order** | **str**| what order to return sorted results | [optional] 

### Return type

[**list[Concept]**](Concept.md)

### Authorization

[oAuth2ClientCredentials](../README.md#oAuth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_graph**
> object get_graph(clustered_query_id)

graph

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
api_instance = layar_api.ClusteredConceptsApi(layar_api.ApiClient(configuration))
clustered_query_id = 'clustered_query_id_example' # str | 

try:
    # graph
    api_response = api_instance.get_graph(clustered_query_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusteredConceptsApi->get_graph: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **clustered_query_id** | **str**|  | 

### Return type

**object**

### Authorization

[oAuth2ClientCredentials](../README.md#oAuth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_relationships**
> list[ConceptRelationship] get_relationships(clustered_query_id, rows=rows)

relationships

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
api_instance = layar_api.ClusteredConceptsApi(layar_api.ApiClient(configuration))
clustered_query_id = 'clustered_query_id_example' # str | 
rows = 56 # int | the number of rows to return (optional)

try:
    # relationships
    api_response = api_instance.get_relationships(clustered_query_id, rows=rows)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusteredConceptsApi->get_relationships: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **clustered_query_id** | **str**|  | 
 **rows** | **int**| the number of rows to return | [optional] 

### Return type

[**list[ConceptRelationship]**](ConceptRelationship.md)

### Authorization

[oAuth2ClientCredentials](../README.md#oAuth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

