# swagger_client.SchoolApi

All URIs are relative to *https://apidev.riroschool.kr*

Method | HTTP request | Description
------------- | ------------- | -------------
[**check_get**](SchoolApi.md#check_get) | **GET** /api/v2/check | 상태 체크
[**health_check_get**](SchoolApi.md#health_check_get) | **GET** /api/v2/health-check | 상태 체크
[**school_get**](SchoolApi.md#school_get) | **GET** /api/v2/school | 리로스쿨 학교 리스트
[**school_menu_get**](SchoolApi.md#school_menu_get) | **GET** /api/v2/menu | 학교 사이드 메뉴
[**school_search_get**](SchoolApi.md#school_search_get) | **GET** /api/v2/school/{search} | 리로스쿨 학교 검색

# **check_get**
> check_get()

상태 체크

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SchoolApi()

try:
    # 상태 체크
    api_instance.check_get()
except ApiException as e:
    print("Exception when calling SchoolApi->check_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **health_check_get**
> health_check_get(client_id)

상태 체크

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SchoolApi()
client_id = 'client_id_example' # str | API Key

try:
    # 상태 체크
    api_instance.health_check_get(client_id)
except ApiException as e:
    print("Exception when calling SchoolApi->health_check_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**| API Key | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **school_get**
> school_get(client_id)

리로스쿨 학교 리스트

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SchoolApi()
client_id = 'client_id_example' # str | API Key

try:
    # 리로스쿨 학교 리스트
    api_instance.school_get(client_id)
except ApiException as e:
    print("Exception when calling SchoolApi->school_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**| API Key | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **school_menu_get**
> school_menu_get(client_id, site_id)

학교 사이드 메뉴

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SchoolApi()
client_id = 'client_id_example' # str | API Key
site_id = 'site_id_example' # str | 학교 아이디

try:
    # 학교 사이드 메뉴
    api_instance.school_menu_get(client_id, site_id)
except ApiException as e:
    print("Exception when calling SchoolApi->school_menu_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**| API Key | 
 **site_id** | **str**| 학교 아이디 | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **school_search_get**
> school_search_get(client_id, search)

리로스쿨 학교 검색

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SchoolApi()
client_id = 'client_id_example' # str | API Key
search = 'search_example' # str | 학교 검색어

try:
    # 리로스쿨 학교 검색
    api_instance.school_search_get(client_id, search)
except ApiException as e:
    print("Exception when calling SchoolApi->school_search_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**| API Key | 
 **search** | **str**| 학교 검색어 | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

