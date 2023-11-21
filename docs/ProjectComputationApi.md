# layar_api.ProjectComputationApi

All URIs are relative to *BASE_PATH*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_computation**](ProjectComputationApi.md#cancel_computation) | **POST** /layar/projectComputation/{id}/cancel | Cancel a project computation job (hard stop)
[**download**](ProjectComputationApi.md#download) | **GET** /layar/projectComputation/{id}/download | Download computation job document based on id and url
[**download_computation**](ProjectComputationApi.md#download_computation) | **GET** /layar/projectComputation/{id}/downloadZipResults | Download computation job documents as zip file
[**download_logs**](ProjectComputationApi.md#download_logs) | **GET** /layar/projectComputation/{id}/downloadLogs | Download all computation job logs
[**get_logs**](ProjectComputationApi.md#get_logs) | **GET** /layar/projectComputation/{id}/logs | Retrieve logs for computation job
[**get_project_computation**](ProjectComputationApi.md#get_project_computation) | **GET** /layar/projectComputation/{id} | Get project computation details
[**stop_job**](ProjectComputationApi.md#stop_job) | **POST** /layar/projectComputation/{id}/stopTraining | Stop a computation job (soft stop)

# **cancel_computation**
> ProjectComputation cancel_computation(id)

Cancel a project computation job (hard stop)

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
    # Cancel a project computation job (hard stop)
    api_response = api_instance.cancel_computation(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectComputationApi->cancel_computation: %s\n" % e)
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

# **download**
> str download(id, url=url)

Download computation job document based on id and url

Download documents for a project computation job

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
url = 'url_example' # str |  (optional)

try:
    # Download computation job document based on id and url
    api_response = api_instance.download(id, url=url)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectComputationApi->download: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **url** | **str**|  | [optional] 

### Return type

**str**

### Authorization

[oAuth2ClientCredentials](../README.md#oAuth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_computation**
> str download_computation(id)

Download computation job documents as zip file

Download all documents for a project computation job into a compressed zip file.

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
    # Download computation job documents as zip file
    api_response = api_instance.download_computation(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectComputationApi->download_computation: %s\n" % e)
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
 - **Accept**: application/zip

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_logs**
> str download_logs(id)

Download all computation job logs

Download the full logs for a project computation job.

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
    # Download all computation job logs
    api_response = api_instance.download_logs(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectComputationApi->download_logs: %s\n" % e)
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
 - **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_logs**
> list[LogStash] get_logs(id, max_rows=max_rows, order=order)

Retrieve logs for computation job

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
max_rows = 56 # int |  (optional)
order = 'order_example' # str |  (optional)

try:
    # Retrieve logs for computation job
    api_response = api_instance.get_logs(id, max_rows=max_rows, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectComputationApi->get_logs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
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

# **get_project_computation**
> ProjectComputation get_project_computation(id)

Get project computation details

Get information provided in a specific Computation object.

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
    # Get project computation details
    api_response = api_instance.get_project_computation(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectComputationApi->get_project_computation: %s\n" % e)
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

# **stop_job**
> StopTraining stop_job(id)

Stop a computation job (soft stop)

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
    # Stop a computation job (soft stop)
    api_response = api_instance.stop_job(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectComputationApi->stop_job: %s\n" % e)
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

