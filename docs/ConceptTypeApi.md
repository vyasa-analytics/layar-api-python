# layar_api.ConceptTypeApi

All URIs are relative to *BASE_PATH*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_concept_type**](ConceptTypeApi.md#create_concept_type) | **POST** /conceptType | Save new concept types
[**delete_concept_type**](ConceptTypeApi.md#delete_concept_type) | **DELETE** /conceptType/{id} | Delete a single concept type
[**delete_concept_types**](ConceptTypeApi.md#delete_concept_types) | **DELETE** /conceptType/deleteMany | Delete all the records with the given IDs
[**get_concept_type**](ConceptTypeApi.md#get_concept_type) | **GET** /conceptType/{id} | Concept type details
[**get_counts**](ConceptTypeApi.md#get_counts) | **GET** /concept/type/counts | Get result counts by concept type
[**get_relationship_templates**](ConceptTypeApi.md#get_relationship_templates) | **GET** /concept/type/relationshipTemplates | Relationship Templates
[**search_concept_types**](ConceptTypeApi.md#search_concept_types) | **GET** /conceptType | Search for concept types
[**update_concept_type**](ConceptTypeApi.md#update_concept_type) | **PUT** /conceptType/{id} | Update a single concept type

# **create_concept_type**
> list[ConceptType] create_concept_type(body)

Save new concept types

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
    # Save new concept types
    api_response = api_instance.create_concept_type(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConceptTypeApi->create_concept_type: %s\n" % e)
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

# **delete_concept_type**
> delete_concept_type(id)

Delete a single concept type

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
    # Delete a single concept type
    api_instance.delete_concept_type(id)
except ApiException as e:
    print("Exception when calling ConceptTypeApi->delete_concept_type: %s\n" % e)
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

# **delete_concept_types**
> delete_concept_types()

Delete all the records with the given IDs

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
    # Delete all the records with the given IDs
    api_instance.delete_concept_types()
except ApiException as e:
    print("Exception when calling ConceptTypeApi->delete_concept_types: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[oAuth2ClientCredentials](../README.md#oAuth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_concept_type**
> ConceptType get_concept_type(id)

Concept type details

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
    # Concept type details
    api_response = api_instance.get_concept_type(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConceptTypeApi->get_concept_type: %s\n" % e)
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
> MapStringObject get_counts()

Get result counts by concept type

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
    # Get result counts by concept type
    api_response = api_instance.get_counts()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConceptTypeApi->get_counts: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**MapStringObject**](MapStringObject.md)

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

# **search_concept_types**
> list[ConceptType] search_concept_types(x_vyasa_data_providers, rows=rows, q=q)

Search for concept types

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
    # Search for concept types
    api_response = api_instance.search_concept_types(x_vyasa_data_providers, rows=rows, q=q)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConceptTypeApi->search_concept_types: %s\n" % e)
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

# **update_concept_type**
> ConceptType update_concept_type(body, id)

Update a single concept type

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
    # Update a single concept type
    api_response = api_instance.update_concept_type(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConceptTypeApi->update_concept_type: %s\n" % e)
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

