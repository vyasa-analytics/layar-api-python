# layar_api.ModuleApi

All URIs are relative to *BASE_PATH*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_module**](ModuleApi.md#create_module) | **POST** /layar/module | Create a new module
[**get_module**](ModuleApi.md#get_module) | **GET** /layar/module/{id} | Get module details
[**search_modules**](ModuleApi.md#search_modules) | **GET** /layar/module | Search for modules

# **create_module**
> list[Module] create_module(body)

Create a new module

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
api_instance = layar_api.ModuleApi(layar_api.ApiClient(configuration))
body = layar_api.Module1() # Module1 | 

try:
    # Create a new module
    api_response = api_instance.create_module(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ModuleApi->create_module: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Module1**](Module1.md)|  | 

### Return type

[**list[Module]**](Module.md)

### Authorization

[oAuth2ClientCredentials](../README.md#oAuth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_module**
> Module get_module(id)

Get module details

Get information provided in a specific Module object.

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
api_instance = layar_api.ModuleApi(layar_api.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Get module details
    api_response = api_instance.get_module(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ModuleApi->get_module: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**Module**](Module.md)

### Authorization

[oAuth2ClientCredentials](../README.md#oAuth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_modules**
> list[Module] search_modules(rows=rows, start=start, q=q)

Search for modules

Find modules by their ID or other object parameters.

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
api_instance = layar_api.ModuleApi(layar_api.ApiClient(configuration))
rows = 56 # int | the number of rows to return (optional)
start = 56 # int | the start offset for the row (optional)
q = 'q_example' # str | the query string to search for (optional)

try:
    # Search for modules
    api_response = api_instance.search_modules(rows=rows, start=start, q=q)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ModuleApi->search_modules: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rows** | **int**| the number of rows to return | [optional] 
 **start** | **int**| the start offset for the row | [optional] 
 **q** | **str**| the query string to search for | [optional] 

### Return type

[**list[Module]**](Module.md)

### Authorization

[oAuth2ClientCredentials](../README.md#oAuth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

