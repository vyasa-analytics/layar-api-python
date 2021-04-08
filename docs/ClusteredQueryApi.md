# layar_api.ClusteredQueryApi

All URIs are relative to *BASE_PATH*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create**](ClusteredQueryApi.md#create) | **POST** /clusteredQuery | create a new clustered query request
[**get**](ClusteredQueryApi.md#get) | **GET** /clusteredQuery/{id} | clustered query details
[**get_by_query_string**](ClusteredQueryApi.md#get_by_query_string) | **GET** /clusteredQuery/byQueryString | find clustered query by query string
[**get_clusters**](ClusteredQueryApi.md#get_clusters) | **GET** /clusteredQuery/{clusteredQueryId}/clusters | getClusters
[**update**](ClusteredQueryApi.md#update) | **PUT** /clusteredQuery/{id} | update

# **create**
> ClusteredQuery create(body)

create a new clustered query request

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
api_instance = layar_api.ClusteredQueryApi(layar_api.ApiClient(configuration))
body = layar_api.ClusteredQuery() # ClusteredQuery | 

try:
    # create a new clustered query request
    api_response = api_instance.create(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusteredQueryApi->create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ClusteredQuery**](ClusteredQuery.md)|  | 

### Return type

[**ClusteredQuery**](ClusteredQuery.md)

### Authorization

[oAuth2ClientCredentials](../README.md#oAuth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get**
> ClusteredQuery get(id)

clustered query details

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
api_instance = layar_api.ClusteredQueryApi(layar_api.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # clustered query details
    api_response = api_instance.get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusteredQueryApi->get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**ClusteredQuery**](ClusteredQuery.md)

### Authorization

[oAuth2ClientCredentials](../README.md#oAuth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_by_query_string**
> ClusteredQuery get_by_query_string(q=q, type=type)

find clustered query by query string

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
api_instance = layar_api.ClusteredQueryApi(layar_api.ApiClient(configuration))
q = 'q_example' # str |  (optional)
type = 'type_example' # str |  (optional)

try:
    # find clustered query by query string
    api_response = api_instance.get_by_query_string(q=q, type=type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusteredQueryApi->get_by_query_string: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **str**|  | [optional] 
 **type** | **str**|  | [optional] 

### Return type

[**ClusteredQuery**](ClusteredQuery.md)

### Authorization

[oAuth2ClientCredentials](../README.md#oAuth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_clusters**
> InlineResponse2001 get_clusters(clustered_query_id)

getClusters

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
api_instance = layar_api.ClusteredQueryApi(layar_api.ApiClient(configuration))
clustered_query_id = 'clustered_query_id_example' # str | 

try:
    # getClusters
    api_response = api_instance.get_clusters(clustered_query_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusteredQueryApi->get_clusters: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **clustered_query_id** | **str**|  | 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[oAuth2ClientCredentials](../README.md#oAuth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update**
> list[ClusteredQuery] update(body, id)

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
api_instance = layar_api.ClusteredQueryApi(layar_api.ApiClient(configuration))
body = layar_api.ClusteredQuery() # ClusteredQuery | 
id = 'id_example' # str | 

try:
    # update
    api_response = api_instance.update(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusteredQueryApi->update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ClusteredQuery**](ClusteredQuery.md)|  | 
 **id** | **str**|  | 

### Return type

[**list[ClusteredQuery]**](ClusteredQuery.md)

### Authorization

[oAuth2ClientCredentials](../README.md#oAuth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

