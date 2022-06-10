# layar_api.LiveSourceApi

All URIs are relative to *BASE_PATH*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_feeds**](LiveSourceApi.md#create_feeds) | **POST** /liveSource | Create a new live source
[**create_feeds_from_column**](LiveSourceApi.md#create_feeds_from_column) | **POST** /liveSource/createFeedsFromColumn | create live source feeds from column of a spreadsheet containing URLs
[**delete_feed**](LiveSourceApi.md#delete_feed) | **DELETE** /liveSource/{id} | Delete a live source
[**delete_feeds**](LiveSourceApi.md#delete_feeds) | **DELETE** /liveSource/deleteMany | delete the set of live source ids
[**get_feed**](LiveSourceApi.md#get_feed) | **GET** /liveSource/{id} | Get live source details
[**get_import_status**](LiveSourceApi.md#get_import_status) | **GET** /liveSource/{id}/importStatus | Returns the percent completed for a live source import
[**get_job_status**](LiveSourceApi.md#get_job_status) | **GET** /liveSource/{id}/jobStatus | Get job status details
[**get_source_document_url**](LiveSourceApi.md#get_source_document_url) | **GET** /liveSource/{id}/sourceDocuments | Get the documents from a particular source
[**search_feeds**](LiveSourceApi.md#search_feeds) | **GET** /liveSource | Search for live sources
[**unschedule_job**](LiveSourceApi.md#unschedule_job) | **PUT** /liveSource/{id}/jobStatus/unschedule | Change a job status to &#x27;Unscheduled&#x27;
[**update_feed**](LiveSourceApi.md#update_feed) | **PUT** /liveSource/{id} | Update a live source
[**update_job**](LiveSourceApi.md#update_job) | **PUT** /liveSource/{id}/{jobAction} | Update a job with a new action

# **create_feeds**
> LiveSource create_feeds(body)

Create a new live source

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
api_instance = layar_api.LiveSourceApi(layar_api.ApiClient(configuration))
body = layar_api.LiveSource() # LiveSource | 

try:
    # Create a new live source
    api_response = api_instance.create_feeds(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LiveSourceApi->create_feeds: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LiveSource**](LiveSource.md)|  | 

### Return type

[**LiveSource**](LiveSource.md)

### Authorization

[oAuth2ClientCredentials](../README.md#oAuth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_feeds_from_column**
> create_feeds_from_column(document_id=document_id, column_key=column_key)

create live source feeds from column of a spreadsheet containing URLs

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
api_instance = layar_api.LiveSourceApi(layar_api.ApiClient(configuration))
document_id = 'document_id_example' # str |  (optional)
column_key = 'column_key_example' # str |  (optional)

try:
    # create live source feeds from column of a spreadsheet containing URLs
    api_instance.create_feeds_from_column(document_id=document_id, column_key=column_key)
except ApiException as e:
    print("Exception when calling LiveSourceApi->create_feeds_from_column: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **document_id** | **str**|  | [optional] 
 **column_key** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[oAuth2ClientCredentials](../README.md#oAuth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_feed**
> delete_feed(id)

Delete a live source

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
api_instance = layar_api.LiveSourceApi(layar_api.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Delete a live source
    api_instance.delete_feed(id)
except ApiException as e:
    print("Exception when calling LiveSourceApi->delete_feed: %s\n" % e)
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

# **delete_feeds**
> delete_feeds()

delete the set of live source ids

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
api_instance = layar_api.LiveSourceApi(layar_api.ApiClient(configuration))

try:
    # delete the set of live source ids
    api_instance.delete_feeds()
except ApiException as e:
    print("Exception when calling LiveSourceApi->delete_feeds: %s\n" % e)
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

# **get_feed**
> LiveSource get_feed(id)

Get live source details

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
api_instance = layar_api.LiveSourceApi(layar_api.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Get live source details
    api_response = api_instance.get_feed(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LiveSourceApi->get_feed: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**LiveSource**](LiveSource.md)

### Authorization

[oAuth2ClientCredentials](../README.md#oAuth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_import_status**
> LiveSourceImportStatus get_import_status(id)

Returns the percent completed for a live source import

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
api_instance = layar_api.LiveSourceApi(layar_api.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Returns the percent completed for a live source import
    api_response = api_instance.get_import_status(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LiveSourceApi->get_import_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**LiveSourceImportStatus**](LiveSourceImportStatus.md)

### Authorization

[oAuth2ClientCredentials](../README.md#oAuth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_job_status**
> LiveSourceJobStatus get_job_status(id)

Get job status details

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
api_instance = layar_api.LiveSourceApi(layar_api.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Get job status details
    api_response = api_instance.get_job_status(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LiveSourceApi->get_job_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**LiveSourceJobStatus**](LiveSourceJobStatus.md)

### Authorization

[oAuth2ClientCredentials](../README.md#oAuth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_source_document_url**
> list[SourceDocument] get_source_document_url(id, rows=rows, start=start)

Get the documents from a particular source

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
api_instance = layar_api.LiveSourceApi(layar_api.ApiClient(configuration))
id = 'id_example' # str | 
rows = 56 # int | the number of rows to return (optional)
start = 56 # int | the start offset for the row (optional)

try:
    # Get the documents from a particular source
    api_response = api_instance.get_source_document_url(id, rows=rows, start=start)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LiveSourceApi->get_source_document_url: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **rows** | **int**| the number of rows to return | [optional] 
 **start** | **int**| the start offset for the row | [optional] 

### Return type

[**list[SourceDocument]**](SourceDocument.md)

### Authorization

[oAuth2ClientCredentials](../README.md#oAuth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_feeds**
> list[LiveSource] search_feeds(start=start, rows=rows, q=q, sort=sort, order=order)

Search for live sources

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
api_instance = layar_api.LiveSourceApi(layar_api.ApiClient(configuration))
start = 56 # int | the start offset for the row (optional)
rows = 56 # int | the number of rows to return (optional)
q = 'q_example' # str | the query string to search for (optional)
sort = 'sort_example' # str | sort results by the given property (optional)
order = 'order_example' # str | what order to return sorted results (optional)

try:
    # Search for live sources
    api_response = api_instance.search_feeds(start=start, rows=rows, q=q, sort=sort, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LiveSourceApi->search_feeds: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start** | **int**| the start offset for the row | [optional] 
 **rows** | **int**| the number of rows to return | [optional] 
 **q** | **str**| the query string to search for | [optional] 
 **sort** | **str**| sort results by the given property | [optional] 
 **order** | **str**| what order to return sorted results | [optional] 

### Return type

[**list[LiveSource]**](LiveSource.md)

### Authorization

[oAuth2ClientCredentials](../README.md#oAuth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unschedule_job**
> LiveSourceJobStatus unschedule_job(id)

Change a job status to 'Unscheduled'

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
api_instance = layar_api.LiveSourceApi(layar_api.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Change a job status to 'Unscheduled'
    api_response = api_instance.unschedule_job(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LiveSourceApi->unschedule_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**LiveSourceJobStatus**](LiveSourceJobStatus.md)

### Authorization

[oAuth2ClientCredentials](../README.md#oAuth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_feed**
> LiveSource update_feed(body, id)

Update a live source

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
api_instance = layar_api.LiveSourceApi(layar_api.ApiClient(configuration))
body = layar_api.LiveSource() # LiveSource | 
id = 'id_example' # str | 

try:
    # Update a live source
    api_response = api_instance.update_feed(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LiveSourceApi->update_feed: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LiveSource**](LiveSource.md)|  | 
 **id** | **str**|  | 

### Return type

[**LiveSource**](LiveSource.md)

### Authorization

[oAuth2ClientCredentials](../README.md#oAuth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_job**
> LiveSourceJobStatus update_job(id, job_action)

Update a job with a new action

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
api_instance = layar_api.LiveSourceApi(layar_api.ApiClient(configuration))
id = 'id_example' # str | 
job_action = 'job_action_example' # str | 

try:
    # Update a job with a new action
    api_response = api_instance.update_job(id, job_action)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LiveSourceApi->update_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **job_action** | **str**|  | 

### Return type

[**LiveSourceJobStatus**](LiveSourceJobStatus.md)

### Authorization

[oAuth2ClientCredentials](../README.md#oAuth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

