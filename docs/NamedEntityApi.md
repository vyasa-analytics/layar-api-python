# layar_api.NamedEntityApi

All URIs are relative to *BASE_PATH*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_types**](NamedEntityApi.md#get_types) | **GET** /layar/namedEntity/types | Retrieve a list of available named entity types
[**named_entity_tag**](NamedEntityApi.md#named_entity_tag) | **POST** /layar/statement/{id}/namedEntity/tag | Tag named entities within specific columns of a table
[**tag_ner**](NamedEntityApi.md#tag_ner) | **POST** /layar/namedEntity/tag | Tag named entities

# **get_types**
> list[str] get_types()

Retrieve a list of available named entity types

Get a list all named entity types Vyasa offers off-the-shelf for NER tagging.

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
    # Retrieve a list of available named entity types
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

Tag named entities within specific columns of a table

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
    # Tag named entities within specific columns of a table
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

# **tag_ner**
> NamedEntityResponse tag_ner(body)

Tag named entities

Tag named entity concepts and their respective concept types for an input string of text.

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
    # Tag named entities
    api_response = api_instance.tag_ner(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NamedEntityApi->tag_ner: %s\n" % e)
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

