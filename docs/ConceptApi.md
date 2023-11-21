# layar_api.ConceptApi

All URIs are relative to *BASE_PATH*

Method | HTTP request | Description
------------- | ------------- | -------------
[**assign_from_term**](ConceptApi.md#assign_from_term) | **POST** /layar/concept/assignTerm | Create a new term for a concept
[**create_concept**](ConceptApi.md#create_concept) | **POST** /layar/concept | Create a new concept
[**delete_concept**](ConceptApi.md#delete_concept) | **DELETE** /layar/concept/{id} | Delete a concept
[**delete_concepts**](ConceptApi.md#delete_concepts) | **DELETE** /layar/concept/deleteMany | Delete multiple concepts
[**demote_concept**](ConceptApi.md#demote_concept) | **PUT** /layar/concept/{id}/demote | Demote a relationship with another concept
[**get_concept**](ConceptApi.md#get_concept) | **GET** /layar/concept/{id} | Get concept details
[**get_external_concepts**](ConceptApi.md#get_external_concepts) | **GET** /layar/concept/external/{idKey}/{idValue} | Search for concepts by external ID
[**get_related_concepts**](ConceptApi.md#get_related_concepts) | **GET** /layar/concept/{id}/related | Find related concepts
[**get_statement_counts_over_time**](ConceptApi.md#get_statement_counts_over_time) | **GET** /layar/concept/{id}/statementCountsOverTime | Get statement counts over time
[**make_primary_synonym**](ConceptApi.md#make_primary_synonym) | **PUT** /layar/concept/{id}/makePrimarySynonym | Set as primary synonym
[**make_synonyms**](ConceptApi.md#make_synonyms) | **PUT** /layar/concept/makeSynonyms | Set as synonyms
[**patch_concept**](ConceptApi.md#patch_concept) | **PATCH** /layar/concept/{id} | Update specific details for a concept
[**remove_synonym**](ConceptApi.md#remove_synonym) | **DELETE** /layar/concept/{id}/removeAsSynonym | Remove as synonym
[**search_concept**](ConceptApi.md#search_concept) | **POST** /layar/concept/search | Search for concepts
[**update_concept**](ConceptApi.md#update_concept) | **PUT** /layar/concept/{id} | Update all details for a concept

# **assign_from_term**
> list[Concept] assign_from_term(body)

Create a new term for a concept

Add a new term or query string into a Concept object.

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
    # Create a new term for a concept
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

Create a new concept

Convert a term or query string into a new Concept object.

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
body = layar_api.Concept1() # Concept1 | 

try:
    # Create a new concept
    api_response = api_instance.create_concept(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConceptApi->create_concept: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Concept1**](Concept1.md)|  | 

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

Delete a concept

Remove a specified Concept object from your Layar instance.

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
    # Delete a concept
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

Delete multiple concepts

Remove the list of specified Concept objects by their concept IDs.

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
    # Delete multiple concepts
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

Demote a relationship with another concept

Demote a linked relationship between the current concept and another concept to a lower relational tier.

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
    # Demote a relationship with another concept
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

Get information provided in a specific Concept object.

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

Search for concepts by external ID

Find concepts by custom IDs, which are added as an external ID in the concept object.

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
    # Search for concepts by external ID
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

Find related concepts

Return a list of concepts ids that are related to the original concept.

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
    # Find related concepts
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

Get statement counts over time

Get a total count of how many statements contain the specified concept each month.

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
    # Get statement counts over time
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

Set as primary synonym

Establish a specific concept as the primary term for its synonym group.

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
    # Set as primary synonym
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

Set as synonyms

Establish all of the provided concept ids as synonyms of each other

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
    # Set as synonyms
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

Update specific details for a concept

Replace a specific attribute of the Concept object.

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
    # Update specific details for a concept
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

Remove as synonym

Remove a specific concept from its associated synonym group.

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
    # Remove as synonym
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

Search for concepts

Find concepts by their ID or other object parameters.

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
    # Search for concepts
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

Update all details for a concept

Replace all current attributes of the Concept object with only those in the request payload.

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
    # Update all details for a concept
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

