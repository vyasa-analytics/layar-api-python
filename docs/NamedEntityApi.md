# layar_api.NamedEntityApi

All URIs are relative to *BASE_PATH*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_types**](NamedEntityApi.md#get_types) | **GET** /namedEntity/types | A list of the available Named Entity Types
[**named_entity_tag**](NamedEntityApi.md#named_entity_tag) | **POST** /statement/{id}/namedEntity/tag | tag named entities within specific columns of a statement
[**tag**](NamedEntityApi.md#tag) | **POST** /namedEntity/tag | 

# **get_types**
> list[str] get_types()

A list of the available Named Entity Types

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
api_instance = layar_api.NamedEntityApi(layar_api.ApiClient(configuration))

try:
    # A list of the available Named Entity Types
    api_response = api_instance.get_types()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NamedEntityApi->get_types: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**list[str]**

### Authorization

[oAuth2ClientCredentials](../README.md#oAuth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **named_entity_tag**
> Statement named_entity_tag(body, id)

tag named entities within specific columns of a statement

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
api_instance = layar_api.NamedEntityApi(layar_api.ApiClient(configuration))
body = layar_api.StatementNamedEntityCommand() # StatementNamedEntityCommand | 
id = 'id_example' # str | 

try:
    # tag named entities within specific columns of a statement
    api_response = api_instance.named_entity_tag(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NamedEntityApi->named_entity_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**StatementNamedEntityCommand**](StatementNamedEntityCommand.md)|  | 
 **id** | **str**|  | 

### Return type

[**Statement**](Statement.md)

### Authorization

[oAuth2ClientCredentials](../README.md#oAuth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tag**
> NamedEntityResponse tag(body)



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
api_instance = layar_api.NamedEntityApi(layar_api.ApiClient(configuration))
body = layar_api.NamedEntityRequest() # NamedEntityRequest | 

try:
    api_response = api_instance.tag(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NamedEntityApi->tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NamedEntityRequest**](NamedEntityRequest.md)|  | 

### Return type

[**NamedEntityResponse**](NamedEntityResponse.md)

### Authorization

[oAuth2ClientCredentials](../README.md#oAuth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

