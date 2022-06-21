# layar_api.AutocompleteApi

All URIs are relative to *BASE_PATH*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_search_history**](AutocompleteApi.md#delete_search_history) | **DELETE** /layar/autocomplete/searchHistory/{term} | Delete a search request
[**get_search_history**](AutocompleteApi.md#get_search_history) | **GET** /layar/autocomplete/searchHistory | Get search history
[**layar_autocomplete_get**](AutocompleteApi.md#layar_autocomplete_get) | **GET** /layar/autocomplete | Search across all domain objects

# **delete_search_history**
> delete_search_history(term)

Delete a search request

Remove a term or search query from your history.

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
api_instance = layar_api.AutocompleteApi(layar_api.ApiClient(configuration))
term = 'term_example' # str | 

try:
    # Delete a search request
    api_instance.delete_search_history(term)
except ApiException as e:
    print("Exception when calling AutocompleteApi->delete_search_history: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **term** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[oAuth2ClientCredentials](../README.md#oAuth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_search_history**
> list[str] get_search_history(q=q)

Get search history

Return a list of previous search requests.

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
api_instance = layar_api.AutocompleteApi(layar_api.ApiClient(configuration))
q = 'q_example' # str |  (optional)

try:
    # Get search history
    api_response = api_instance.get_search_history(q=q)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AutocompleteApi->get_search_history: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **str**|  | [optional] 

### Return type

**list[str]**

### Authorization

[oAuth2ClientCredentials](../README.md#oAuth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **layar_autocomplete_get**
> AutocompleteResult layar_autocomplete_get(q, index_type=index_type)

Search across all domain objects

Find any objects across all domains (e.g. Answers, Concepts, Paragraphs, Projects, etc.) where the input query string exists as the name.

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
api_instance = layar_api.AutocompleteApi(layar_api.ApiClient(configuration))
q = 'q_example' # str | 
index_type = 'index_type_example' # str |  (optional)

try:
    # Search across all domain objects
    api_response = api_instance.layar_autocomplete_get(q, index_type=index_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AutocompleteApi->layar_autocomplete_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **str**|  | 
 **index_type** | **str**|  | [optional] 

### Return type

[**AutocompleteResult**](AutocompleteResult.md)

### Authorization

[oAuth2ClientCredentials](../README.md#oAuth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

