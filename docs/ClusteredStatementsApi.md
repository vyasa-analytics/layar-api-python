# layar_api.ClusteredStatementsApi

All URIs are relative to *BASE_PATH*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create**](ClusteredStatementsApi.md#create) | **POST** /clusteredStatements | create a new clustered statement request
[**get**](ClusteredStatementsApi.md#get) | **GET** /clusteredStatements/{id} | clustered statements details
[**get_statements**](ClusteredStatementsApi.md#get_statements) | **GET** /clusteredStatements/{clusteredStatementsId}/statements | statements

# **create**
> ClusteredStatements create(body)

create a new clustered statement request

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
api_instance = layar_api.ClusteredStatementsApi(layar_api.ApiClient(configuration))
body = layar_api.ClusteredStatements() # ClusteredStatements | 

try:
    # create a new clustered statement request
    api_response = api_instance.create(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusteredStatementsApi->create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ClusteredStatements**](ClusteredStatements.md)|  | 

### Return type

[**ClusteredStatements**](ClusteredStatements.md)

### Authorization

[oAuth2ClientCredentials](../README.md#oAuth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get**
> ClusteredStatements get()

clustered statements details

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
api_instance = layar_api.ClusteredStatementsApi(layar_api.ApiClient(configuration))

try:
    # clustered statements details
    api_response = api_instance.get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusteredStatementsApi->get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ClusteredStatements**](ClusteredStatements.md)

### Authorization

[oAuth2ClientCredentials](../README.md#oAuth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_statements**
> object get_statements()

statements

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
api_instance = layar_api.ClusteredStatementsApi(layar_api.ApiClient(configuration))

try:
    # statements
    api_response = api_instance.get_statements()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusteredStatementsApi->get_statements: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**object**

### Authorization

[oAuth2ClientCredentials](../README.md#oAuth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

