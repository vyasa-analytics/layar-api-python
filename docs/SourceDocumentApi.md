# layar_api.SourceDocumentApi

All URIs are relative to *BASE_PATH*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_annotation**](SourceDocumentApi.md#add_annotation) | **POST** /sourceDocument/{id}/addAnnotation | bySource
[**add_annotations**](SourceDocumentApi.md#add_annotations) | **POST** /sourceDocument/{id}/addAnnotations | bySource
[**add_column**](SourceDocumentApi.md#add_column) | **PUT** /sourceDocument/{id}/addColumn | addColumn
[**add_viewer**](SourceDocumentApi.md#add_viewer) | **POST** /sourceDocument/{id}/viewers | add a viewer to the source document
[**create**](SourceDocumentApi.md#create) | **POST** /sourceDocument | save
[**delete**](SourceDocumentApi.md#delete) | **DELETE** /sourceDocument/{id} | delete
[**delete_many**](SourceDocumentApi.md#delete_many) | **DELETE** /sourceDocument/deleteMany | deleteMany
[**download**](SourceDocumentApi.md#download) | **GET** /sourceDocument/{id}/download | download
[**download_annotations**](SourceDocumentApi.md#download_annotations) | **GET** /sourceDocument/downloadAnnotations | downloads annotations as csv of one or more source document
[**extract_table_by_page**](SourceDocumentApi.md#extract_table_by_page) | **POST** /sourceDocument/{id}/page/{page}/extractTable | extract a table from a specific page
[**extract_tables**](SourceDocumentApi.md#extract_tables) | **POST** /sourceDocument/{id}/extractTables | extract tables from a document
[**get**](SourceDocumentApi.md#get) | **GET** /sourceDocument/{id} | source document details
[**get_concepts**](SourceDocumentApi.md#get_concepts) | **GET** /sourceDocument/{id}/concepts | count concepts by source document
[**get_counts_by_suggested_category**](SourceDocumentApi.md#get_counts_by_suggested_category) | **GET** /sourceDocument/{projectComputationId}/countBySuggestedCategory | countBySuggestedCategory
[**get_counts_by_type**](SourceDocumentApi.md#get_counts_by_type) | **GET** /sourceDocument/countByType | countByType
[**get_counts_over_time**](SourceDocumentApi.md#get_counts_over_time) | **GET** /sourceDocument/docCountsOverTime | doc counts over time for term
[**get_field_counts**](SourceDocumentApi.md#get_field_counts) | **POST** /sourceDocument/{field}/counts | 
[**get_page_preview**](SourceDocumentApi.md#get_page_preview) | **GET** /sourceDocument/{id}/page/{page}/preview | preview of a specific page
[**get_preview**](SourceDocumentApi.md#get_preview) | **GET** /sourceDocument/{id}/preview | preview
[**get_statement_counts**](SourceDocumentApi.md#get_statement_counts) | **GET** /sourceDocument/{id}/statementCount | get statement counts
[**get_statements**](SourceDocumentApi.md#get_statements) | **GET** /sourceDocument/{id}/statements | bySource
[**get_status**](SourceDocumentApi.md#get_status) | **GET** /sourceDocument/{id}/status | status
[**get_viewers**](SourceDocumentApi.md#get_viewers) | **GET** /sourceDocument/{id}/viewers | get a list of all viewers of the source document
[**remove_annotation**](SourceDocumentApi.md#remove_annotation) | **DELETE** /sourceDocument/{id}/annotations/{annotationId} | delete
[**render_pdf**](SourceDocumentApi.md#render_pdf) | **GET** /sourceDocument/{id}/renderPdf | renderPdf
[**search**](SourceDocumentApi.md#search) | **POST** /sourceDocument/search | 
[**update**](SourceDocumentApi.md#update) | **PUT** /sourceDocument/{id} | update
[**update_annotation**](SourceDocumentApi.md#update_annotation) | **PUT** /sourceDocument/{id}/annotations | updateAnnotations

# **add_annotation**
> add_annotation(body, id)

bySource

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
api_instance = layar_api.SourceDocumentApi(layar_api.ApiClient(configuration))
body = layar_api.Annotation() # Annotation | 
id = 'id_example' # str | 

try:
    # bySource
    api_instance.add_annotation(body, id)
except ApiException as e:
    print("Exception when calling SourceDocumentApi->add_annotation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Annotation**](Annotation.md)|  | 
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[oAuth2ClientCredentials](../README.md#oAuth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_annotations**
> add_annotations(body, id)

bySource

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
api_instance = layar_api.SourceDocumentApi(layar_api.ApiClient(configuration))
body = [layar_api.Annotation()] # list[Annotation] | 
id = 'id_example' # str | 

try:
    # bySource
    api_instance.add_annotations(body, id)
except ApiException as e:
    print("Exception when calling SourceDocumentApi->add_annotations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[Annotation]**](Annotation.md)|  | 
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[oAuth2ClientCredentials](../README.md#oAuth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_column**
> add_column(body, id)

addColumn

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
api_instance = layar_api.SourceDocumentApi(layar_api.ApiClient(configuration))
body = layar_api.AddColumnCommand() # AddColumnCommand | 
id = 'id_example' # str | 

try:
    # addColumn
    api_instance.add_column(body, id)
except ApiException as e:
    print("Exception when calling SourceDocumentApi->add_column: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AddColumnCommand**](AddColumnCommand.md)|  | 
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[oAuth2ClientCredentials](../README.md#oAuth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_viewer**
> SourceDocumentViewer add_viewer(id)

add a viewer to the source document

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
api_instance = layar_api.SourceDocumentApi(layar_api.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # add a viewer to the source document
    api_response = api_instance.add_viewer(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SourceDocumentApi->add_viewer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**SourceDocumentViewer**](SourceDocumentViewer.md)

### Authorization

[oAuth2ClientCredentials](../README.md#oAuth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create**
> SourceDocument create(x_vyasa_data_providers, file=file, name=name, cortex_document_type=cortex_document_type)

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
api_instance = layar_api.SourceDocumentApi(layar_api.ApiClient(configuration))
x_vyasa_data_providers = 'x_vyasa_data_providers_example' # str | remote data providers to query
file = 'file_example' # str |  (optional)
name = 'name_example' # str |  (optional)
cortex_document_type = 'cortex_document_type_example' # str |  (optional)

try:
    # save
    api_response = api_instance.create(x_vyasa_data_providers, file=file, name=name, cortex_document_type=cortex_document_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SourceDocumentApi->create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_vyasa_data_providers** | **str**| remote data providers to query | 
 **file** | **str**|  | [optional] 
 **name** | **str**|  | [optional] 
 **cortex_document_type** | **str**|  | [optional] 

### Return type

[**SourceDocument**](SourceDocument.md)

### Authorization

[oAuth2ClientCredentials](../README.md#oAuth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: multipart/form-data
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
api_instance = layar_api.SourceDocumentApi(layar_api.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # delete
    api_instance.delete(id)
except ApiException as e:
    print("Exception when calling SourceDocumentApi->delete: %s\n" % e)
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

deleteMany

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
api_instance = layar_api.SourceDocumentApi(layar_api.ApiClient(configuration))
body = layar_api.ListOfIds() # ListOfIds | 

try:
    # deleteMany
    api_instance.delete_many(body)
except ApiException as e:
    print("Exception when calling SourceDocumentApi->delete_many: %s\n" % e)
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

# **download**
> str download(id)

download

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
api_instance = layar_api.SourceDocumentApi(layar_api.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # download
    api_response = api_instance.download(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SourceDocumentApi->download: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

**str**

### Authorization

[oAuth2ClientCredentials](../README.md#oAuth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_annotations**
> str download_annotations(search_command=search_command)

downloads annotations as csv of one or more source document

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
api_instance = layar_api.SourceDocumentApi(layar_api.ApiClient(configuration))
search_command = 'search_command_example' # str |  (optional)

try:
    # downloads annotations as csv of one or more source document
    api_response = api_instance.download_annotations(search_command=search_command)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SourceDocumentApi->download_annotations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_command** | **str**|  | [optional] 

### Return type

**str**

### Authorization

[oAuth2ClientCredentials](../README.md#oAuth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **extract_table_by_page**
> SourceDocument extract_table_by_page(body, id, page)

extract a table from a specific page

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
api_instance = layar_api.SourceDocumentApi(layar_api.ApiClient(configuration))
body = layar_api.Coordinates() # Coordinates | 
id = 'id_example' # str | 
page = 56 # int | 

try:
    # extract a table from a specific page
    api_response = api_instance.extract_table_by_page(body, id, page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SourceDocumentApi->extract_table_by_page: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Coordinates**](Coordinates.md)|  | 
 **id** | **str**|  | 
 **page** | **int**|  | 

### Return type

[**SourceDocument**](SourceDocument.md)

### Authorization

[oAuth2ClientCredentials](../README.md#oAuth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **extract_tables**
> list[str] extract_tables(body, id)

extract tables from a document

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
api_instance = layar_api.SourceDocumentApi(layar_api.ApiClient(configuration))
body = layar_api.ExtractTablesCommand() # ExtractTablesCommand | 
id = 'id_example' # str | 

try:
    # extract tables from a document
    api_response = api_instance.extract_tables(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SourceDocumentApi->extract_tables: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ExtractTablesCommand**](ExtractTablesCommand.md)|  | 
 **id** | **str**|  | 

### Return type

**list[str]**

### Authorization

[oAuth2ClientCredentials](../README.md#oAuth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get**
> SourceDocument get(id, x_vyasa_data_providers=x_vyasa_data_providers)

source document details

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
api_instance = layar_api.SourceDocumentApi(layar_api.ApiClient(configuration))
id = 'id_example' # str | 
x_vyasa_data_providers = 'x_vyasa_data_providers_example' # str | remote data providers to query (optional)

try:
    # source document details
    api_response = api_instance.get(id, x_vyasa_data_providers=x_vyasa_data_providers)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SourceDocumentApi->get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **x_vyasa_data_providers** | **str**| remote data providers to query | [optional] 

### Return type

[**SourceDocument**](SourceDocument.md)

### Authorization

[oAuth2ClientCredentials](../README.md#oAuth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_concepts**
> list[ConceptCountCommand] get_concepts(id)

count concepts by source document

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
api_instance = layar_api.SourceDocumentApi(layar_api.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # count concepts by source document
    api_response = api_instance.get_concepts(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SourceDocumentApi->get_concepts: %s\n" % e)
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

# **get_counts_by_suggested_category**
> list[CountCommand] get_counts_by_suggested_category(project_computation_id)

countBySuggestedCategory

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
api_instance = layar_api.SourceDocumentApi(layar_api.ApiClient(configuration))
project_computation_id = 'project_computation_id_example' # str | 

try:
    # countBySuggestedCategory
    api_response = api_instance.get_counts_by_suggested_category(project_computation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SourceDocumentApi->get_counts_by_suggested_category: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_computation_id** | **str**|  | 

### Return type

[**list[CountCommand]**](CountCommand.md)

### Authorization

[oAuth2ClientCredentials](../README.md#oAuth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_counts_by_type**
> list[CountCommand] get_counts_by_type()

countByType

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
api_instance = layar_api.SourceDocumentApi(layar_api.ApiClient(configuration))

try:
    # countByType
    api_response = api_instance.get_counts_by_type()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SourceDocumentApi->get_counts_by_type: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[CountCommand]**](CountCommand.md)

### Authorization

[oAuth2ClientCredentials](../README.md#oAuth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_counts_over_time**
> list[DocCountsInStatementsOverTime] get_counts_over_time(term)

doc counts over time for term

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
api_instance = layar_api.SourceDocumentApi(layar_api.ApiClient(configuration))
term = 'term_example' # str | 

try:
    # doc counts over time for term
    api_response = api_instance.get_counts_over_time(term)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SourceDocumentApi->get_counts_over_time: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **term** | **str**|  | 

### Return type

[**list[DocCountsInStatementsOverTime]**](DocCountsInStatementsOverTime.md)

### Authorization

[oAuth2ClientCredentials](../README.md#oAuth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_field_counts**
> list[FieldCount] get_field_counts(body, field, annotation_key=annotation_key, value_type=value_type)



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
api_instance = layar_api.SourceDocumentApi(layar_api.ApiClient(configuration))
body = layar_api.SourceDocumentSearchCommand() # SourceDocumentSearchCommand | 
field = 'field_example' # str | 
annotation_key = 'annotation_key_example' # str |  (optional)
value_type = 'value_type_example' # str |  (optional)

try:
    api_response = api_instance.get_field_counts(body, field, annotation_key=annotation_key, value_type=value_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SourceDocumentApi->get_field_counts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SourceDocumentSearchCommand**](SourceDocumentSearchCommand.md)|  | 
 **field** | **str**|  | 
 **annotation_key** | **str**|  | [optional] 
 **value_type** | **str**|  | [optional] 

### Return type

[**list[FieldCount]**](FieldCount.md)

### Authorization

[oAuth2ClientCredentials](../README.md#oAuth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_page_preview**
> str get_page_preview(id, page)

preview of a specific page

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
api_instance = layar_api.SourceDocumentApi(layar_api.ApiClient(configuration))
id = 'id_example' # str | 
page = 56 # int | 

try:
    # preview of a specific page
    api_response = api_instance.get_page_preview(id, page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SourceDocumentApi->get_page_preview: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **page** | **int**|  | 

### Return type

**str**

### Authorization

[oAuth2ClientCredentials](../README.md#oAuth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_preview**
> str get_preview(id)

preview

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
api_instance = layar_api.SourceDocumentApi(layar_api.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # preview
    api_response = api_instance.get_preview(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SourceDocumentApi->get_preview: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

**str**

### Authorization

[oAuth2ClientCredentials](../README.md#oAuth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_statement_counts**
> InlineResponse2005 get_statement_counts(id)

get statement counts

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
api_instance = layar_api.SourceDocumentApi(layar_api.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # get statement counts
    api_response = api_instance.get_statement_counts(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SourceDocumentApi->get_statement_counts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**InlineResponse2005**](InlineResponse2005.md)

### Authorization

[oAuth2ClientCredentials](../README.md#oAuth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_statements**
> list[Statement] get_statements(id)

bySource

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
api_instance = layar_api.SourceDocumentApi(layar_api.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # bySource
    api_response = api_instance.get_statements(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SourceDocumentApi->get_statements: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**list[Statement]**](Statement.md)

### Authorization

[oAuth2ClientCredentials](../README.md#oAuth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_status**
> SourceDocumentImportStatus get_status(id)

status

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
api_instance = layar_api.SourceDocumentApi(layar_api.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # status
    api_response = api_instance.get_status(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SourceDocumentApi->get_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**SourceDocumentImportStatus**](SourceDocumentImportStatus.md)

### Authorization

[oAuth2ClientCredentials](../README.md#oAuth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_viewers**
> list[SourceDocumentViewer] get_viewers(id)

get a list of all viewers of the source document

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
api_instance = layar_api.SourceDocumentApi(layar_api.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # get a list of all viewers of the source document
    api_response = api_instance.get_viewers(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SourceDocumentApi->get_viewers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**list[SourceDocumentViewer]**](SourceDocumentViewer.md)

### Authorization

[oAuth2ClientCredentials](../README.md#oAuth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_annotation**
> remove_annotation()

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
api_instance = layar_api.SourceDocumentApi(layar_api.ApiClient(configuration))

try:
    # delete
    api_instance.remove_annotation()
except ApiException as e:
    print("Exception when calling SourceDocumentApi->remove_annotation: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[oAuth2ClientCredentials](../README.md#oAuth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **render_pdf**
> str render_pdf(id)

renderPdf

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
api_instance = layar_api.SourceDocumentApi(layar_api.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # renderPdf
    api_response = api_instance.render_pdf(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SourceDocumentApi->render_pdf: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

**str**

### Authorization

[oAuth2ClientCredentials](../README.md#oAuth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/pdf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search**
> list[SourceDocument] search(body, x_vyasa_data_providers)



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
api_instance = layar_api.SourceDocumentApi(layar_api.ApiClient(configuration))
body = layar_api.SourceDocumentSearchCommand() # SourceDocumentSearchCommand | 
x_vyasa_data_providers = 'x_vyasa_data_providers_example' # str | remote data providers to query

try:
    api_response = api_instance.search(body, x_vyasa_data_providers)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SourceDocumentApi->search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SourceDocumentSearchCommand**](SourceDocumentSearchCommand.md)|  | 
 **x_vyasa_data_providers** | **str**| remote data providers to query | 

### Return type

[**list[SourceDocument]**](SourceDocument.md)

### Authorization

[oAuth2ClientCredentials](../README.md#oAuth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update**
> SourceDocument update(body, id)

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
api_instance = layar_api.SourceDocumentApi(layar_api.ApiClient(configuration))
body = layar_api.SourceDocument() # SourceDocument | 
id = 'id_example' # str | 

try:
    # update
    api_response = api_instance.update(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SourceDocumentApi->update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SourceDocument**](SourceDocument.md)|  | 
 **id** | **str**|  | 

### Return type

[**SourceDocument**](SourceDocument.md)

### Authorization

[oAuth2ClientCredentials](../README.md#oAuth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_annotation**
> update_annotation(body, id)

updateAnnotations

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
api_instance = layar_api.SourceDocumentApi(layar_api.ApiClient(configuration))
body = layar_api.Annotation() # Annotation | 
id = 'id_example' # str | 

try:
    # updateAnnotations
    api_instance.update_annotation(body, id)
except ApiException as e:
    print("Exception when calling SourceDocumentApi->update_annotation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Annotation**](Annotation.md)|  | 
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[oAuth2ClientCredentials](../README.md#oAuth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

