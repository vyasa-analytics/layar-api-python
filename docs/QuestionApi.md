# layar_api.QuestionApi

All URIs are relative to *BASE_PATH*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ask**](QuestionApi.md#ask) | **POST** /question/ask | 
[**cancel_batch**](QuestionApi.md#cancel_batch) | **PUT** /question/cancelBulkQuestionAnswerJob/{jobID} | cancel an existing request to ask a batch of questions
[**create**](QuestionApi.md#create) | **POST** /question | save a new question
[**delete**](QuestionApi.md#delete) | **DELETE** /question/{id} | delete
[**delete_many**](QuestionApi.md#delete_many) | **DELETE** /question/deleteMany | delete all the records with the given IDs
[**find_more_answers**](QuestionApi.md#find_more_answers) | **POST** /question/{id}/answers/more | look for more answers to this question
[**get**](QuestionApi.md#get) | **GET** /question/{id} | question details
[**get_field_counts**](QuestionApi.md#get_field_counts) | **POST** /question/{field}/counts | 
[**patch**](QuestionApi.md#patch) | **PATCH** /question/{id} | patch
[**query_expansion**](QuestionApi.md#query_expansion) | **POST** /question/queryExpansion | 
[**refresh_answers**](QuestionApi.md#refresh_answers) | **POST** /question/{id}/answers/refresh | look for answers in new documents
[**search**](QuestionApi.md#search) | **POST** /question/search | search for questions
[**start_batch**](QuestionApi.md#start_batch) | **POST** /question/startBulkQuestionAnswerJob | submit a request to ask a batch of questions
[**update**](QuestionApi.md#update) | **PUT** /question/{id} | update

# **ask**
> AskQuestionResponse ask(body)



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
api_instance = layar_api.QuestionApi(layar_api.ApiClient(configuration))
body = layar_api.AskQuestionCommand() # AskQuestionCommand | 

try:
    api_response = api_instance.ask(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuestionApi->ask: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AskQuestionCommand**](AskQuestionCommand.md)|  | 

### Return type

[**AskQuestionResponse**](AskQuestionResponse.md)

### Authorization

[oAuth2ClientCredentials](../README.md#oAuth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cancel_batch**
> InlineResponse2002 cancel_batch(job_id)

cancel an existing request to ask a batch of questions

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
api_instance = layar_api.QuestionApi(layar_api.ApiClient(configuration))
job_id = 'job_id_example' # str | 

try:
    # cancel an existing request to ask a batch of questions
    api_response = api_instance.cancel_batch(job_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuestionApi->cancel_batch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**|  | 

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

[oAuth2ClientCredentials](../README.md#oAuth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create**
> Question create(body, x_vyasa_data_providers)

save a new question

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
api_instance = layar_api.QuestionApi(layar_api.ApiClient(configuration))
body = layar_api.Question() # Question | 
x_vyasa_data_providers = 'x_vyasa_data_providers_example' # str | remote data providers to query

try:
    # save a new question
    api_response = api_instance.create(body, x_vyasa_data_providers)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuestionApi->create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Question**](Question.md)|  | 
 **x_vyasa_data_providers** | **str**| remote data providers to query | 

### Return type

[**Question**](Question.md)

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
api_instance = layar_api.QuestionApi(layar_api.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # delete
    api_instance.delete(id)
except ApiException as e:
    print("Exception when calling QuestionApi->delete: %s\n" % e)
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
api_instance = layar_api.QuestionApi(layar_api.ApiClient(configuration))
body = layar_api.ListOfIds() # ListOfIds | 

try:
    # delete all the records with the given IDs
    api_instance.delete_many(body)
except ApiException as e:
    print("Exception when calling QuestionApi->delete_many: %s\n" % e)
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

# **find_more_answers**
> find_more_answers(id)

look for more answers to this question

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
api_instance = layar_api.QuestionApi(layar_api.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # look for more answers to this question
    api_instance.find_more_answers(id)
except ApiException as e:
    print("Exception when calling QuestionApi->find_more_answers: %s\n" % e)
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

# **get**
> Question get(id)

question details

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
api_instance = layar_api.QuestionApi(layar_api.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # question details
    api_response = api_instance.get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuestionApi->get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**Question**](Question.md)

### Authorization

[oAuth2ClientCredentials](../README.md#oAuth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_field_counts**
> list[FieldCount] get_field_counts(body, field)



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
api_instance = layar_api.QuestionApi(layar_api.ApiClient(configuration))
body = layar_api.QuestionSearchCommand() # QuestionSearchCommand | 
field = 'field_example' # str | 

try:
    api_response = api_instance.get_field_counts(body, field)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuestionApi->get_field_counts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**QuestionSearchCommand**](QuestionSearchCommand.md)|  | 
 **field** | **str**|  | 

### Return type

[**list[FieldCount]**](FieldCount.md)

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
api_instance = layar_api.QuestionApi(layar_api.ApiClient(configuration))
body = layar_api.PatchCommand() # PatchCommand | 
id = 'id_example' # str | 

try:
    # patch
    api_instance.patch(body, id)
except ApiException as e:
    print("Exception when calling QuestionApi->patch: %s\n" % e)
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

# **query_expansion**
> QueryExpansionResponse query_expansion(body)



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
api_instance = layar_api.QuestionApi(layar_api.ApiClient(configuration))
body = layar_api.QueryExpansionRequest() # QueryExpansionRequest | 

try:
    api_response = api_instance.query_expansion(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuestionApi->query_expansion: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**QueryExpansionRequest**](QueryExpansionRequest.md)|  | 

### Return type

[**QueryExpansionResponse**](QueryExpansionResponse.md)

### Authorization

[oAuth2ClientCredentials](../README.md#oAuth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **refresh_answers**
> refresh_answers(id)

look for answers in new documents

Look for answers in new documents (since the last time this endpoint was called or since the question was created, if this endpoint has never been called)

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
api_instance = layar_api.QuestionApi(layar_api.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # look for answers in new documents
    api_instance.refresh_answers(id)
except ApiException as e:
    print("Exception when calling QuestionApi->refresh_answers: %s\n" % e)
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

# **search**
> list[Question] search(body=body)

search for questions

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
api_instance = layar_api.QuestionApi(layar_api.ApiClient(configuration))
body = layar_api.QuestionSearchCommand() # QuestionSearchCommand |  (optional)

try:
    # search for questions
    api_response = api_instance.search(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuestionApi->search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**QuestionSearchCommand**](QuestionSearchCommand.md)|  | [optional] 

### Return type

[**list[Question]**](Question.md)

### Authorization

[oAuth2ClientCredentials](../README.md#oAuth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_batch**
> InlineResponse2003 start_batch(body=body)

submit a request to ask a batch of questions

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
api_instance = layar_api.QuestionApi(layar_api.ApiClient(configuration))
body = layar_api.BulkQuestionCommand() # BulkQuestionCommand |  (optional)

try:
    # submit a request to ask a batch of questions
    api_response = api_instance.start_batch(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuestionApi->start_batch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BulkQuestionCommand**](BulkQuestionCommand.md)|  | [optional] 

### Return type

[**InlineResponse2003**](InlineResponse2003.md)

### Authorization

[oAuth2ClientCredentials](../README.md#oAuth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update**
> Question update(body, id)

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
api_instance = layar_api.QuestionApi(layar_api.ApiClient(configuration))
body = layar_api.Question() # Question | 
id = 'id_example' # str | 

try:
    # update
    api_response = api_instance.update(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuestionApi->update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Question**](Question.md)|  | 
 **id** | **str**|  | 

### Return type

[**Question**](Question.md)

### Authorization

[oAuth2ClientCredentials](../README.md#oAuth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

