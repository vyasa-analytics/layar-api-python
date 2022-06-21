# layar_api.AnswerApi

All URIs are relative to *BASE_PATH*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_answer**](AnswerApi.md#get_answer) | **GET** /layar/answer/{id} | Get answer details
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

