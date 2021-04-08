# layar_api.SetAnalyticsApi

All URIs are relative to *BASE_PATH*

Method | HTTP request | Description
------------- | ------------- | -------------
[**download**](SetAnalyticsApi.md#download) | **GET** /set/analytics/download | download
[**get_concepts**](SetAnalyticsApi.md#get_concepts) | **POST** /set/analytics/concepts | concepts
[**get_concepts_tree**](SetAnalyticsApi.md#get_concepts_tree) | **POST** /set/analytics/concepts/tree | conceptTree
[**get_relationships**](SetAnalyticsApi.md#get_relationships) | **POST** /set/analytics/concepts/relationships | relationships
[**get_summary**](SetAnalyticsApi.md#get_summary) | **POST** /set/analytics/summary | summary

# **download**
> Concept download(body)

download

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
api_instance = layar_api.SetAnalyticsApi(layar_api.ApiClient(configuration))
body = layar_api.SetAnalyticsQuery() # SetAnalyticsQuery | 

try:
    # download
    api_response = api_instance.download(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SetAnalyticsApi->download: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SetAnalyticsQuery**](SetAnalyticsQuery.md)|  | 

### Return type

[**Concept**](Concept.md)

### Authorization

[oAuth2ClientCredentials](../README.md#oAuth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_concepts**
> list[Concept] get_concepts(body)

concepts

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
api_instance = layar_api.SetAnalyticsApi(layar_api.ApiClient(configuration))
body = layar_api.SetAnalyticsQuery() # SetAnalyticsQuery | 

try:
    # concepts
    api_response = api_instance.get_concepts(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SetAnalyticsApi->get_concepts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SetAnalyticsQuery**](SetAnalyticsQuery.md)|  | 

### Return type

[**list[Concept]**](Concept.md)

### Authorization

[oAuth2ClientCredentials](../README.md#oAuth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_concepts_tree**
> list[Concept] get_concepts_tree(body)

conceptTree

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
api_instance = layar_api.SetAnalyticsApi(layar_api.ApiClient(configuration))
body = layar_api.SetAnalyticsQuery() # SetAnalyticsQuery | 

try:
    # conceptTree
    api_response = api_instance.get_concepts_tree(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SetAnalyticsApi->get_concepts_tree: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SetAnalyticsQuery**](SetAnalyticsQuery.md)|  | 

### Return type

[**list[Concept]**](Concept.md)

### Authorization

[oAuth2ClientCredentials](../README.md#oAuth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_relationships**
> list[ConceptRelationship] get_relationships(body)

relationships

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
api_instance = layar_api.SetAnalyticsApi(layar_api.ApiClient(configuration))
body = layar_api.RelationshipQuery() # RelationshipQuery | 

try:
    # relationships
    api_response = api_instance.get_relationships(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SetAnalyticsApi->get_relationships: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RelationshipQuery**](RelationshipQuery.md)|  | 

### Return type

[**list[ConceptRelationship]**](ConceptRelationship.md)

### Authorization

[oAuth2ClientCredentials](../README.md#oAuth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_summary**
> SetAnalyticsSummary get_summary(body)

summary

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
api_instance = layar_api.SetAnalyticsApi(layar_api.ApiClient(configuration))
body = layar_api.RelationshipQuery() # RelationshipQuery | 

try:
    # summary
    api_response = api_instance.get_summary(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SetAnalyticsApi->get_summary: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RelationshipQuery**](RelationshipQuery.md)|  | 

### Return type

[**SetAnalyticsSummary**](SetAnalyticsSummary.md)

### Authorization

[oAuth2ClientCredentials](../README.md#oAuth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

