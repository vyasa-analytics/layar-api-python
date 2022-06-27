# layar_api.AnswerApi

All URIs are relative to *BASE_PATH*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_answer**](AnswerApi.md#get_answer) | **GET** /layar/answer/{id} | Get answer details
[**layar_answer_get**](AnswerApi.md#layar_answer_get) | **GET** /layar/answer | 
[**search_answer**](AnswerApi.md#search_answer) | **POST** /layar/answer/search | Search for answers
[**update_answer**](AnswerApi.md#update_answer) | **PUT** /layar/answer/{id} | Update answer details

# **get_answer**
> Answer get_answer(id)

Get answer details

Get information provided in a specific Answer object.

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
api_instance = layar_api.AnswerApi(layar_api.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Get answer details
    api_response = api_instance.get_answer(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnswerApi->get_answer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**Answer**](Answer.md)

### Authorization

[oAuth2ClientCredentials](../README.md#oAuth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **layar_answer_get**
> AnswerArray layar_answer_get(q=q, rows=rows, start=start, sort=sort, order=order, from_date=from_date, to_date=to_date, batch_grouping_key=batch_grouping_key, question_ids=question_ids, rejected=rejected, show_accepted_first=show_accepted_first, single_doc_question_document_id=single_doc_question_document_id, with_concepts=with_concepts)



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
api_instance = layar_api.AnswerApi(layar_api.ApiClient(configuration))
q = 'q_example' # str | the query string to search for (optional)
rows = 56 # int | the number of rows to return (optional)
start = 56 # int | the start offset for the row (optional)
sort = 'sort_example' # str | sort results by the given property (optional)
order = 'order_example' # str | what order to return sorted results (optional)
from_date = '2013-10-20' # date | beginning of date range to return (optional)
to_date = '2013-10-20' # date | end of date range to return (optional)
batch_grouping_key = 'batch_grouping_key_example' # str | limit results to answers from a batch query (optional)
question_ids = ['question_ids_example'] # list[str] | limit results to answers that came from specific questions (optional)
rejected = true # bool | include results that have been rejected (optional)
show_accepted_first = true # bool | order results with accepted answers first (optional)
single_doc_question_document_id = 'single_doc_question_document_id_example' # str | include answers that were asked of a single document (optional)
with_concepts = true # bool | return concept matches for each answer (optional)

try:
    api_response = api_instance.layar_answer_get(q=q, rows=rows, start=start, sort=sort, order=order, from_date=from_date, to_date=to_date, batch_grouping_key=batch_grouping_key, question_ids=question_ids, rejected=rejected, show_accepted_first=show_accepted_first, single_doc_question_document_id=single_doc_question_document_id, with_concepts=with_concepts)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnswerApi->layar_answer_get: %s\n" % e)
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
 **batch_grouping_key** | **str**| limit results to answers from a batch query | [optional] 
 **question_ids** | [**list[str]**](str.md)| limit results to answers that came from specific questions | [optional] 
 **rejected** | **bool**| include results that have been rejected | [optional] 
 **show_accepted_first** | **bool**| order results with accepted answers first | [optional] 
 **single_doc_question_document_id** | **str**| include answers that were asked of a single document | [optional] 
 **with_concepts** | **bool**| return concept matches for each answer | [optional] 

### Return type

[**AnswerArray**](AnswerArray.md)

### Authorization

[oAuth2ClientCredentials](../README.md#oAuth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_answer**
> list[Answer] search_answer(body=body)

Search for answers

Find answers by their ID or other object parameters.

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
api_instance = layar_api.AnswerApi(layar_api.ApiClient(configuration))
body = layar_api.AnswerSearchCommand() # AnswerSearchCommand |  (optional)

try:
    # Search for answers
    api_response = api_instance.search_answer(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnswerApi->search_answer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AnswerSearchCommand**](AnswerSearchCommand.md)|  | [optional] 

### Return type

[**list[Answer]**](Answer.md)

### Authorization

[oAuth2ClientCredentials](../README.md#oAuth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_answer**
> list[Answer] update_answer(body, id)

Update answer details

Modify the information provided for a specific Answer object.

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
api_instance = layar_api.AnswerApi(layar_api.ApiClient(configuration))
body = layar_api.Answer() # Answer | 
id = 'id_example' # str | 

try:
    # Update answer details
    api_response = api_instance.update_answer(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnswerApi->update_answer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Answer**](Answer.md)|  | 
 **id** | **str**|  | 

### Return type

[**list[Answer]**](Answer.md)

### Authorization

[oAuth2ClientCredentials](../README.md#oAuth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

