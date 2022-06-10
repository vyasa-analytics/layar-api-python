# layar_api.ConnectorApi

All URIs are relative to *BASE_PATH*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_connector**](ConnectorApi.md#create_connector) | **POST** /connector | Add a new Layar connector
[**delete_connector**](ConnectorApi.md#delete_connector) | **DELETE** /connector/{id} | Delete a single Layar connector
[**delete_connectors**](ConnectorApi.md#delete_connectors) | **DELETE** /connector/deleteMany | delete all the records with the given IDs
[**get_connector**](ConnectorApi.md#get_connector) | **GET** /connector/{id} | Get the details for a single Layar connector
[**patch_connector**](ConnectorApi.md#patch_connector) | **PATCH** /connector/{id} | patch
[**search_connectors**](ConnectorApi.md#search_connectors) | **GET** /connector | Get the details for a given Layar connector
[**update_connector**](ConnectorApi.md#update_connector) | **PUT** /connector/{id} | Update the details for a single Layar connector

# **create_connector**
> list[Connector] create_connector(body)

Add a new Layar connector

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
api_instance = layar_api.ConnectorApi(layar_api.ApiClient(configuration))
body = layar_api.Connector() # Connector | 

try:
    # Add a new Layar connector
    api_response = api_instance.create_connector(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConnectorApi->create_connector: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Connector**](Connector.md)|  | 

### Return type

[**list[Connector]**](Connector.md)

### Authorization

[oAuth2ClientCredentials](../README.md#oAuth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_connector**
> delete_connector(id)

Delete a single Layar connector

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
api_instance = layar_api.ConnectorApi(layar_api.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Delete a single Layar connector
    api_instance.delete_connector(id)
except ApiException as e:
    print("Exception when calling ConnectorApi->delete_connector: %s\n" % e)
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

# **delete_connectors**
> delete_connectors()

delete all the records with the given IDs

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
api_instance = layar_api.ConnectorApi(layar_api.ApiClient(configuration))

try:
    # delete all the records with the given IDs
    api_instance.delete_connectors()
except ApiException as e:
    print("Exception when calling ConnectorApi->delete_connectors: %s\n" % e)
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

# **get_connector**
> Connector get_connector(id)

Get the details for a single Layar connector

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
api_instance = layar_api.ConnectorApi(layar_api.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Get the details for a single Layar connector
    api_response = api_instance.get_connector(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConnectorApi->get_connector: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**Connector**](Connector.md)

### Authorization

[oAuth2ClientCredentials](../README.md#oAuth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_connector**
> patch_connector(body, id)

patch

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
api_instance = layar_api.ConnectorApi(layar_api.ApiClient(configuration))
body = layar_api.PatchCommand() # PatchCommand | 
id = 'id_example' # str | 

try:
    # patch
    api_instance.patch_connector(body, id)
except ApiException as e:
    print("Exception when calling ConnectorApi->patch_connector: %s\n" % e)
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

# **search_connectors**
> list[Connector] search_connectors()

Get the details for a given Layar connector

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
api_instance = layar_api.ConnectorApi(layar_api.ApiClient(configuration))

try:
    # Get the details for a given Layar connector
    api_response = api_instance.search_connectors()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConnectorApi->search_connectors: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Connector]**](Connector.md)

### Authorization

[oAuth2ClientCredentials](../README.md#oAuth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_connector**
> list[Connector] update_connector(body, id)

Update the details for a single Layar connector

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
api_instance = layar_api.ConnectorApi(layar_api.ApiClient(configuration))
body = layar_api.Connector() # Connector | 
id = 'id_example' # str | 

try:
    # Update the details for a single Layar connector
    api_response = api_instance.update_connector(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConnectorApi->update_connector: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Connector**](Connector.md)|  | 
 **id** | **str**|  | 

### Return type

[**list[Connector]**](Connector.md)

### Authorization

[oAuth2ClientCredentials](../README.md#oAuth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

