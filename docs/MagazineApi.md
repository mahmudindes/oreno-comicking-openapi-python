# comicking_openapi.MagazineApi

All URIs are relative to */api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_magazine**](MagazineApi.md#add_magazine) | **POST** /rest/magazines | Add magazine.
[**delete_magazine**](MagazineApi.md#delete_magazine) | **DELETE** /rest/magazines/{code} | Delete magazine.
[**get_magazine**](MagazineApi.md#get_magazine) | **GET** /rest/magazines/{code} | Get magazine.
[**list_magazine**](MagazineApi.md#list_magazine) | **GET** /rest/magazines | List magazine.
[**update_magazine**](MagazineApi.md#update_magazine) | **PATCH** /rest/magazines/{code} | Update magazine.


# **add_magazine**
> Magazine add_magazine(new_magazine)

Add magazine.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import comicking_openapi
from comicking_openapi.models.magazine import Magazine
from comicking_openapi.models.new_magazine import NewMagazine
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
    api_instance = comicking_openapi.MagazineApi(api_client)
    new_magazine = comicking_openapi.NewMagazine() # NewMagazine | 

    try:
        # Add magazine.
        api_response = api_instance.add_magazine(new_magazine)
        print("The response of MagazineApi->add_magazine:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MagazineApi->add_magazine: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **new_magazine** | [**NewMagazine**](NewMagazine.md)|  | 

### Return type

[**Magazine**](Magazine.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Magazine added. |  * Location -  <br>  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_magazine**
> delete_magazine(code)

Delete magazine.

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
    api_instance = comicking_openapi.MagazineApi(api_client)
    code = 'code_example' # str | 

    try:
        # Delete magazine.
        api_instance.delete_magazine(code)
    except Exception as e:
        print("Exception when calling MagazineApi->delete_magazine: %s\n" % e)
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
**204** | Magazine deleted. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_magazine**
> Magazine get_magazine(code)

Get magazine.

### Example


```python
import comicking_openapi
from comicking_openapi.models.magazine import Magazine
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
    api_instance = comicking_openapi.MagazineApi(api_client)
    code = 'code_example' # str | 

    try:
        # Get magazine.
        api_response = api_instance.get_magazine(code)
        print("The response of MagazineApi->get_magazine:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MagazineApi->get_magazine: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**|  | 

### Return type

[**Magazine**](Magazine.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Magazine gets. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_magazine**
> List[Magazine] list_magazine(page=page, limit=limit, order=order, order_by=order_by)

List magazine.

### Example


```python
import comicking_openapi
from comicking_openapi.models.magazine import Magazine
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
    api_instance = comicking_openapi.MagazineApi(api_client)
    page = 56 # int |  (optional)
    limit = 56 # int |  (optional)
    order = 'order_example' # str |  (optional)
    order_by = ['order_by_example'] # List[str] |  (optional)

    try:
        # List magazine.
        api_response = api_instance.list_magazine(page=page, limit=limit, order=order, order_by=order_by)
        print("The response of MagazineApi->list_magazine:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MagazineApi->list_magazine: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] 
 **limit** | **int**|  | [optional] 
 **order** | **str**|  | [optional] 
 **order_by** | [**List[str]**](str.md)|  | [optional] 

### Return type

[**List[Magazine]**](Magazine.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Magazine list. |  * X-Total-Count -  <br>  * X-Pagination-Limit -  <br>  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_magazine**
> Magazine update_magazine(code, set_magazine)

Update magazine.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import comicking_openapi
from comicking_openapi.models.magazine import Magazine
from comicking_openapi.models.set_magazine import SetMagazine
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
    api_instance = comicking_openapi.MagazineApi(api_client)
    code = 'code_example' # str | 
    set_magazine = comicking_openapi.SetMagazine() # SetMagazine | 

    try:
        # Update magazine.
        api_response = api_instance.update_magazine(code, set_magazine)
        print("The response of MagazineApi->update_magazine:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MagazineApi->update_magazine: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**|  | 
 **set_magazine** | [**SetMagazine**](SetMagazine.md)|  | 

### Return type

[**Magazine**](Magazine.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Magazine updated. |  * Location -  <br>  |
**204** | Magazine unmodified. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

