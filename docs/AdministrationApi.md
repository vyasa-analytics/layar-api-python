# layar_api.AdministrationApi

All URIs are relative to *BASE_PATH*

Method | HTTP request | Description
------------- | ------------- | -------------
[**debug_logging**](AdministrationApi.md#debug_logging) | **POST** /admin/debugLogging | temporarily (15m) enable DEBUG level logging
[**diagnostics**](AdministrationApi.md#diagnostics) | **GET** /admin/diagnostics | generate an encrypted diagnostics file

# **debug_logging**
> debug_logging()

temporarily (15m) enable DEBUG level logging

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
api_instance = layar_api.AdministrationApi(layar_api.ApiClient(configuration))

try:
    # temporarily (15m) enable DEBUG level logging
    api_instance.debug_logging()
except ApiException as e:
    print("Exception when calling AdministrationApi->debug_logging: %s\n" % e)
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

# **diagnostics**
> diagnostics()

generate an encrypted diagnostics file

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
api_instance = layar_api.AdministrationApi(layar_api.ApiClient(configuration))

try:
    # generate an encrypted diagnostics file
    api_instance.diagnostics()
except ApiException as e:
    print("Exception when calling AdministrationApi->diagnostics: %s\n" % e)
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

