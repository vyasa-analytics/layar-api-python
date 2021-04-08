# layar_api.AllApi

All URIs are relative to *BASE_PATH*

Method | HTTP request | Description
------------- | ------------- | -------------
[**search**](AllApi.md#search) | **GET** /all | 

# **search**
> AllSearchResponse search(q=q, start=start, rows=rows, concept_id=concept_id, type_filter=type_filter)



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
api_instance = layar_api.AllApi(layar_api.ApiClient(configuration))
q = 'q_example' # str | the query string to search for (optional)
start = 56 # int | the start offset for the row (optional)
rows = 56 # int | the number of rows to return (optional)
concept_id = 'concept_id_example' # str | limit results to those tagged with the given concept ID (optional)
type_filter = 'type_filter_example' # str |  (optional)

try:
    api_response = api_instance.search(q=q, start=start, rows=rows, concept_id=concept_id, type_filter=type_filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AllApi->search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **str**| the query string to search for | [optional] 
 **start** | **int**| the start offset for the row | [optional] 
 **rows** | **int**| the number of rows to return | [optional] 
 **concept_id** | **str**| limit results to those tagged with the given concept ID | [optional] 
 **type_filter** | [**str**](.md)|  | [optional] 

### Return type

[**AllSearchResponse**](AllSearchResponse.md)

### Authorization

[oAuth2ClientCredentials](../README.md#oAuth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

