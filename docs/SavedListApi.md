# layar_api.SavedListApi

All URIs are relative to *BASE_PATH*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_items**](SavedListApi.md#add_items) | **PUT** /layar/savedList/{id}/addItem | Add items to a set
[**add_items_by_search**](SavedListApi.md#add_items_by_search) | **PUT** /layar/savedList/{id}/add | Add items to a set
[**create_saved_list**](SavedListApi.md#create_saved_list) | **POST** /layar/savedList | Create a new set
[**delete_saved_list**](SavedListApi.md#delete_saved_list) | **DELETE** /layar/savedList/{id} | Delete a set
[**delete_saved_lists**](SavedListApi.md#delete_saved_lists) | **DELETE** /layar/savedList/deleteMany | Delete multiple sets
[**download_saved_list**](SavedListApi.md#download_saved_list) | **GET** /layar/savedList/{id}/downloadCsv | Download set contents to a CSV
[**get_saved_list**](SavedListApi.md#get_saved_list) | **GET** /layar/savedList/{id} | Get set details
[**remove_items**](SavedListApi.md#remove_items) | **DELETE** /layar/savedList/{id}/removeItem | Remove items from a Layar set
[**search_saved_list**](SavedListApi.md#search_saved_list) | **GET** /layar/savedList | Search for sets
[**update_saved_list**](SavedListApi.md#update_saved_list) | **PUT** /layar/savedList/{id} | Update set details

# **add_items**
> add_items(body, id, x_vyasa_data_providers=x_vyasa_data_providers)

Add items to a set

Modify the items added to a specific Layar Set.

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
api_instance = layar_api.SavedListApi(layar_api.ApiClient(configuration))
body = layar_api.ListOfItemIds() # ListOfItemIds | 
id = 'id_example' # str | 
x_vyasa_data_providers = 'x_vyasa_data_providers_example' # str | remote data providers to query (optional)

try:
    # Add items to a set
    api_instance.add_items(body, id, x_vyasa_data_providers=x_vyasa_data_providers)
except ApiException as e:
    print("Exception when calling SavedListApi->add_items: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ListOfItemIds**](ListOfItemIds.md)|  | 
 **id** | **str**|  | 
 **x_vyasa_data_providers** | **str**| remote data providers to query | [optional] 

### Return type

void (empty response body)

### Authorization

[oAuth2ClientCredentials](../README.md#oAuth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_items_by_search**
> add_items_by_search(body, id, x_vyasa_data_providers=x_vyasa_data_providers)

Add items to a set

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
api_instance = layar_api.SavedListApi(layar_api.ApiClient(configuration))
body = layar_api.DistributedSourceDocumentSearchCommand() # DistributedSourceDocumentSearchCommand | 
id = 'id_example' # str | 
x_vyasa_data_providers = 'x_vyasa_data_providers_example' # str | remote data providers to query (optional)

try:
    # Add items to a set
    api_instance.add_items_by_search(body, id, x_vyasa_data_providers=x_vyasa_data_providers)
except ApiException as e:
    print("Exception when calling SavedListApi->add_items_by_search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DistributedSourceDocumentSearchCommand**](DistributedSourceDocumentSearchCommand.md)|  | 
 **id** | **str**|  | 
 **x_vyasa_data_providers** | **str**| remote data providers to query | [optional] 

### Return type

void (empty response body)

### Authorization

[oAuth2ClientCredentials](../README.md#oAuth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_saved_list**
> SavedList create_saved_list(body, x_vyasa_client_hint=x_vyasa_client_hint)

Create a new set

Create a new Layar Set.

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
api_instance = layar_api.SavedListApi(layar_api.ApiClient(configuration))
body = layar_api.SavedList1() # SavedList1 | 
x_vyasa_client_hint = 'x_vyasa_client_hint_example' # str | intended client application UI (optional)

try:
    # Create a new set
    api_response = api_instance.create_saved_list(body, x_vyasa_client_hint=x_vyasa_client_hint)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SavedListApi->create_saved_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SavedList1**](SavedList1.md)|  | 
 **x_vyasa_client_hint** | **str**| intended client application UI | [optional] 

### Return type

[**SavedList**](SavedList.md)

### Authorization

[oAuth2ClientCredentials](../README.md#oAuth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_saved_list**
> delete_saved_list(id)

Delete a set

Remove a specified Set object from your Layar instance.

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
api_instance = layar_api.SavedListApi(layar_api.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Delete a set
    api_instance.delete_saved_list(id)
except ApiException as e:
    print("Exception when calling SavedListApi->delete_saved_list: %s\n" % e)
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

# **delete_saved_lists**
> delete_saved_lists()

Delete multiple sets

Remove the list of specified Set objects by their set IDs.

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
api_instance = layar_api.SavedListApi(layar_api.ApiClient(configuration))

try:
    # Delete multiple sets
    api_instance.delete_saved_lists()
except ApiException as e:
    print("Exception when calling SavedListApi->delete_saved_lists: %s\n" % e)
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

# **download_saved_list**
> str download_saved_list(id)

Download set contents to a CSV

Download the items within a Layar set to a CSV file.

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
api_instance = layar_api.SavedListApi(layar_api.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Download set contents to a CSV
    api_response = api_instance.download_saved_list(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SavedListApi->download_saved_list: %s\n" % e)
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

# **get_saved_list**
> SavedList get_saved_list(id)

Get set details

Get information provided in a specific Set object.

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
api_instance = layar_api.SavedListApi(layar_api.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Get set details
    api_response = api_instance.get_saved_list(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SavedListApi->get_saved_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**SavedList**](SavedList.md)

### Authorization

[oAuth2ClientCredentials](../README.md#oAuth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_items**
> remove_items(id)

Remove items from a Layar set

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
api_instance = layar_api.SavedListApi(layar_api.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Remove items from a Layar set
    api_instance.remove_items(id)
except ApiException as e:
    print("Exception when calling SavedListApi->remove_items: %s\n" % e)
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

# **search_saved_list**
> list[SavedList] search_saved_list(rows=rows, start=start, q=q)

Search for sets

Find a set by their ID or other object parameters.

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
api_instance = layar_api.SavedListApi(layar_api.ApiClient(configuration))
rows = 56 # int | the number of rows to return (optional)
start = 56 # int | the start offset for the row (optional)
q = 'q_example' # str | the query string to search for (optional)

try:
    # Search for sets
    api_response = api_instance.search_saved_list(rows=rows, start=start, q=q)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SavedListApi->search_saved_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rows** | **int**| the number of rows to return | [optional] 
 **start** | **int**| the start offset for the row | [optional] 
 **q** | **str**| the query string to search for | [optional] 

### Return type

[**list[SavedList]**](SavedList.md)

### Authorization

[oAuth2ClientCredentials](../README.md#oAuth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_saved_list**
> SavedList update_saved_list(body, id)

Update set details

Modify the information provided for a specific Set object.

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
api_instance = layar_api.SavedListApi(layar_api.ApiClient(configuration))
body = layar_api.SavedList() # SavedList | 
id = 'id_example' # str | 

try:
    # Update set details
    api_response = api_instance.update_saved_list(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SavedListApi->update_saved_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SavedList**](SavedList.md)|  | 
 **id** | **str**|  | 

### Return type

[**SavedList**](SavedList.md)

### Authorization

[oAuth2ClientCredentials](../README.md#oAuth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

