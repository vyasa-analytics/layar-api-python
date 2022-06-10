# layar_api.AutocompleteApi

All URIs are relative to *BASE_PATH*

Method | HTTP request | Description
------------- | ------------- | -------------
[**autocomplete_get**](AutocompleteApi.md#autocomplete_get) | **GET** /autocomplete | search for names used in various cortex domain objects
[**delete_search_history**](AutocompleteApi.md#delete_search_history) | **DELETE** /autocomplete/searchHistory/{term} | delete a previous search request
[**get_search_history**](AutocompleteApi.md#get_search_history) | **GET** /autocomplete/searchHistory | find previous search requests

# **autocomplete_get**
> AutocompleteResult autocomplete_get(q, index_type=index_type)

search for names used in various cortex domain objects

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
    # search for names used in various cortex domain objects
    api_response = api_instance.autocomplete_get(q, index_type=index_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AutocompleteApi->autocomplete_get: %s\n" % e)
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

# **delete_search_history**
> delete_search_history(term)

delete a previous search request

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
    # delete a previous search request
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

find previous search requests

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
    # find previous search requests
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

