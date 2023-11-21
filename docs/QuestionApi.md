# layar_api.QuestionApi

All URIs are relative to *BASE_PATH*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ask**](QuestionApi.md#ask) | **POST** /layar/question/ask | Ask a new question
[**cancel_batch**](QuestionApi.md#cancel_batch) | **PUT** /layar/question/cancelBulkQuestionAnswerJob/{jobID} | Cancel a bulk QA job request
[**create_question**](QuestionApi.md#create_question) | **POST** /layar/question | Create a new question
[**delete_question**](QuestionApi.md#delete_question) | **DELETE** /layar/question/{id} | Delete a question
[**delete_questions**](QuestionApi.md#delete_questions) | **DELETE** /layar/question/deleteMany | Delete multiple questions
[**find_more_answers**](QuestionApi.md#find_more_answers) | **POST** /layar/question/{id}/answers/more | Find more answers to a question
[**get_question**](QuestionApi.md#get_question) | **GET** /layar/question/{id} | Get question details
[**get_question_field_counts**](QuestionApi.md#get_question_field_counts) | **POST** /layar/question/{field}/counts | Get curation details by field type
[**patch_question**](QuestionApi.md#patch_question) | **PATCH** /layar/question/{id} | Update specific details for a question
[**query_expansion**](QuestionApi.md#query_expansion) | **POST** /layar/question/queryExpansion | Enable query expansion
[**refresh_answers**](QuestionApi.md#refresh_answers) | **POST** /layar/question/{id}/answers/refresh | Search for answers in new documents
[**search_question_batch**](QuestionApi.md#search_question_batch) | **POST** /layar/question/searchQuestionBatch | Search for question batches
[**search_questions**](QuestionApi.md#search_questions) | **POST** /layar/question/search | Search for questions
[**start_batch**](QuestionApi.md#start_batch) | **POST** /layar/question/startBulkQuestionAnswerJob | Submit a bulk QA job request
[**update_question**](QuestionApi.md#update_question) | **PUT** /layar/question/{id} | Update a saved question

# **ask**
> AskQuestionResponse ask(body, x_vyasa_advanced_parameters=x_vyasa_advanced_parameters)

Ask a new question

Ask a new question string and auto-generate a new Question object at the same time.

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
x_vyasa_advanced_parameters = 'x_vyasa_advanced_parameters_example' # str | for advanced users and debugging.  A JSON structure overriding default Question Answering parameters (optional)

try:
    # Ask a new question
    api_response = api_instance.ask(body, x_vyasa_advanced_parameters=x_vyasa_advanced_parameters)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuestionApi->ask: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AskQuestionCommand**](AskQuestionCommand.md)|  | 
 **x_vyasa_advanced_parameters** | **str**| for advanced users and debugging.  A JSON structure overriding default Question Answering parameters | [optional] 

### Return type

[**AskQuestionResponse**](AskQuestionResponse.md)

### Authorization

[oAuth2ClientCredentials](../README.md#oAuth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cancel_batch**
> InlineResponse2003 cancel_batch(job_id)

Cancel a bulk QA job request

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
    # Cancel a bulk QA job request
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

[**InlineResponse2003**](InlineResponse2003.md)

### Authorization

[oAuth2ClientCredentials](../README.md#oAuth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_question**
> Question create_question(body, x_vyasa_data_providers, x_vyasa_advanced_parameters=x_vyasa_advanced_parameters)

Create a new question

Create a new Question object.

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
body = layar_api.Body6() # Body6 | 
x_vyasa_data_providers = 'x_vyasa_data_providers_example' # str | remote data providers to query
x_vyasa_advanced_parameters = 'x_vyasa_advanced_parameters_example' # str | for advanced users and debugging.  A JSON structure overriding default Question Answering parameters (optional)

try:
    # Create a new question
    api_response = api_instance.create_question(body, x_vyasa_data_providers, x_vyasa_advanced_parameters=x_vyasa_advanced_parameters)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuestionApi->create_question: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body6**](Body6.md)|  | 
 **x_vyasa_data_providers** | **str**| remote data providers to query | 
 **x_vyasa_advanced_parameters** | **str**| for advanced users and debugging.  A JSON structure overriding default Question Answering parameters | [optional] 

### Return type

[**Question**](Question.md)

### Authorization

[oAuth2ClientCredentials](../README.md#oAuth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_question**
> delete_question(id)

Delete a question

Remove a specified Question object from your Layar instance.

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
    # Delete a question
    api_instance.delete_question(id)
except ApiException as e:
    print("Exception when calling QuestionApi->delete_question: %s\n" % e)
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

# **delete_questions**
> delete_questions()

Delete multiple questions

Remove the list of specified Question objects by their question IDs.

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

try:
    # Delete multiple questions
    api_instance.delete_questions()
except ApiException as e:
    print("Exception when calling QuestionApi->delete_questions: %s\n" % e)
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

# **find_more_answers**
> find_more_answers(id)

Find more answers to a question

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
    # Find more answers to a question
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

# **get_question**
> Question get_question(id)

Get question details

Modify the information provided for a specific Question object.

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
    # Get question details
    api_response = api_instance.get_question(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuestionApi->get_question: %s\n" % e)
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

# **get_question_field_counts**
> list[FieldCount] get_question_field_counts(body, field)

Get curation details by field type

Get a total number of questions that meet specific Question object parameters (curationType, moderators, discord, etc.)

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
    # Get curation details by field type
    api_response = api_instance.get_question_field_counts(body, field)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuestionApi->get_question_field_counts: %s\n" % e)
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

# **patch_question**
> patch_question(body, id)

Update specific details for a question

Replace a specific attribute of the Question object.

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
    # Update specific details for a question
    api_instance.patch_question(body, id)
except ApiException as e:
    print("Exception when calling QuestionApi->patch_question: %s\n" % e)
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

Enable query expansion

Expand the scope of query understanding within the QA Service by enabling our new query expansion method.

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
    # Enable query expansion
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

Search for answers in new documents

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
    # Search for answers in new documents
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

# **search_question_batch**
> list[QuestionBatch] search_question_batch(body=body)

Search for question batches

Find a question batch by their batch ID, job ID, or other object parameters.

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
body = layar_api.BulkQuestionSearchCommand() # BulkQuestionSearchCommand |  (optional)

try:
    # Search for question batches
    api_response = api_instance.search_question_batch(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuestionApi->search_question_batch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BulkQuestionSearchCommand**](BulkQuestionSearchCommand.md)|  | [optional] 

### Return type

[**list[QuestionBatch]**](QuestionBatch.md)

### Authorization

[oAuth2ClientCredentials](../README.md#oAuth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_questions**
> list[Question] search_questions(body=body)

Search for questions

Find a question by their ID or other object parameters.

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
    # Search for questions
    api_response = api_instance.search_questions(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuestionApi->search_questions: %s\n" % e)
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
> InlineResponse2002 start_batch(body=body)

Submit a bulk QA job request

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
    # Submit a bulk QA job request
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

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

[oAuth2ClientCredentials](../README.md#oAuth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_question**
> Question update_question(body, id)

Update a saved question

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
    # Update a saved question
    api_response = api_instance.update_question(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuestionApi->update_question: %s\n" % e)
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

