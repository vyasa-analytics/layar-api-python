# layar_api.CompoundApi

All URIs are relative to *BASE_PATH*

Method | HTTP request | Description
------------- | ------------- | -------------
[**render**](CompoundApi.md#render) | **GET** /compound/render | render

# **render**
> str render(smiles_string=smiles_string, height=height, width=width)

render

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
api_instance = layar_api.CompoundApi(layar_api.ApiClient(configuration))
smiles_string = 'smiles_string_example' # str | the SMILES string of the compound structure to render (optional)
height = 56 # int | the height in pixels of the rendered compound structure (optional)
width = 56 # int | the width in pixels of the rendered compound structure (optional)

try:
    # render
    api_response = api_instance.render(smiles_string=smiles_string, height=height, width=width)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CompoundApi->render: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **smiles_string** | **str**| the SMILES string of the compound structure to render | [optional] 
 **height** | **int**| the height in pixels of the rendered compound structure | [optional] 
 **width** | **int**| the width in pixels of the rendered compound structure | [optional] 

### Return type

**str**

### Authorization

[oAuth2ClientCredentials](../README.md#oAuth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: image/svg+xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

