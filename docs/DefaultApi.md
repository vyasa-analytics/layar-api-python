# layar_api.DefaultApi

All URIs are relative to *BASE_PATH*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ontology_term_search_get**](DefaultApi.md#ontology_term_search_get) | **GET** /ontologyTerm/search | 
[**paragraph_search_get**](DefaultApi.md#paragraph_search_get) | **GET** /paragraph/search | 

# **ontology_term_search_get**
> ontology_term_search_get()



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
api_instance = layar_api.DefaultApi(layar_api.ApiClient(configuration))

try:
    api_instance.ontology_term_search_get()
except ApiException as e:
    print("Exception when calling DefaultApi->ontology_term_search_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[oAuth2ClientCredentials](../README.md#oAuth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **paragraph_search_get**
> paragraph_search_get()



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
api_instance = layar_api.DefaultApi(layar_api.ApiClient(configuration))

try:
    api_instance.paragraph_search_get()
except ApiException as e:
    print("Exception when calling DefaultApi->paragraph_search_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[oAuth2ClientCredentials](../README.md#oAuth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

