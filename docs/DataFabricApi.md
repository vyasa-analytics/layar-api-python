# layar_api.DataFabricApi

All URIs are relative to *BASE_PATH*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_data_providers**](DataFabricApi.md#get_data_providers) | **GET** /layar/node | Search for data providers
[**get_fabrics**](DataFabricApi.md#get_fabrics) | **GET** /layar/fabric | Search for data fabrics

# **get_data_providers**
> object get_data_providers(q=q, max=max, offset=offset, sort=sort, order=order, all=all)

Search for data providers

Find data providers available for use in data fabrics.

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
api_instance = layar_api.DataFabricApi(layar_api.ApiClient(configuration))
q = 'q_example' # str | the query string to search for (optional)
max = 56 # int |  (optional)
offset = 56 # int |  (optional)
sort = 'sort_example' # str |  (optional)
order = 'order_example' # str |  (optional)
all = true # bool |  (optional)

try:
    # Search for data providers
    api_response = api_instance.get_data_providers(q=q, max=max, offset=offset, sort=sort, order=order, all=all)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataFabricApi->get_data_providers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **str**| the query string to search for | [optional] 
 **max** | **int**|  | [optional] 
 **offset** | **int**|  | [optional] 
 **sort** | **str**|  | [optional] 
 **order** | **str**|  | [optional] 
 **all** | **bool**|  | [optional] 

### Return type

**object**

### Authorization

[oAuth2ClientCredentials](../README.md#oAuth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_fabrics**
> object get_fabrics(q=q, max=max, offset=offset, sort=sort, order=order)

Search for data fabrics

Find data fabrics used to store or query data.

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
api_instance = layar_api.DataFabricApi(layar_api.ApiClient(configuration))
q = 'q_example' # str | the query string to search for (optional)
max = 56 # int |  (optional)
offset = 56 # int |  (optional)
sort = 'sort_example' # str |  (optional)
order = 'order_example' # str |  (optional)

try:
    # Search for data fabrics
    api_response = api_instance.get_fabrics(q=q, max=max, offset=offset, sort=sort, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataFabricApi->get_fabrics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **str**| the query string to search for | [optional] 
 **max** | **int**|  | [optional] 
 **offset** | **int**|  | [optional] 
 **sort** | **str**|  | [optional] 
 **order** | **str**|  | [optional] 

### Return type

**object**

### Authorization

[oAuth2ClientCredentials](../README.md#oAuth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

