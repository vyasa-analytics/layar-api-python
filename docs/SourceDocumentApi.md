# layar_api.SourceDocumentApi

All URIs are relative to *BASE_PATH*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_annotation**](SourceDocumentApi.md#add_annotation) | **POST** /layar/sourceDocument/{id}/addAnnotation | Add an annotation to a document
[**add_annotations**](SourceDocumentApi.md#add_annotations) | **POST** /layar/sourceDocument/{id}/addAnnotations | Add a list of annotations to a document
[**add_column**](SourceDocumentApi.md#add_column) | **PUT** /layar/sourceDocument/{id}/addColumn | Add a column to a table document
[**add_viewer**](SourceDocumentApi.md#add_viewer) | **POST** /layar/sourceDocument/{id}/viewers | Authorize a viewer for the source document
[**create_document**](SourceDocumentApi.md#create_document) | **POST** /layar/sourceDocument | Create a source document
[**create_table_ontology**](SourceDocumentApi.md#create_table_ontology) | **POST** /layar/sourceDocument/{id}/createOntology | Create an ontology from a table
[**delete_document**](SourceDocumentApi.md#delete_document) | **DELETE** /layar/sourceDocument/{id} | Delete a document
[**delete_documents**](SourceDocumentApi.md#delete_documents) | **DELETE** /layar/sourceDocument/deleteMany | Delete multiple documents
[**download_annotations**](SourceDocumentApi.md#download_annotations) | **GET** /layar/sourceDocument/downloadAnnotations | Download document annotations to a CSV
[**download_document**](SourceDocumentApi.md#download_document) | **GET** /layar/sourceDocument/{id}/download | Download document by ID
[**extract_table_by_page**](SourceDocumentApi.md#extract_table_by_page) | **POST** /layar/sourceDocument/{id}/page/{page}/extractTable | Extract table from a specific page
[**extract_tables**](SourceDocumentApi.md#extract_tables) | **POST** /layar/sourceDocument/{id}/extractTables | Extract tables from a document
[**get_counts_by_suggested_category**](SourceDocumentApi.md#get_counts_by_suggested_category) | **GET** /layar/sourceDocument/{projectComputationId}/countBySuggestedCategory | Get document counts for suggested concept type by computation id
[**get_counts_by_type**](SourceDocumentApi.md#get_counts_by_type) | **GET** /layar/sourceDocument/countByType | Get document counts by type
[**get_counts_over_time**](SourceDocumentApi.md#get_counts_over_time) | **GET** /layar/sourceDocument/docCountsOverTime | Get document counts over time
[**get_doc_field_counts**](SourceDocumentApi.md#get_doc_field_counts) | **POST** /layar/sourceDocument/{field}/counts | Get document counts by field type
[**get_document**](SourceDocumentApi.md#get_document) | **GET** /layar/sourceDocument/{id} | Get source document details
[**get_document_concepts**](SourceDocumentApi.md#get_document_concepts) | **GET** /layar/sourceDocument/{id}/concepts | Get concept counts by document ID
[**get_document_statements**](SourceDocumentApi.md#get_document_statements) | **GET** /layar/sourceDocument/{id}/statements | Get statement counts by document ID
[**get_document_status**](SourceDocumentApi.md#get_document_status) | **GET** /layar/sourceDocument/{id}/status | Get the import status for a document
[**get_page_preview**](SourceDocumentApi.md#get_page_preview) | **GET** /layar/sourceDocument/{id}/page/{page}/preview | Get a document preview for a specific page
[**get_preview**](SourceDocumentApi.md#get_preview) | **GET** /layar/sourceDocument/{id}/preview | Get a document preview
[**get_statement_counts**](SourceDocumentApi.md#get_statement_counts) | **GET** /layar/sourceDocument/{id}/statementCount | Get a count of all statements in a document
[**get_viewers**](SourceDocumentApi.md#get_viewers) | **GET** /layar/sourceDocument/{id}/viewers | Get a list of all viewers of the source document
[**remove_annotation**](SourceDocumentApi.md#remove_annotation) | **DELETE** /layar/sourceDocument/{id}/annotations/{annotationId} | Delete annotations by annotation ID
[**render_pdf**](SourceDocumentApi.md#render_pdf) | **GET** /layar/sourceDocument/{id}/renderPdf | Render a PDF of a document
[**search_documents**](SourceDocumentApi.md#search_documents) | **POST** /layar/sourceDocument/search | Search for documents
[**table_similarity**](SourceDocumentApi.md#table_similarity) | **POST** /layar/sourceDocument/similarity | Calculate table similarity
[**update_annotation**](SourceDocumentApi.md#update_annotation) | **PUT** /layar/sourceDocument/{id}/annotations | Update annotation details
[**update_document**](SourceDocumentApi.md#update_document) | **PUT** /layar/sourceDocument/{id} | Update document details

# **add_annotation**
> add_annotation(body, id)

Add an annotation to a document

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
    # Add an annotation to a document
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

Add a list of annotations to a document

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
    # Add a list of annotations to a document
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

Add a column to a table document

Add a new column to a specific Layar table document.

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
    # Add a column to a table document
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

Authorize a viewer for the source document

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
    # Authorize a viewer for the source document
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

# **create_document**
> SourceDocument create_document(x_vyasa_data_providers, file=file, name=name, cortex_document_type=cortex_document_type)

Create a source document

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
    # Create a source document
    api_response = api_instance.create_document(x_vyasa_data_providers, file=file, name=name, cortex_document_type=cortex_document_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SourceDocumentApi->create_document: %s\n" % e)
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

# **create_table_ontology**
> SourceDocument create_table_ontology(id, name=name, id2=id2, label=label, synonyms=synonyms, properties=properties, delimeter=delimeter)

Create an ontology from a table

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
id = 'id_example' # str | The Layar ID for the table to be converted
name = 'name_example' # str |  (optional)
id2 = 'id_example' # str |  (optional)
label = 'label_example' # str |  (optional)
synonyms = ['synonyms_example'] # list[str] |  (optional)
properties = ['properties_example'] # list[str] |  (optional)
delimeter = 'delimeter_example' # str |  (optional)

try:
    # Create an ontology from a table
    api_response = api_instance.create_table_ontology(id, name=name, id2=id2, label=label, synonyms=synonyms, properties=properties, delimeter=delimeter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SourceDocumentApi->create_table_ontology: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The Layar ID for the table to be converted | 
 **name** | **str**|  | [optional] 
 **id2** | **str**|  | [optional] 
 **label** | **str**|  | [optional] 
 **synonyms** | [**list[str]**](str.md)|  | [optional] 
 **properties** | [**list[str]**](str.md)|  | [optional] 
 **delimeter** | **str**|  | [optional] 

### Return type

[**SourceDocument**](SourceDocument.md)

### Authorization

[oAuth2ClientCredentials](../README.md#oAuth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_document**
> delete_document(id)

Delete a document

Remove a specified Source Document object from your Layar instance.

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
    # Delete a document
    api_instance.delete_document(id)
except ApiException as e:
    print("Exception when calling SourceDocumentApi->delete_document: %s\n" % e)
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

# **delete_documents**
> delete_documents()

Delete multiple documents

Remove the list of specified Source Document objects by their document IDs.

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
    # Delete multiple documents
    api_instance.delete_documents()
except ApiException as e:
    print("Exception when calling SourceDocumentApi->delete_documents: %s\n" % e)
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

# **download_annotations**
> str download_annotations(search_command=search_command)

Download document annotations to a CSV

Download the annotations for a given source document to a CSV file.

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
    # Download document annotations to a CSV
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

# **download_document**
> str download_document(id)

Download document by ID

Download the original document by its source document ID.

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
id = 'id_example' # str | the Layar ID for that document

try:
    # Download document by ID
    api_response = api_instance.download_document(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SourceDocumentApi->download_document: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| the Layar ID for that document | 

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

Extract table from a specific page

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
    # Extract table from a specific page
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

Extract tables from a document

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
    # Extract tables from a document
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

# **get_counts_by_suggested_category**
> list[CountCommand] get_counts_by_suggested_category(project_computation_id)

Get document counts for suggested concept type by computation id

Return a total number of documents where a specific concept type has been suggested.

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
    # Get document counts for suggested concept type by computation id
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

Get document counts by type

Get total number of documents based on what document type they are (Documents, Images, Tables, etc.)

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
    # Get document counts by type
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
> list[DocCountsInStatementsOverTime] get_counts_over_time()

Get document counts over time

Get a total count of how many documents contain the specified term each month.

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
    # Get document counts over time
    api_response = api_instance.get_counts_over_time()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SourceDocumentApi->get_counts_over_time: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[DocCountsInStatementsOverTime]**](DocCountsInStatementsOverTime.md)

### Authorization

[oAuth2ClientCredentials](../README.md#oAuth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_doc_field_counts**
> list[FieldCount] get_doc_field_counts(body, field, annotation_key=annotation_key, value_type=value_type)

Get document counts by field type

Get a total number of documents based on a specific Document object parameter (type, date, etc.)

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
    # Get document counts by field type
    api_response = api_instance.get_doc_field_counts(body, field, annotation_key=annotation_key, value_type=value_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SourceDocumentApi->get_doc_field_counts: %s\n" % e)
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

# **get_document**
> SourceDocument get_document(id, x_vyasa_data_providers=x_vyasa_data_providers)

Get source document details

Get information provided in a specific Source Document object.

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
    # Get source document details
    api_response = api_instance.get_document(id, x_vyasa_data_providers=x_vyasa_data_providers)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SourceDocumentApi->get_document: %s\n" % e)
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

# **get_document_concepts**
> list[ConceptCountCommand] get_document_concepts(id)

Get concept counts by document ID

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
    # Get concept counts by document ID
    api_response = api_instance.get_document_concepts(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SourceDocumentApi->get_document_concepts: %s\n" % e)
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

# **get_document_statements**
> list[Statement] get_document_statements(id)

Get statement counts by document ID

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
    # Get statement counts by document ID
    api_response = api_instance.get_document_statements(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SourceDocumentApi->get_document_statements: %s\n" % e)
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

# **get_document_status**
> SourceDocumentImportStatus get_document_status(id)

Get the import status for a document

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
    # Get the import status for a document
    api_response = api_instance.get_document_status(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SourceDocumentApi->get_document_status: %s\n" % e)
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

# **get_page_preview**
> str get_page_preview(id, page)

Get a document preview for a specific page

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
    # Get a document preview for a specific page
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

Get a document preview

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
    # Get a document preview
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
> InlineResponse2004 get_statement_counts(id)

Get a count of all statements in a document

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
    # Get a count of all statements in a document
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

[**InlineResponse2004**](InlineResponse2004.md)

### Authorization

[oAuth2ClientCredentials](../README.md#oAuth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_viewers**
> list[SourceDocumentViewer] get_viewers(id)

Get a list of all viewers of the source document

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
    # Get a list of all viewers of the source document
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
> remove_annotation(id, annotation_id)

Delete annotations by annotation ID

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
annotation_id = 'annotation_id_example' # str | 

try:
    # Delete annotations by annotation ID
    api_instance.remove_annotation(id, annotation_id)
except ApiException as e:
    print("Exception when calling SourceDocumentApi->remove_annotation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **annotation_id** | **str**|  | 

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

Render a PDF of a document

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
    # Render a PDF of a document
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

# **search_documents**
> list[SourceDocument] search_documents(body, x_vyasa_data_providers)

Search for documents

Find a source document by their ID or other object parameters.

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
    # Search for documents
    api_response = api_instance.search_documents(body, x_vyasa_data_providers)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SourceDocumentApi->search_documents: %s\n" % e)
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

# **table_similarity**
> list[TableSimilarity] table_similarity(body)

Calculate table similarity

Calculate similarity between columns of two different tables.

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
body = layar_api.SourceDocumentSimilarityCommand() # SourceDocumentSimilarityCommand | 

try:
    # Calculate table similarity
    api_response = api_instance.table_similarity(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SourceDocumentApi->table_similarity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SourceDocumentSimilarityCommand**](SourceDocumentSimilarityCommand.md)|  | 

### Return type

[**list[TableSimilarity]**](TableSimilarity.md)

### Authorization

[oAuth2ClientCredentials](../README.md#oAuth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_annotation**
> update_annotation(body, id)

Update annotation details

Modify the information provided for a specific annotation within the Source Document object.

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
    # Update annotation details
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

# **update_document**
> SourceDocument update_document(body, id)

Update document details

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
    # Update document details
    api_response = api_instance.update_document(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SourceDocumentApi->update_document: %s\n" % e)
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

