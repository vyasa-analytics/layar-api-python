# layar_api.SmilesApi

All URIs are relative to *BASE_PATH*

Method | HTTP request | Description
------------- | ------------- | -------------
[**similarity_vector_search**](SmilesApi.md#similarity_vector_search) | **POST** /layar/smiles/similarity | Search similar compounds with a list of smiles

# **similarity_vector_search**
> similarity_vector_search(body)

Search similar compounds with a list of smiles

Search similar compounds with a list of smiles

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
api_instance = layar_api.SmilesApi(layar_api.ApiClient(configuration))
body = layar_api.SOMRequest() # SOMRequest | 

try:
    # Search similar compounds with a list of smiles
    api_instance.similarity_vector_search(body)
except ApiException as e:
    print("Exception when calling SmilesApi->similarity_vector_search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SOMRequest**](SOMRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[oAuth2ClientCredentials](../README.md#oAuth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

