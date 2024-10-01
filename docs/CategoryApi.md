# comicking_openapi.CategoryApi

All URIs are relative to */api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_category**](CategoryApi.md#add_category) | **POST** /rest/categories | Add category.
[**add_category_type**](CategoryApi.md#add_category_type) | **POST** /rest/category-types | Add category type.
[**delete_category**](CategoryApi.md#delete_category) | **DELETE** /rest/categories/{typeCode}:{code} | Delete category.
[**delete_category_type**](CategoryApi.md#delete_category_type) | **DELETE** /rest/category-types/{code} | Delete category type.
[**get_category**](CategoryApi.md#get_category) | **GET** /rest/categories/{typeCode}:{code} | Get category.
[**get_category_type**](CategoryApi.md#get_category_type) | **GET** /rest/category-types/{code} | Get category type.
[**list_category**](CategoryApi.md#list_category) | **GET** /rest/categories | List category.
[**list_category_type**](CategoryApi.md#list_category_type) | **GET** /rest/category-types | List category type.
[**update_category**](CategoryApi.md#update_category) | **PATCH** /rest/categories/{typeCode}:{code} | Update category.
[**update_category_type**](CategoryApi.md#update_category_type) | **PATCH** /rest/category-types/{code} | Update category type.


# **add_category**
> Category add_category(new_category)

Add category.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import comicking_openapi
from comicking_openapi.models.category import Category
from comicking_openapi.models.new_category import NewCategory
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
    api_instance = comicking_openapi.CategoryApi(api_client)
    new_category = comicking_openapi.NewCategory() # NewCategory | 

    try:
        # Add category.
        api_response = api_instance.add_category(new_category)
        print("The response of CategoryApi->add_category:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CategoryApi->add_category: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **new_category** | [**NewCategory**](NewCategory.md)|  | 

### Return type

[**Category**](Category.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Category added. |  * Location -  <br>  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_category_type**
> GenericType add_category_type(new_generic_type)

Add category type.

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
    api_instance = comicking_openapi.CategoryApi(api_client)
    new_generic_type = comicking_openapi.NewGenericType() # NewGenericType | 

    try:
        # Add category type.
        api_response = api_instance.add_category_type(new_generic_type)
        print("The response of CategoryApi->add_category_type:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CategoryApi->add_category_type: %s\n" % e)
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
**201** | Category type added. |  * Location -  <br>  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_category**
> delete_category(type_code, code)

Delete category.

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
    api_instance = comicking_openapi.CategoryApi(api_client)
    type_code = 'type_code_example' # str | 
    code = 'code_example' # str | 

    try:
        # Delete category.
        api_instance.delete_category(type_code, code)
    except Exception as e:
        print("Exception when calling CategoryApi->delete_category: %s\n" % e)
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
**204** | Category deleted. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_category_type**
> delete_category_type(code)

Delete category type.

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
    api_instance = comicking_openapi.CategoryApi(api_client)
    code = 'code_example' # str | 

    try:
        # Delete category type.
        api_instance.delete_category_type(code)
    except Exception as e:
        print("Exception when calling CategoryApi->delete_category_type: %s\n" % e)
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
**204** | Category type deleted. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_category**
> Category get_category(type_code, code)

Get category.

### Example


```python
import comicking_openapi
from comicking_openapi.models.category import Category
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
    api_instance = comicking_openapi.CategoryApi(api_client)
    type_code = 'type_code_example' # str | 
    code = 'code_example' # str | 

    try:
        # Get category.
        api_response = api_instance.get_category(type_code, code)
        print("The response of CategoryApi->get_category:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CategoryApi->get_category: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type_code** | **str**|  | 
 **code** | **str**|  | 

### Return type

[**Category**](Category.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Category gets. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_category_type**
> GenericType get_category_type(code)

Get category type.

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
    api_instance = comicking_openapi.CategoryApi(api_client)
    code = 'code_example' # str | 

    try:
        # Get category type.
        api_response = api_instance.get_category_type(code)
        print("The response of CategoryApi->get_category_type:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CategoryApi->get_category_type: %s\n" % e)
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
**200** | Category type gets. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_category**
> List[Category] list_category(page=page, limit=limit, order=order, order_by=order_by, type_code=type_code, parent_code=parent_code)

List category.

### Example


```python
import comicking_openapi
from comicking_openapi.models.category import Category
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
    api_instance = comicking_openapi.CategoryApi(api_client)
    page = 56 # int |  (optional)
    limit = 56 # int |  (optional)
    order = 'order_example' # str |  (optional)
    order_by = ['order_by_example'] # List[str] |  (optional)
    type_code = ['type_code_example'] # List[str] |  (optional)
    parent_code = ['parent_code_example'] # List[str] |  (optional)

    try:
        # List category.
        api_response = api_instance.list_category(page=page, limit=limit, order=order, order_by=order_by, type_code=type_code, parent_code=parent_code)
        print("The response of CategoryApi->list_category:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CategoryApi->list_category: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] 
 **limit** | **int**|  | [optional] 
 **order** | **str**|  | [optional] 
 **order_by** | [**List[str]**](str.md)|  | [optional] 
 **type_code** | [**List[str]**](str.md)|  | [optional] 
 **parent_code** | [**List[str]**](str.md)|  | [optional] 

### Return type

[**List[Category]**](Category.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Category list. |  * X-Total-Count -  <br>  * X-Pagination-Limit -  <br>  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_category_type**
> List[GenericType] list_category_type(page=page, limit=limit, order=order, order_by=order_by)

List category type.

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
    api_instance = comicking_openapi.CategoryApi(api_client)
    page = 56 # int |  (optional)
    limit = 56 # int |  (optional)
    order = 'order_example' # str |  (optional)
    order_by = ['order_by_example'] # List[str] |  (optional)

    try:
        # List category type.
        api_response = api_instance.list_category_type(page=page, limit=limit, order=order, order_by=order_by)
        print("The response of CategoryApi->list_category_type:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CategoryApi->list_category_type: %s\n" % e)
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
**200** | Category type list. |  * X-Total-Count -  <br>  * X-Pagination-Limit -  <br>  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_category**
> Category update_category(type_code, code, set_category)

Update category.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import comicking_openapi
from comicking_openapi.models.category import Category
from comicking_openapi.models.set_category import SetCategory
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
    api_instance = comicking_openapi.CategoryApi(api_client)
    type_code = 'type_code_example' # str | 
    code = 'code_example' # str | 
    set_category = comicking_openapi.SetCategory() # SetCategory | 

    try:
        # Update category.
        api_response = api_instance.update_category(type_code, code, set_category)
        print("The response of CategoryApi->update_category:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CategoryApi->update_category: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type_code** | **str**|  | 
 **code** | **str**|  | 
 **set_category** | [**SetCategory**](SetCategory.md)|  | 

### Return type

[**Category**](Category.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Category updated. |  * Location -  <br>  |
**204** | Category unmodified. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_category_type**
> GenericType update_category_type(code, set_generic_type)

Update category type.

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
    api_instance = comicking_openapi.CategoryApi(api_client)
    code = 'code_example' # str | 
    set_generic_type = comicking_openapi.SetGenericType() # SetGenericType | 

    try:
        # Update category type.
        api_response = api_instance.update_category_type(code, set_generic_type)
        print("The response of CategoryApi->update_category_type:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CategoryApi->update_category_type: %s\n" % e)
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
**200** | Category type updated. |  * Location -  <br>  |
**204** | Category type unmodified. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

