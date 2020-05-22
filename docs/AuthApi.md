# swagger_client.AuthApi

All URIs are relative to *https://apidev.riroschool.kr*

Method | HTTP request | Description
------------- | ------------- | -------------
[**auth_authorize_get**](AuthApi.md#auth_authorize_get) | **GET** /api/v2/auth/authorize | 인증코드 요청
[**auth_callback_post**](AuthApi.md#auth_callback_post) | **POST** /api/v2/callback | 본인 인증 Callback 페이지
[**auth_cancel_post**](AuthApi.md#auth_cancel_post) | **POST** /api/v2/cancel | 본인 인증 cancel 페이지
[**auth_info_get**](AuthApi.md#auth_info_get) | **GET** /api/v2/auth/info | 본인 인증
[**auth_login_get**](AuthApi.md#auth_login_get) | **GET** /api/v2/old/login | 업데이트 이전 사용자들 새 버전로그인으로 갈아타기
[**auth_me_get**](AuthApi.md#auth_me_get) | **GET** /api/v2/auth/me | 
[**auth_refesh_token_get**](AuthApi.md#auth_refesh_token_get) | **GET** /api/v2/auth/refresh-token | 토큰 재발급
[**auth_sign_out_get**](AuthApi.md#auth_sign_out_get) | **GET** /api/v2/auth/sign-out | 로그아웃
[**auth_token_get**](AuthApi.md#auth_token_get) | **GET** /api/v2/auth/token | 토큰 발급

# **auth_authorize_get**
> auth_authorize_get(client_id, id, password, site_id, parent=parent)

인증코드 요청

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AuthApi()
client_id = 'client_id_example' # str | API Key
id = 'id_example' # str | 사용자 아이디
password = 'password_example' # str | 사용자 비밀번호
site_id = 'site_id_example' # str | 학교 아이디
parent = 'parent_example' # str | 학부모구분 엄마:M, 아빠:F (optional)

try:
    # 인증코드 요청
    api_instance.auth_authorize_get(client_id, id, password, site_id, parent=parent)
except ApiException as e:
    print("Exception when calling AuthApi->auth_authorize_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**| API Key | 
 **id** | **str**| 사용자 아이디 | 
 **password** | **str**| 사용자 비밀번호 | 
 **site_id** | **str**| 학교 아이디 | 
 **parent** | **str**| 학부모구분 엄마:M, 아빠:F | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **auth_callback_post**
> auth_callback_post()

본인 인증 Callback 페이지

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AuthApi()

try:
    # 본인 인증 Callback 페이지
    api_instance.auth_callback_post()
except ApiException as e:
    print("Exception when calling AuthApi->auth_callback_post: %s\n" % e)
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

# **auth_cancel_post**
> auth_cancel_post()

본인 인증 cancel 페이지

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AuthApi()

try:
    # 본인 인증 cancel 페이지
    api_instance.auth_cancel_post()
except ApiException as e:
    print("Exception when calling AuthApi->auth_cancel_post: %s\n" % e)
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

# **auth_info_get**
> auth_info_get(client_id, tid, auth_info)

본인 인증

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AuthApi()
client_id = 'client_id_example' # str | API Key
tid = 'tid_example' # str | 본인인증에서 callback 받은 tid
auth_info = 'auth_info_example' # str | 본인인증에서 callback 받은 auth_info

try:
    # 본인 인증
    api_instance.auth_info_get(client_id, tid, auth_info)
except ApiException as e:
    print("Exception when calling AuthApi->auth_info_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**| API Key | 
 **tid** | **str**| 본인인증에서 callback 받은 tid | 
 **auth_info** | **str**| 본인인증에서 callback 받은 auth_info | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **auth_login_get**
> auth_login_get(client_id, cookie_token)

업데이트 이전 사용자들 새 버전로그인으로 갈아타기

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AuthApi()
client_id = 'client_id_example' # str | API Key
cookie_token = 'cookie_token_example' # str | API Key

try:
    # 업데이트 이전 사용자들 새 버전로그인으로 갈아타기
    api_instance.auth_login_get(client_id, cookie_token)
except ApiException as e:
    print("Exception when calling AuthApi->auth_login_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **auth_me_get**
> auth_me_get(client_id, site_id)



본인 인증 순서 1. /api/v2/auth/me 통신 후 response 값 중 mobile_url 값으로 페이지 이동 2. 본인인증 완료 후 url 감지하여 /api/v2/callback 이 페이지로 이동 되면 body 의 json 값을 GET 함 (위 페이지는 노출 되지 않게 가리는것이 좋음) 3. /api/v2/auth/info 통신으로 본인인증한 정보를 받아 온다. 4. 받아온 정보를 이용하여 회원가입을 진행한다.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AuthApi()
client_id = 'client_id_example' # str | API Key
site_id = 'site_id_example' # str | 학교 아이디

try:
    api_instance.auth_me_get(client_id, site_id)
except ApiException as e:
    print("Exception when calling AuthApi->auth_me_get: %s\n" % e)
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

# **auth_refesh_token_get**
> auth_refesh_token_get(client_id, authorization)

토큰 재발급

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AuthApi()
client_id = 'client_id_example' # str | API Key
authorization = 'authorization_example' # str | 토큰 : tokenType + ' ' + refreshToken

try:
    # 토큰 재발급
    api_instance.auth_refesh_token_get(client_id, authorization)
except ApiException as e:
    print("Exception when calling AuthApi->auth_refesh_token_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**| API Key | 
 **authorization** | **str**| 토큰 : tokenType + &#x27; &#x27; + refreshToken | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **auth_sign_out_get**
> auth_sign_out_get(client_id, authorization_code)

로그아웃

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AuthApi()
client_id = 'client_id_example' # str | API Key
authorization_code = 'authorization_code_example' # str | 인증 코드

try:
    # 로그아웃
    api_instance.auth_sign_out_get(client_id, authorization_code)
except ApiException as e:
    print("Exception when calling AuthApi->auth_sign_out_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**| API Key | 
 **authorization_code** | **str**| 인증 코드 | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **auth_token_get**
> auth_token_get(client_id, authorization_code)

토큰 발급

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AuthApi()
client_id = 'client_id_example' # str | API Key
authorization_code = 'authorization_code_example' # str | 인증 코드

try:
    # 토큰 발급
    api_instance.auth_token_get(client_id, authorization_code)
except ApiException as e:
    print("Exception when calling AuthApi->auth_token_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**| API Key | 
 **authorization_code** | **str**| 인증 코드 | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

