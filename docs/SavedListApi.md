# layar_api.SavedListApi

All URIs are relative to *BASE_PATH*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_items**](SavedListApi.md#add_items) | **PUT** /savedList/{id}/addItem | Add items to a saved list
[**add_items_by_search**](SavedListApi.md#add_items_by_search) | **PUT** /savedList/{id}/add | Add items to a saved list from a search
[**create_saved_list**](SavedListApi.md#create_saved_list) | **POST** /savedList | Create a new saved list
[**delete_saved_list**](SavedListApi.md#delete_saved_list) | **DELETE** /savedList/{id} | Delete a saved list
[**delete_saved_lists**](SavedListApi.md#delete_saved_lists) | **DELETE** /savedList/deleteMany | delete all the given ids
[**download_saved_list**](SavedListApi.md#download_saved_list) | **GET** /savedList/{id}/downloadCsv | Download the contents of a savedc list as a csv file
[**get_saved_list**](SavedListApi.md#get_saved_list) | **GET** /savedList/{id} | saved list details
[**remove_items**](SavedListApi.md#remove_items) | **DELETE** /savedList/{id}/removeItem | Remove items from a saved list
[**search_saved_list**](SavedListApi.md#search_saved_list) | **GET** /savedList | Search for saved lists
[**update_saved_list**](SavedListApi.md#update_saved_list) | **PUT** /savedList/{id} | Update a saved list

# **add_items**
> add_items(body, id, x_vyasa_data_providers=x_vyasa_data_providers)

Add items to a saved list

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
    # Add items to a saved list
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

Add items to a saved list from a search

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
    # Add items to a saved list from a search
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

Create a new saved list

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
x_vyasa_client_hint = 'x_vyasa_client_hint_example' # str | intended client application UI (optional)

try:
    # Create a new saved list
    api_response = api_instance.create_saved_list(body, x_vyasa_client_hint=x_vyasa_client_hint)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SavedListApi->create_saved_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SavedList**](SavedList.md)|  | 
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

Delete a saved list

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
    # Delete a saved list
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

delete all the given ids

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
    # delete all the given ids
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

Download the contents of a savedc list as a csv file

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
    # Download the contents of a savedc list as a csv file
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

saved list details

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
    # saved list details
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

Remove items from a saved list

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
    # Remove items from a saved list
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

Search for saved lists

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
    # Search for saved lists
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

Update a saved list

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
    # Update a saved list
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

