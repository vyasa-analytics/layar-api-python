# layar_api.ConceptTypeApi

All URIs are relative to *BASE_PATH*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create**](ConceptTypeApi.md#create) | **POST** /conceptType | save
[**delete**](ConceptTypeApi.md#delete) | **DELETE** /conceptType/{id} | delete
[**delete_many**](ConceptTypeApi.md#delete_many) | **DELETE** /conceptType/deleteMany | delete all the records with the given IDs
[**get**](ConceptTypeApi.md#get) | **GET** /conceptType/{id} | concept type details
[**get_counts**](ConceptTypeApi.md#get_counts) | **GET** /concept/type/counts | get counts concepts broken down by concept type
[**get_relationship_templates**](ConceptTypeApi.md#get_relationship_templates) | **GET** /concept/type/relationshipTemplates | Relationship Templates
[**search**](ConceptTypeApi.md#search) | **GET** /conceptType | search for concept types
[**update**](ConceptTypeApi.md#update) | **PUT** /conceptType/{id} | update

# **create**
> list[ConceptType] create(body)

save

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
api_instance = layar_api.ConceptTypeApi(layar_api.ApiClient(configuration))
body = layar_api.ConceptType() # ConceptType | 

try:
    # save
    api_response = api_instance.create(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConceptTypeApi->create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ConceptType**](ConceptType.md)|  | 

### Return type

[**list[ConceptType]**](ConceptType.md)

### Authorization

[oAuth2ClientCredentials](../README.md#oAuth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete**
> delete(id)

delete

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
api_instance = layar_api.ConceptTypeApi(layar_api.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # delete
    api_instance.delete(id)
except ApiException as e:
    print("Exception when calling ConceptTypeApi->delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[oAuth2ClientCredentials](../README.md#oAuth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_many**
> delete_many(body)

delete all the records with the given IDs

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
api_instance = layar_api.ConceptTypeApi(layar_api.ApiClient(configuration))
body = layar_api.ListOfIds() # ListOfIds | 

try:
    # delete all the records with the given IDs
    api_instance.delete_many(body)
except ApiException as e:
    print("Exception when calling ConceptTypeApi->delete_many: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ListOfIds**](ListOfIds.md)|  | 

### Return type

void (empty response body)

### Authorization

[oAuth2ClientCredentials](../README.md#oAuth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get**
> ConceptType get(id)

concept type details

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
api_instance = layar_api.ConceptTypeApi(layar_api.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # concept type details
    api_response = api_instance.get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConceptTypeApi->get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**ConceptType**](ConceptType.md)

### Authorization

[oAuth2ClientCredentials](../README.md#oAuth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_counts**
> MapC2ABstring2CobjectC2BB get_counts()

get counts concepts broken down by concept type

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
api_instance = layar_api.ConceptTypeApi(layar_api.ApiClient(configuration))

try:
    # get counts concepts broken down by concept type
    api_response = api_instance.get_counts()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConceptTypeApi->get_counts: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**MapC2ABstring2CobjectC2BB**](MapC2ABstring2CobjectC2BB.md)

### Authorization

[oAuth2ClientCredentials](../README.md#oAuth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_relationship_templates**
> list[ConceptTypeRelationshipTemplate] get_relationship_templates()

Relationship Templates

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
api_instance = layar_api.ConceptTypeApi(layar_api.ApiClient(configuration))

try:
    # Relationship Templates
    api_response = api_instance.get_relationship_templates()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConceptTypeApi->get_relationship_templates: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[ConceptTypeRelationshipTemplate]**](ConceptTypeRelationshipTemplate.md)

### Authorization

[oAuth2ClientCredentials](../README.md#oAuth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search**
> list[ConceptType] search(x_vyasa_data_providers, rows=rows, q=q)

search for concept types

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
api_instance = layar_api.ConceptTypeApi(layar_api.ApiClient(configuration))
x_vyasa_data_providers = 'x_vyasa_data_providers_example' # str | remote data providers to query
rows = 56 # int | the number of rows to return (optional)
q = 'q_example' # str | the query string to search for (optional)

try:
    # search for concept types
    api_response = api_instance.search(x_vyasa_data_providers, rows=rows, q=q)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConceptTypeApi->search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_vyasa_data_providers** | **str**| remote data providers to query | 
 **rows** | **int**| the number of rows to return | [optional] 
 **q** | **str**| the query string to search for | [optional] 

### Return type

[**list[ConceptType]**](ConceptType.md)

### Authorization

[oAuth2ClientCredentials](../README.md#oAuth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update**
> ConceptType update(body, id)

update

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
api_instance = layar_api.ConceptTypeApi(layar_api.ApiClient(configuration))
body = layar_api.ConceptType() # ConceptType | 
id = 'id_example' # str | 

try:
    # update
    api_response = api_instance.update(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConceptTypeApi->update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ConceptType**](ConceptType.md)|  | 
 **id** | **str**|  | 

### Return type

[**ConceptType**](ConceptType.md)

### Authorization

[oAuth2ClientCredentials](../README.md#oAuth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

