# layar_api.VectorSimilarityApi

All URIs are relative to *BASE_PATH*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_vector_similarity**](VectorSimilarityApi.md#create_vector_similarity) | **POST** /layar/vectorSimilarity | Create a new vector embedding
[**get_similar_statements**](VectorSimilarityApi.md#get_similar_statements) | **GET** /layar/vectorSimilarity/{similarityRequestId}/statements | Find similar statements by statement ID
[**get_vector_similarity**](VectorSimilarityApi.md#get_vector_similarity) | **GET** /layar/vectorSimilarity/{id} | Get vector details
[**get_vectors_by_query_string**](VectorSimilarityApi.md#get_vectors_by_query_string) | **GET** /layar/vectorSimilarity/byQueryString | Find similar embeddings by query string

# **create_vector_similarity**
> VectorSimilarityResponse create_vector_similarity(body)

Create a new vector embedding

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
    # Create a new vector embedding
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

[**VectorSimilarityResponse**](VectorSimilarityResponse.md)

### Authorization

[oAuth2ClientCredentials](../README.md#oAuth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_similar_statements**
> list[Statement] get_similar_statements(similarity_request_id)

Find similar statements by statement ID

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
    # Find similar statements by statement ID
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

Get vector details

Get information provided in a specific Vector Embedding object.

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
    # Get vector details
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

Find similar embeddings by query string

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
    # Find similar embeddings by query string
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

