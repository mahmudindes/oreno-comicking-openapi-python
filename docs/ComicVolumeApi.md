# comicking_openapi.ComicVolumeApi

All URIs are relative to */api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_comic_volume**](ComicVolumeApi.md#add_comic_volume) | **POST** /rest/comics/{comicCode}/volumes | Add comic volume.
[**add_comic_volume_cover**](ComicVolumeApi.md#add_comic_volume_cover) | **POST** /rest/comics/{comicCode}/volumes/{volumeNumber}/covers | Add comic volume cover.
[**add_comic_volume_title**](ComicVolumeApi.md#add_comic_volume_title) | **POST** /rest/comics/{comicCode}/volumes/{volumeNumber}/titles | Add comic volume title.
[**delete_comic_volume**](ComicVolumeApi.md#delete_comic_volume) | **DELETE** /rest/comics/{comicCode}/volumes/{volume} | Delete comic volume.
[**delete_comic_volume_cover**](ComicVolumeApi.md#delete_comic_volume_cover) | **DELETE** /rest/comics/{comicCode}/volumes/{volumeNumber}/covers/{ulid} | Delete comic volume cover.
[**delete_comic_volume_title**](ComicVolumeApi.md#delete_comic_volume_title) | **DELETE** /rest/comics/{comicCode}/volumes/{volumeNumber}/titles/{ulid} | Delete comic volume title.
[**get_comic_volume**](ComicVolumeApi.md#get_comic_volume) | **GET** /rest/comics/{comicCode}/volumes/{volume} | Get comic volume.
[**get_comic_volume_cover**](ComicVolumeApi.md#get_comic_volume_cover) | **GET** /rest/comics/{comicCode}/volumes/{volumeNumber}/covers/{ulid} | Get comic volume cover.
[**get_comic_volume_title**](ComicVolumeApi.md#get_comic_volume_title) | **GET** /rest/comics/{comicCode}/volumes/{volumeNumber}/titles/{ulid} | Get comic volume title.
[**list_comic_volume**](ComicVolumeApi.md#list_comic_volume) | **GET** /rest/comics/{comicCode}/volumes | List comic volume.
[**list_comic_volume_cover**](ComicVolumeApi.md#list_comic_volume_cover) | **GET** /rest/comics/{comicCode}/volumes/{volumeNumber}/covers | List comic volume cover.
[**list_comic_volume_title**](ComicVolumeApi.md#list_comic_volume_title) | **GET** /rest/comics/{comicCode}/volumes/{volumeNumber}/titles | List comic volume title.
[**update_comic_volume**](ComicVolumeApi.md#update_comic_volume) | **PATCH** /rest/comics/{comicCode}/volumes/{volume} | Update comic volume.
[**update_comic_volume_cover**](ComicVolumeApi.md#update_comic_volume_cover) | **PATCH** /rest/comics/{comicCode}/volumes/{volumeNumber}/covers/{ulid} | Update volume comic cover.
[**update_comic_volume_title**](ComicVolumeApi.md#update_comic_volume_title) | **PATCH** /rest/comics/{comicCode}/volumes/{volumeNumber}/titles/{ulid} | Update comic volume title.


# **add_comic_volume**
> ComicVolume add_comic_volume(comic_code, new_comic_volume)

Add comic volume.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import comicking_openapi
from comicking_openapi.models.comic_volume import ComicVolume
from comicking_openapi.models.new_comic_volume import NewComicVolume
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
    api_instance = comicking_openapi.ComicVolumeApi(api_client)
    comic_code = 'comic_code_example' # str | 
    new_comic_volume = comicking_openapi.NewComicVolume() # NewComicVolume | 

    try:
        # Add comic volume.
        api_response = api_instance.add_comic_volume(comic_code, new_comic_volume)
        print("The response of ComicVolumeApi->add_comic_volume:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComicVolumeApi->add_comic_volume: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **comic_code** | **str**|  | 
 **new_comic_volume** | [**NewComicVolume**](NewComicVolume.md)|  | 

### Return type

[**ComicVolume**](ComicVolume.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Comic volume added. |  * Location -  <br>  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_comic_volume_cover**
> ComicVolumeCover add_comic_volume_cover(comic_code, volume_number, new_comic_volume_cover)

Add comic volume cover.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import comicking_openapi
from comicking_openapi.models.comic_volume_cover import ComicVolumeCover
from comicking_openapi.models.new_comic_volume_cover import NewComicVolumeCover
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
    api_instance = comicking_openapi.ComicVolumeApi(api_client)
    comic_code = 'comic_code_example' # str | 
    volume_number = 'volume_number_example' # str | 
    new_comic_volume_cover = comicking_openapi.NewComicVolumeCover() # NewComicVolumeCover | 

    try:
        # Add comic volume cover.
        api_response = api_instance.add_comic_volume_cover(comic_code, volume_number, new_comic_volume_cover)
        print("The response of ComicVolumeApi->add_comic_volume_cover:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComicVolumeApi->add_comic_volume_cover: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **comic_code** | **str**|  | 
 **volume_number** | **str**|  | 
 **new_comic_volume_cover** | [**NewComicVolumeCover**](NewComicVolumeCover.md)|  | 

### Return type

[**ComicVolumeCover**](ComicVolumeCover.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Comic volume cover added. |  * Location -  <br>  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_comic_volume_title**
> ComicVolumeTitle add_comic_volume_title(comic_code, volume_number, new_comic_volume_title)

Add comic volume title.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import comicking_openapi
from comicking_openapi.models.comic_volume_title import ComicVolumeTitle
from comicking_openapi.models.new_comic_volume_title import NewComicVolumeTitle
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
    api_instance = comicking_openapi.ComicVolumeApi(api_client)
    comic_code = 'comic_code_example' # str | 
    volume_number = 'volume_number_example' # str | 
    new_comic_volume_title = comicking_openapi.NewComicVolumeTitle() # NewComicVolumeTitle | 

    try:
        # Add comic volume title.
        api_response = api_instance.add_comic_volume_title(comic_code, volume_number, new_comic_volume_title)
        print("The response of ComicVolumeApi->add_comic_volume_title:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComicVolumeApi->add_comic_volume_title: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **comic_code** | **str**|  | 
 **volume_number** | **str**|  | 
 **new_comic_volume_title** | [**NewComicVolumeTitle**](NewComicVolumeTitle.md)|  | 

### Return type

[**ComicVolumeTitle**](ComicVolumeTitle.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Comic volume title added. |  * Location -  <br>  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_comic_volume**
> delete_comic_volume(comic_code, volume)

Delete comic volume.

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
    api_instance = comicking_openapi.ComicVolumeApi(api_client)
    comic_code = 'comic_code_example' # str | 
    volume = 'volume_example' # str | 

    try:
        # Delete comic volume.
        api_instance.delete_comic_volume(comic_code, volume)
    except Exception as e:
        print("Exception when calling ComicVolumeApi->delete_comic_volume: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **comic_code** | **str**|  | 
 **volume** | **str**|  | 

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
**204** | Comic volume deleted. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_comic_volume_cover**
> delete_comic_volume_cover(comic_code, volume_number, ulid)

Delete comic volume cover.

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
    api_instance = comicking_openapi.ComicVolumeApi(api_client)
    comic_code = 'comic_code_example' # str | 
    volume_number = 'volume_number_example' # str | 
    ulid = 'ulid_example' # str | 

    try:
        # Delete comic volume cover.
        api_instance.delete_comic_volume_cover(comic_code, volume_number, ulid)
    except Exception as e:
        print("Exception when calling ComicVolumeApi->delete_comic_volume_cover: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **comic_code** | **str**|  | 
 **volume_number** | **str**|  | 
 **ulid** | **str**|  | 

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
**204** | Comic volume cover deleted. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_comic_volume_title**
> delete_comic_volume_title(comic_code, volume_number, ulid)

Delete comic volume title.

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
    api_instance = comicking_openapi.ComicVolumeApi(api_client)
    comic_code = 'comic_code_example' # str | 
    volume_number = 'volume_number_example' # str | 
    ulid = 'ulid_example' # str | 

    try:
        # Delete comic volume title.
        api_instance.delete_comic_volume_title(comic_code, volume_number, ulid)
    except Exception as e:
        print("Exception when calling ComicVolumeApi->delete_comic_volume_title: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **comic_code** | **str**|  | 
 **volume_number** | **str**|  | 
 **ulid** | **str**|  | 

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
**204** | Comic volume title deleted. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_comic_volume**
> ComicVolume get_comic_volume(comic_code, volume)

Get comic volume.

### Example


```python
import comicking_openapi
from comicking_openapi.models.comic_volume import ComicVolume
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
    api_instance = comicking_openapi.ComicVolumeApi(api_client)
    comic_code = 'comic_code_example' # str | 
    volume = 'volume_example' # str | 

    try:
        # Get comic volume.
        api_response = api_instance.get_comic_volume(comic_code, volume)
        print("The response of ComicVolumeApi->get_comic_volume:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComicVolumeApi->get_comic_volume: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **comic_code** | **str**|  | 
 **volume** | **str**|  | 

### Return type

[**ComicVolume**](ComicVolume.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Comic volume gets. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_comic_volume_cover**
> ComicVolumeCover get_comic_volume_cover(comic_code, volume_number, ulid)

Get comic volume cover.

### Example


```python
import comicking_openapi
from comicking_openapi.models.comic_volume_cover import ComicVolumeCover
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
    api_instance = comicking_openapi.ComicVolumeApi(api_client)
    comic_code = 'comic_code_example' # str | 
    volume_number = 'volume_number_example' # str | 
    ulid = 'ulid_example' # str | 

    try:
        # Get comic volume cover.
        api_response = api_instance.get_comic_volume_cover(comic_code, volume_number, ulid)
        print("The response of ComicVolumeApi->get_comic_volume_cover:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComicVolumeApi->get_comic_volume_cover: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **comic_code** | **str**|  | 
 **volume_number** | **str**|  | 
 **ulid** | **str**|  | 

### Return type

[**ComicVolumeCover**](ComicVolumeCover.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Comic volume cover gets. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_comic_volume_title**
> ComicVolumeTitle get_comic_volume_title(comic_code, volume_number, ulid)

Get comic volume title.

### Example


```python
import comicking_openapi
from comicking_openapi.models.comic_volume_title import ComicVolumeTitle
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
    api_instance = comicking_openapi.ComicVolumeApi(api_client)
    comic_code = 'comic_code_example' # str | 
    volume_number = 'volume_number_example' # str | 
    ulid = 'ulid_example' # str | 

    try:
        # Get comic volume title.
        api_response = api_instance.get_comic_volume_title(comic_code, volume_number, ulid)
        print("The response of ComicVolumeApi->get_comic_volume_title:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComicVolumeApi->get_comic_volume_title: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **comic_code** | **str**|  | 
 **volume_number** | **str**|  | 
 **ulid** | **str**|  | 

### Return type

[**ComicVolumeTitle**](ComicVolumeTitle.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Comic volume title gets. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_comic_volume**
> List[ComicVolume] list_comic_volume(comic_code, page=page, limit=limit, order=order, order_by=order_by, volume_volume=volume_volume)

List comic volume.

### Example


```python
import comicking_openapi
from comicking_openapi.models.comic_volume import ComicVolume
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
    api_instance = comicking_openapi.ComicVolumeApi(api_client)
    comic_code = 'comic_code_example' # str | 
    page = 56 # int |  (optional)
    limit = 56 # int |  (optional)
    order = 'order_example' # str |  (optional)
    order_by = ['order_by_example'] # List[str] |  (optional)
    volume_volume = ['volume_volume_example'] # List[str] |  (optional)

    try:
        # List comic volume.
        api_response = api_instance.list_comic_volume(comic_code, page=page, limit=limit, order=order, order_by=order_by, volume_volume=volume_volume)
        print("The response of ComicVolumeApi->list_comic_volume:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComicVolumeApi->list_comic_volume: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **comic_code** | **str**|  | 
 **page** | **int**|  | [optional] 
 **limit** | **int**|  | [optional] 
 **order** | **str**|  | [optional] 
 **order_by** | [**List[str]**](str.md)|  | [optional] 
 **volume_volume** | [**List[str]**](str.md)|  | [optional] 

### Return type

[**List[ComicVolume]**](ComicVolume.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Comic volume list. |  * X-Total-Count -  <br>  * X-Pagination-Limit -  <br>  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_comic_volume_cover**
> List[ComicVolumeCover] list_comic_volume_cover(comic_code, volume_number, page=page, limit=limit, order=order, order_by=order_by, link_website_host=link_website_host, link_relative_reference=link_relative_reference, link_href=link_href)

List comic volume cover.

### Example


```python
import comicking_openapi
from comicking_openapi.models.comic_volume_cover import ComicVolumeCover
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
    api_instance = comicking_openapi.ComicVolumeApi(api_client)
    comic_code = 'comic_code_example' # str | 
    volume_number = 'volume_number_example' # str | 
    page = 56 # int |  (optional)
    limit = 56 # int |  (optional)
    order = 'order_example' # str |  (optional)
    order_by = ['order_by_example'] # List[str] |  (optional)
    link_website_host = ['link_website_host_example'] # List[str] |  (optional)
    link_relative_reference = ['link_relative_reference_example'] # List[str] |  (optional)
    link_href = ['link_href_example'] # List[str] |  (optional)

    try:
        # List comic volume cover.
        api_response = api_instance.list_comic_volume_cover(comic_code, volume_number, page=page, limit=limit, order=order, order_by=order_by, link_website_host=link_website_host, link_relative_reference=link_relative_reference, link_href=link_href)
        print("The response of ComicVolumeApi->list_comic_volume_cover:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComicVolumeApi->list_comic_volume_cover: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **comic_code** | **str**|  | 
 **volume_number** | **str**|  | 
 **page** | **int**|  | [optional] 
 **limit** | **int**|  | [optional] 
 **order** | **str**|  | [optional] 
 **order_by** | [**List[str]**](str.md)|  | [optional] 
 **link_website_host** | [**List[str]**](str.md)|  | [optional] 
 **link_relative_reference** | [**List[str]**](str.md)|  | [optional] 
 **link_href** | [**List[str]**](str.md)|  | [optional] 

### Return type

[**List[ComicVolumeCover]**](ComicVolumeCover.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Comic volume cover list. |  * X-Total-Count -  <br>  * X-Pagination-Limit -  <br>  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_comic_volume_title**
> List[ComicVolumeTitle] list_comic_volume_title(comic_code, volume_number, page=page, limit=limit, order=order, order_by=order_by)

List comic volume title.

### Example


```python
import comicking_openapi
from comicking_openapi.models.comic_volume_title import ComicVolumeTitle
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
    api_instance = comicking_openapi.ComicVolumeApi(api_client)
    comic_code = 'comic_code_example' # str | 
    volume_number = 'volume_number_example' # str | 
    page = 56 # int |  (optional)
    limit = 56 # int |  (optional)
    order = 'order_example' # str |  (optional)
    order_by = ['order_by_example'] # List[str] |  (optional)

    try:
        # List comic volume title.
        api_response = api_instance.list_comic_volume_title(comic_code, volume_number, page=page, limit=limit, order=order, order_by=order_by)
        print("The response of ComicVolumeApi->list_comic_volume_title:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComicVolumeApi->list_comic_volume_title: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **comic_code** | **str**|  | 
 **volume_number** | **str**|  | 
 **page** | **int**|  | [optional] 
 **limit** | **int**|  | [optional] 
 **order** | **str**|  | [optional] 
 **order_by** | [**List[str]**](str.md)|  | [optional] 

### Return type

[**List[ComicVolumeTitle]**](ComicVolumeTitle.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Comic volume title list. |  * X-Total-Count -  <br>  * X-Pagination-Limit -  <br>  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_comic_volume**
> ComicVolume update_comic_volume(comic_code, volume, set_comic_volume)

Update comic volume.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import comicking_openapi
from comicking_openapi.models.comic_volume import ComicVolume
from comicking_openapi.models.set_comic_volume import SetComicVolume
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
    api_instance = comicking_openapi.ComicVolumeApi(api_client)
    comic_code = 'comic_code_example' # str | 
    volume = 'volume_example' # str | 
    set_comic_volume = comicking_openapi.SetComicVolume() # SetComicVolume | 

    try:
        # Update comic volume.
        api_response = api_instance.update_comic_volume(comic_code, volume, set_comic_volume)
        print("The response of ComicVolumeApi->update_comic_volume:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComicVolumeApi->update_comic_volume: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **comic_code** | **str**|  | 
 **volume** | **str**|  | 
 **set_comic_volume** | [**SetComicVolume**](SetComicVolume.md)|  | 

### Return type

[**ComicVolume**](ComicVolume.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Comic volume updated. |  * Location -  <br>  |
**204** | Comic volume unmodified. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_comic_volume_cover**
> ComicVolumeCover update_comic_volume_cover(comic_code, volume_number, ulid, set_comic_volume_cover)

Update volume comic cover.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import comicking_openapi
from comicking_openapi.models.comic_volume_cover import ComicVolumeCover
from comicking_openapi.models.set_comic_volume_cover import SetComicVolumeCover
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
    api_instance = comicking_openapi.ComicVolumeApi(api_client)
    comic_code = 'comic_code_example' # str | 
    volume_number = 'volume_number_example' # str | 
    ulid = 'ulid_example' # str | 
    set_comic_volume_cover = comicking_openapi.SetComicVolumeCover() # SetComicVolumeCover | 

    try:
        # Update volume comic cover.
        api_response = api_instance.update_comic_volume_cover(comic_code, volume_number, ulid, set_comic_volume_cover)
        print("The response of ComicVolumeApi->update_comic_volume_cover:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComicVolumeApi->update_comic_volume_cover: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **comic_code** | **str**|  | 
 **volume_number** | **str**|  | 
 **ulid** | **str**|  | 
 **set_comic_volume_cover** | [**SetComicVolumeCover**](SetComicVolumeCover.md)|  | 

### Return type

[**ComicVolumeCover**](ComicVolumeCover.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Comic volume cover updated. |  * Location -  <br>  |
**204** | Comic volume cover unmodified. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_comic_volume_title**
> ComicVolumeTitle update_comic_volume_title(comic_code, volume_number, ulid, set_comic_volume_title)

Update comic volume title.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import comicking_openapi
from comicking_openapi.models.comic_volume_title import ComicVolumeTitle
from comicking_openapi.models.set_comic_volume_title import SetComicVolumeTitle
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
    api_instance = comicking_openapi.ComicVolumeApi(api_client)
    comic_code = 'comic_code_example' # str | 
    volume_number = 'volume_number_example' # str | 
    ulid = 'ulid_example' # str | 
    set_comic_volume_title = comicking_openapi.SetComicVolumeTitle() # SetComicVolumeTitle | 

    try:
        # Update comic volume title.
        api_response = api_instance.update_comic_volume_title(comic_code, volume_number, ulid, set_comic_volume_title)
        print("The response of ComicVolumeApi->update_comic_volume_title:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComicVolumeApi->update_comic_volume_title: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **comic_code** | **str**|  | 
 **volume_number** | **str**|  | 
 **ulid** | **str**|  | 
 **set_comic_volume_title** | [**SetComicVolumeTitle**](SetComicVolumeTitle.md)|  | 

### Return type

[**ComicVolumeTitle**](ComicVolumeTitle.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Comic volume title updated. |  * Location -  <br>  |
**204** | Comic volume title unmodified. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

