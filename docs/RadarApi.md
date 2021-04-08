# layar_api.RadarApi

All URIs are relative to *BASE_PATH*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get**](RadarApi.md#get) | **GET** /radar | 
[**get_by_concept_id**](RadarApi.md#get_by_concept_id) | **GET** /radar/byConceptId | find semantically similar terms
[**get_by_query_string**](RadarApi.md#get_by_query_string) | **GET** /radar/byQueryString | find semantically similar terms
[**get_count**](RadarApi.md#get_count) | **GET** /radar/count | count of nearest neighbor terms that match the term in the query string

# **get**
> list[Radar] get(x_vyasa_data_providers, start=start, rows=rows, q=q, sort=sort, order=order, from_date=from_date, to_date=to_date, minimum_similarity=minimum_similarity, terms=terms, context_terms=context_terms, live_source_ids=live_source_ids, concept_type_ids=concept_type_ids, excludes=excludes)



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
api_instance = layar_api.RadarApi(layar_api.ApiClient(configuration))
x_vyasa_data_providers = 'x_vyasa_data_providers_example' # str | remote data providers to query
start = 56 # int | the start offset for the row (optional)
rows = 56 # int | the number of rows to return (optional)
q = 'q_example' # str | the query string to search for (optional)
sort = 'sort_example' # str | sort results by the given property (optional)
order = 'order_example' # str | what order to return sorted results (optional)
from_date = '2013-10-20' # date | beginning of date range to return (optional)
to_date = '2013-10-20' # date | end of date range to return (optional)
minimum_similarity = 3.4 # float | threshold for term similarity (optional)
terms = ['terms_example'] # list[str] | query terms (results will be similar to these terms) (optional)
context_terms = ['context_terms_example'] # list[str] |  (optional)
live_source_ids = ['live_source_ids_example'] # list[str] | limit results to those found in a specific live source (optional)
concept_type_ids = ['concept_type_ids_example'] # list[str] | limit results to those of a specific concept type (optional)
excludes = layar_api.RadarExcludeSearchCommand() # RadarExcludeSearchCommand | limit results to those without these properties (optional)

try:
    api_response = api_instance.get(x_vyasa_data_providers, start=start, rows=rows, q=q, sort=sort, order=order, from_date=from_date, to_date=to_date, minimum_similarity=minimum_similarity, terms=terms, context_terms=context_terms, live_source_ids=live_source_ids, concept_type_ids=concept_type_ids, excludes=excludes)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RadarApi->get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_vyasa_data_providers** | **str**| remote data providers to query | 
 **start** | **int**| the start offset for the row | [optional] 
 **rows** | **int**| the number of rows to return | [optional] 
 **q** | **str**| the query string to search for | [optional] 
 **sort** | **str**| sort results by the given property | [optional] 
 **order** | **str**| what order to return sorted results | [optional] 
 **from_date** | **date**| beginning of date range to return | [optional] 
 **to_date** | **date**| end of date range to return | [optional] 
 **minimum_similarity** | **float**| threshold for term similarity | [optional] 
 **terms** | [**list[str]**](str.md)| query terms (results will be similar to these terms) | [optional] 
 **context_terms** | [**list[str]**](str.md)|  | [optional] 
 **live_source_ids** | [**list[str]**](str.md)| limit results to those found in a specific live source | [optional] 
 **concept_type_ids** | [**list[str]**](str.md)| limit results to those of a specific concept type | [optional] 
 **excludes** | [**RadarExcludeSearchCommand**](.md)| limit results to those without these properties | [optional] 

### Return type

[**list[Radar]**](Radar.md)

### Authorization

[oAuth2ClientCredentials](../README.md#oAuth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_by_concept_id**
> list[Radar] get_by_concept_id(size=size, minimum_similarity=minimum_similarity, concept_id=concept_id, source=source)

find semantically similar terms

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
api_instance = layar_api.RadarApi(layar_api.ApiClient(configuration))
size = 56 # int | the number of rows to return (optional)
minimum_similarity = 3.4 # float |  (optional)
concept_id = 'concept_id_example' # str |  (optional)
source = 'source_example' # str |  (optional)

try:
    # find semantically similar terms
    api_response = api_instance.get_by_concept_id(size=size, minimum_similarity=minimum_similarity, concept_id=concept_id, source=source)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RadarApi->get_by_concept_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **size** | **int**| the number of rows to return | [optional] 
 **minimum_similarity** | **float**|  | [optional] 
 **concept_id** | **str**|  | [optional] 
 **source** | **str**|  | [optional] 

### Return type

[**list[Radar]**](Radar.md)

### Authorization

[oAuth2ClientCredentials](../README.md#oAuth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_by_query_string**
> list[Radar] get_by_query_string(x_vyasa_data_providers, q=q, size=size, minimum_similarity=minimum_similarity, source=source)

find semantically similar terms

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
api_instance = layar_api.RadarApi(layar_api.ApiClient(configuration))
x_vyasa_data_providers = 'x_vyasa_data_providers_example' # str | remote data providers to query
q = 'q_example' # str | the query string to search for (optional)
size = 56 # int | the number of rows to return (optional)
minimum_similarity = 3.4 # float |  (optional)
source = 'source_example' # str |  (optional)

try:
    # find semantically similar terms
    api_response = api_instance.get_by_query_string(x_vyasa_data_providers, q=q, size=size, minimum_similarity=minimum_similarity, source=source)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RadarApi->get_by_query_string: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_vyasa_data_providers** | **str**| remote data providers to query | 
 **q** | **str**| the query string to search for | [optional] 
 **size** | **int**| the number of rows to return | [optional] 
 **minimum_similarity** | **float**|  | [optional] 
 **source** | **str**|  | [optional] 

### Return type

[**list[Radar]**](Radar.md)

### Authorization

[oAuth2ClientCredentials](../README.md#oAuth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_count**
> InlineResponse2004 get_count(x_vyasa_data_providers, terms=terms)

count of nearest neighbor terms that match the term in the query string

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
api_instance = layar_api.RadarApi(layar_api.ApiClient(configuration))
x_vyasa_data_providers = 'x_vyasa_data_providers_example' # str | remote data providers to query
terms = 'terms_example' # str |  (optional)

try:
    # count of nearest neighbor terms that match the term in the query string
    api_response = api_instance.get_count(x_vyasa_data_providers, terms=terms)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RadarApi->get_count: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_vyasa_data_providers** | **str**| remote data providers to query | 
 **terms** | **str**|  | [optional] 

### Return type

[**InlineResponse2004**](InlineResponse2004.md)

### Authorization

[oAuth2ClientCredentials](../README.md#oAuth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

