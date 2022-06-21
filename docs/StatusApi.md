# layar_api.StatusApi

All URIs are relative to *BASE_PATH*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_app_status**](StatusApi.md#get_app_status) | **GET** /layar/app | Get app uptime status

# **get_app_status**
> InlineResponse200 get_app_status()

Get app uptime status

Check to see whether your Layar instance is up ('OK') or down.

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
api_instance = layar_api.StatusApi(layar_api.ApiClient(configuration))

try:
    # Get app uptime status
    api_response = api_instance.get_app_status()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatusApi->get_app_status: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[oAuth2ClientCredentials](../README.md#oAuth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

