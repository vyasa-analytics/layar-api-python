# layar_api.ModelApi

All URIs are relative to *BASE_PATH*

Method | HTTP request | Description
------------- | ------------- | -------------
[**download_model**](ModelApi.md#download_model) | **GET** /model/{id}/download | Download a learning model by ID
[**search_models_by_computation_id**](ModelApi.md#search_models_by_computation_id) | **GET** /projectComputation/{id}/models | find deep learning models by project computation
[**search_models_by_module_id**](ModelApi.md#search_models_by_module_id) | **GET** /module/{moduleId}/models | Find deep learning models by module
[**search_models_by_project_id**](ModelApi.md#search_models_by_project_id) | **GET** /project/{projectId}/models | find deep learning models by project

# **download_model**
> str download_model(id)

Download a learning model by ID

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
api_instance = layar_api.ModelApi(layar_api.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Download a learning model by ID
    api_response = api_instance.download_model(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ModelApi->download_model: %s\n" % e)
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

# **search_models_by_computation_id**
> list[DeepLearningModel] search_models_by_computation_id(id, start=start, rows=rows, q=q)

find deep learning models by project computation

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
api_instance = layar_api.ModelApi(layar_api.ApiClient(configuration))
id = 'id_example' # str | 
start = 56 # int | the start offset for the row (optional)
rows = 56 # int | the number of rows to return (optional)
q = 'q_example' # str | the query string to search for (optional)

try:
    # find deep learning models by project computation
    api_response = api_instance.search_models_by_computation_id(id, start=start, rows=rows, q=q)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ModelApi->search_models_by_computation_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **start** | **int**| the start offset for the row | [optional] 
 **rows** | **int**| the number of rows to return | [optional] 
 **q** | **str**| the query string to search for | [optional] 

### Return type

[**list[DeepLearningModel]**](DeepLearningModel.md)

### Authorization

[oAuth2ClientCredentials](../README.md#oAuth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_models_by_module_id**
> list[DeepLearningModel] search_models_by_module_id(module_id, start=start, rows=rows, q=q)

Find deep learning models by module

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
api_instance = layar_api.ModelApi(layar_api.ApiClient(configuration))
module_id = 'module_id_example' # str | 
start = 56 # int | the start offset for the row (optional)
rows = 56 # int | the number of rows to return (optional)
q = 'q_example' # str | the query string to search for (optional)

try:
    # Find deep learning models by module
    api_response = api_instance.search_models_by_module_id(module_id, start=start, rows=rows, q=q)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ModelApi->search_models_by_module_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **module_id** | **str**|  | 
 **start** | **int**| the start offset for the row | [optional] 
 **rows** | **int**| the number of rows to return | [optional] 
 **q** | **str**| the query string to search for | [optional] 

### Return type

[**list[DeepLearningModel]**](DeepLearningModel.md)

### Authorization

[oAuth2ClientCredentials](../README.md#oAuth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_models_by_project_id**
> list[DeepLearningModel] search_models_by_project_id(project_id, start=start, rows=rows, q=q)

find deep learning models by project

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
api_instance = layar_api.ModelApi(layar_api.ApiClient(configuration))
project_id = 'project_id_example' # str | 
start = 56 # int | the start offset for the row (optional)
rows = 56 # int | the number of rows to return (optional)
q = 'q_example' # str | the query string to search for (optional)

try:
    # find deep learning models by project
    api_response = api_instance.search_models_by_project_id(project_id, start=start, rows=rows, q=q)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ModelApi->search_models_by_project_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **start** | **int**| the start offset for the row | [optional] 
 **rows** | **int**| the number of rows to return | [optional] 
 **q** | **str**| the query string to search for | [optional] 

### Return type

[**list[DeepLearningModel]**](DeepLearningModel.md)

### Authorization

[oAuth2ClientCredentials](../README.md#oAuth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

