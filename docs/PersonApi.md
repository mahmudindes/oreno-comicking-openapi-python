# comicking_openapi.PersonApi

All URIs are relative to */api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_person**](PersonApi.md#add_person) | **POST** /rest/people | Add person.
[**delete_person**](PersonApi.md#delete_person) | **DELETE** /rest/people/{code} | Delete person.
[**get_person**](PersonApi.md#get_person) | **GET** /rest/people/{code} | Get person.
[**list_person**](PersonApi.md#list_person) | **GET** /rest/people | List person.
[**update_person**](PersonApi.md#update_person) | **PATCH** /rest/people/{code} | Update person.


# **add_person**
> Person add_person(new_person)

Add person.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import comicking_openapi
from comicking_openapi.models.new_person import NewPerson
from comicking_openapi.models.person import Person
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
    api_instance = comicking_openapi.PersonApi(api_client)
    new_person = comicking_openapi.NewPerson() # NewPerson | 

    try:
        # Add person.
        api_response = api_instance.add_person(new_person)
        print("The response of PersonApi->add_person:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PersonApi->add_person: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **new_person** | [**NewPerson**](NewPerson.md)|  | 

### Return type

[**Person**](Person.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Person added. |  * Location -  <br>  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_person**
> delete_person(code)

Delete person.

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
    api_instance = comicking_openapi.PersonApi(api_client)
    code = 'code_example' # str | 

    try:
        # Delete person.
        api_instance.delete_person(code)
    except Exception as e:
        print("Exception when calling PersonApi->delete_person: %s\n" % e)
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
**204** | Person deleted. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_person**
> Person get_person(code)

Get person.

### Example


```python
import comicking_openapi
from comicking_openapi.models.person import Person
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
    api_instance = comicking_openapi.PersonApi(api_client)
    code = 'code_example' # str | 

    try:
        # Get person.
        api_response = api_instance.get_person(code)
        print("The response of PersonApi->get_person:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PersonApi->get_person: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**|  | 

### Return type

[**Person**](Person.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Person gets. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_person**
> List[Person] list_person(page=page, limit=limit, order=order, order_by=order_by)

List person.

### Example


```python
import comicking_openapi
from comicking_openapi.models.person import Person
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
    api_instance = comicking_openapi.PersonApi(api_client)
    page = 56 # int |  (optional)
    limit = 56 # int |  (optional)
    order = 'order_example' # str |  (optional)
    order_by = ['order_by_example'] # List[str] |  (optional)

    try:
        # List person.
        api_response = api_instance.list_person(page=page, limit=limit, order=order, order_by=order_by)
        print("The response of PersonApi->list_person:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PersonApi->list_person: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] 
 **limit** | **int**|  | [optional] 
 **order** | **str**|  | [optional] 
 **order_by** | [**List[str]**](str.md)|  | [optional] 

### Return type

[**List[Person]**](Person.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Person list. |  * X-Total-Count -  <br>  * X-Pagination-Limit -  <br>  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_person**
> Person update_person(code, set_person)

Update person.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import comicking_openapi
from comicking_openapi.models.person import Person
from comicking_openapi.models.set_person import SetPerson
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
    api_instance = comicking_openapi.PersonApi(api_client)
    code = 'code_example' # str | 
    set_person = comicking_openapi.SetPerson() # SetPerson | 

    try:
        # Update person.
        api_response = api_instance.update_person(code, set_person)
        print("The response of PersonApi->update_person:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PersonApi->update_person: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**|  | 
 **set_person** | [**SetPerson**](SetPerson.md)|  | 

### Return type

[**Person**](Person.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Person updated. |  * Location -  <br>  |
**204** | Person unmodified. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

