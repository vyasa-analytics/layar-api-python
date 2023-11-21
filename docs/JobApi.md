# layar_api.JobApi

All URIs are relative to *BASE_PATH*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_job**](JobApi.md#get_job) | **GET** /layar/job/{id} | Get job details

# **get_job**
> AsyncJob get_job(id)

Get job details

Get information about a specific asynchronous job object.

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
api_instance = layar_api.JobApi(layar_api.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Get job details
    api_response = api_instance.get_job(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JobApi->get_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**AsyncJob**](AsyncJob.md)

### Authorization

[oAuth2ClientCredentials](../README.md#oAuth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

