# layar_api.ConceptApi

All URIs are relative to *BASE_PATH*

Method | HTTP request | Description
------------- | ------------- | -------------
[**assign_from_term**](ConceptApi.md#assign_from_term) | **POST** /concept/assignTerm | create a concept from an arbitrary text string
[**create_concept**](ConceptApi.md#create_concept) | **POST** /concept | Save a new concept
[**delete_concept**](ConceptApi.md#delete_concept) | **DELETE** /concept/{id} | Delete a concept from Layar
[**delete_concepts**](ConceptApi.md#delete_concepts) | **DELETE** /concept/deleteMany | delete all the records with the given IDs
[**demote_concept**](ConceptApi.md#demote_concept) | **PUT** /concept/{id}/demote | Remove relationship with a concept
[**get_concept**](ConceptApi.md#get_concept) | **GET** /concept/{id} | Get concept details
[**get_external_concepts**](ConceptApi.md#get_external_concepts) | **GET** /concept/external/{idKey}/{idValue} | find concepts by external id
[**get_related_concepts**](ConceptApi.md#get_related_concepts) | **GET** /concept/{id}/related | Returns a list of concepts related to the original concept.
[**get_statement_counts_over_time**](ConceptApi.md#get_statement_counts_over_time) | **GET** /concept/{id}/statementCountsOverTime | statement counts over time for concept id
[**make_primary_synonym**](ConceptApi.md#make_primary_synonym) | **PUT** /concept/{id}/makePrimarySynonym | Set a concept as the primary in its group of synonyms
[**make_synonyms**](ConceptApi.md#make_synonyms) | **PUT** /concept/makeSynonyms | Set all of the provided concept ids as synonyms of each other
[**patch_concept**](ConceptApi.md#patch_concept) | **PATCH** /concept/{id} | patch
[**remove_synonym**](ConceptApi.md#remove_synonym) | **DELETE** /concept/{id}/removeAsSynonym | Remove a concept from its group of synonyms
[**search_concept**](ConceptApi.md#search_concept) | **POST** /concept/search | search for concepts
[**update_concept**](ConceptApi.md#update_concept) | **PUT** /concept/{id} | Update concept details

# **assign_from_term**
> list[Concept] assign_from_term(body)

create a concept from an arbitrary text string

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
api_instance = layar_api.ConceptApi(layar_api.ApiClient(configuration))
body = layar_api.ConceptTermAssignment() # ConceptTermAssignment | 

try:
    # create a concept from an arbitrary text string
    api_response = api_instance.assign_from_term(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConceptApi->assign_from_term: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ConceptTermAssignment**](ConceptTermAssignment.md)|  | 

### Return type

[**list[Concept]**](Concept.md)

### Authorization

[oAuth2ClientCredentials](../README.md#oAuth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_concept**
> Concept create_concept(body)

Save a new concept

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
api_instance = layar_api.ConceptApi(layar_api.ApiClient(configuration))
body = layar_api.Concept() # Concept | 

try:
    # Save a new concept
    api_response = api_instance.create_concept(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConceptApi->create_concept: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Concept**](Concept.md)|  | 

### Return type

[**Concept**](Concept.md)

### Authorization

[oAuth2ClientCredentials](../README.md#oAuth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_concept**
> delete_concept(id)

Delete a concept from Layar

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
api_instance = layar_api.ConceptApi(layar_api.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Delete a concept from Layar
    api_instance.delete_concept(id)
except ApiException as e:
    print("Exception when calling ConceptApi->delete_concept: %s\n" % e)
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
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_concepts**
> delete_concepts()

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
api_instance = layar_api.ConceptApi(layar_api.ApiClient(configuration))

try:
    # delete all the records with the given IDs
    api_instance.delete_concepts()
except ApiException as e:
    print("Exception when calling ConceptApi->delete_concepts: %s\n" % e)
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

# **demote_concept**
> demote_concept(id)

Remove relationship with a concept

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
api_instance = layar_api.ConceptApi(layar_api.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Remove relationship with a concept
    api_instance.demote_concept(id)
except ApiException as e:
    print("Exception when calling ConceptApi->demote_concept: %s\n" % e)
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

# **get_concept**
> Concept get_concept(id)

Get concept details

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
api_instance = layar_api.ConceptApi(layar_api.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Get concept details
    api_response = api_instance.get_concept(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConceptApi->get_concept: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**Concept**](Concept.md)

### Authorization

[oAuth2ClientCredentials](../README.md#oAuth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_external_concepts**
> list[Concept] get_external_concepts(id_key, id_value)

find concepts by external id

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
api_instance = layar_api.ConceptApi(layar_api.ApiClient(configuration))
id_key = 'id_key_example' # str | 
id_value = 'id_value_example' # str | 

try:
    # find concepts by external id
    api_response = api_instance.get_external_concepts(id_key, id_value)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConceptApi->get_external_concepts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_key** | **str**|  | 
 **id_value** | **str**|  | 

### Return type

[**list[Concept]**](Concept.md)

### Authorization

[oAuth2ClientCredentials](../README.md#oAuth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_related_concepts**
> list[ConceptCountCommand] get_related_concepts(id)

Returns a list of concepts related to the original concept.

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
api_instance = layar_api.ConceptApi(layar_api.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Returns a list of concepts related to the original concept.
    api_response = api_instance.get_related_concepts(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConceptApi->get_related_concepts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**list[ConceptCountCommand]**](ConceptCountCommand.md)

### Authorization

[oAuth2ClientCredentials](../README.md#oAuth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_statement_counts_over_time**
> list[ConceptCountsInStatementsOverTime] get_statement_counts_over_time(id)

statement counts over time for concept id

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
api_instance = layar_api.ConceptApi(layar_api.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # statement counts over time for concept id
    api_response = api_instance.get_statement_counts_over_time(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConceptApi->get_statement_counts_over_time: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**list[ConceptCountsInStatementsOverTime]**](ConceptCountsInStatementsOverTime.md)

### Authorization

[oAuth2ClientCredentials](../README.md#oAuth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **make_primary_synonym**
> list[ConceptSynonymAssignmentResponse] make_primary_synonym(id)

Set a concept as the primary in its group of synonyms

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
api_instance = layar_api.ConceptApi(layar_api.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Set a concept as the primary in its group of synonyms
    api_response = api_instance.make_primary_synonym(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConceptApi->make_primary_synonym: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**list[ConceptSynonymAssignmentResponse]**](ConceptSynonymAssignmentResponse.md)

### Authorization

[oAuth2ClientCredentials](../README.md#oAuth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **make_synonyms**
> ConceptSynonymAssignmentResponse make_synonyms(body)

Set all of the provided concept ids as synonyms of each other

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
api_instance = layar_api.ConceptApi(layar_api.ApiClient(configuration))
body = layar_api.ListOfIds() # ListOfIds | 

try:
    # Set all of the provided concept ids as synonyms of each other
    api_response = api_instance.make_synonyms(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConceptApi->make_synonyms: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ListOfIds**](ListOfIds.md)|  | 

### Return type

[**ConceptSynonymAssignmentResponse**](ConceptSynonymAssignmentResponse.md)

### Authorization

[oAuth2ClientCredentials](../README.md#oAuth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_concept**
> patch_concept(body, id)

patch

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
api_instance = layar_api.ConceptApi(layar_api.ApiClient(configuration))
body = layar_api.PatchCommand() # PatchCommand | 
id = 'id_example' # str | 

try:
    # patch
    api_instance.patch_concept(body, id)
except ApiException as e:
    print("Exception when calling ConceptApi->patch_concept: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PatchCommand**](PatchCommand.md)|  | 
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[oAuth2ClientCredentials](../README.md#oAuth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_synonym**
> list[Concept] remove_synonym(id)

Remove a concept from its group of synonyms

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
api_instance = layar_api.ConceptApi(layar_api.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Remove a concept from its group of synonyms
    api_response = api_instance.remove_synonym(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConceptApi->remove_synonym: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**list[Concept]**](Concept.md)

### Authorization

[oAuth2ClientCredentials](../README.md#oAuth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_concept**
> list[Concept] search_concept(body=body)

search for concepts

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
api_instance = layar_api.ConceptApi(layar_api.ApiClient(configuration))
body = layar_api.Body() # Body |  (optional)

try:
    # search for concepts
    api_response = api_instance.search_concept(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConceptApi->search_concept: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body**](Body.md)|  | [optional] 

### Return type

[**list[Concept]**](Concept.md)

### Authorization

[oAuth2ClientCredentials](../README.md#oAuth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_concept**
> Concept update_concept(body, id)

Update concept details

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
api_instance = layar_api.ConceptApi(layar_api.ApiClient(configuration))
body = layar_api.Concept() # Concept | 
id = 'id_example' # str | 

try:
    # Update concept details
    api_response = api_instance.update_concept(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConceptApi->update_concept: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Concept**](Concept.md)|  | 
 **id** | **str**|  | 

### Return type

[**Concept**](Concept.md)

### Authorization

[oAuth2ClientCredentials](../README.md#oAuth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

