# layar_api.GroupApi

All URIs are relative to *BASE_PATH*

Method | HTTP request | Description
------------- | ------------- | -------------
[**group_terms**](GroupApi.md#group_terms) | **POST** /layar/group/terms | group similar terms (eg, &#x27;Vyasa Analytics&#x27; and &#x27;Vyasa Analytics, LLC&#x27;)

# **group_terms**
> list[list[str]] group_terms(body)

group similar terms (eg, 'Vyasa Analytics' and 'Vyasa Analytics, LLC')

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
body = layar_api.GroupTermsCommand() # GroupTermsCommand | 

try:
    # group similar terms (eg, 'Vyasa Analytics' and 'Vyasa Analytics, LLC')
    api_response = api_instance.group_terms(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupApi->group_terms: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GroupTermsCommand**](GroupTermsCommand.md)|  | 

### Return type

**list[list[str]]**

### Authorization

[oAuth2ClientCredentials](../README.md#oAuth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

