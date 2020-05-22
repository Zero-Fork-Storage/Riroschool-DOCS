# swagger_client.MemberApi

All URIs are relative to *https://apidev.riroschool.kr*

Method | HTTP request | Description
------------- | ------------- | -------------
[**auth_sign_up_post**](MemberApi.md#auth_sign_up_post) | **POST** /api/v2/sign-up | 회원가입
[**member_change_password_get**](MemberApi.md#member_change_password_get) | **GET** /api/v2/change-password | 비밀번호 변경
[**member_check_id_get**](MemberApi.md#member_check_id_get) | **GET** /api/v2/check/{siteId}/{id} | 아이디 중복체크
[**member_confirm_password_get**](MemberApi.md#member_confirm_password_get) | **GET** /api/v2/confirm-password | 비밀번호 확인
[**member_find_id_get**](MemberApi.md#member_find_id_get) | **GET** /api/v2/find-id | 아이디 찾기
[**member_find_password_get**](MemberApi.md#member_find_password_get) | **GET** /api/v2/find-password | 비밀번호 찾기 / 처음에 인증번호 없이 보내면 알림톡으로 인증번호 발송됨 두번째는 인증번호와 함께 다시 전송.
[**member_info_get**](MemberApi.md#member_info_get) | **GET** /api/v2/info | 내정보 가져가기
[**member_info_put**](MemberApi.md#member_info_put) | **PUT** /api/v2/info | 내정보 수정하기
[**member_me_get**](MemberApi.md#member_me_get) | **PUT** /api/v2/me | 내 정보
[**member_phone_get**](MemberApi.md#member_phone_get) | **GET** /api/v2/phone | 전화번호 인증

# **auth_sign_up_post**
> auth_sign_up_post(body, client_id)

회원가입

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MemberApi()
body = swagger_client.Member() # Member | 회원정보
client_id = 'client_id_example' # str | API Key

try:
    # 회원가입
    api_instance.auth_sign_up_post(body, client_id)
except ApiException as e:
    print("Exception when calling MemberApi->auth_sign_up_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Member**](Member.md)| 회원정보 | 
 **client_id** | **str**| API Key | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **member_change_password_get**
> member_change_password_get(client_id, site_id, id, password, uuid)

비밀번호 변경

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MemberApi()
client_id = 'client_id_example' # str | API Key
site_id = 'site_id_example' # str | 학교 아이디
id = 'id_example' # str | 아이디
password = 'password_example' # str | 비밀번호
uuid = 'uuid_example' # str | 디바이스 고유번호 (비밀번호 생성시 사용)

try:
    # 비밀번호 변경
    api_instance.member_change_password_get(client_id, site_id, id, password, uuid)
except ApiException as e:
    print("Exception when calling MemberApi->member_change_password_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**| API Key | 
 **site_id** | **str**| 학교 아이디 | 
 **id** | **str**| 아이디 | 
 **password** | **str**| 비밀번호 | 
 **uuid** | **str**| 디바이스 고유번호 (비밀번호 생성시 사용) | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **member_check_id_get**
> member_check_id_get(client_id, site_id, id)

아이디 중복체크

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MemberApi()
client_id = 'client_id_example' # str | API Key
site_id = 'site_id_example' # str | 학교 아이디
id = 'id_example' # str | 중복체크 할 아이디

try:
    # 아이디 중복체크
    api_instance.member_check_id_get(client_id, site_id, id)
except ApiException as e:
    print("Exception when calling MemberApi->member_check_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**| API Key | 
 **site_id** | **str**| 학교 아이디 | 
 **id** | **str**| 중복체크 할 아이디 | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **member_confirm_password_get**
> member_confirm_password_get(authorization, client_id, password)

비밀번호 확인

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MemberApi()
authorization = 'authorization_example' # str | 토큰 : tokenType + ' ' + token
client_id = 'client_id_example' # str | API Key
password = 'password_example' # str | 비밀번호

try:
    # 비밀번호 확인
    api_instance.member_confirm_password_get(authorization, client_id, password)
except ApiException as e:
    print("Exception when calling MemberApi->member_confirm_password_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| 토큰 : tokenType + &#x27; &#x27; + token | 
 **client_id** | **str**| API Key | 
 **password** | **str**| 비밀번호 | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **member_find_id_get**
> member_find_id_get(client_id, site_id, name, phone)

아이디 찾기

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MemberApi()
client_id = 'client_id_example' # str | API Key
site_id = 'site_id_example' # str | 학교 아이디
name = 'name_example' # str | 이름
phone = 'phone_example' # str | 전화번호

try:
    # 아이디 찾기
    api_instance.member_find_id_get(client_id, site_id, name, phone)
except ApiException as e:
    print("Exception when calling MemberApi->member_find_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**| API Key | 
 **site_id** | **str**| 학교 아이디 | 
 **name** | **str**| 이름 | 
 **phone** | **str**| 전화번호 | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **member_find_password_get**
> member_find_password_get(client_id, site_id, name, id, phone, auth_number=auth_number)

비밀번호 찾기 / 처음에 인증번호 없이 보내면 알림톡으로 인증번호 발송됨 두번째는 인증번호와 함께 다시 전송.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MemberApi()
client_id = 'client_id_example' # str | API Key
site_id = 'site_id_example' # str | 학교 아이디
name = 'name_example' # str | 이름
id = 'id_example' # str | 아이디
phone = 'phone_example' # str | 전화번호
auth_number = 'auth_number_example' # str | 인증번호 (알림톡 발송된 인증번호 입력) (optional)

try:
    # 비밀번호 찾기 / 처음에 인증번호 없이 보내면 알림톡으로 인증번호 발송됨 두번째는 인증번호와 함께 다시 전송.
    api_instance.member_find_password_get(client_id, site_id, name, id, phone, auth_number=auth_number)
except ApiException as e:
    print("Exception when calling MemberApi->member_find_password_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**| API Key | 
 **site_id** | **str**| 학교 아이디 | 
 **name** | **str**| 이름 | 
 **id** | **str**| 아이디 | 
 **phone** | **str**| 전화번호 | 
 **auth_number** | **str**| 인증번호 (알림톡 발송된 인증번호 입력) | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **member_info_get**
> member_info_get(authorization, client_id, password)

내정보 가져가기

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MemberApi()
authorization = 'authorization_example' # str | 토큰 : tokenType + ' ' + token
client_id = 'client_id_example' # str | API Key
password = 'password_example' # str | 비밀번호

try:
    # 내정보 가져가기
    api_instance.member_info_get(authorization, client_id, password)
except ApiException as e:
    print("Exception when calling MemberApi->member_info_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| 토큰 : tokenType + &#x27; &#x27; + token | 
 **client_id** | **str**| API Key | 
 **password** | **str**| 비밀번호 | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **member_info_put**
> member_info_put(authorization, client_id, password)

내정보 수정하기

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MemberApi()
authorization = 'authorization_example' # str | 토큰 : tokenType + ' ' + token
client_id = 'client_id_example' # str | API Key
password = 'password_example' # str | 비밀번호

try:
    # 내정보 수정하기
    api_instance.member_info_put(authorization, client_id, password)
except ApiException as e:
    print("Exception when calling MemberApi->member_info_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| 토큰 : tokenType + &#x27; &#x27; + token | 
 **client_id** | **str**| API Key | 
 **password** | **str**| 비밀번호 | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **member_me_get**
> member_me_get(body, authorization, client_id)

내 정보

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MemberApi()
body = swagger_client.Device() # Device | 기기 정보
authorization = 'authorization_example' # str | 토큰 : tokenType + ' ' + token
client_id = 'client_id_example' # str | API Key

try:
    # 내 정보
    api_instance.member_me_get(body, authorization, client_id)
except ApiException as e:
    print("Exception when calling MemberApi->member_me_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Device**](Device.md)| 기기 정보 | 
 **authorization** | **str**| 토큰 : tokenType + &#x27; &#x27; + token | 
 **client_id** | **str**| API Key | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **member_phone_get**
> member_phone_get(client_id, tid, auth_info)

전화번호 인증

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MemberApi()
client_id = 'client_id_example' # str | API Key
tid = 'tid_example' # str | 본인인증에서 callback 받은 tid
auth_info = 'auth_info_example' # str | 본인인증에서 callback 받은 auth_info

try:
    # 전화번호 인증
    api_instance.member_phone_get(client_id, tid, auth_info)
except ApiException as e:
    print("Exception when calling MemberApi->member_phone_get: %s\n" % e)
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

