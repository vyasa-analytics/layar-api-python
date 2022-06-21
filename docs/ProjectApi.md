# layar_api.ProjectApi

All URIs are relative to *BASE_PATH*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_input**](ProjectApi.md#add_input) | **PUT** /layar/project/{id}/addInput | Add items to a project
[**create_project**](ProjectApi.md#create_project) | **POST** /layar/project | Create a new project
[**delete_project**](ProjectApi.md#delete_project) | **DELETE** /layar/project/{id} | Delete a project
[**delete_projects**](ProjectApi.md#delete_projects) | **DELETE** /layar/project/deleteMany | Delete multiple projects
[**download_results**](ProjectApi.md#download_results) | **GET** /layar/project/{id}/results/download | Download project results as zip file
[**get_project**](ProjectApi.md#get_project) | **GET** /layar/project/{id} | Get project details
[**get_results**](ProjectApi.md#get_results) | **GET** /layar/project/{id}/results | Get project results details
[**get_results_som**](ProjectApi.md#get_results_som) | **GET** /layar/project/{id}/results/som | Download project results as SOM
[**remove_input**](ProjectApi.md#remove_input) | **PUT** /layar/project/{id}/removeInput | Remove items from a project
[**run_project**](ProjectApi.md#run_project) | **POST** /layar/project/{id}/run | Run a new project
[**search_projects**](ProjectApi.md#search_projects) | **GET** /layar/project | Search for projects
[**update_project**](ProjectApi.md#update_project) | **PUT** /layar/project/{id} | Update project details

# **add_input**
> add_input(body, id)

Add items to a project

Modify the items added to a specific project ID.

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
api_instance = layar_api.ProjectApi(layar_api.ApiClient(configuration))
body = layar_api.ListOfSourceIds() # ListOfSourceIds | 
id = 'id_example' # str | 

try:
    # Add items to a project
    api_instance.add_input(body, id)
except ApiException as e:
    print("Exception when calling ProjectApi->add_input: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ListOfSourceIds**](ListOfSourceIds.md)|  | 
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[oAuth2ClientCredentials](../README.md#oAuth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_project**
> Project create_project(body)

Create a new project

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
api_instance = layar_api.ProjectApi(layar_api.ApiClient(configuration))
body = layar_api.Project() # Project | 

try:
    # Create a new project
    api_response = api_instance.create_project(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->create_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Project**](Project.md)|  | 

### Return type

[**Project**](Project.md)

### Authorization

[oAuth2ClientCredentials](../README.md#oAuth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_project**
> delete_project(id)

Delete a project

Remove a specified Project object from your Layar instance.

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
api_instance = layar_api.ProjectApi(layar_api.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Delete a project
    api_instance.delete_project(id)
except ApiException as e:
    print("Exception when calling ProjectApi->delete_project: %s\n" % e)
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

# **delete_projects**
> delete_projects()

Delete multiple projects

Remove the list of specified Project objects by their project IDs.

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
api_instance = layar_api.ProjectApi(layar_api.ApiClient(configuration))

try:
    # Delete multiple projects
    api_instance.delete_projects()
except ApiException as e:
    print("Exception when calling ProjectApi->delete_projects: %s\n" % e)
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

# **download_results**
> str download_results(id)

Download project results as zip file

Download all results for a given project into a compressed zip file.

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
api_instance = layar_api.ProjectApi(layar_api.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Download project results as zip file
    api_response = api_instance.download_results(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->download_results: %s\n" % e)
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

# **get_project**
> Project get_project(id)

Get project details

Get information provided in a specific Project object.

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
api_instance = layar_api.ProjectApi(layar_api.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Get project details
    api_response = api_instance.get_project(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->get_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**Project**](Project.md)

### Authorization

[oAuth2ClientCredentials](../README.md#oAuth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_results**
> list[ProjectComputation] get_results(id)

Get project results details

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
api_instance = layar_api.ProjectApi(layar_api.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Get project results details
    api_response = api_instance.get_results(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->get_results: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**list[ProjectComputation]**](ProjectComputation.md)

### Authorization

[oAuth2ClientCredentials](../README.md#oAuth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_results_som**
> object get_results_som(id)

Download project results as SOM

Download all results for a given project into a self organizing map (SOM)

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
api_instance = layar_api.ProjectApi(layar_api.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Download project results as SOM
    api_response = api_instance.get_results_som(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->get_results_som: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

**object**

### Authorization

[oAuth2ClientCredentials](../README.md#oAuth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_input**
> remove_input(body, id)

Remove items from a project

Modify the items added to a specific project ID.

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
api_instance = layar_api.ProjectApi(layar_api.ApiClient(configuration))
body = layar_api.ListOfSourceIds() # ListOfSourceIds | 
id = 'id_example' # str | 

try:
    # Remove items from a project
    api_instance.remove_input(body, id)
except ApiException as e:
    print("Exception when calling ProjectApi->remove_input: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ListOfSourceIds**](ListOfSourceIds.md)|  | 
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[oAuth2ClientCredentials](../README.md#oAuth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **run_project**
> ProjectComputation run_project(body, id)

Run a new project

Create and run a new project from the same command.

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
api_instance = layar_api.ProjectApi(layar_api.ApiClient(configuration))
body = layar_api.Body2() # Body2 | 
id = 'id_example' # str | 

try:
    # Run a new project
    api_response = api_instance.run_project(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->run_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body2**](Body2.md)|  | 
 **id** | **str**|  | 

### Return type

[**ProjectComputation**](ProjectComputation.md)

### Authorization

[oAuth2ClientCredentials](../README.md#oAuth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_projects**
> list[Project] search_projects(rows=rows, start=start, q=q)

Search for projects

Find projects by their ID or other object parameters.

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
api_instance = layar_api.ProjectApi(layar_api.ApiClient(configuration))
rows = 56 # int | the number of rows to return (optional)
start = 56 # int | the start offset for the row (optional)
q = 'q_example' # str | the query string to search for (optional)

try:
    # Search for projects
    api_response = api_instance.search_projects(rows=rows, start=start, q=q)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->search_projects: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rows** | **int**| the number of rows to return | [optional] 
 **start** | **int**| the start offset for the row | [optional] 
 **q** | **str**| the query string to search for | [optional] 

### Return type

[**list[Project]**](Project.md)

### Authorization

[oAuth2ClientCredentials](../README.md#oAuth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_project**
> Project update_project(body, id)

Update project details

Modify the information provided for a specific Project object.

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
api_instance = layar_api.ProjectApi(layar_api.ApiClient(configuration))
body = layar_api.Project() # Project | 
id = 'id_example' # str | 

try:
    # Update project details
    api_response = api_instance.update_project(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->update_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Project**](Project.md)|  | 
 **id** | **str**|  | 

### Return type

[**Project**](Project.md)

### Authorization

[oAuth2ClientCredentials](../README.md#oAuth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

