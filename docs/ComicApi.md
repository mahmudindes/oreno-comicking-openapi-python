# comicking_openapi.ComicApi

All URIs are relative to */api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_comic**](ComicApi.md#add_comic) | **POST** /rest/comics | Add comic.
[**add_comic_author**](ComicApi.md#add_comic_author) | **POST** /rest/comics/{comicCode}/authors | Add comic author.
[**add_comic_author_note**](ComicApi.md#add_comic_author_note) | **POST** /rest/comics/{comicCode}/authors/{authorTypeCode}:{authorPersonCode}/notes | Add comic author note.
[**add_comic_author_type**](ComicApi.md#add_comic_author_type) | **POST** /rest/comic-author-types | Add comic author type.
[**add_comic_category**](ComicApi.md#add_comic_category) | **POST** /rest/comics/{comicCode}/categories | Add comic category.
[**add_comic_character**](ComicApi.md#add_comic_character) | **POST** /rest/comics/{comicCode}/characters | Add comic character.
[**add_comic_cover**](ComicApi.md#add_comic_cover) | **POST** /rest/comics/{comicCode}/covers | Add comic cover.
[**add_comic_external**](ComicApi.md#add_comic_external) | **POST** /rest/comics/{comicCode}/externals | Add comic external.
[**add_comic_relation**](ComicApi.md#add_comic_relation) | **POST** /rest/comics/{comicCode}/relations | Add comic relation.
[**add_comic_relation_type**](ComicApi.md#add_comic_relation_type) | **POST** /rest/comic-relation-types | Add comic relation type.
[**add_comic_serialization**](ComicApi.md#add_comic_serialization) | **POST** /rest/comics/{comicCode}/serializations | Add comic serialization.
[**add_comic_synopsis**](ComicApi.md#add_comic_synopsis) | **POST** /rest/comics/{comicCode}/synopses | Add comic synopsis.
[**add_comic_tag**](ComicApi.md#add_comic_tag) | **POST** /rest/comics/{comicCode}/tags | Add comic tag.
[**add_comic_title**](ComicApi.md#add_comic_title) | **POST** /rest/comics/{comicCode}/titles | Add comic title.
[**delete_comic**](ComicApi.md#delete_comic) | **DELETE** /rest/comics/{code} | Delete comic.
[**delete_comic_author**](ComicApi.md#delete_comic_author) | **DELETE** /rest/comics/{comicCode}/authors/{typeCode}:{personCode} | Delete comic author.
[**delete_comic_author_note**](ComicApi.md#delete_comic_author_note) | **DELETE** /rest/comics/{comicCode}/authors/{authorTypeCode}:{authorPersonCode}/notes/{ulid} | Delete comic author note.
[**delete_comic_author_type**](ComicApi.md#delete_comic_author_type) | **DELETE** /rest/comic-author-types/{code} | Delete comic author type.
[**delete_comic_category**](ComicApi.md#delete_comic_category) | **DELETE** /rest/comics/{comicCode}/categories/{categoryTypeCode}:{categoryCode} | Delete comic category.
[**delete_comic_character**](ComicApi.md#delete_comic_character) | **DELETE** /rest/comics/{comicCode}/characters/{characterCode} | Delete comic character.
[**delete_comic_cover**](ComicApi.md#delete_comic_cover) | **DELETE** /rest/comics/{comicCode}/covers/{ulid} | Delete comic cover.
[**delete_comic_external**](ComicApi.md#delete_comic_external) | **DELETE** /rest/comics/{comicCode}/externals/{ulid} | Delete comic external.
[**delete_comic_relation**](ComicApi.md#delete_comic_relation) | **DELETE** /rest/comics/{comicCode}/relations/{typeCode}:{childCode} | Delete comic relation.
[**delete_comic_relation_type**](ComicApi.md#delete_comic_relation_type) | **DELETE** /rest/comic-relation-types/{code} | Delete comic relation type.
[**delete_comic_serialization**](ComicApi.md#delete_comic_serialization) | **DELETE** /rest/comics/{comicCode}/serializations/{magazineCode} | Delete comic serialization.
[**delete_comic_synopsis**](ComicApi.md#delete_comic_synopsis) | **DELETE** /rest/comics/{comicCode}/synopses/{ulid} | Delete comic synopsis.
[**delete_comic_tag**](ComicApi.md#delete_comic_tag) | **DELETE** /rest/comics/{comicCode}/tags/{tagTypeCode}:{tagCode} | Delete comic tag.
[**delete_comic_title**](ComicApi.md#delete_comic_title) | **DELETE** /rest/comics/{comicCode}/titles/{ulid} | Delete comic title.
[**get_comic**](ComicApi.md#get_comic) | **GET** /rest/comics/{code} | Get comic.
[**get_comic_author**](ComicApi.md#get_comic_author) | **GET** /rest/comics/{comicCode}/authors/{typeCode}:{personCode} | Get comic author.
[**get_comic_author_note**](ComicApi.md#get_comic_author_note) | **GET** /rest/comics/{comicCode}/authors/{authorTypeCode}:{authorPersonCode}/notes/{ulid} | Get comic author note.
[**get_comic_author_type**](ComicApi.md#get_comic_author_type) | **GET** /rest/comic-author-types/{code} | Get comic author type.
[**get_comic_category**](ComicApi.md#get_comic_category) | **GET** /rest/comics/{comicCode}/categories/{categoryTypeCode}:{categoryCode} | Get comic category.
[**get_comic_character**](ComicApi.md#get_comic_character) | **GET** /rest/comics/{comicCode}/characters/{characterCode} | Get comic character.
[**get_comic_cover**](ComicApi.md#get_comic_cover) | **GET** /rest/comics/{comicCode}/covers/{ulid} | Get comic cover.
[**get_comic_external**](ComicApi.md#get_comic_external) | **GET** /rest/comics/{comicCode}/externals/{ulid} | Get comic external.
[**get_comic_relation**](ComicApi.md#get_comic_relation) | **GET** /rest/comics/{comicCode}/relations/{typeCode}:{childCode} | Get comic relation.
[**get_comic_relation_type**](ComicApi.md#get_comic_relation_type) | **GET** /rest/comic-relation-types/{code} | Get comic relation type.
[**get_comic_serialization**](ComicApi.md#get_comic_serialization) | **GET** /rest/comics/{comicCode}/serializations/{magazineCode} | Get comic serialization.
[**get_comic_synopsis**](ComicApi.md#get_comic_synopsis) | **GET** /rest/comics/{comicCode}/synopses/{ulid} | Get comic synopsis.
[**get_comic_tag**](ComicApi.md#get_comic_tag) | **GET** /rest/comics/{comicCode}/tags/{tagTypeCode}:{tagCode} | Get comic tag.
[**get_comic_title**](ComicApi.md#get_comic_title) | **GET** /rest/comics/{comicCode}/titles/{ulid} | Get comic title.
[**list_comic**](ComicApi.md#list_comic) | **GET** /rest/comics | List comic.
[**list_comic_author**](ComicApi.md#list_comic_author) | **GET** /rest/comics/{comicCode}/authors | List comic author.
[**list_comic_author_note**](ComicApi.md#list_comic_author_note) | **GET** /rest/comics/{comicCode}/authors/{authorTypeCode}:{authorPersonCode}/notes | List comic author note.
[**list_comic_author_type**](ComicApi.md#list_comic_author_type) | **GET** /rest/comic-author-types | List comic author type.
[**list_comic_category**](ComicApi.md#list_comic_category) | **GET** /rest/comics/{comicCode}/categories | List comic category.
[**list_comic_character**](ComicApi.md#list_comic_character) | **GET** /rest/comics/{comicCode}/characters | List comic character.
[**list_comic_cover**](ComicApi.md#list_comic_cover) | **GET** /rest/comics/{comicCode}/covers | List comic cover.
[**list_comic_external**](ComicApi.md#list_comic_external) | **GET** /rest/comics/{comicCode}/externals | List comic external.
[**list_comic_relation**](ComicApi.md#list_comic_relation) | **GET** /rest/comics/{comicCode}/relations | List comic relation.
[**list_comic_relation_type**](ComicApi.md#list_comic_relation_type) | **GET** /rest/comic-relation-types | List comic relation type.
[**list_comic_serialization**](ComicApi.md#list_comic_serialization) | **GET** /rest/comics/{comicCode}/serializations | List comic serialization.
[**list_comic_synopsis**](ComicApi.md#list_comic_synopsis) | **GET** /rest/comics/{comicCode}/synopses | List comic synopsis.
[**list_comic_tag**](ComicApi.md#list_comic_tag) | **GET** /rest/comics/{comicCode}/tags | List comic tag.
[**list_comic_title**](ComicApi.md#list_comic_title) | **GET** /rest/comics/{comicCode}/titles | List comic title.
[**update_comic**](ComicApi.md#update_comic) | **PATCH** /rest/comics/{code} | Update comic.
[**update_comic_author**](ComicApi.md#update_comic_author) | **PATCH** /rest/comics/{comicCode}/authors/{typeCode}:{personCode} | Update comic author.
[**update_comic_author_note**](ComicApi.md#update_comic_author_note) | **PATCH** /rest/comics/{comicCode}/authors/{authorTypeCode}:{authorPersonCode}/notes/{ulid} | Update comic author note.
[**update_comic_author_type**](ComicApi.md#update_comic_author_type) | **PATCH** /rest/comic-author-types/{code} | Update comic author type.
[**update_comic_category**](ComicApi.md#update_comic_category) | **PATCH** /rest/comics/{comicCode}/categories/{categoryTypeCode}:{categoryCode} | Update comic category.
[**update_comic_character**](ComicApi.md#update_comic_character) | **PATCH** /rest/comics/{comicCode}/characters/{characterCode} | Update comic character.
[**update_comic_cover**](ComicApi.md#update_comic_cover) | **PATCH** /rest/comics/{comicCode}/covers/{ulid} | Update comic cover.
[**update_comic_external**](ComicApi.md#update_comic_external) | **PATCH** /rest/comics/{comicCode}/externals/{ulid} | Update comic external.
[**update_comic_relation**](ComicApi.md#update_comic_relation) | **PATCH** /rest/comics/{comicCode}/relations/{typeCode}:{childCode} | Update comic relation.
[**update_comic_relation_type**](ComicApi.md#update_comic_relation_type) | **PATCH** /rest/comic-relation-types/{code} | Update comic relation type.
[**update_comic_serialization**](ComicApi.md#update_comic_serialization) | **PATCH** /rest/comics/{comicCode}/serializations/{magazineCode} | Update comic serialization.
[**update_comic_synopsis**](ComicApi.md#update_comic_synopsis) | **PATCH** /rest/comics/{comicCode}/synopses/{ulid} | Update comic synopsis.
[**update_comic_tag**](ComicApi.md#update_comic_tag) | **PATCH** /rest/comics/{comicCode}/tags/{tagTypeCode}:{tagCode} | Update comic tag.
[**update_comic_title**](ComicApi.md#update_comic_title) | **PATCH** /rest/comics/{comicCode}/titles/{ulid} | Update comic title.


# **add_comic**
> Comic add_comic(new_comic)

Add comic.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import comicking_openapi
from comicking_openapi.models.comic import Comic
from comicking_openapi.models.new_comic import NewComic
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
    api_instance = comicking_openapi.ComicApi(api_client)
    new_comic = comicking_openapi.NewComic() # NewComic | 

    try:
        # Add comic.
        api_response = api_instance.add_comic(new_comic)
        print("The response of ComicApi->add_comic:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComicApi->add_comic: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **new_comic** | [**NewComic**](NewComic.md)|  | 

### Return type

[**Comic**](Comic.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Comic added. |  * Location -  <br>  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_comic_author**
> ComicAuthor add_comic_author(comic_code, new_comic_author)

Add comic author.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import comicking_openapi
from comicking_openapi.models.comic_author import ComicAuthor
from comicking_openapi.models.new_comic_author import NewComicAuthor
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
    api_instance = comicking_openapi.ComicApi(api_client)
    comic_code = 'comic_code_example' # str | 
    new_comic_author = comicking_openapi.NewComicAuthor() # NewComicAuthor | 

    try:
        # Add comic author.
        api_response = api_instance.add_comic_author(comic_code, new_comic_author)
        print("The response of ComicApi->add_comic_author:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComicApi->add_comic_author: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **comic_code** | **str**|  | 
 **new_comic_author** | [**NewComicAuthor**](NewComicAuthor.md)|  | 

### Return type

[**ComicAuthor**](ComicAuthor.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Comic author added. |  * Location -  <br>  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_comic_author_note**
> ComicAuthorNote add_comic_author_note(comic_code, author_type_code, author_person_code, new_comic_author_note)

Add comic author note.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import comicking_openapi
from comicking_openapi.models.comic_author_note import ComicAuthorNote
from comicking_openapi.models.new_comic_author_note import NewComicAuthorNote
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
    api_instance = comicking_openapi.ComicApi(api_client)
    comic_code = 'comic_code_example' # str | 
    author_type_code = 'author_type_code_example' # str | 
    author_person_code = 'author_person_code_example' # str | 
    new_comic_author_note = comicking_openapi.NewComicAuthorNote() # NewComicAuthorNote | 

    try:
        # Add comic author note.
        api_response = api_instance.add_comic_author_note(comic_code, author_type_code, author_person_code, new_comic_author_note)
        print("The response of ComicApi->add_comic_author_note:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComicApi->add_comic_author_note: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **comic_code** | **str**|  | 
 **author_type_code** | **str**|  | 
 **author_person_code** | **str**|  | 
 **new_comic_author_note** | [**NewComicAuthorNote**](NewComicAuthorNote.md)|  | 

### Return type

[**ComicAuthorNote**](ComicAuthorNote.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Comic author note added. |  * Location -  <br>  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_comic_author_type**
> GenericType add_comic_author_type(new_generic_type)

Add comic author type.

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
    api_instance = comicking_openapi.ComicApi(api_client)
    new_generic_type = comicking_openapi.NewGenericType() # NewGenericType | 

    try:
        # Add comic author type.
        api_response = api_instance.add_comic_author_type(new_generic_type)
        print("The response of ComicApi->add_comic_author_type:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComicApi->add_comic_author_type: %s\n" % e)
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
**201** | Comic author type added. |  * Location -  <br>  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_comic_category**
> ComicCategory add_comic_category(comic_code, new_comic_category)

Add comic category.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import comicking_openapi
from comicking_openapi.models.comic_category import ComicCategory
from comicking_openapi.models.new_comic_category import NewComicCategory
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
    api_instance = comicking_openapi.ComicApi(api_client)
    comic_code = 'comic_code_example' # str | 
    new_comic_category = comicking_openapi.NewComicCategory() # NewComicCategory | 

    try:
        # Add comic category.
        api_response = api_instance.add_comic_category(comic_code, new_comic_category)
        print("The response of ComicApi->add_comic_category:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComicApi->add_comic_category: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **comic_code** | **str**|  | 
 **new_comic_category** | [**NewComicCategory**](NewComicCategory.md)|  | 

### Return type

[**ComicCategory**](ComicCategory.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Comic category added. |  * Location -  <br>  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_comic_character**
> ComicCharacter add_comic_character(comic_code, new_comic_character)

Add comic character.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import comicking_openapi
from comicking_openapi.models.comic_character import ComicCharacter
from comicking_openapi.models.new_comic_character import NewComicCharacter
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
    api_instance = comicking_openapi.ComicApi(api_client)
    comic_code = 'comic_code_example' # str | 
    new_comic_character = comicking_openapi.NewComicCharacter() # NewComicCharacter | 

    try:
        # Add comic character.
        api_response = api_instance.add_comic_character(comic_code, new_comic_character)
        print("The response of ComicApi->add_comic_character:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComicApi->add_comic_character: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **comic_code** | **str**|  | 
 **new_comic_character** | [**NewComicCharacter**](NewComicCharacter.md)|  | 

### Return type

[**ComicCharacter**](ComicCharacter.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Comic character added. |  * Location -  <br>  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_comic_cover**
> ComicCover add_comic_cover(comic_code, new_comic_cover)

Add comic cover.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import comicking_openapi
from comicking_openapi.models.comic_cover import ComicCover
from comicking_openapi.models.new_comic_cover import NewComicCover
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
    api_instance = comicking_openapi.ComicApi(api_client)
    comic_code = 'comic_code_example' # str | 
    new_comic_cover = comicking_openapi.NewComicCover() # NewComicCover | 

    try:
        # Add comic cover.
        api_response = api_instance.add_comic_cover(comic_code, new_comic_cover)
        print("The response of ComicApi->add_comic_cover:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComicApi->add_comic_cover: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **comic_code** | **str**|  | 
 **new_comic_cover** | [**NewComicCover**](NewComicCover.md)|  | 

### Return type

[**ComicCover**](ComicCover.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Comic cover added. |  * Location -  <br>  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_comic_external**
> ComicExternal add_comic_external(comic_code, new_comic_external)

Add comic external.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import comicking_openapi
from comicking_openapi.models.comic_external import ComicExternal
from comicking_openapi.models.new_comic_external import NewComicExternal
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
    api_instance = comicking_openapi.ComicApi(api_client)
    comic_code = 'comic_code_example' # str | 
    new_comic_external = comicking_openapi.NewComicExternal() # NewComicExternal | 

    try:
        # Add comic external.
        api_response = api_instance.add_comic_external(comic_code, new_comic_external)
        print("The response of ComicApi->add_comic_external:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComicApi->add_comic_external: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **comic_code** | **str**|  | 
 **new_comic_external** | [**NewComicExternal**](NewComicExternal.md)|  | 

### Return type

[**ComicExternal**](ComicExternal.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Comic external added. |  * Location -  <br>  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_comic_relation**
> ComicRelation add_comic_relation(comic_code, new_comic_relation)

Add comic relation.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import comicking_openapi
from comicking_openapi.models.comic_relation import ComicRelation
from comicking_openapi.models.new_comic_relation import NewComicRelation
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
    api_instance = comicking_openapi.ComicApi(api_client)
    comic_code = 'comic_code_example' # str | 
    new_comic_relation = comicking_openapi.NewComicRelation() # NewComicRelation | 

    try:
        # Add comic relation.
        api_response = api_instance.add_comic_relation(comic_code, new_comic_relation)
        print("The response of ComicApi->add_comic_relation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComicApi->add_comic_relation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **comic_code** | **str**|  | 
 **new_comic_relation** | [**NewComicRelation**](NewComicRelation.md)|  | 

### Return type

[**ComicRelation**](ComicRelation.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Comic relation added. |  * Location -  <br>  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_comic_relation_type**
> GenericType add_comic_relation_type(new_generic_type)

Add comic relation type.

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
    api_instance = comicking_openapi.ComicApi(api_client)
    new_generic_type = comicking_openapi.NewGenericType() # NewGenericType | 

    try:
        # Add comic relation type.
        api_response = api_instance.add_comic_relation_type(new_generic_type)
        print("The response of ComicApi->add_comic_relation_type:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComicApi->add_comic_relation_type: %s\n" % e)
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
**201** | Comic relation type added. |  * Location -  <br>  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_comic_serialization**
> ComicSerialization add_comic_serialization(comic_code, new_comic_serialization)

Add comic serialization.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import comicking_openapi
from comicking_openapi.models.comic_serialization import ComicSerialization
from comicking_openapi.models.new_comic_serialization import NewComicSerialization
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
    api_instance = comicking_openapi.ComicApi(api_client)
    comic_code = 'comic_code_example' # str | 
    new_comic_serialization = comicking_openapi.NewComicSerialization() # NewComicSerialization | 

    try:
        # Add comic serialization.
        api_response = api_instance.add_comic_serialization(comic_code, new_comic_serialization)
        print("The response of ComicApi->add_comic_serialization:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComicApi->add_comic_serialization: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **comic_code** | **str**|  | 
 **new_comic_serialization** | [**NewComicSerialization**](NewComicSerialization.md)|  | 

### Return type

[**ComicSerialization**](ComicSerialization.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Comic serialization added. |  * Location -  <br>  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_comic_synopsis**
> ComicSynopsis add_comic_synopsis(comic_code, new_comic_synopsis)

Add comic synopsis.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import comicking_openapi
from comicking_openapi.models.comic_synopsis import ComicSynopsis
from comicking_openapi.models.new_comic_synopsis import NewComicSynopsis
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
    api_instance = comicking_openapi.ComicApi(api_client)
    comic_code = 'comic_code_example' # str | 
    new_comic_synopsis = comicking_openapi.NewComicSynopsis() # NewComicSynopsis | 

    try:
        # Add comic synopsis.
        api_response = api_instance.add_comic_synopsis(comic_code, new_comic_synopsis)
        print("The response of ComicApi->add_comic_synopsis:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComicApi->add_comic_synopsis: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **comic_code** | **str**|  | 
 **new_comic_synopsis** | [**NewComicSynopsis**](NewComicSynopsis.md)|  | 

### Return type

[**ComicSynopsis**](ComicSynopsis.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Comic synopsis added. |  * Location -  <br>  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_comic_tag**
> ComicTag add_comic_tag(comic_code, new_comic_tag)

Add comic tag.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import comicking_openapi
from comicking_openapi.models.comic_tag import ComicTag
from comicking_openapi.models.new_comic_tag import NewComicTag
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
    api_instance = comicking_openapi.ComicApi(api_client)
    comic_code = 'comic_code_example' # str | 
    new_comic_tag = comicking_openapi.NewComicTag() # NewComicTag | 

    try:
        # Add comic tag.
        api_response = api_instance.add_comic_tag(comic_code, new_comic_tag)
        print("The response of ComicApi->add_comic_tag:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComicApi->add_comic_tag: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **comic_code** | **str**|  | 
 **new_comic_tag** | [**NewComicTag**](NewComicTag.md)|  | 

### Return type

[**ComicTag**](ComicTag.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Comic tag added. |  * Location -  <br>  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_comic_title**
> ComicTitle add_comic_title(comic_code, new_comic_title)

Add comic title.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import comicking_openapi
from comicking_openapi.models.comic_title import ComicTitle
from comicking_openapi.models.new_comic_title import NewComicTitle
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
    api_instance = comicking_openapi.ComicApi(api_client)
    comic_code = 'comic_code_example' # str | 
    new_comic_title = comicking_openapi.NewComicTitle() # NewComicTitle | 

    try:
        # Add comic title.
        api_response = api_instance.add_comic_title(comic_code, new_comic_title)
        print("The response of ComicApi->add_comic_title:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComicApi->add_comic_title: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **comic_code** | **str**|  | 
 **new_comic_title** | [**NewComicTitle**](NewComicTitle.md)|  | 

### Return type

[**ComicTitle**](ComicTitle.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Comic title added. |  * Location -  <br>  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_comic**
> delete_comic(code)

Delete comic.

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
    api_instance = comicking_openapi.ComicApi(api_client)
    code = 'code_example' # str | 

    try:
        # Delete comic.
        api_instance.delete_comic(code)
    except Exception as e:
        print("Exception when calling ComicApi->delete_comic: %s\n" % e)
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
**204** | Comic deleted. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_comic_author**
> delete_comic_author(comic_code, type_code, person_code)

Delete comic author.

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
    api_instance = comicking_openapi.ComicApi(api_client)
    comic_code = 'comic_code_example' # str | 
    type_code = 'type_code_example' # str | 
    person_code = 'person_code_example' # str | 

    try:
        # Delete comic author.
        api_instance.delete_comic_author(comic_code, type_code, person_code)
    except Exception as e:
        print("Exception when calling ComicApi->delete_comic_author: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **comic_code** | **str**|  | 
 **type_code** | **str**|  | 
 **person_code** | **str**|  | 

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
**204** | Comic author deleted. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_comic_author_note**
> delete_comic_author_note(comic_code, author_type_code, author_person_code, ulid)

Delete comic author note.

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
    api_instance = comicking_openapi.ComicApi(api_client)
    comic_code = 'comic_code_example' # str | 
    author_type_code = 'author_type_code_example' # str | 
    author_person_code = 'author_person_code_example' # str | 
    ulid = 'ulid_example' # str | 

    try:
        # Delete comic author note.
        api_instance.delete_comic_author_note(comic_code, author_type_code, author_person_code, ulid)
    except Exception as e:
        print("Exception when calling ComicApi->delete_comic_author_note: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **comic_code** | **str**|  | 
 **author_type_code** | **str**|  | 
 **author_person_code** | **str**|  | 
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
**204** | Comic author note deleted. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_comic_author_type**
> delete_comic_author_type(code)

Delete comic author type.

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
    api_instance = comicking_openapi.ComicApi(api_client)
    code = 'code_example' # str | 

    try:
        # Delete comic author type.
        api_instance.delete_comic_author_type(code)
    except Exception as e:
        print("Exception when calling ComicApi->delete_comic_author_type: %s\n" % e)
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
**204** | Comic author type deleted. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_comic_category**
> delete_comic_category(comic_code, category_type_code, category_code)

Delete comic category.

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
    api_instance = comicking_openapi.ComicApi(api_client)
    comic_code = 'comic_code_example' # str | 
    category_type_code = 'category_type_code_example' # str | 
    category_code = 'category_code_example' # str | 

    try:
        # Delete comic category.
        api_instance.delete_comic_category(comic_code, category_type_code, category_code)
    except Exception as e:
        print("Exception when calling ComicApi->delete_comic_category: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **comic_code** | **str**|  | 
 **category_type_code** | **str**|  | 
 **category_code** | **str**|  | 

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
**204** | Comic category deleted. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_comic_character**
> delete_comic_character(comic_code, character_code)

Delete comic character.

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
    api_instance = comicking_openapi.ComicApi(api_client)
    comic_code = 'comic_code_example' # str | 
    character_code = 'character_code_example' # str | 

    try:
        # Delete comic character.
        api_instance.delete_comic_character(comic_code, character_code)
    except Exception as e:
        print("Exception when calling ComicApi->delete_comic_character: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **comic_code** | **str**|  | 
 **character_code** | **str**|  | 

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
**204** | Comic character deleted. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_comic_cover**
> delete_comic_cover(comic_code, ulid)

Delete comic cover.

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
    api_instance = comicking_openapi.ComicApi(api_client)
    comic_code = 'comic_code_example' # str | 
    ulid = 'ulid_example' # str | 

    try:
        # Delete comic cover.
        api_instance.delete_comic_cover(comic_code, ulid)
    except Exception as e:
        print("Exception when calling ComicApi->delete_comic_cover: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **comic_code** | **str**|  | 
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
**204** | Comic cover deleted. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_comic_external**
> delete_comic_external(comic_code, ulid)

Delete comic external.

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
    api_instance = comicking_openapi.ComicApi(api_client)
    comic_code = 'comic_code_example' # str | 
    ulid = 'ulid_example' # str | 

    try:
        # Delete comic external.
        api_instance.delete_comic_external(comic_code, ulid)
    except Exception as e:
        print("Exception when calling ComicApi->delete_comic_external: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **comic_code** | **str**|  | 
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
**204** | Comic external deleted. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_comic_relation**
> delete_comic_relation(comic_code, type_code, child_code)

Delete comic relation.

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
    api_instance = comicking_openapi.ComicApi(api_client)
    comic_code = 'comic_code_example' # str | 
    type_code = 'type_code_example' # str | 
    child_code = 'child_code_example' # str | 

    try:
        # Delete comic relation.
        api_instance.delete_comic_relation(comic_code, type_code, child_code)
    except Exception as e:
        print("Exception when calling ComicApi->delete_comic_relation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **comic_code** | **str**|  | 
 **type_code** | **str**|  | 
 **child_code** | **str**|  | 

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
**204** | Comic relation deleted. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_comic_relation_type**
> delete_comic_relation_type(code)

Delete comic relation type.

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
    api_instance = comicking_openapi.ComicApi(api_client)
    code = 'code_example' # str | 

    try:
        # Delete comic relation type.
        api_instance.delete_comic_relation_type(code)
    except Exception as e:
        print("Exception when calling ComicApi->delete_comic_relation_type: %s\n" % e)
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
**204** | Comic relation type deleted. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_comic_serialization**
> delete_comic_serialization(comic_code, magazine_code)

Delete comic serialization.

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
    api_instance = comicking_openapi.ComicApi(api_client)
    comic_code = 'comic_code_example' # str | 
    magazine_code = 'magazine_code_example' # str | 

    try:
        # Delete comic serialization.
        api_instance.delete_comic_serialization(comic_code, magazine_code)
    except Exception as e:
        print("Exception when calling ComicApi->delete_comic_serialization: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **comic_code** | **str**|  | 
 **magazine_code** | **str**|  | 

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
**204** | Comic serialization deleted. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_comic_synopsis**
> delete_comic_synopsis(comic_code, ulid)

Delete comic synopsis.

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
    api_instance = comicking_openapi.ComicApi(api_client)
    comic_code = 'comic_code_example' # str | 
    ulid = 'ulid_example' # str | 

    try:
        # Delete comic synopsis.
        api_instance.delete_comic_synopsis(comic_code, ulid)
    except Exception as e:
        print("Exception when calling ComicApi->delete_comic_synopsis: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **comic_code** | **str**|  | 
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
**204** | Comic synopsis deleted. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_comic_tag**
> delete_comic_tag(comic_code, tag_type_code, tag_code)

Delete comic tag.

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
    api_instance = comicking_openapi.ComicApi(api_client)
    comic_code = 'comic_code_example' # str | 
    tag_type_code = 'tag_type_code_example' # str | 
    tag_code = 'tag_code_example' # str | 

    try:
        # Delete comic tag.
        api_instance.delete_comic_tag(comic_code, tag_type_code, tag_code)
    except Exception as e:
        print("Exception when calling ComicApi->delete_comic_tag: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **comic_code** | **str**|  | 
 **tag_type_code** | **str**|  | 
 **tag_code** | **str**|  | 

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
**204** | Comic tag deleted. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_comic_title**
> delete_comic_title(comic_code, ulid)

Delete comic title.

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
    api_instance = comicking_openapi.ComicApi(api_client)
    comic_code = 'comic_code_example' # str | 
    ulid = 'ulid_example' # str | 

    try:
        # Delete comic title.
        api_instance.delete_comic_title(comic_code, ulid)
    except Exception as e:
        print("Exception when calling ComicApi->delete_comic_title: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **comic_code** | **str**|  | 
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
**204** | Comic title deleted. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_comic**
> Comic get_comic(code)

Get comic.

### Example


```python
import comicking_openapi
from comicking_openapi.models.comic import Comic
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
    api_instance = comicking_openapi.ComicApi(api_client)
    code = 'code_example' # str | 

    try:
        # Get comic.
        api_response = api_instance.get_comic(code)
        print("The response of ComicApi->get_comic:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComicApi->get_comic: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**|  | 

### Return type

[**Comic**](Comic.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Comic gets. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_comic_author**
> ComicAuthor get_comic_author(comic_code, type_code, person_code)

Get comic author.

### Example


```python
import comicking_openapi
from comicking_openapi.models.comic_author import ComicAuthor
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
    api_instance = comicking_openapi.ComicApi(api_client)
    comic_code = 'comic_code_example' # str | 
    type_code = 'type_code_example' # str | 
    person_code = 'person_code_example' # str | 

    try:
        # Get comic author.
        api_response = api_instance.get_comic_author(comic_code, type_code, person_code)
        print("The response of ComicApi->get_comic_author:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComicApi->get_comic_author: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **comic_code** | **str**|  | 
 **type_code** | **str**|  | 
 **person_code** | **str**|  | 

### Return type

[**ComicAuthor**](ComicAuthor.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Comic author gets. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_comic_author_note**
> ComicAuthorNote get_comic_author_note(comic_code, author_type_code, author_person_code, ulid)

Get comic author note.

### Example


```python
import comicking_openapi
from comicking_openapi.models.comic_author_note import ComicAuthorNote
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
    api_instance = comicking_openapi.ComicApi(api_client)
    comic_code = 'comic_code_example' # str | 
    author_type_code = 'author_type_code_example' # str | 
    author_person_code = 'author_person_code_example' # str | 
    ulid = 'ulid_example' # str | 

    try:
        # Get comic author note.
        api_response = api_instance.get_comic_author_note(comic_code, author_type_code, author_person_code, ulid)
        print("The response of ComicApi->get_comic_author_note:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComicApi->get_comic_author_note: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **comic_code** | **str**|  | 
 **author_type_code** | **str**|  | 
 **author_person_code** | **str**|  | 
 **ulid** | **str**|  | 

### Return type

[**ComicAuthorNote**](ComicAuthorNote.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Comic author note gets. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_comic_author_type**
> GenericType get_comic_author_type(code)

Get comic author type.

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
    api_instance = comicking_openapi.ComicApi(api_client)
    code = 'code_example' # str | 

    try:
        # Get comic author type.
        api_response = api_instance.get_comic_author_type(code)
        print("The response of ComicApi->get_comic_author_type:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComicApi->get_comic_author_type: %s\n" % e)
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
**200** | Comic author type gets. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_comic_category**
> ComicCategory get_comic_category(comic_code, category_type_code, category_code)

Get comic category.

### Example


```python
import comicking_openapi
from comicking_openapi.models.comic_category import ComicCategory
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
    api_instance = comicking_openapi.ComicApi(api_client)
    comic_code = 'comic_code_example' # str | 
    category_type_code = 'category_type_code_example' # str | 
    category_code = 'category_code_example' # str | 

    try:
        # Get comic category.
        api_response = api_instance.get_comic_category(comic_code, category_type_code, category_code)
        print("The response of ComicApi->get_comic_category:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComicApi->get_comic_category: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **comic_code** | **str**|  | 
 **category_type_code** | **str**|  | 
 **category_code** | **str**|  | 

### Return type

[**ComicCategory**](ComicCategory.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Comic category gets. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_comic_character**
> ComicCharacter get_comic_character(comic_code, character_code)

Get comic character.

### Example


```python
import comicking_openapi
from comicking_openapi.models.comic_character import ComicCharacter
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
    api_instance = comicking_openapi.ComicApi(api_client)
    comic_code = 'comic_code_example' # str | 
    character_code = 'character_code_example' # str | 

    try:
        # Get comic character.
        api_response = api_instance.get_comic_character(comic_code, character_code)
        print("The response of ComicApi->get_comic_character:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComicApi->get_comic_character: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **comic_code** | **str**|  | 
 **character_code** | **str**|  | 

### Return type

[**ComicCharacter**](ComicCharacter.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Comic character gets. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_comic_cover**
> ComicCover get_comic_cover(comic_code, ulid)

Get comic cover.

### Example


```python
import comicking_openapi
from comicking_openapi.models.comic_cover import ComicCover
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
    api_instance = comicking_openapi.ComicApi(api_client)
    comic_code = 'comic_code_example' # str | 
    ulid = 'ulid_example' # str | 

    try:
        # Get comic cover.
        api_response = api_instance.get_comic_cover(comic_code, ulid)
        print("The response of ComicApi->get_comic_cover:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComicApi->get_comic_cover: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **comic_code** | **str**|  | 
 **ulid** | **str**|  | 

### Return type

[**ComicCover**](ComicCover.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Comic cover gets. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_comic_external**
> ComicExternal get_comic_external(comic_code, ulid)

Get comic external.

### Example


```python
import comicking_openapi
from comicking_openapi.models.comic_external import ComicExternal
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
    api_instance = comicking_openapi.ComicApi(api_client)
    comic_code = 'comic_code_example' # str | 
    ulid = 'ulid_example' # str | 

    try:
        # Get comic external.
        api_response = api_instance.get_comic_external(comic_code, ulid)
        print("The response of ComicApi->get_comic_external:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComicApi->get_comic_external: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **comic_code** | **str**|  | 
 **ulid** | **str**|  | 

### Return type

[**ComicExternal**](ComicExternal.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Comic external gets. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_comic_relation**
> ComicRelation get_comic_relation(comic_code, type_code, child_code)

Get comic relation.

### Example


```python
import comicking_openapi
from comicking_openapi.models.comic_relation import ComicRelation
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
    api_instance = comicking_openapi.ComicApi(api_client)
    comic_code = 'comic_code_example' # str | 
    type_code = 'type_code_example' # str | 
    child_code = 'child_code_example' # str | 

    try:
        # Get comic relation.
        api_response = api_instance.get_comic_relation(comic_code, type_code, child_code)
        print("The response of ComicApi->get_comic_relation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComicApi->get_comic_relation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **comic_code** | **str**|  | 
 **type_code** | **str**|  | 
 **child_code** | **str**|  | 

### Return type

[**ComicRelation**](ComicRelation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Comic relation gets. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_comic_relation_type**
> GenericType get_comic_relation_type(code)

Get comic relation type.

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
    api_instance = comicking_openapi.ComicApi(api_client)
    code = 'code_example' # str | 

    try:
        # Get comic relation type.
        api_response = api_instance.get_comic_relation_type(code)
        print("The response of ComicApi->get_comic_relation_type:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComicApi->get_comic_relation_type: %s\n" % e)
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
**200** | Comic relation type gets. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_comic_serialization**
> ComicSerialization get_comic_serialization(comic_code, magazine_code)

Get comic serialization.

### Example


```python
import comicking_openapi
from comicking_openapi.models.comic_serialization import ComicSerialization
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
    api_instance = comicking_openapi.ComicApi(api_client)
    comic_code = 'comic_code_example' # str | 
    magazine_code = 'magazine_code_example' # str | 

    try:
        # Get comic serialization.
        api_response = api_instance.get_comic_serialization(comic_code, magazine_code)
        print("The response of ComicApi->get_comic_serialization:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComicApi->get_comic_serialization: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **comic_code** | **str**|  | 
 **magazine_code** | **str**|  | 

### Return type

[**ComicSerialization**](ComicSerialization.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Comic serialization gets. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_comic_synopsis**
> ComicSynopsis get_comic_synopsis(comic_code, ulid)

Get comic synopsis.

### Example


```python
import comicking_openapi
from comicking_openapi.models.comic_synopsis import ComicSynopsis
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
    api_instance = comicking_openapi.ComicApi(api_client)
    comic_code = 'comic_code_example' # str | 
    ulid = 'ulid_example' # str | 

    try:
        # Get comic synopsis.
        api_response = api_instance.get_comic_synopsis(comic_code, ulid)
        print("The response of ComicApi->get_comic_synopsis:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComicApi->get_comic_synopsis: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **comic_code** | **str**|  | 
 **ulid** | **str**|  | 

### Return type

[**ComicSynopsis**](ComicSynopsis.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Comic synopsis gets. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_comic_tag**
> ComicTag get_comic_tag(comic_code, tag_type_code, tag_code)

Get comic tag.

### Example


```python
import comicking_openapi
from comicking_openapi.models.comic_tag import ComicTag
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
    api_instance = comicking_openapi.ComicApi(api_client)
    comic_code = 'comic_code_example' # str | 
    tag_type_code = 'tag_type_code_example' # str | 
    tag_code = 'tag_code_example' # str | 

    try:
        # Get comic tag.
        api_response = api_instance.get_comic_tag(comic_code, tag_type_code, tag_code)
        print("The response of ComicApi->get_comic_tag:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComicApi->get_comic_tag: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **comic_code** | **str**|  | 
 **tag_type_code** | **str**|  | 
 **tag_code** | **str**|  | 

### Return type

[**ComicTag**](ComicTag.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Comic tag gets. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_comic_title**
> ComicTitle get_comic_title(comic_code, ulid)

Get comic title.

### Example


```python
import comicking_openapi
from comicking_openapi.models.comic_title import ComicTitle
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
    api_instance = comicking_openapi.ComicApi(api_client)
    comic_code = 'comic_code_example' # str | 
    ulid = 'ulid_example' # str | 

    try:
        # Get comic title.
        api_response = api_instance.get_comic_title(comic_code, ulid)
        print("The response of ComicApi->get_comic_title:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComicApi->get_comic_title: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **comic_code** | **str**|  | 
 **ulid** | **str**|  | 

### Return type

[**ComicTitle**](ComicTitle.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Comic title gets. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_comic**
> List[Comic] list_comic(page=page, limit=limit, order=order, order_by=order_by, external=external)

List comic.

### Example


```python
import comicking_openapi
from comicking_openapi.models.comic import Comic
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
    api_instance = comicking_openapi.ComicApi(api_client)
    page = 56 # int |  (optional)
    limit = 56 # int |  (optional)
    order = 'order_example' # str |  (optional)
    order_by = ['order_by_example'] # List[str] |  (optional)
    external = ['external_example'] # List[str] |  (optional)

    try:
        # List comic.
        api_response = api_instance.list_comic(page=page, limit=limit, order=order, order_by=order_by, external=external)
        print("The response of ComicApi->list_comic:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComicApi->list_comic: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] 
 **limit** | **int**|  | [optional] 
 **order** | **str**|  | [optional] 
 **order_by** | [**List[str]**](str.md)|  | [optional] 
 **external** | [**List[str]**](str.md)|  | [optional] 

### Return type

[**List[Comic]**](Comic.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Comic list. |  * X-Total-Count -  <br>  * X-Pagination-Limit -  <br>  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_comic_author**
> List[ComicAuthor] list_comic_author(comic_code, page=page, limit=limit, order=order, order_by=order_by, type_code=type_code)

List comic author.

### Example


```python
import comicking_openapi
from comicking_openapi.models.comic_author import ComicAuthor
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
    api_instance = comicking_openapi.ComicApi(api_client)
    comic_code = 'comic_code_example' # str | 
    page = 56 # int |  (optional)
    limit = 56 # int |  (optional)
    order = 'order_example' # str |  (optional)
    order_by = ['order_by_example'] # List[str] |  (optional)
    type_code = ['type_code_example'] # List[str] |  (optional)

    try:
        # List comic author.
        api_response = api_instance.list_comic_author(comic_code, page=page, limit=limit, order=order, order_by=order_by, type_code=type_code)
        print("The response of ComicApi->list_comic_author:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComicApi->list_comic_author: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **comic_code** | **str**|  | 
 **page** | **int**|  | [optional] 
 **limit** | **int**|  | [optional] 
 **order** | **str**|  | [optional] 
 **order_by** | [**List[str]**](str.md)|  | [optional] 
 **type_code** | [**List[str]**](str.md)|  | [optional] 

### Return type

[**List[ComicAuthor]**](ComicAuthor.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Comic author list. |  * X-Total-Count -  <br>  * X-Pagination-Limit -  <br>  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_comic_author_note**
> List[ComicAuthorNote] list_comic_author_note(comic_code, author_type_code, author_person_code, page=page, limit=limit, order=order, order_by=order_by)

List comic author note.

### Example


```python
import comicking_openapi
from comicking_openapi.models.comic_author_note import ComicAuthorNote
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
    api_instance = comicking_openapi.ComicApi(api_client)
    comic_code = 'comic_code_example' # str | 
    author_type_code = 'author_type_code_example' # str | 
    author_person_code = 'author_person_code_example' # str | 
    page = 56 # int |  (optional)
    limit = 56 # int |  (optional)
    order = 'order_example' # str |  (optional)
    order_by = ['order_by_example'] # List[str] |  (optional)

    try:
        # List comic author note.
        api_response = api_instance.list_comic_author_note(comic_code, author_type_code, author_person_code, page=page, limit=limit, order=order, order_by=order_by)
        print("The response of ComicApi->list_comic_author_note:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComicApi->list_comic_author_note: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **comic_code** | **str**|  | 
 **author_type_code** | **str**|  | 
 **author_person_code** | **str**|  | 
 **page** | **int**|  | [optional] 
 **limit** | **int**|  | [optional] 
 **order** | **str**|  | [optional] 
 **order_by** | [**List[str]**](str.md)|  | [optional] 

### Return type

[**List[ComicAuthorNote]**](ComicAuthorNote.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Comic author note list. |  * X-Total-Count -  <br>  * X-Pagination-Limit -  <br>  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_comic_author_type**
> List[GenericType] list_comic_author_type(page=page, limit=limit, order=order, order_by=order_by)

List comic author type.

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
    api_instance = comicking_openapi.ComicApi(api_client)
    page = 56 # int |  (optional)
    limit = 56 # int |  (optional)
    order = 'order_example' # str |  (optional)
    order_by = ['order_by_example'] # List[str] |  (optional)

    try:
        # List comic author type.
        api_response = api_instance.list_comic_author_type(page=page, limit=limit, order=order, order_by=order_by)
        print("The response of ComicApi->list_comic_author_type:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComicApi->list_comic_author_type: %s\n" % e)
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
**200** | Comic author type list. |  * X-Total-Count -  <br>  * X-Pagination-Limit -  <br>  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_comic_category**
> List[ComicCategory] list_comic_category(comic_code, page=page, limit=limit, order=order, order_by=order_by, category_type_code=category_type_code)

List comic category.

### Example


```python
import comicking_openapi
from comicking_openapi.models.comic_category import ComicCategory
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
    api_instance = comicking_openapi.ComicApi(api_client)
    comic_code = 'comic_code_example' # str | 
    page = 56 # int |  (optional)
    limit = 56 # int |  (optional)
    order = 'order_example' # str |  (optional)
    order_by = ['order_by_example'] # List[str] |  (optional)
    category_type_code = ['category_type_code_example'] # List[str] |  (optional)

    try:
        # List comic category.
        api_response = api_instance.list_comic_category(comic_code, page=page, limit=limit, order=order, order_by=order_by, category_type_code=category_type_code)
        print("The response of ComicApi->list_comic_category:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComicApi->list_comic_category: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **comic_code** | **str**|  | 
 **page** | **int**|  | [optional] 
 **limit** | **int**|  | [optional] 
 **order** | **str**|  | [optional] 
 **order_by** | [**List[str]**](str.md)|  | [optional] 
 **category_type_code** | [**List[str]**](str.md)|  | [optional] 

### Return type

[**List[ComicCategory]**](ComicCategory.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Comic category list. |  * X-Total-Count -  <br>  * X-Pagination-Limit -  <br>  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_comic_character**
> List[ComicCharacter] list_comic_character(comic_code, page=page, limit=limit, order=order, order_by=order_by)

List comic character.

### Example


```python
import comicking_openapi
from comicking_openapi.models.comic_character import ComicCharacter
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
    api_instance = comicking_openapi.ComicApi(api_client)
    comic_code = 'comic_code_example' # str | 
    page = 56 # int |  (optional)
    limit = 56 # int |  (optional)
    order = 'order_example' # str |  (optional)
    order_by = ['order_by_example'] # List[str] |  (optional)

    try:
        # List comic character.
        api_response = api_instance.list_comic_character(comic_code, page=page, limit=limit, order=order, order_by=order_by)
        print("The response of ComicApi->list_comic_character:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComicApi->list_comic_character: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **comic_code** | **str**|  | 
 **page** | **int**|  | [optional] 
 **limit** | **int**|  | [optional] 
 **order** | **str**|  | [optional] 
 **order_by** | [**List[str]**](str.md)|  | [optional] 

### Return type

[**List[ComicCharacter]**](ComicCharacter.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Comic character list. |  * X-Total-Count -  <br>  * X-Pagination-Limit -  <br>  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_comic_cover**
> List[ComicCover] list_comic_cover(comic_code, page=page, limit=limit, order=order, order_by=order_by, link_website_host=link_website_host, link_relative_reference=link_relative_reference, link_href=link_href)

List comic cover.

### Example


```python
import comicking_openapi
from comicking_openapi.models.comic_cover import ComicCover
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
    api_instance = comicking_openapi.ComicApi(api_client)
    comic_code = 'comic_code_example' # str | 
    page = 56 # int |  (optional)
    limit = 56 # int |  (optional)
    order = 'order_example' # str |  (optional)
    order_by = ['order_by_example'] # List[str] |  (optional)
    link_website_host = ['link_website_host_example'] # List[str] |  (optional)
    link_relative_reference = ['link_relative_reference_example'] # List[str] |  (optional)
    link_href = ['link_href_example'] # List[str] |  (optional)

    try:
        # List comic cover.
        api_response = api_instance.list_comic_cover(comic_code, page=page, limit=limit, order=order, order_by=order_by, link_website_host=link_website_host, link_relative_reference=link_relative_reference, link_href=link_href)
        print("The response of ComicApi->list_comic_cover:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComicApi->list_comic_cover: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **comic_code** | **str**|  | 
 **page** | **int**|  | [optional] 
 **limit** | **int**|  | [optional] 
 **order** | **str**|  | [optional] 
 **order_by** | [**List[str]**](str.md)|  | [optional] 
 **link_website_host** | [**List[str]**](str.md)|  | [optional] 
 **link_relative_reference** | [**List[str]**](str.md)|  | [optional] 
 **link_href** | [**List[str]**](str.md)|  | [optional] 

### Return type

[**List[ComicCover]**](ComicCover.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Comic cover list. |  * X-Total-Count -  <br>  * X-Pagination-Limit -  <br>  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_comic_external**
> List[ComicExternal] list_comic_external(comic_code, page=page, limit=limit, order=order, order_by=order_by, link_website_host=link_website_host, link_relative_reference=link_relative_reference, link_href=link_href)

List comic external.

### Example


```python
import comicking_openapi
from comicking_openapi.models.comic_external import ComicExternal
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
    api_instance = comicking_openapi.ComicApi(api_client)
    comic_code = 'comic_code_example' # str | 
    page = 56 # int |  (optional)
    limit = 56 # int |  (optional)
    order = 'order_example' # str |  (optional)
    order_by = ['order_by_example'] # List[str] |  (optional)
    link_website_host = ['link_website_host_example'] # List[str] |  (optional)
    link_relative_reference = ['link_relative_reference_example'] # List[str] |  (optional)
    link_href = ['link_href_example'] # List[str] |  (optional)

    try:
        # List comic external.
        api_response = api_instance.list_comic_external(comic_code, page=page, limit=limit, order=order, order_by=order_by, link_website_host=link_website_host, link_relative_reference=link_relative_reference, link_href=link_href)
        print("The response of ComicApi->list_comic_external:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComicApi->list_comic_external: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **comic_code** | **str**|  | 
 **page** | **int**|  | [optional] 
 **limit** | **int**|  | [optional] 
 **order** | **str**|  | [optional] 
 **order_by** | [**List[str]**](str.md)|  | [optional] 
 **link_website_host** | [**List[str]**](str.md)|  | [optional] 
 **link_relative_reference** | [**List[str]**](str.md)|  | [optional] 
 **link_href** | [**List[str]**](str.md)|  | [optional] 

### Return type

[**List[ComicExternal]**](ComicExternal.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Comic external list. |  * X-Total-Count -  <br>  * X-Pagination-Limit -  <br>  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_comic_relation**
> List[ComicRelation] list_comic_relation(comic_code, page=page, limit=limit, order=order, order_by=order_by, type_code=type_code)

List comic relation.

### Example


```python
import comicking_openapi
from comicking_openapi.models.comic_relation import ComicRelation
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
    api_instance = comicking_openapi.ComicApi(api_client)
    comic_code = 'comic_code_example' # str | 
    page = 56 # int |  (optional)
    limit = 56 # int |  (optional)
    order = 'order_example' # str |  (optional)
    order_by = ['order_by_example'] # List[str] |  (optional)
    type_code = ['type_code_example'] # List[str] |  (optional)

    try:
        # List comic relation.
        api_response = api_instance.list_comic_relation(comic_code, page=page, limit=limit, order=order, order_by=order_by, type_code=type_code)
        print("The response of ComicApi->list_comic_relation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComicApi->list_comic_relation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **comic_code** | **str**|  | 
 **page** | **int**|  | [optional] 
 **limit** | **int**|  | [optional] 
 **order** | **str**|  | [optional] 
 **order_by** | [**List[str]**](str.md)|  | [optional] 
 **type_code** | [**List[str]**](str.md)|  | [optional] 

### Return type

[**List[ComicRelation]**](ComicRelation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Comic relation list. |  * X-Total-Count -  <br>  * X-Pagination-Limit -  <br>  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_comic_relation_type**
> List[GenericType] list_comic_relation_type(page=page, limit=limit, order=order, order_by=order_by)

List comic relation type.

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
    api_instance = comicking_openapi.ComicApi(api_client)
    page = 56 # int |  (optional)
    limit = 56 # int |  (optional)
    order = 'order_example' # str |  (optional)
    order_by = ['order_by_example'] # List[str] |  (optional)

    try:
        # List comic relation type.
        api_response = api_instance.list_comic_relation_type(page=page, limit=limit, order=order, order_by=order_by)
        print("The response of ComicApi->list_comic_relation_type:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComicApi->list_comic_relation_type: %s\n" % e)
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
**200** | Comic relation type list. |  * X-Total-Count -  <br>  * X-Pagination-Limit -  <br>  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_comic_serialization**
> List[ComicSerialization] list_comic_serialization(comic_code, page=page, limit=limit, order=order, order_by=order_by)

List comic serialization.

### Example


```python
import comicking_openapi
from comicking_openapi.models.comic_serialization import ComicSerialization
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
    api_instance = comicking_openapi.ComicApi(api_client)
    comic_code = 'comic_code_example' # str | 
    page = 56 # int |  (optional)
    limit = 56 # int |  (optional)
    order = 'order_example' # str |  (optional)
    order_by = ['order_by_example'] # List[str] |  (optional)

    try:
        # List comic serialization.
        api_response = api_instance.list_comic_serialization(comic_code, page=page, limit=limit, order=order, order_by=order_by)
        print("The response of ComicApi->list_comic_serialization:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComicApi->list_comic_serialization: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **comic_code** | **str**|  | 
 **page** | **int**|  | [optional] 
 **limit** | **int**|  | [optional] 
 **order** | **str**|  | [optional] 
 **order_by** | [**List[str]**](str.md)|  | [optional] 

### Return type

[**List[ComicSerialization]**](ComicSerialization.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Comic serialization list. |  * X-Total-Count -  <br>  * X-Pagination-Limit -  <br>  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_comic_synopsis**
> List[ComicSynopsis] list_comic_synopsis(comic_code, page=page, limit=limit, order=order, order_by=order_by)

List comic synopsis.

### Example


```python
import comicking_openapi
from comicking_openapi.models.comic_synopsis import ComicSynopsis
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
    api_instance = comicking_openapi.ComicApi(api_client)
    comic_code = 'comic_code_example' # str | 
    page = 56 # int |  (optional)
    limit = 56 # int |  (optional)
    order = 'order_example' # str |  (optional)
    order_by = ['order_by_example'] # List[str] |  (optional)

    try:
        # List comic synopsis.
        api_response = api_instance.list_comic_synopsis(comic_code, page=page, limit=limit, order=order, order_by=order_by)
        print("The response of ComicApi->list_comic_synopsis:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComicApi->list_comic_synopsis: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **comic_code** | **str**|  | 
 **page** | **int**|  | [optional] 
 **limit** | **int**|  | [optional] 
 **order** | **str**|  | [optional] 
 **order_by** | [**List[str]**](str.md)|  | [optional] 

### Return type

[**List[ComicSynopsis]**](ComicSynopsis.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Comic synopsis list. |  * X-Total-Count -  <br>  * X-Pagination-Limit -  <br>  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_comic_tag**
> List[ComicTag] list_comic_tag(comic_code, page=page, limit=limit, order=order, order_by=order_by, tag_type_code=tag_type_code)

List comic tag.

### Example


```python
import comicking_openapi
from comicking_openapi.models.comic_tag import ComicTag
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
    api_instance = comicking_openapi.ComicApi(api_client)
    comic_code = 'comic_code_example' # str | 
    page = 56 # int |  (optional)
    limit = 56 # int |  (optional)
    order = 'order_example' # str |  (optional)
    order_by = ['order_by_example'] # List[str] |  (optional)
    tag_type_code = ['tag_type_code_example'] # List[str] |  (optional)

    try:
        # List comic tag.
        api_response = api_instance.list_comic_tag(comic_code, page=page, limit=limit, order=order, order_by=order_by, tag_type_code=tag_type_code)
        print("The response of ComicApi->list_comic_tag:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComicApi->list_comic_tag: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **comic_code** | **str**|  | 
 **page** | **int**|  | [optional] 
 **limit** | **int**|  | [optional] 
 **order** | **str**|  | [optional] 
 **order_by** | [**List[str]**](str.md)|  | [optional] 
 **tag_type_code** | [**List[str]**](str.md)|  | [optional] 

### Return type

[**List[ComicTag]**](ComicTag.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Comic tag list. |  * X-Total-Count -  <br>  * X-Pagination-Limit -  <br>  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_comic_title**
> List[ComicTitle] list_comic_title(comic_code, page=page, limit=limit, order=order, order_by=order_by)

List comic title.

### Example


```python
import comicking_openapi
from comicking_openapi.models.comic_title import ComicTitle
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
    api_instance = comicking_openapi.ComicApi(api_client)
    comic_code = 'comic_code_example' # str | 
    page = 56 # int |  (optional)
    limit = 56 # int |  (optional)
    order = 'order_example' # str |  (optional)
    order_by = ['order_by_example'] # List[str] |  (optional)

    try:
        # List comic title.
        api_response = api_instance.list_comic_title(comic_code, page=page, limit=limit, order=order, order_by=order_by)
        print("The response of ComicApi->list_comic_title:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComicApi->list_comic_title: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **comic_code** | **str**|  | 
 **page** | **int**|  | [optional] 
 **limit** | **int**|  | [optional] 
 **order** | **str**|  | [optional] 
 **order_by** | [**List[str]**](str.md)|  | [optional] 

### Return type

[**List[ComicTitle]**](ComicTitle.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Comic title list. |  * X-Total-Count -  <br>  * X-Pagination-Limit -  <br>  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_comic**
> Comic update_comic(code, set_comic)

Update comic.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import comicking_openapi
from comicking_openapi.models.comic import Comic
from comicking_openapi.models.set_comic import SetComic
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
    api_instance = comicking_openapi.ComicApi(api_client)
    code = 'code_example' # str | 
    set_comic = comicking_openapi.SetComic() # SetComic | 

    try:
        # Update comic.
        api_response = api_instance.update_comic(code, set_comic)
        print("The response of ComicApi->update_comic:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComicApi->update_comic: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**|  | 
 **set_comic** | [**SetComic**](SetComic.md)|  | 

### Return type

[**Comic**](Comic.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Comic updated. |  * Location -  <br>  |
**204** | Comic unmodified. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_comic_author**
> ComicAuthor update_comic_author(comic_code, type_code, person_code, set_comic_author)

Update comic author.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import comicking_openapi
from comicking_openapi.models.comic_author import ComicAuthor
from comicking_openapi.models.set_comic_author import SetComicAuthor
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
    api_instance = comicking_openapi.ComicApi(api_client)
    comic_code = 'comic_code_example' # str | 
    type_code = 'type_code_example' # str | 
    person_code = 'person_code_example' # str | 
    set_comic_author = comicking_openapi.SetComicAuthor() # SetComicAuthor | 

    try:
        # Update comic author.
        api_response = api_instance.update_comic_author(comic_code, type_code, person_code, set_comic_author)
        print("The response of ComicApi->update_comic_author:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComicApi->update_comic_author: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **comic_code** | **str**|  | 
 **type_code** | **str**|  | 
 **person_code** | **str**|  | 
 **set_comic_author** | [**SetComicAuthor**](SetComicAuthor.md)|  | 

### Return type

[**ComicAuthor**](ComicAuthor.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Comic author updated. |  * Location -  <br>  |
**204** | Comic author unmodified. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_comic_author_note**
> ComicAuthorNote update_comic_author_note(comic_code, author_type_code, author_person_code, ulid, set_comic_author_note)

Update comic author note.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import comicking_openapi
from comicking_openapi.models.comic_author_note import ComicAuthorNote
from comicking_openapi.models.set_comic_author_note import SetComicAuthorNote
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
    api_instance = comicking_openapi.ComicApi(api_client)
    comic_code = 'comic_code_example' # str | 
    author_type_code = 'author_type_code_example' # str | 
    author_person_code = 'author_person_code_example' # str | 
    ulid = 'ulid_example' # str | 
    set_comic_author_note = comicking_openapi.SetComicAuthorNote() # SetComicAuthorNote | 

    try:
        # Update comic author note.
        api_response = api_instance.update_comic_author_note(comic_code, author_type_code, author_person_code, ulid, set_comic_author_note)
        print("The response of ComicApi->update_comic_author_note:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComicApi->update_comic_author_note: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **comic_code** | **str**|  | 
 **author_type_code** | **str**|  | 
 **author_person_code** | **str**|  | 
 **ulid** | **str**|  | 
 **set_comic_author_note** | [**SetComicAuthorNote**](SetComicAuthorNote.md)|  | 

### Return type

[**ComicAuthorNote**](ComicAuthorNote.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Comic author note updated. |  * Location -  <br>  |
**204** | Comic author note unmodified. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_comic_author_type**
> GenericType update_comic_author_type(code, set_generic_type)

Update comic author type.

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
    api_instance = comicking_openapi.ComicApi(api_client)
    code = 'code_example' # str | 
    set_generic_type = comicking_openapi.SetGenericType() # SetGenericType | 

    try:
        # Update comic author type.
        api_response = api_instance.update_comic_author_type(code, set_generic_type)
        print("The response of ComicApi->update_comic_author_type:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComicApi->update_comic_author_type: %s\n" % e)
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

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Comic author type updated. |  * Location -  <br>  |
**204** | Comic author type unmodified. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_comic_category**
> ComicCategory update_comic_category(comic_code, category_type_code, category_code, set_comic_category)

Update comic category.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import comicking_openapi
from comicking_openapi.models.comic_category import ComicCategory
from comicking_openapi.models.set_comic_category import SetComicCategory
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
    api_instance = comicking_openapi.ComicApi(api_client)
    comic_code = 'comic_code_example' # str | 
    category_type_code = 'category_type_code_example' # str | 
    category_code = 'category_code_example' # str | 
    set_comic_category = comicking_openapi.SetComicCategory() # SetComicCategory | 

    try:
        # Update comic category.
        api_response = api_instance.update_comic_category(comic_code, category_type_code, category_code, set_comic_category)
        print("The response of ComicApi->update_comic_category:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComicApi->update_comic_category: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **comic_code** | **str**|  | 
 **category_type_code** | **str**|  | 
 **category_code** | **str**|  | 
 **set_comic_category** | [**SetComicCategory**](SetComicCategory.md)|  | 

### Return type

[**ComicCategory**](ComicCategory.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Comic category updated. |  * Location -  <br>  |
**204** | Comic category unmodified. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_comic_character**
> ComicCharacter update_comic_character(comic_code, character_code, set_comic_character)

Update comic character.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import comicking_openapi
from comicking_openapi.models.comic_character import ComicCharacter
from comicking_openapi.models.set_comic_character import SetComicCharacter
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
    api_instance = comicking_openapi.ComicApi(api_client)
    comic_code = 'comic_code_example' # str | 
    character_code = 'character_code_example' # str | 
    set_comic_character = comicking_openapi.SetComicCharacter() # SetComicCharacter | 

    try:
        # Update comic character.
        api_response = api_instance.update_comic_character(comic_code, character_code, set_comic_character)
        print("The response of ComicApi->update_comic_character:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComicApi->update_comic_character: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **comic_code** | **str**|  | 
 **character_code** | **str**|  | 
 **set_comic_character** | [**SetComicCharacter**](SetComicCharacter.md)|  | 

### Return type

[**ComicCharacter**](ComicCharacter.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Comic character updated. |  * Location -  <br>  |
**204** | Comic character unmodified. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_comic_cover**
> ComicCover update_comic_cover(comic_code, ulid, set_comic_cover)

Update comic cover.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import comicking_openapi
from comicking_openapi.models.comic_cover import ComicCover
from comicking_openapi.models.set_comic_cover import SetComicCover
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
    api_instance = comicking_openapi.ComicApi(api_client)
    comic_code = 'comic_code_example' # str | 
    ulid = 'ulid_example' # str | 
    set_comic_cover = comicking_openapi.SetComicCover() # SetComicCover | 

    try:
        # Update comic cover.
        api_response = api_instance.update_comic_cover(comic_code, ulid, set_comic_cover)
        print("The response of ComicApi->update_comic_cover:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComicApi->update_comic_cover: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **comic_code** | **str**|  | 
 **ulid** | **str**|  | 
 **set_comic_cover** | [**SetComicCover**](SetComicCover.md)|  | 

### Return type

[**ComicCover**](ComicCover.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Comic cover updated. |  * Location -  <br>  |
**204** | Comic cover unmodified. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_comic_external**
> ComicExternal update_comic_external(comic_code, ulid, set_comic_external)

Update comic external.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import comicking_openapi
from comicking_openapi.models.comic_external import ComicExternal
from comicking_openapi.models.set_comic_external import SetComicExternal
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
    api_instance = comicking_openapi.ComicApi(api_client)
    comic_code = 'comic_code_example' # str | 
    ulid = 'ulid_example' # str | 
    set_comic_external = comicking_openapi.SetComicExternal() # SetComicExternal | 

    try:
        # Update comic external.
        api_response = api_instance.update_comic_external(comic_code, ulid, set_comic_external)
        print("The response of ComicApi->update_comic_external:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComicApi->update_comic_external: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **comic_code** | **str**|  | 
 **ulid** | **str**|  | 
 **set_comic_external** | [**SetComicExternal**](SetComicExternal.md)|  | 

### Return type

[**ComicExternal**](ComicExternal.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Comic external updated. |  * Location -  <br>  |
**204** | Comic external unmodified. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_comic_relation**
> ComicRelation update_comic_relation(comic_code, type_code, child_code, set_comic_relation)

Update comic relation.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import comicking_openapi
from comicking_openapi.models.comic_relation import ComicRelation
from comicking_openapi.models.set_comic_relation import SetComicRelation
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
    api_instance = comicking_openapi.ComicApi(api_client)
    comic_code = 'comic_code_example' # str | 
    type_code = 'type_code_example' # str | 
    child_code = 'child_code_example' # str | 
    set_comic_relation = comicking_openapi.SetComicRelation() # SetComicRelation | 

    try:
        # Update comic relation.
        api_response = api_instance.update_comic_relation(comic_code, type_code, child_code, set_comic_relation)
        print("The response of ComicApi->update_comic_relation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComicApi->update_comic_relation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **comic_code** | **str**|  | 
 **type_code** | **str**|  | 
 **child_code** | **str**|  | 
 **set_comic_relation** | [**SetComicRelation**](SetComicRelation.md)|  | 

### Return type

[**ComicRelation**](ComicRelation.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Comic relation updated. |  * Location -  <br>  |
**204** | Comic relation unmodified. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_comic_relation_type**
> GenericType update_comic_relation_type(code, set_generic_type)

Update comic relation type.

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
    api_instance = comicking_openapi.ComicApi(api_client)
    code = 'code_example' # str | 
    set_generic_type = comicking_openapi.SetGenericType() # SetGenericType | 

    try:
        # Update comic relation type.
        api_response = api_instance.update_comic_relation_type(code, set_generic_type)
        print("The response of ComicApi->update_comic_relation_type:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComicApi->update_comic_relation_type: %s\n" % e)
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

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Comic relation type updated. |  * Location -  <br>  |
**204** | Comic relation type unmodified. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_comic_serialization**
> ComicSerialization update_comic_serialization(comic_code, magazine_code, set_comic_serialization)

Update comic serialization.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import comicking_openapi
from comicking_openapi.models.comic_serialization import ComicSerialization
from comicking_openapi.models.set_comic_serialization import SetComicSerialization
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
    api_instance = comicking_openapi.ComicApi(api_client)
    comic_code = 'comic_code_example' # str | 
    magazine_code = 'magazine_code_example' # str | 
    set_comic_serialization = comicking_openapi.SetComicSerialization() # SetComicSerialization | 

    try:
        # Update comic serialization.
        api_response = api_instance.update_comic_serialization(comic_code, magazine_code, set_comic_serialization)
        print("The response of ComicApi->update_comic_serialization:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComicApi->update_comic_serialization: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **comic_code** | **str**|  | 
 **magazine_code** | **str**|  | 
 **set_comic_serialization** | [**SetComicSerialization**](SetComicSerialization.md)|  | 

### Return type

[**ComicSerialization**](ComicSerialization.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Comic serialization updated. |  * Location -  <br>  |
**204** | Comic serialization unmodified. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_comic_synopsis**
> ComicSynopsis update_comic_synopsis(comic_code, ulid, set_comic_synopsis)

Update comic synopsis.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import comicking_openapi
from comicking_openapi.models.comic_synopsis import ComicSynopsis
from comicking_openapi.models.set_comic_synopsis import SetComicSynopsis
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
    api_instance = comicking_openapi.ComicApi(api_client)
    comic_code = 'comic_code_example' # str | 
    ulid = 'ulid_example' # str | 
    set_comic_synopsis = comicking_openapi.SetComicSynopsis() # SetComicSynopsis | 

    try:
        # Update comic synopsis.
        api_response = api_instance.update_comic_synopsis(comic_code, ulid, set_comic_synopsis)
        print("The response of ComicApi->update_comic_synopsis:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComicApi->update_comic_synopsis: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **comic_code** | **str**|  | 
 **ulid** | **str**|  | 
 **set_comic_synopsis** | [**SetComicSynopsis**](SetComicSynopsis.md)|  | 

### Return type

[**ComicSynopsis**](ComicSynopsis.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Comic synopsis updated. |  * Location -  <br>  |
**204** | Comic synopsis unmodified. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_comic_tag**
> ComicTag update_comic_tag(comic_code, tag_type_code, tag_code, set_comic_tag)

Update comic tag.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import comicking_openapi
from comicking_openapi.models.comic_tag import ComicTag
from comicking_openapi.models.set_comic_tag import SetComicTag
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
    api_instance = comicking_openapi.ComicApi(api_client)
    comic_code = 'comic_code_example' # str | 
    tag_type_code = 'tag_type_code_example' # str | 
    tag_code = 'tag_code_example' # str | Code of tag.
    set_comic_tag = comicking_openapi.SetComicTag() # SetComicTag | 

    try:
        # Update comic tag.
        api_response = api_instance.update_comic_tag(comic_code, tag_type_code, tag_code, set_comic_tag)
        print("The response of ComicApi->update_comic_tag:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComicApi->update_comic_tag: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **comic_code** | **str**|  | 
 **tag_type_code** | **str**|  | 
 **tag_code** | **str**| Code of tag. | 
 **set_comic_tag** | [**SetComicTag**](SetComicTag.md)|  | 

### Return type

[**ComicTag**](ComicTag.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Comic tag updated. |  * Location -  <br>  |
**204** | Comic tag unmodified. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_comic_title**
> ComicTitle update_comic_title(comic_code, ulid, set_comic_title)

Update comic title.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import comicking_openapi
from comicking_openapi.models.comic_title import ComicTitle
from comicking_openapi.models.set_comic_title import SetComicTitle
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
    api_instance = comicking_openapi.ComicApi(api_client)
    comic_code = 'comic_code_example' # str | 
    ulid = 'ulid_example' # str | 
    set_comic_title = comicking_openapi.SetComicTitle() # SetComicTitle | 

    try:
        # Update comic title.
        api_response = api_instance.update_comic_title(comic_code, ulid, set_comic_title)
        print("The response of ComicApi->update_comic_title:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComicApi->update_comic_title: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **comic_code** | **str**|  | 
 **ulid** | **str**|  | 
 **set_comic_title** | [**SetComicTitle**](SetComicTitle.md)|  | 

### Return type

[**ComicTitle**](ComicTitle.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Comic title updated. |  * Location -  <br>  |
**204** | Comic title unmodified. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

