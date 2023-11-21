# layar_api.GptApi

All URIs are relative to *BASE_PATH*

Method | HTTP request | Description
------------- | ------------- | -------------
[**generate**](GptApi.md#generate) | **POST** /layar/gpt/generate | Call Vyasa LLM to generate a system message and return the corresponding sources used

# **generate**
> InlineResponse2001 generate(body)

Call Vyasa LLM to generate a system message and return the corresponding sources used

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
api_instance = layar_api.GptApi(layar_api.ApiClient(configuration))
body = layar_api.GptGenerateCommand() # GptGenerateCommand | 

try:
    # Call Vyasa LLM to generate a system message and return the corresponding sources used
    api_response = api_instance.generate(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GptApi->generate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GptGenerateCommand**](GptGenerateCommand.md)|  | 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[oAuth2ClientCredentials](../README.md#oAuth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

