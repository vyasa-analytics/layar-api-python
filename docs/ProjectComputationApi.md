# layar_api.ProjectComputationApi

All URIs are relative to *BASE_PATH*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel**](ProjectComputationApi.md#cancel) | **POST** /projectComputation/{id}/cancel | cancel and shut down project computation without expecting any results back
[**download_logs**](ProjectComputationApi.md#download_logs) | **GET** /projectComputation/{id}/downloadLogs | download full logs for computation job
[**download_results**](ProjectComputationApi.md#download_results) | **GET** /projectComputation/{id}/downloadZipResults | download zip of documents created during computation
[**get**](ProjectComputationApi.md#get) | **GET** /projectComputation/{id} | project computation details
[**get_logs**](ProjectComputationApi.md#get_logs) | **GET** /projectComputation/{id}/logs | retrieve logs for computation job
[**stop**](ProjectComputationApi.md#stop) | **POST** /projectComputation/{id}/stopTraining | send computation job a stop message encouraging it to stop and send any results back

# **cancel**
> ProjectComputation cancel(id)

cancel and shut down project computation without expecting any results back

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
api_instance = layar_api.ProjectComputationApi(layar_api.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # cancel and shut down project computation without expecting any results back
    api_response = api_instance.cancel(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectComputationApi->cancel: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**ProjectComputation**](ProjectComputation.md)

### Authorization

[oAuth2ClientCredentials](../README.md#oAuth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_logs**
> str download_logs(id, computation_id)

download full logs for computation job

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
api_instance = layar_api.ProjectComputationApi(layar_api.ApiClient(configuration))
id = 'id_example' # str | 
computation_id = 'computation_id_example' # str | 

try:
    # download full logs for computation job
    api_response = api_instance.download_logs(id, computation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectComputationApi->download_logs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **computation_id** | **str**|  | 

### Return type

**str**

### Authorization

[oAuth2ClientCredentials](../README.md#oAuth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_results**
> str download_results(id, computation_id)

download zip of documents created during computation

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
api_instance = layar_api.ProjectComputationApi(layar_api.ApiClient(configuration))
id = 'id_example' # str | 
computation_id = 'computation_id_example' # str | 

try:
    # download zip of documents created during computation
    api_response = api_instance.download_results(id, computation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectComputationApi->download_results: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **computation_id** | **str**|  | 

### Return type

**str**

### Authorization

[oAuth2ClientCredentials](../README.md#oAuth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/zip

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get**
> ProjectComputation get(id)

project computation details

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
api_instance = layar_api.ProjectComputationApi(layar_api.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # project computation details
    api_response = api_instance.get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectComputationApi->get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**ProjectComputation**](ProjectComputation.md)

### Authorization

[oAuth2ClientCredentials](../README.md#oAuth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_logs**
> list[LogStash] get_logs(id, computation_id, max_rows=max_rows, order=order)

retrieve logs for computation job

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
api_instance = layar_api.ProjectComputationApi(layar_api.ApiClient(configuration))
id = 'id_example' # str | 
computation_id = 'computation_id_example' # str | 
max_rows = 56 # int |  (optional)
order = 'order_example' # str |  (optional)

try:
    # retrieve logs for computation job
    api_response = api_instance.get_logs(id, computation_id, max_rows=max_rows, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectComputationApi->get_logs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **computation_id** | **str**|  | 
 **max_rows** | **int**|  | [optional] 
 **order** | **str**|  | [optional] 

### Return type

[**list[LogStash]**](LogStash.md)

### Authorization

[oAuth2ClientCredentials](../README.md#oAuth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stop**
> StopTraining stop(id)

send computation job a stop message encouraging it to stop and send any results back

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
api_instance = layar_api.ProjectComputationApi(layar_api.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # send computation job a stop message encouraging it to stop and send any results back
    api_response = api_instance.stop(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectComputationApi->stop: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**StopTraining**](StopTraining.md)

### Authorization

[oAuth2ClientCredentials](../README.md#oAuth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

