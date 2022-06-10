# layar_api.SmilesApi

All URIs are relative to *BASE_PATH*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_tox_csv**](SmilesApi.md#create_tox_csv) | **POST** /smiles/createTox21CSV | Runs Tox21 toxicity analysis against list of smiles and returns the results in a CSV file.
[**create_tox_som**](SmilesApi.md#create_tox_som) | **POST** /smiles/createTox21SOM | Runs Tox21 toxicity analysis against list of smiles and returns the results in a Self Organizing Map (SOM)

# **create_tox_csv**
> create_tox_csv(body)

Runs Tox21 toxicity analysis against list of smiles and returns the results in a CSV file.

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
api_instance = layar_api.SmilesApi(layar_api.ApiClient(configuration))
body = layar_api.SOMRequest() # SOMRequest | 

try:
    # Runs Tox21 toxicity analysis against list of smiles and returns the results in a CSV file.
    api_instance.create_tox_csv(body)
except ApiException as e:
    print("Exception when calling SmilesApi->create_tox_csv: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SOMRequest**](SOMRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[oAuth2ClientCredentials](../README.md#oAuth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_tox_som**
> create_tox_som(body)

Runs Tox21 toxicity analysis against list of smiles and returns the results in a Self Organizing Map (SOM)

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
api_instance = layar_api.SmilesApi(layar_api.ApiClient(configuration))
body = layar_api.SOMRequest() # SOMRequest | 

try:
    # Runs Tox21 toxicity analysis against list of smiles and returns the results in a Self Organizing Map (SOM)
    api_instance.create_tox_som(body)
except ApiException as e:
    print("Exception when calling SmilesApi->create_tox_som: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SOMRequest**](SOMRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[oAuth2ClientCredentials](../README.md#oAuth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

