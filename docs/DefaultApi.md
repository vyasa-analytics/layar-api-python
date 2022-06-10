# layar_api.DefaultApi

All URIs are relative to *BASE_PATH*

Method | HTTP request | Description
------------- | ------------- | -------------
[**search_paragraph**](DefaultApi.md#search_paragraph) | **POST** /paragraph/search | 
[**search_term**](DefaultApi.md#search_term) | **POST** /ontologyTerm/search | 

# **search_paragraph**
> list[Paragraph] search_paragraph(body=body)



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
api_instance = layar_api.DefaultApi(layar_api.ApiClient(configuration))
body = layar_api.ParagraphSearchCommand() # ParagraphSearchCommand |  (optional)

try:
    api_response = api_instance.search_paragraph(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->search_paragraph: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ParagraphSearchCommand**](ParagraphSearchCommand.md)|  | [optional] 

### Return type

[**list[Paragraph]**](Paragraph.md)

### Authorization

[oAuth2ClientCredentials](../README.md#oAuth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_term**
> list[OntologyTerm] search_term(body=body)



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
api_instance = layar_api.DefaultApi(layar_api.ApiClient(configuration))
body = layar_api.OntologySearchCommand() # OntologySearchCommand |  (optional)

try:
    api_response = api_instance.search_term(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->search_term: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**OntologySearchCommand**](OntologySearchCommand.md)|  | [optional] 

### Return type

[**list[OntologyTerm]**](OntologyTerm.md)

### Authorization

[oAuth2ClientCredentials](../README.md#oAuth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

