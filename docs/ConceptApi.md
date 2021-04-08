# layar_api.ConceptApi

All URIs are relative to *BASE_PATH*

Method | HTTP request | Description
------------- | ------------- | -------------
[**assign_from_column**](ConceptApi.md#assign_from_column) | **POST** /concept/assign | start an async process to create concepts from a column in an uploaded spreadsheet
[**assign_from_term**](ConceptApi.md#assign_from_term) | **POST** /concept/assignTerm | create a concept from an arbitrary text string
[**create**](ConceptApi.md#create) | **POST** /concept | save a new concept
[**delete**](ConceptApi.md#delete) | **DELETE** /concept/{id} | delete
[**delete_many**](ConceptApi.md#delete_many) | **DELETE** /concept/deleteMany | delete all the records with the given IDs
[**demote**](ConceptApi.md#demote) | **PUT** /concept/{id}/demote | demote concept
[**get**](ConceptApi.md#get) | **GET** /concept/{id} | concept details
[**get_external_concepts**](ConceptApi.md#get_external_concepts) | **GET** /concept/external/{idKey}/{idValue} | find concepts by external id
[**get_related_concepts**](ConceptApi.md#get_related_concepts) | **GET** /concept/{id}/related | find related concepts
[**get_statement_counts_over_time**](ConceptApi.md#get_statement_counts_over_time) | **GET** /concept/{id}/statementCountsOverTime | statement counts over time for concept id
[**make_primary_synonym**](ConceptApi.md#make_primary_synonym) | **PUT** /concept/{id}/makePrimarySynonym | Make Primary Synonym
[**make_synonyms**](ConceptApi.md#make_synonyms) | **PUT** /concept/makeSynonyms | set all the concept ids as synonyms of each other
[**patch**](ConceptApi.md#patch) | **PATCH** /concept/{id} | patch
[**remove_synonym**](ConceptApi.md#remove_synonym) | **DELETE** /concept/{id}/removeAsSynonym | Remove As Synonym
[**search**](ConceptApi.md#search) | **POST** /concept/search | search for concepts
[**update**](ConceptApi.md#update) | **PUT** /concept/{id} | update

# **assign_from_column**
> ConceptAssignment assign_from_column(body)

start an async process to create concepts from a column in an uploaded spreadsheet

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
body = layar_api.ConceptAssignment() # ConceptAssignment | 

try:
    # start an async process to create concepts from a column in an uploaded spreadsheet
    api_response = api_instance.assign_from_column(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConceptApi->assign_from_column: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ConceptAssignment**](ConceptAssignment.md)|  | 

### Return type

[**ConceptAssignment**](ConceptAssignment.md)

### Authorization

[oAuth2ClientCredentials](../README.md#oAuth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

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

# **create**
> Concept create(body)

save a new concept

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
    # save a new concept
    api_response = api_instance.create(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConceptApi->create: %s\n" % e)
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
api_instance = layar_api.ConceptApi(layar_api.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # delete
    api_instance.delete(id)
except ApiException as e:
    print("Exception when calling ConceptApi->delete: %s\n" % e)
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
api_instance = layar_api.ConceptApi(layar_api.ApiClient(configuration))
body = layar_api.ListOfIds() # ListOfIds | 

try:
    # delete all the records with the given IDs
    api_instance.delete_many(body)
except ApiException as e:
    print("Exception when calling ConceptApi->delete_many: %s\n" % e)
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

# **demote**
> demote(concept_id)

demote concept

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
concept_id = 'concept_id_example' # str | 

try:
    # demote concept
    api_instance.demote(concept_id)
except ApiException as e:
    print("Exception when calling ConceptApi->demote: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **concept_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[oAuth2ClientCredentials](../README.md#oAuth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get**
> Concept get(id)

concept details

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
    # concept details
    api_response = api_instance.get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConceptApi->get: %s\n" % e)
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
> list[ConceptCountCommand] get_related_concepts(concept_id)

find related concepts

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
concept_id = 'concept_id_example' # str | 

try:
    # find related concepts
    api_response = api_instance.get_related_concepts(concept_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConceptApi->get_related_concepts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **concept_id** | **str**|  | 

### Return type

[**list[ConceptCountCommand]**](ConceptCountCommand.md)

### Authorization

[oAuth2ClientCredentials](../README.md#oAuth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_statement_counts_over_time**
> list[ConceptCountsInStatementsOverTime] get_statement_counts_over_time(concept_id)

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
concept_id = 'concept_id_example' # str | 

try:
    # statement counts over time for concept id
    api_response = api_instance.get_statement_counts_over_time(concept_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConceptApi->get_statement_counts_over_time: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **concept_id** | **str**|  | 

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

Make Primary Synonym

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
    # Make Primary Synonym
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

set all the concept ids as synonyms of each other

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
    # set all the concept ids as synonyms of each other
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

# **patch**
> patch(body, id)

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
    api_instance.patch(body, id)
except ApiException as e:
    print("Exception when calling ConceptApi->patch: %s\n" % e)
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

Remove As Synonym

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
    # Remove As Synonym
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

# **search**
> Concept search(body=body)

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
    api_response = api_instance.search(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConceptApi->search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body**](Body.md)|  | [optional] 

### Return type

[**Concept**](Concept.md)

### Authorization

[oAuth2ClientCredentials](../README.md#oAuth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update**
> Concept update(body, id)

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
api_instance = layar_api.ConceptApi(layar_api.ApiClient(configuration))
body = layar_api.Concept() # Concept | 
id = 'id_example' # str | 

try:
    # update
    api_response = api_instance.update(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConceptApi->update: %s\n" % e)
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

