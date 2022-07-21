# layar_api.GroupApi

All URIs are relative to *BASE_PATH*

Method | HTTP request | Description
------------- | ------------- | -------------
[**group_terms**](GroupApi.md#group_terms) | **POST** /layar/group/terms | Group similar terms

# **group_terms**
> list[list[str]] group_terms(body)

Group similar terms

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
api_instance = layar_api.GroupApi(layar_api.ApiClient(configuration))
body = layar_api.Body3() # Body3 | 

try:
    # Group similar terms
    api_response = api_instance.group_terms(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupApi->group_terms: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body3**](Body3.md)|  | 

### Return type

**list[list[str]]**

### Authorization

[oAuth2ClientCredentials](../README.md#oAuth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

