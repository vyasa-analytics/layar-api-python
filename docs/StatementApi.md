# layar_api.StatementApi

All URIs are relative to *BASE_PATH*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_statement**](StatementApi.md#create_statement) | **POST** /statement | Create a new statement
[**delete_statement**](StatementApi.md#delete_statement) | **DELETE** /statement/{id} | Delete a statement by ID
[**delete_statements**](StatementApi.md#delete_statements) | **DELETE** /statement/deleteMany | Delete all the statements in an array
[**get_relationship_evidence**](StatementApi.md#get_relationship_evidence) | **GET** /statement/relationshipEvidence/{conceptId1}/{relationship}/{conceptId2} | Get the relationship evidence between two given concepts
[**get_statement**](StatementApi.md#get_statement) | **GET** /statement/{id} | Get statement details by ID
[**get_statement_field_counts**](StatementApi.md#get_statement_field_counts) | **POST** /statement/{field}/counts | Get statement counts by table column
[**named_entity_tag**](StatementApi.md#named_entity_tag) | **POST** /statement/{id}/namedEntity/tag | tag named entities within specific columns of a statement
[**search_statements**](StatementApi.md#search_statements) | **POST** /statement/search | search for statements
[**update_statement**](StatementApi.md#update_statement) | **PUT** /statement/{id} | Update a statement by ID

# **create_statement**
> Statement create_statement(body)

Create a new statement

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
api_instance = layar_api.StatementApi(layar_api.ApiClient(configuration))
body = layar_api.Statement() # Statement | 

try:
    # Create a new statement
    api_response = api_instance.create_statement(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatementApi->create_statement: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Statement**](Statement.md)|  | 

### Return type

[**Statement**](Statement.md)

### Authorization

[oAuth2ClientCredentials](../README.md#oAuth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_statement**
> delete_statement(id)

Delete a statement by ID

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
api_instance = layar_api.StatementApi(layar_api.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Delete a statement by ID
    api_instance.delete_statement(id)
except ApiException as e:
    print("Exception when calling StatementApi->delete_statement: %s\n" % e)
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

# **delete_statements**
> delete_statements()

Delete all the statements in an array

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
api_instance = layar_api.StatementApi(layar_api.ApiClient(configuration))

try:
    # Delete all the statements in an array
    api_instance.delete_statements()
except ApiException as e:
    print("Exception when calling StatementApi->delete_statements: %s\n" % e)
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

# **get_relationship_evidence**
> list[Statement] get_relationship_evidence(concept_id1, relationship, concept_id2)

Get the relationship evidence between two given concepts

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
api_instance = layar_api.StatementApi(layar_api.ApiClient(configuration))
concept_id1 = 'concept_id1_example' # str | 
relationship = 'relationship_example' # str | 
concept_id2 = 'concept_id2_example' # str | 

try:
    # Get the relationship evidence between two given concepts
    api_response = api_instance.get_relationship_evidence(concept_id1, relationship, concept_id2)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatementApi->get_relationship_evidence: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **concept_id1** | **str**|  | 
 **relationship** | **str**|  | 
 **concept_id2** | **str**|  | 

### Return type

[**list[Statement]**](Statement.md)

### Authorization

[oAuth2ClientCredentials](../README.md#oAuth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_statement**
> Statement get_statement(id)

Get statement details by ID

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
api_instance = layar_api.StatementApi(layar_api.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Get statement details by ID
    api_response = api_instance.get_statement(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatementApi->get_statement: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**Statement**](Statement.md)

### Authorization

[oAuth2ClientCredentials](../README.md#oAuth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_statement_field_counts**
> list[FieldCount] get_statement_field_counts(body, field)

Get statement counts by table column

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
api_instance = layar_api.StatementApi(layar_api.ApiClient(configuration))
body = layar_api.StatementSearchCommand() # StatementSearchCommand | 
field = 'field_example' # str | 

try:
    # Get statement counts by table column
    api_response = api_instance.get_statement_field_counts(body, field)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatementApi->get_statement_field_counts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**StatementSearchCommand**](StatementSearchCommand.md)|  | 
 **field** | **str**|  | 

### Return type

[**list[FieldCount]**](FieldCount.md)

### Authorization

[oAuth2ClientCredentials](../README.md#oAuth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: application/json
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
api_instance = layar_api.StatementApi(layar_api.ApiClient(configuration))
body = layar_api.StatementNamedEntityCommand() # StatementNamedEntityCommand | 
id = 'id_example' # str | 

try:
    # tag named entities within specific columns of a statement
    api_response = api_instance.named_entity_tag(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatementApi->named_entity_tag: %s\n" % e)
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

# **search_statements**
> list[Statement] search_statements(body=body)

search for statements

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
api_instance = layar_api.StatementApi(layar_api.ApiClient(configuration))
body = layar_api.StatementSearchCommand() # StatementSearchCommand |  (optional)

try:
    # search for statements
    api_response = api_instance.search_statements(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatementApi->search_statements: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**StatementSearchCommand**](StatementSearchCommand.md)|  | [optional] 

### Return type

[**list[Statement]**](Statement.md)

### Authorization

[oAuth2ClientCredentials](../README.md#oAuth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_statement**
> Statement update_statement(body, id)

Update a statement by ID

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
api_instance = layar_api.StatementApi(layar_api.ApiClient(configuration))
body = layar_api.Statement() # Statement | 
id = 'id_example' # str | 

try:
    # Update a statement by ID
    api_response = api_instance.update_statement(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatementApi->update_statement: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Statement**](Statement.md)|  | 
 **id** | **str**|  | 

### Return type

[**Statement**](Statement.md)

### Authorization

[oAuth2ClientCredentials](../README.md#oAuth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

