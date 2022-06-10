# layar_api.VectorSimilarityApi

All URIs are relative to *BASE_PATH*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_vector_similarity**](VectorSimilarityApi.md#create_vector_similarity) | **POST** /vectorSimilarity | save
[**get_similar_statements**](VectorSimilarityApi.md#get_similar_statements) | **GET** /vectorSimilarity/{similarityRequestId}/statements | similarStatements
[**get_vector_similarity**](VectorSimilarityApi.md#get_vector_similarity) | **GET** /vectorSimilarity/{id} | vector similarity details
[**get_vectors_by_query_string**](VectorSimilarityApi.md#get_vectors_by_query_string) | **GET** /vectorSimilarity/byQueryString | byQueryString

# **create_vector_similarity**
> VectorSimilarityRequest create_vector_similarity(body)

save

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
api_instance = layar_api.VectorSimilarityApi(layar_api.ApiClient(configuration))
body = layar_api.VectorSimilarityRequest() # VectorSimilarityRequest | 

try:
    # save
    api_response = api_instance.create_vector_similarity(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VectorSimilarityApi->create_vector_similarity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**VectorSimilarityRequest**](VectorSimilarityRequest.md)|  | 

### Return type

[**VectorSimilarityRequest**](VectorSimilarityRequest.md)

### Authorization

[oAuth2ClientCredentials](../README.md#oAuth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_similar_statements**
> list[Statement] get_similar_statements(similarity_request_id)

similarStatements

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
api_instance = layar_api.VectorSimilarityApi(layar_api.ApiClient(configuration))
similarity_request_id = 'similarity_request_id_example' # str | 

try:
    # similarStatements
    api_response = api_instance.get_similar_statements(similarity_request_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VectorSimilarityApi->get_similar_statements: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **similarity_request_id** | **str**|  | 

### Return type

[**list[Statement]**](Statement.md)

### Authorization

[oAuth2ClientCredentials](../README.md#oAuth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_vector_similarity**
> VectorSimilarityRequest get_vector_similarity(id)

vector similarity details

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
api_instance = layar_api.VectorSimilarityApi(layar_api.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # vector similarity details
    api_response = api_instance.get_vector_similarity(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VectorSimilarityApi->get_vector_similarity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**VectorSimilarityRequest**](VectorSimilarityRequest.md)

### Authorization

[oAuth2ClientCredentials](../README.md#oAuth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_vectors_by_query_string**
> VectorSimilarityRequest get_vectors_by_query_string(q=q)

byQueryString

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
api_instance = layar_api.VectorSimilarityApi(layar_api.ApiClient(configuration))
q = 'q_example' # str | the query string to search for (optional)

try:
    # byQueryString
    api_response = api_instance.get_vectors_by_query_string(q=q)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VectorSimilarityApi->get_vectors_by_query_string: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **str**| the query string to search for | [optional] 

### Return type

[**VectorSimilarityRequest**](VectorSimilarityRequest.md)

### Authorization

[oAuth2ClientCredentials](../README.md#oAuth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

