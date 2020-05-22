# swagger_client.MessageApi

All URIs are relative to *https://apidev.riroschool.kr*

Method | HTTP request | Description
------------- | ------------- | -------------
[**message_badge_get**](MessageApi.md#message_badge_get) | **GET** /api/v2/badge | 뱃지 가져오기
[**message_message_delete**](MessageApi.md#message_message_delete) | **DELETE** /api/v2/message | 메시지 삭제하기
[**message_message_get**](MessageApi.md#message_message_get) | **GET** /api/v2/message | 메시지 가져오기
[**message_read_get**](MessageApi.md#message_read_get) | **GET** /api/v2/message/read | 메시지 읽음 표시

# **message_badge_get**
> message_badge_get(authorization, client_id, cookie_token, fcm_code)

뱃지 가져오기

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MessageApi()
authorization = 'authorization_example' # str | 토큰 : tokenType + ' ' + token
client_id = 'client_id_example' # str | API Key
cookie_token = 'cookie_token_example' # str | API Key
fcm_code = 'fcm_code_example' # str | API Key

try:
    # 뱃지 가져오기
    api_instance.message_badge_get(authorization, client_id, cookie_token, fcm_code)
except ApiException as e:
    print("Exception when calling MessageApi->message_badge_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| 토큰 : tokenType + &#x27; &#x27; + token | 
 **client_id** | **str**| API Key | 
 **cookie_token** | **str**| API Key | 
 **fcm_code** | **str**| API Key | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **message_message_delete**
> message_message_delete(authorization, client_id, cookie_token, uid)

메시지 삭제하기

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MessageApi()
authorization = 'authorization_example' # str | 토큰 : tokenType + ' ' + token
client_id = 'client_id_example' # str | API Key
cookie_token = 'cookie_token_example' # str | API Key
uid = 'uid_example' # str | Message Uid

try:
    # 메시지 삭제하기
    api_instance.message_message_delete(authorization, client_id, cookie_token, uid)
except ApiException as e:
    print("Exception when calling MessageApi->message_message_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| 토큰 : tokenType + &#x27; &#x27; + token | 
 **client_id** | **str**| API Key | 
 **cookie_token** | **str**| API Key | 
 **uid** | **str**| Message Uid | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **message_message_get**
> message_message_get(authorization, client_id, cookie_token)

메시지 가져오기

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MessageApi()
authorization = 'authorization_example' # str | 토큰 : tokenType + ' ' + token
client_id = 'client_id_example' # str | API Key
cookie_token = 'cookie_token_example' # str | API Key

try:
    # 메시지 가져오기
    api_instance.message_message_get(authorization, client_id, cookie_token)
except ApiException as e:
    print("Exception when calling MessageApi->message_message_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| 토큰 : tokenType + &#x27; &#x27; + token | 
 **client_id** | **str**| API Key | 
 **cookie_token** | **str**| API Key | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **message_read_get**
> message_read_get(authorization, client_id, cookie_token, num)

메시지 읽음 표시

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MessageApi()
authorization = 'authorization_example' # str | 토큰 : tokenType + ' ' + token
client_id = 'client_id_example' # str | API Key
cookie_token = 'cookie_token_example' # str | API Key
num = 'num_example' # str | message num

try:
    # 메시지 읽음 표시
    api_instance.message_read_get(authorization, client_id, cookie_token, num)
except ApiException as e:
    print("Exception when calling MessageApi->message_read_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| 토큰 : tokenType + &#x27; &#x27; + token | 
 **client_id** | **str**| API Key | 
 **cookie_token** | **str**| API Key | 
 **num** | **str**| message num | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

