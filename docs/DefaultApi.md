# layar_api.DefaultApi

All URIs are relative to *BASE_PATH*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_data_providers**](DefaultApi.md#get_data_providers) | **GET** /connect/node | Search for data providers
[**get_fabrics**](DefaultApi.md#get_fabrics) | **GET** /connect/fabric | Search for data fabrics
[**layar_paragraph_get**](DefaultApi.md#layar_paragraph_get) | **GET** /layar/paragraph | 
[**search_paragraph**](DefaultApi.md#search_paragraph) | **POST** /layar/paragraph/search | 
[**search_term**](DefaultApi.md#search_term) | **POST** /layar/ontologyTerm/search | 

# **get_data_providers**
> object get_data_providers(q=q, max=max, offset=offset, sort=sort, order=order, all=all)

Search for data providers

Find data providers available for use in data fabrics.

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
api_instance = layar_api.DefaultApi(layar_api.ApiClient(configuration))
q = 'q_example' # str | the query string to search for (optional)
max = 56 # int |  (optional)
offset = 56 # int |  (optional)
sort = 'sort_example' # str |  (optional)
order = 'order_example' # str |  (optional)
all = true # bool |  (optional)

try:
    # Search for data providers
    api_response = api_instance.get_data_providers(q=q, max=max, offset=offset, sort=sort, order=order, all=all)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_data_providers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **str**| the query string to search for | [optional] 
 **max** | **int**|  | [optional] 
 **offset** | **int**|  | [optional] 
 **sort** | **str**|  | [optional] 
 **order** | **str**|  | [optional] 
 **all** | **bool**|  | [optional] 

### Return type

**object**

### Authorization

[oAuth2ClientCredentials](../README.md#oAuth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_fabrics**
> object get_fabrics(q=q, max=max, offset=offset, sort=sort, order=order)

Search for data fabrics

Find data fabrics used to store or query data.

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
api_instance = layar_api.DefaultApi(layar_api.ApiClient(configuration))
q = 'q_example' # str | the query string to search for (optional)
max = 56 # int |  (optional)
offset = 56 # int |  (optional)
sort = 'sort_example' # str |  (optional)
order = 'order_example' # str |  (optional)

try:
    # Search for data fabrics
    api_response = api_instance.get_fabrics(q=q, max=max, offset=offset, sort=sort, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_fabrics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **str**| the query string to search for | [optional] 
 **max** | **int**|  | [optional] 
 **offset** | **int**|  | [optional] 
 **sort** | **str**|  | [optional] 
 **order** | **str**|  | [optional] 

### Return type

**object**

### Authorization

[oAuth2ClientCredentials](../README.md#oAuth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **layar_paragraph_get**
> list[Paragraph] layar_paragraph_get(q=q, rows=rows, start=start, sort=sort, order=order, from_date=from_date, to_date=to_date, ids=ids, document_ids=document_ids, highlight=highlight, similar_ids=similar_ids, similar_text=similar_text, sources=sources)



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
api_instance = layar_api.DefaultApi(layar_api.ApiClient(configuration))
q = 'q_example' # str | the query string to search for (optional)
rows = 56 # int | the number of rows to return (optional)
start = 56 # int | the start offset for the row (optional)
sort = 'sort_example' # str | sort results by the given property (optional)
order = 'order_example' # str | what order to return sorted results (optional)
from_date = '2013-10-20' # date | beginning of date range to return (optional)
to_date = '2013-10-20' # date | end of date range to return (optional)
ids = ['ids_example'] # list[str] | limit results to specific paragraphs (optional)
document_ids = ['document_ids_example'] # list[str] | limit results to paragraphs from specific documents (optional)
highlight = true # bool | highlight the query results within the paragraphs (optional)
similar_ids = ['similar_ids_example'] # list[str] | find paragraphs that are similar to others (by their IDs) (optional)
similar_text = ['similar_text_example'] # list[str] | find paragraphs that are similar to the supplied text (optional)
sources = ['sources_example'] # list[str] | limit results to paragraphs from specific sources (optional)

try:
    api_response = api_instance.layar_paragraph_get(q=q, rows=rows, start=start, sort=sort, order=order, from_date=from_date, to_date=to_date, ids=ids, document_ids=document_ids, highlight=highlight, similar_ids=similar_ids, similar_text=similar_text, sources=sources)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->layar_paragraph_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **str**| the query string to search for | [optional] 
 **rows** | **int**| the number of rows to return | [optional] 
 **start** | **int**| the start offset for the row | [optional] 
 **sort** | **str**| sort results by the given property | [optional] 
 **order** | **str**| what order to return sorted results | [optional] 
 **from_date** | **date**| beginning of date range to return | [optional] 
 **to_date** | **date**| end of date range to return | [optional] 
 **ids** | [**list[str]**](str.md)| limit results to specific paragraphs | [optional] 
 **document_ids** | [**list[str]**](str.md)| limit results to paragraphs from specific documents | [optional] 
 **highlight** | **bool**| highlight the query results within the paragraphs | [optional] 
 **similar_ids** | [**list[str]**](str.md)| find paragraphs that are similar to others (by their IDs) | [optional] 
 **similar_text** | [**list[str]**](str.md)| find paragraphs that are similar to the supplied text | [optional] 
 **sources** | [**list[str]**](str.md)| limit results to paragraphs from specific sources | [optional] 

### Return type

[**list[Paragraph]**](Paragraph.md)

### Authorization

[oAuth2ClientCredentials](../README.md#oAuth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_paragraph**
> list[Paragraph] search_paragraph(body=body)



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
api_instance = layar_api.DefaultApi(layar_api.ApiClient(configuration))
body = layar_api.ParagraphSearchCommand() # ParagraphSearchCommand |  (optional)

try:
    api_response = api_instance.search_paragraph(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->search_paragraph: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ParagraphSearchCommand**](ParagraphSearchCommand.md)|  | [optional] 

### Return type

[**list[Paragraph]**](Paragraph.md)

### Authorization

[oAuth2ClientCredentials](../README.md#oAuth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_term**
> list[OntologyTerm] search_term(body=body)



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
api_instance = layar_api.DefaultApi(layar_api.ApiClient(configuration))
body = layar_api.OntologySearchCommand() # OntologySearchCommand |  (optional)

try:
    api_response = api_instance.search_term(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->search_term: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**OntologySearchCommand**](OntologySearchCommand.md)|  | [optional] 

### Return type

[**list[OntologyTerm]**](OntologyTerm.md)

### Authorization

[oAuth2ClientCredentials](../README.md#oAuth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

