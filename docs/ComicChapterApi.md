# comicking_openapi.ComicChapterApi

All URIs are relative to */api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_comic_chapter**](ComicChapterApi.md#add_comic_chapter) | **POST** /rest/comics/{comicCode}/chapters | Add comic chapter.
[**add_comic_chapter_title**](ComicChapterApi.md#add_comic_chapter_title) | **POST** /rest/comics/{comicCode}/chapters/{chapterNV}/titles | Add comic chapter title.
[**delete_comic_chapter**](ComicChapterApi.md#delete_comic_chapter) | **DELETE** /rest/comics/{comicCode}/chapters/{nv} | Delete comic chapter.
[**delete_comic_chapter_title**](ComicChapterApi.md#delete_comic_chapter_title) | **DELETE** /rest/comics/{comicCode}/chapters/{chapterNV}/titles/{ulid} | Delete comic chapter title.
[**get_comic_chapter**](ComicChapterApi.md#get_comic_chapter) | **GET** /rest/comics/{comicCode}/chapters/{nv} | Get comic chapter.
[**get_comic_chapter_title**](ComicChapterApi.md#get_comic_chapter_title) | **GET** /rest/comics/{comicCode}/chapters/{chapterNV}/titles/{ulid} | Get comic chapter title.
[**list_comic_chapter**](ComicChapterApi.md#list_comic_chapter) | **GET** /rest/comics/{comicCode}/chapters | List comic chapter.
[**list_comic_chapter_title**](ComicChapterApi.md#list_comic_chapter_title) | **GET** /rest/comics/{comicCode}/chapters/{chapterNV}/titles | List comic chapter title.
[**update_comic_chapter**](ComicChapterApi.md#update_comic_chapter) | **PATCH** /rest/comics/{comicCode}/chapters/{nv} | Update comic chapter.
[**update_comic_chapter_title**](ComicChapterApi.md#update_comic_chapter_title) | **PATCH** /rest/comics/{comicCode}/chapters/{chapterNV}/titles/{ulid} | Update comic chapter title.


# **add_comic_chapter**
> ComicChapter add_comic_chapter(comic_code, new_comic_chapter)

Add comic chapter.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import comicking_openapi
from comicking_openapi.models.comic_chapter import ComicChapter
from comicking_openapi.models.new_comic_chapter import NewComicChapter
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
    api_instance = comicking_openapi.ComicChapterApi(api_client)
    comic_code = 'comic_code_example' # str | 
    new_comic_chapter = comicking_openapi.NewComicChapter() # NewComicChapter | 

    try:
        # Add comic chapter.
        api_response = api_instance.add_comic_chapter(comic_code, new_comic_chapter)
        print("The response of ComicChapterApi->add_comic_chapter:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComicChapterApi->add_comic_chapter: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **comic_code** | **str**|  | 
 **new_comic_chapter** | [**NewComicChapter**](NewComicChapter.md)|  | 

### Return type

[**ComicChapter**](ComicChapter.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Comic chapter added. |  * Location -  <br>  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_comic_chapter_title**
> ComicChapterTitle add_comic_chapter_title(comic_code, chapter_nv, new_comic_chapter_title)

Add comic chapter title.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import comicking_openapi
from comicking_openapi.models.comic_chapter_title import ComicChapterTitle
from comicking_openapi.models.new_comic_chapter_title import NewComicChapterTitle
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
    api_instance = comicking_openapi.ComicChapterApi(api_client)
    comic_code = 'comic_code_example' # str | 
    chapter_nv = 'chapter_nv_example' # str | Number[+Version]
    new_comic_chapter_title = comicking_openapi.NewComicChapterTitle() # NewComicChapterTitle | 

    try:
        # Add comic chapter title.
        api_response = api_instance.add_comic_chapter_title(comic_code, chapter_nv, new_comic_chapter_title)
        print("The response of ComicChapterApi->add_comic_chapter_title:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComicChapterApi->add_comic_chapter_title: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **comic_code** | **str**|  | 
 **chapter_nv** | **str**| Number[+Version] | 
 **new_comic_chapter_title** | [**NewComicChapterTitle**](NewComicChapterTitle.md)|  | 

### Return type

[**ComicChapterTitle**](ComicChapterTitle.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Comic chapter title added. |  * Location -  <br>  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_comic_chapter**
> delete_comic_chapter(comic_code, nv)

Delete comic chapter.

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
    api_instance = comicking_openapi.ComicChapterApi(api_client)
    comic_code = 'comic_code_example' # str | 
    nv = 'nv_example' # str | Number[+Version]

    try:
        # Delete comic chapter.
        api_instance.delete_comic_chapter(comic_code, nv)
    except Exception as e:
        print("Exception when calling ComicChapterApi->delete_comic_chapter: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **comic_code** | **str**|  | 
 **nv** | **str**| Number[+Version] | 

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
**204** | Comic chapter deleted. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_comic_chapter_title**
> delete_comic_chapter_title(comic_code, chapter_nv, ulid)

Delete comic chapter title.

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
    api_instance = comicking_openapi.ComicChapterApi(api_client)
    comic_code = 'comic_code_example' # str | 
    chapter_nv = 'chapter_nv_example' # str | Number[+Version]
    ulid = 'ulid_example' # str | 

    try:
        # Delete comic chapter title.
        api_instance.delete_comic_chapter_title(comic_code, chapter_nv, ulid)
    except Exception as e:
        print("Exception when calling ComicChapterApi->delete_comic_chapter_title: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **comic_code** | **str**|  | 
 **chapter_nv** | **str**| Number[+Version] | 
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
**204** | Comic chapter title deleted. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_comic_chapter**
> ComicChapter get_comic_chapter(comic_code, nv)

Get comic chapter.

### Example


```python
import comicking_openapi
from comicking_openapi.models.comic_chapter import ComicChapter
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
    api_instance = comicking_openapi.ComicChapterApi(api_client)
    comic_code = 'comic_code_example' # str | 
    nv = 'nv_example' # str | Number[+Version]

    try:
        # Get comic chapter.
        api_response = api_instance.get_comic_chapter(comic_code, nv)
        print("The response of ComicChapterApi->get_comic_chapter:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComicChapterApi->get_comic_chapter: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **comic_code** | **str**|  | 
 **nv** | **str**| Number[+Version] | 

### Return type

[**ComicChapter**](ComicChapter.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Comic chapter gets. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_comic_chapter_title**
> ComicChapterTitle get_comic_chapter_title(comic_code, chapter_nv, ulid)

Get comic chapter title.

### Example


```python
import comicking_openapi
from comicking_openapi.models.comic_chapter_title import ComicChapterTitle
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
    api_instance = comicking_openapi.ComicChapterApi(api_client)
    comic_code = 'comic_code_example' # str | 
    chapter_nv = 'chapter_nv_example' # str | Number[+Version]
    ulid = 'ulid_example' # str | 

    try:
        # Get comic chapter title.
        api_response = api_instance.get_comic_chapter_title(comic_code, chapter_nv, ulid)
        print("The response of ComicChapterApi->get_comic_chapter_title:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComicChapterApi->get_comic_chapter_title: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **comic_code** | **str**|  | 
 **chapter_nv** | **str**| Number[+Version] | 
 **ulid** | **str**|  | 

### Return type

[**ComicChapterTitle**](ComicChapterTitle.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Comic chapter title gets. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_comic_chapter**
> List[ComicChapter] list_comic_chapter(comic_code, page=page, limit=limit, order=order, order_by=order_by, volume_number=volume_number)

List comic chapter.

### Example


```python
import comicking_openapi
from comicking_openapi.models.comic_chapter import ComicChapter
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
    api_instance = comicking_openapi.ComicChapterApi(api_client)
    comic_code = 'comic_code_example' # str | 
    page = 56 # int |  (optional)
    limit = 56 # int |  (optional)
    order = 'order_example' # str |  (optional)
    order_by = ['order_by_example'] # List[str] |  (optional)
    volume_number = ['volume_number_example'] # List[str] |  (optional)

    try:
        # List comic chapter.
        api_response = api_instance.list_comic_chapter(comic_code, page=page, limit=limit, order=order, order_by=order_by, volume_number=volume_number)
        print("The response of ComicChapterApi->list_comic_chapter:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComicChapterApi->list_comic_chapter: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **comic_code** | **str**|  | 
 **page** | **int**|  | [optional] 
 **limit** | **int**|  | [optional] 
 **order** | **str**|  | [optional] 
 **order_by** | [**List[str]**](str.md)|  | [optional] 
 **volume_number** | [**List[str]**](str.md)|  | [optional] 

### Return type

[**List[ComicChapter]**](ComicChapter.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Comic chapter list. |  * X-Total-Count -  <br>  * X-Pagination-Limit -  <br>  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_comic_chapter_title**
> List[ComicChapterTitle] list_comic_chapter_title(comic_code, chapter_nv, page=page, limit=limit, order=order, order_by=order_by)

List comic chapter title.

### Example


```python
import comicking_openapi
from comicking_openapi.models.comic_chapter_title import ComicChapterTitle
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
    api_instance = comicking_openapi.ComicChapterApi(api_client)
    comic_code = 'comic_code_example' # str | 
    chapter_nv = 'chapter_nv_example' # str | Number[+Version]
    page = 56 # int |  (optional)
    limit = 56 # int |  (optional)
    order = 'order_example' # str |  (optional)
    order_by = ['order_by_example'] # List[str] |  (optional)

    try:
        # List comic chapter title.
        api_response = api_instance.list_comic_chapter_title(comic_code, chapter_nv, page=page, limit=limit, order=order, order_by=order_by)
        print("The response of ComicChapterApi->list_comic_chapter_title:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComicChapterApi->list_comic_chapter_title: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **comic_code** | **str**|  | 
 **chapter_nv** | **str**| Number[+Version] | 
 **page** | **int**|  | [optional] 
 **limit** | **int**|  | [optional] 
 **order** | **str**|  | [optional] 
 **order_by** | [**List[str]**](str.md)|  | [optional] 

### Return type

[**List[ComicChapterTitle]**](ComicChapterTitle.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Comic chapter title list. |  * X-Total-Count -  <br>  * X-Pagination-Limit -  <br>  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_comic_chapter**
> ComicChapter update_comic_chapter(comic_code, nv, set_comic_chapter)

Update comic chapter.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import comicking_openapi
from comicking_openapi.models.comic_chapter import ComicChapter
from comicking_openapi.models.set_comic_chapter import SetComicChapter
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
    api_instance = comicking_openapi.ComicChapterApi(api_client)
    comic_code = 'comic_code_example' # str | 
    nv = 'nv_example' # str | Number[+Version]
    set_comic_chapter = comicking_openapi.SetComicChapter() # SetComicChapter | 

    try:
        # Update comic chapter.
        api_response = api_instance.update_comic_chapter(comic_code, nv, set_comic_chapter)
        print("The response of ComicChapterApi->update_comic_chapter:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComicChapterApi->update_comic_chapter: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **comic_code** | **str**|  | 
 **nv** | **str**| Number[+Version] | 
 **set_comic_chapter** | [**SetComicChapter**](SetComicChapter.md)|  | 

### Return type

[**ComicChapter**](ComicChapter.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Comic chapter updated. |  * Location -  <br>  |
**204** | Comic chapter unmodified. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_comic_chapter_title**
> ComicChapterTitle update_comic_chapter_title(comic_code, chapter_nv, ulid, set_comic_chapter_title)

Update comic chapter title.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import comicking_openapi
from comicking_openapi.models.comic_chapter_title import ComicChapterTitle
from comicking_openapi.models.set_comic_chapter_title import SetComicChapterTitle
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
    api_instance = comicking_openapi.ComicChapterApi(api_client)
    comic_code = 'comic_code_example' # str | 
    chapter_nv = 'chapter_nv_example' # str | Number[+Version]
    ulid = 'ulid_example' # str | 
    set_comic_chapter_title = comicking_openapi.SetComicChapterTitle() # SetComicChapterTitle | 

    try:
        # Update comic chapter title.
        api_response = api_instance.update_comic_chapter_title(comic_code, chapter_nv, ulid, set_comic_chapter_title)
        print("The response of ComicChapterApi->update_comic_chapter_title:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComicChapterApi->update_comic_chapter_title: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **comic_code** | **str**|  | 
 **chapter_nv** | **str**| Number[+Version] | 
 **ulid** | **str**|  | 
 **set_comic_chapter_title** | [**SetComicChapterTitle**](SetComicChapterTitle.md)|  | 

### Return type

[**ComicChapterTitle**](ComicChapterTitle.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Comic chapter title updated. |  * Location -  <br>  |
**204** | Comic chapter title unmodified. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

