# swagger_client.ChildApi

All URIs are relative to *https://apidev.riroschool.kr*

Method | HTTP request | Description
------------- | ------------- | -------------
[**child_delete**](ChildApi.md#child_delete) | **DELETE** /api/v2/child | 자녀 등록 해제
[**child_get**](ChildApi.md#child_get) | **GET** /api/v2/child | 자녀 목록
[**child_post**](ChildApi.md#child_post) | **POST** /api/v2/child | 자녀 인증
[**child_put**](ChildApi.md#child_put) | **PUT** /api/v2/child | 자녀 등록

# **child_delete**
> child_delete(client_id, authorization, site_id, name, snum)

자녀 등록 해제

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ChildApi()
client_id = 'client_id_example' # str | API Key
authorization = 'authorization_example' # str | 토큰 : tokenType + ' ' + token
site_id = 'site_id_example' # str | 학교 아이디
name = 'name_example' # str | 자녀 이름
snum = 'snum_example' # str | 자녀 학번

try:
    # 자녀 등록 해제
    api_instance.child_delete(client_id, authorization, site_id, name, snum)
except ApiException as e:
    print("Exception when calling ChildApi->child_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**| API Key | 
 **authorization** | **str**| 토큰 : tokenType + &#x27; &#x27; + token | 
 **site_id** | **str**| 학교 아이디 | 
 **name** | **str**| 자녀 이름 | 
 **snum** | **str**| 자녀 학번 | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **child_get**
> child_get(client_id, authorization)

자녀 목록

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ChildApi()
client_id = 'client_id_example' # str | API Key
authorization = 'authorization_example' # str | 토큰 : tokenType + ' ' + token

try:
    # 자녀 목록
    api_instance.child_get(client_id, authorization)
except ApiException as e:
    print("Exception when calling ChildApi->child_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**| API Key | 
 **authorization** | **str**| 토큰 : tokenType + &#x27; &#x27; + token | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **child_post**
> child_post(client_id, body=body)

자녀 인증

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ChildApi()
client_id = 'client_id_example' # str | API Key
body = swagger_client.Child() # Child | 학생정보 (optional)

try:
    # 자녀 인증
    api_instance.child_post(client_id, body=body)
except ApiException as e:
    print("Exception when calling ChildApi->child_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**| API Key | 
 **body** | [**Child**](Child.md)| 학생정보 | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **child_put**
> child_put(authorization, client_id, body=body)

자녀 등록

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ChildApi()
authorization = 'authorization_example' # str | 토큰 : tokenType + ' ' + token
client_id = 'client_id_example' # str | API Key
body = swagger_client.Child() # Child | 학생정보 (optional)

try:
    # 자녀 등록
    api_instance.child_put(authorization, client_id, body=body)
except ApiException as e:
    print("Exception when calling ChildApi->child_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| 토큰 : tokenType + &#x27; &#x27; + token | 
 **client_id** | **str**| API Key | 
 **body** | [**Child**](Child.md)| 학생정보 | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

