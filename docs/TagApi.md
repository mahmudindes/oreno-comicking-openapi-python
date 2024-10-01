# comicking_openapi.TagApi

All URIs are relative to */api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_tag**](TagApi.md#add_tag) | **POST** /rest/tags | Add tag.
[**add_tag_type**](TagApi.md#add_tag_type) | **POST** /rest/tag-types | Add tag type.
[**delete_tag**](TagApi.md#delete_tag) | **DELETE** /rest/tags/{typeCode}:{code} | Delete tag.
[**delete_tag_type**](TagApi.md#delete_tag_type) | **DELETE** /rest/tag-types/{code} | Delete tag type.
[**get_tag**](TagApi.md#get_tag) | **GET** /rest/tags/{typeCode}:{code} | Get tag.
[**get_tag_type**](TagApi.md#get_tag_type) | **GET** /rest/tag-types/{code} | Get tag type.
[**list_tag**](TagApi.md#list_tag) | **GET** /rest/tags | List tag.
[**list_tag_type**](TagApi.md#list_tag_type) | **GET** /rest/tag-types | List tag type.
[**update_tag**](TagApi.md#update_tag) | **PATCH** /rest/tags/{typeCode}:{code} | Update tag.
[**update_tag_type**](TagApi.md#update_tag_type) | **PATCH** /rest/tag-types/{code} | Update tag type.


# **add_tag**
> Tag add_tag(new_tag)

Add tag.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import comicking_openapi
from comicking_openapi.models.new_tag import NewTag
from comicking_openapi.models.tag import Tag
from comicking_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = comicking_openapi.Configuration(
    host = "/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): BearerAuth
configuration = comicking_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with comicking_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = comicking_openapi.TagApi(api_client)
    new_tag = comicking_openapi.NewTag() # NewTag | 

    try:
        # Add tag.
        api_response = api_instance.add_tag(new_tag)
        print("The response of TagApi->add_tag:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TagApi->add_tag: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **new_tag** | [**NewTag**](NewTag.md)|  | 

### Return type

[**Tag**](Tag.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Tag added. |  * Location -  <br>  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_tag_type**
> GenericType add_tag_type(new_generic_type)

Add tag type.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import comicking_openapi
from comicking_openapi.models.generic_type import GenericType
from comicking_openapi.models.new_generic_type import NewGenericType
from comicking_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = comicking_openapi.Configuration(
    host = "/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): BearerAuth
configuration = comicking_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with comicking_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = comicking_openapi.TagApi(api_client)
    new_generic_type = comicking_openapi.NewGenericType() # NewGenericType | 

    try:
        # Add tag type.
        api_response = api_instance.add_tag_type(new_generic_type)
        print("The response of TagApi->add_tag_type:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TagApi->add_tag_type: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **new_generic_type** | [**NewGenericType**](NewGenericType.md)|  | 

### Return type

[**GenericType**](GenericType.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Tag type added. |  * Location -  <br>  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_tag**
> delete_tag(type_code, code)

Delete tag.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import comicking_openapi
from comicking_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = comicking_openapi.Configuration(
    host = "/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): BearerAuth
configuration = comicking_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with comicking_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = comicking_openapi.TagApi(api_client)
    type_code = 'type_code_example' # str | 
    code = 'code_example' # str | 

    try:
        # Delete tag.
        api_instance.delete_tag(type_code, code)
    except Exception as e:
        print("Exception when calling TagApi->delete_tag: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type_code** | **str**|  | 
 **code** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Tag deleted. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_tag_type**
> delete_tag_type(code)

Delete tag type.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import comicking_openapi
from comicking_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = comicking_openapi.Configuration(
    host = "/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): BearerAuth
configuration = comicking_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with comicking_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = comicking_openapi.TagApi(api_client)
    code = 'code_example' # str | 

    try:
        # Delete tag type.
        api_instance.delete_tag_type(code)
    except Exception as e:
        print("Exception when calling TagApi->delete_tag_type: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Tag type deleted. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tag**
> Tag get_tag(type_code, code)

Get tag.

### Example


```python
import comicking_openapi
from comicking_openapi.models.tag import Tag
from comicking_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = comicking_openapi.Configuration(
    host = "/api"
)


# Enter a context with an instance of the API client
with comicking_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = comicking_openapi.TagApi(api_client)
    type_code = 'type_code_example' # str | 
    code = 'code_example' # str | 

    try:
        # Get tag.
        api_response = api_instance.get_tag(type_code, code)
        print("The response of TagApi->get_tag:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TagApi->get_tag: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type_code** | **str**|  | 
 **code** | **str**|  | 

### Return type

[**Tag**](Tag.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Tag gets. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tag_type**
> GenericType get_tag_type(code)

Get tag type.

### Example


```python
import comicking_openapi
from comicking_openapi.models.generic_type import GenericType
from comicking_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = comicking_openapi.Configuration(
    host = "/api"
)


# Enter a context with an instance of the API client
with comicking_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = comicking_openapi.TagApi(api_client)
    code = 'code_example' # str | 

    try:
        # Get tag type.
        api_response = api_instance.get_tag_type(code)
        print("The response of TagApi->get_tag_type:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TagApi->get_tag_type: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**|  | 

### Return type

[**GenericType**](GenericType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Tag type gets. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_tag**
> List[Tag] list_tag(page=page, limit=limit, order=order, order_by=order_by, type_code=type_code)

List tag.

### Example


```python
import comicking_openapi
from comicking_openapi.models.tag import Tag
from comicking_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = comicking_openapi.Configuration(
    host = "/api"
)


# Enter a context with an instance of the API client
with comicking_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = comicking_openapi.TagApi(api_client)
    page = 56 # int |  (optional)
    limit = 56 # int |  (optional)
    order = 'order_example' # str |  (optional)
    order_by = ['order_by_example'] # List[str] |  (optional)
    type_code = ['type_code_example'] # List[str] |  (optional)

    try:
        # List tag.
        api_response = api_instance.list_tag(page=page, limit=limit, order=order, order_by=order_by, type_code=type_code)
        print("The response of TagApi->list_tag:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TagApi->list_tag: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] 
 **limit** | **int**|  | [optional] 
 **order** | **str**|  | [optional] 
 **order_by** | [**List[str]**](str.md)|  | [optional] 
 **type_code** | [**List[str]**](str.md)|  | [optional] 

### Return type

[**List[Tag]**](Tag.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Tag list. |  * X-Total-Count -  <br>  * X-Pagination-Limit -  <br>  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_tag_type**
> List[GenericType] list_tag_type(page=page, limit=limit, order=order, order_by=order_by)

List tag type.

### Example


```python
import comicking_openapi
from comicking_openapi.models.generic_type import GenericType
from comicking_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = comicking_openapi.Configuration(
    host = "/api"
)


# Enter a context with an instance of the API client
with comicking_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = comicking_openapi.TagApi(api_client)
    page = 56 # int |  (optional)
    limit = 56 # int |  (optional)
    order = 'order_example' # str |  (optional)
    order_by = ['order_by_example'] # List[str] |  (optional)

    try:
        # List tag type.
        api_response = api_instance.list_tag_type(page=page, limit=limit, order=order, order_by=order_by)
        print("The response of TagApi->list_tag_type:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TagApi->list_tag_type: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] 
 **limit** | **int**|  | [optional] 
 **order** | **str**|  | [optional] 
 **order_by** | [**List[str]**](str.md)|  | [optional] 

### Return type

[**List[GenericType]**](GenericType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Tag type list. |  * X-Total-Count -  <br>  * X-Pagination-Limit -  <br>  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_tag**
> Tag update_tag(type_code, code, set_tag)

Update tag.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import comicking_openapi
from comicking_openapi.models.set_tag import SetTag
from comicking_openapi.models.tag import Tag
from comicking_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = comicking_openapi.Configuration(
    host = "/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): BearerAuth
configuration = comicking_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with comicking_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = comicking_openapi.TagApi(api_client)
    type_code = 'type_code_example' # str | 
    code = 'code_example' # str | 
    set_tag = comicking_openapi.SetTag() # SetTag | 

    try:
        # Update tag.
        api_response = api_instance.update_tag(type_code, code, set_tag)
        print("The response of TagApi->update_tag:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TagApi->update_tag: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type_code** | **str**|  | 
 **code** | **str**|  | 
 **set_tag** | [**SetTag**](SetTag.md)|  | 

### Return type

[**Tag**](Tag.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Tag updated. |  * Location -  <br>  |
**204** | Tag unmodified. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_tag_type**
> GenericType update_tag_type(code, set_generic_type)

Update tag type.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import comicking_openapi
from comicking_openapi.models.generic_type import GenericType
from comicking_openapi.models.set_generic_type import SetGenericType
from comicking_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = comicking_openapi.Configuration(
    host = "/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): BearerAuth
configuration = comicking_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with comicking_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = comicking_openapi.TagApi(api_client)
    code = 'code_example' # str | 
    set_generic_type = comicking_openapi.SetGenericType() # SetGenericType | 

    try:
        # Update tag type.
        api_response = api_instance.update_tag_type(code, set_generic_type)
        print("The response of TagApi->update_tag_type:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TagApi->update_tag_type: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**|  | 
 **set_generic_type** | [**SetGenericType**](SetGenericType.md)|  | 

### Return type

[**GenericType**](GenericType.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Tag type updated. |  * Location -  <br>  |
**204** | Tag type unmodified. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

