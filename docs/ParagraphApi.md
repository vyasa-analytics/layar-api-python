# layar_api.ParagraphApi

All URIs are relative to *BASE_PATH*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_paragraph**](ParagraphApi.md#get_paragraph) | **GET** /paragraph/{id} | Get details for a single paragraph
[**paragraph_get**](ParagraphApi.md#paragraph_get) | **GET** /paragraph | search for paragraphs
[**parse_text**](ParagraphApi.md#parse_text) | **POST** /partOfSpeech/parseText | Parse text into part of speech components and queryable terms

# **get_paragraph**
> Paragraph get_paragraph(id)

Get details for a single paragraph

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
api_instance = layar_api.ParagraphApi(layar_api.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Get details for a single paragraph
    api_response = api_instance.get_paragraph(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ParagraphApi->get_paragraph: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**Paragraph**](Paragraph.md)

### Authorization

[oAuth2ClientCredentials](../README.md#oAuth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **paragraph_get**
> list[Paragraph] paragraph_get(q=q, rows=rows, start=start, sort=sort, order=order, from_date=from_date, to_date=to_date, ids=ids, document_ids=document_ids, highlight=highlight, similar_ids=similar_ids, similar_text=similar_text, sources=sources)

search for paragraphs

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
api_instance = layar_api.ParagraphApi(layar_api.ApiClient(configuration))
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
    # search for paragraphs
    api_response = api_instance.paragraph_get(q=q, rows=rows, start=start, sort=sort, order=order, from_date=from_date, to_date=to_date, ids=ids, document_ids=document_ids, highlight=highlight, similar_ids=similar_ids, similar_text=similar_text, sources=sources)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ParagraphApi->paragraph_get: %s\n" % e)
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

# **parse_text**
> PartOfSpeechResponse parse_text(body=body)

Parse text into part of speech components and queryable terms

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
api_instance = layar_api.ParagraphApi(layar_api.ApiClient(configuration))
body = layar_api.PartOfSpeechCommand() # PartOfSpeechCommand |  (optional)

try:
    # Parse text into part of speech components and queryable terms
    api_response = api_instance.parse_text(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ParagraphApi->parse_text: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PartOfSpeechCommand**](PartOfSpeechCommand.md)|  | [optional] 

### Return type

[**PartOfSpeechResponse**](PartOfSpeechResponse.md)

### Authorization

[oAuth2ClientCredentials](../README.md#oAuth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

