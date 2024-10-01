# comicking-openapi
PHP Symfony-based comic catalog full-stack.

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 0.0.1
- Package version: 0.0.1
- Generator version: 7.4.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python 3.7+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import comicking_openapi
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import comicking_openapi
```

### Tests

Execute `pytest` to run the tests.

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

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
    new_category = comicking_openapi.NewCategory() # NewCategory | 

    try:
        # Add category.
        api_response = api_instance.add_category(new_category)
        print("The response of CategoryApi->add_category:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CategoryApi->add_category: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to */api*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*CategoryApi* | [**add_category**](docs/CategoryApi.md#add_category) | **POST** /rest/categories | Add category.
*CategoryApi* | [**add_category_type**](docs/CategoryApi.md#add_category_type) | **POST** /rest/category-types | Add category type.
*CategoryApi* | [**delete_category**](docs/CategoryApi.md#delete_category) | **DELETE** /rest/categories/{typeCode}:{code} | Delete category.
*CategoryApi* | [**delete_category_type**](docs/CategoryApi.md#delete_category_type) | **DELETE** /rest/category-types/{code} | Delete category type.
*CategoryApi* | [**get_category**](docs/CategoryApi.md#get_category) | **GET** /rest/categories/{typeCode}:{code} | Get category.
*CategoryApi* | [**get_category_type**](docs/CategoryApi.md#get_category_type) | **GET** /rest/category-types/{code} | Get category type.
*CategoryApi* | [**list_category**](docs/CategoryApi.md#list_category) | **GET** /rest/categories | List category.
*CategoryApi* | [**list_category_type**](docs/CategoryApi.md#list_category_type) | **GET** /rest/category-types | List category type.
*CategoryApi* | [**update_category**](docs/CategoryApi.md#update_category) | **PATCH** /rest/categories/{typeCode}:{code} | Update category.
*CategoryApi* | [**update_category_type**](docs/CategoryApi.md#update_category_type) | **PATCH** /rest/category-types/{code} | Update category type.
*CharacterApi* | [**add_character**](docs/CharacterApi.md#add_character) | **POST** /rest/characters | Add character.
*CharacterApi* | [**delete_character**](docs/CharacterApi.md#delete_character) | **DELETE** /rest/characters/{code} | Delete character.
*CharacterApi* | [**get_character**](docs/CharacterApi.md#get_character) | **GET** /rest/characters/{code} | Get character.
*CharacterApi* | [**list_character**](docs/CharacterApi.md#list_character) | **GET** /rest/characters | List character.
*CharacterApi* | [**update_character**](docs/CharacterApi.md#update_character) | **PATCH** /rest/characters/{code} | Update character.
*ComicApi* | [**add_comic**](docs/ComicApi.md#add_comic) | **POST** /rest/comics | Add comic.
*ComicApi* | [**add_comic_author**](docs/ComicApi.md#add_comic_author) | **POST** /rest/comics/{comicCode}/authors | Add comic author.
*ComicApi* | [**add_comic_author_note**](docs/ComicApi.md#add_comic_author_note) | **POST** /rest/comics/{comicCode}/authors/{authorTypeCode}:{authorPersonCode}/notes | Add comic author note.
*ComicApi* | [**add_comic_author_type**](docs/ComicApi.md#add_comic_author_type) | **POST** /rest/comic-author-types | Add comic author type.
*ComicApi* | [**add_comic_category**](docs/ComicApi.md#add_comic_category) | **POST** /rest/comics/{comicCode}/categories | Add comic category.
*ComicApi* | [**add_comic_character**](docs/ComicApi.md#add_comic_character) | **POST** /rest/comics/{comicCode}/characters | Add comic character.
*ComicApi* | [**add_comic_cover**](docs/ComicApi.md#add_comic_cover) | **POST** /rest/comics/{comicCode}/covers | Add comic cover.
*ComicApi* | [**add_comic_external**](docs/ComicApi.md#add_comic_external) | **POST** /rest/comics/{comicCode}/externals | Add comic external.
*ComicApi* | [**add_comic_relation**](docs/ComicApi.md#add_comic_relation) | **POST** /rest/comics/{comicCode}/relations | Add comic relation.
*ComicApi* | [**add_comic_relation_type**](docs/ComicApi.md#add_comic_relation_type) | **POST** /rest/comic-relation-types | Add comic relation type.
*ComicApi* | [**add_comic_serialization**](docs/ComicApi.md#add_comic_serialization) | **POST** /rest/comics/{comicCode}/serializations | Add comic serialization.
*ComicApi* | [**add_comic_synopsis**](docs/ComicApi.md#add_comic_synopsis) | **POST** /rest/comics/{comicCode}/synopses | Add comic synopsis.
*ComicApi* | [**add_comic_tag**](docs/ComicApi.md#add_comic_tag) | **POST** /rest/comics/{comicCode}/tags | Add comic tag.
*ComicApi* | [**add_comic_title**](docs/ComicApi.md#add_comic_title) | **POST** /rest/comics/{comicCode}/titles | Add comic title.
*ComicApi* | [**delete_comic**](docs/ComicApi.md#delete_comic) | **DELETE** /rest/comics/{code} | Delete comic.
*ComicApi* | [**delete_comic_author**](docs/ComicApi.md#delete_comic_author) | **DELETE** /rest/comics/{comicCode}/authors/{typeCode}:{personCode} | Delete comic author.
*ComicApi* | [**delete_comic_author_note**](docs/ComicApi.md#delete_comic_author_note) | **DELETE** /rest/comics/{comicCode}/authors/{authorTypeCode}:{authorPersonCode}/notes/{ulid} | Delete comic author note.
*ComicApi* | [**delete_comic_author_type**](docs/ComicApi.md#delete_comic_author_type) | **DELETE** /rest/comic-author-types/{code} | Delete comic author type.
*ComicApi* | [**delete_comic_category**](docs/ComicApi.md#delete_comic_category) | **DELETE** /rest/comics/{comicCode}/categories/{categoryTypeCode}:{categoryCode} | Delete comic category.
*ComicApi* | [**delete_comic_character**](docs/ComicApi.md#delete_comic_character) | **DELETE** /rest/comics/{comicCode}/characters/{characterCode} | Delete comic character.
*ComicApi* | [**delete_comic_cover**](docs/ComicApi.md#delete_comic_cover) | **DELETE** /rest/comics/{comicCode}/covers/{ulid} | Delete comic cover.
*ComicApi* | [**delete_comic_external**](docs/ComicApi.md#delete_comic_external) | **DELETE** /rest/comics/{comicCode}/externals/{ulid} | Delete comic external.
*ComicApi* | [**delete_comic_relation**](docs/ComicApi.md#delete_comic_relation) | **DELETE** /rest/comics/{comicCode}/relations/{typeCode}:{childCode} | Delete comic relation.
*ComicApi* | [**delete_comic_relation_type**](docs/ComicApi.md#delete_comic_relation_type) | **DELETE** /rest/comic-relation-types/{code} | Delete comic relation type.
*ComicApi* | [**delete_comic_serialization**](docs/ComicApi.md#delete_comic_serialization) | **DELETE** /rest/comics/{comicCode}/serializations/{magazineCode} | Delete comic serialization.
*ComicApi* | [**delete_comic_synopsis**](docs/ComicApi.md#delete_comic_synopsis) | **DELETE** /rest/comics/{comicCode}/synopses/{ulid} | Delete comic synopsis.
*ComicApi* | [**delete_comic_tag**](docs/ComicApi.md#delete_comic_tag) | **DELETE** /rest/comics/{comicCode}/tags/{tagTypeCode}:{tagCode} | Delete comic tag.
*ComicApi* | [**delete_comic_title**](docs/ComicApi.md#delete_comic_title) | **DELETE** /rest/comics/{comicCode}/titles/{ulid} | Delete comic title.
*ComicApi* | [**get_comic**](docs/ComicApi.md#get_comic) | **GET** /rest/comics/{code} | Get comic.
*ComicApi* | [**get_comic_author**](docs/ComicApi.md#get_comic_author) | **GET** /rest/comics/{comicCode}/authors/{typeCode}:{personCode} | Get comic author.
*ComicApi* | [**get_comic_author_note**](docs/ComicApi.md#get_comic_author_note) | **GET** /rest/comics/{comicCode}/authors/{authorTypeCode}:{authorPersonCode}/notes/{ulid} | Get comic author note.
*ComicApi* | [**get_comic_author_type**](docs/ComicApi.md#get_comic_author_type) | **GET** /rest/comic-author-types/{code} | Get comic author type.
*ComicApi* | [**get_comic_category**](docs/ComicApi.md#get_comic_category) | **GET** /rest/comics/{comicCode}/categories/{categoryTypeCode}:{categoryCode} | Get comic category.
*ComicApi* | [**get_comic_character**](docs/ComicApi.md#get_comic_character) | **GET** /rest/comics/{comicCode}/characters/{characterCode} | Get comic character.
*ComicApi* | [**get_comic_cover**](docs/ComicApi.md#get_comic_cover) | **GET** /rest/comics/{comicCode}/covers/{ulid} | Get comic cover.
*ComicApi* | [**get_comic_external**](docs/ComicApi.md#get_comic_external) | **GET** /rest/comics/{comicCode}/externals/{ulid} | Get comic external.
*ComicApi* | [**get_comic_relation**](docs/ComicApi.md#get_comic_relation) | **GET** /rest/comics/{comicCode}/relations/{typeCode}:{childCode} | Get comic relation.
*ComicApi* | [**get_comic_relation_type**](docs/ComicApi.md#get_comic_relation_type) | **GET** /rest/comic-relation-types/{code} | Get comic relation type.
*ComicApi* | [**get_comic_serialization**](docs/ComicApi.md#get_comic_serialization) | **GET** /rest/comics/{comicCode}/serializations/{magazineCode} | Get comic serialization.
*ComicApi* | [**get_comic_synopsis**](docs/ComicApi.md#get_comic_synopsis) | **GET** /rest/comics/{comicCode}/synopses/{ulid} | Get comic synopsis.
*ComicApi* | [**get_comic_tag**](docs/ComicApi.md#get_comic_tag) | **GET** /rest/comics/{comicCode}/tags/{tagTypeCode}:{tagCode} | Get comic tag.
*ComicApi* | [**get_comic_title**](docs/ComicApi.md#get_comic_title) | **GET** /rest/comics/{comicCode}/titles/{ulid} | Get comic title.
*ComicApi* | [**list_comic**](docs/ComicApi.md#list_comic) | **GET** /rest/comics | List comic.
*ComicApi* | [**list_comic_author**](docs/ComicApi.md#list_comic_author) | **GET** /rest/comics/{comicCode}/authors | List comic author.
*ComicApi* | [**list_comic_author_note**](docs/ComicApi.md#list_comic_author_note) | **GET** /rest/comics/{comicCode}/authors/{authorTypeCode}:{authorPersonCode}/notes | List comic author note.
*ComicApi* | [**list_comic_author_type**](docs/ComicApi.md#list_comic_author_type) | **GET** /rest/comic-author-types | List comic author type.
*ComicApi* | [**list_comic_category**](docs/ComicApi.md#list_comic_category) | **GET** /rest/comics/{comicCode}/categories | List comic category.
*ComicApi* | [**list_comic_character**](docs/ComicApi.md#list_comic_character) | **GET** /rest/comics/{comicCode}/characters | List comic character.
*ComicApi* | [**list_comic_cover**](docs/ComicApi.md#list_comic_cover) | **GET** /rest/comics/{comicCode}/covers | List comic cover.
*ComicApi* | [**list_comic_external**](docs/ComicApi.md#list_comic_external) | **GET** /rest/comics/{comicCode}/externals | List comic external.
*ComicApi* | [**list_comic_relation**](docs/ComicApi.md#list_comic_relation) | **GET** /rest/comics/{comicCode}/relations | List comic relation.
*ComicApi* | [**list_comic_relation_type**](docs/ComicApi.md#list_comic_relation_type) | **GET** /rest/comic-relation-types | List comic relation type.
*ComicApi* | [**list_comic_serialization**](docs/ComicApi.md#list_comic_serialization) | **GET** /rest/comics/{comicCode}/serializations | List comic serialization.
*ComicApi* | [**list_comic_synopsis**](docs/ComicApi.md#list_comic_synopsis) | **GET** /rest/comics/{comicCode}/synopses | List comic synopsis.
*ComicApi* | [**list_comic_tag**](docs/ComicApi.md#list_comic_tag) | **GET** /rest/comics/{comicCode}/tags | List comic tag.
*ComicApi* | [**list_comic_title**](docs/ComicApi.md#list_comic_title) | **GET** /rest/comics/{comicCode}/titles | List comic title.
*ComicApi* | [**update_comic**](docs/ComicApi.md#update_comic) | **PATCH** /rest/comics/{code} | Update comic.
*ComicApi* | [**update_comic_author**](docs/ComicApi.md#update_comic_author) | **PATCH** /rest/comics/{comicCode}/authors/{typeCode}:{personCode} | Update comic author.
*ComicApi* | [**update_comic_author_note**](docs/ComicApi.md#update_comic_author_note) | **PATCH** /rest/comics/{comicCode}/authors/{authorTypeCode}:{authorPersonCode}/notes/{ulid} | Update comic author note.
*ComicApi* | [**update_comic_author_type**](docs/ComicApi.md#update_comic_author_type) | **PATCH** /rest/comic-author-types/{code} | Update comic author type.
*ComicApi* | [**update_comic_category**](docs/ComicApi.md#update_comic_category) | **PATCH** /rest/comics/{comicCode}/categories/{categoryTypeCode}:{categoryCode} | Update comic category.
*ComicApi* | [**update_comic_character**](docs/ComicApi.md#update_comic_character) | **PATCH** /rest/comics/{comicCode}/characters/{characterCode} | Update comic character.
*ComicApi* | [**update_comic_cover**](docs/ComicApi.md#update_comic_cover) | **PATCH** /rest/comics/{comicCode}/covers/{ulid} | Update comic cover.
*ComicApi* | [**update_comic_external**](docs/ComicApi.md#update_comic_external) | **PATCH** /rest/comics/{comicCode}/externals/{ulid} | Update comic external.
*ComicApi* | [**update_comic_relation**](docs/ComicApi.md#update_comic_relation) | **PATCH** /rest/comics/{comicCode}/relations/{typeCode}:{childCode} | Update comic relation.
*ComicApi* | [**update_comic_relation_type**](docs/ComicApi.md#update_comic_relation_type) | **PATCH** /rest/comic-relation-types/{code} | Update comic relation type.
*ComicApi* | [**update_comic_serialization**](docs/ComicApi.md#update_comic_serialization) | **PATCH** /rest/comics/{comicCode}/serializations/{magazineCode} | Update comic serialization.
*ComicApi* | [**update_comic_synopsis**](docs/ComicApi.md#update_comic_synopsis) | **PATCH** /rest/comics/{comicCode}/synopses/{ulid} | Update comic synopsis.
*ComicApi* | [**update_comic_tag**](docs/ComicApi.md#update_comic_tag) | **PATCH** /rest/comics/{comicCode}/tags/{tagTypeCode}:{tagCode} | Update comic tag.
*ComicApi* | [**update_comic_title**](docs/ComicApi.md#update_comic_title) | **PATCH** /rest/comics/{comicCode}/titles/{ulid} | Update comic title.
*ComicChapterApi* | [**add_comic_chapter**](docs/ComicChapterApi.md#add_comic_chapter) | **POST** /rest/comics/{comicCode}/chapters | Add comic chapter.
*ComicChapterApi* | [**add_comic_chapter_title**](docs/ComicChapterApi.md#add_comic_chapter_title) | **POST** /rest/comics/{comicCode}/chapters/{chapterNV}/titles | Add comic chapter title.
*ComicChapterApi* | [**delete_comic_chapter**](docs/ComicChapterApi.md#delete_comic_chapter) | **DELETE** /rest/comics/{comicCode}/chapters/{nv} | Delete comic chapter.
*ComicChapterApi* | [**delete_comic_chapter_title**](docs/ComicChapterApi.md#delete_comic_chapter_title) | **DELETE** /rest/comics/{comicCode}/chapters/{chapterNV}/titles/{ulid} | Delete comic chapter title.
*ComicChapterApi* | [**get_comic_chapter**](docs/ComicChapterApi.md#get_comic_chapter) | **GET** /rest/comics/{comicCode}/chapters/{nv} | Get comic chapter.
*ComicChapterApi* | [**get_comic_chapter_title**](docs/ComicChapterApi.md#get_comic_chapter_title) | **GET** /rest/comics/{comicCode}/chapters/{chapterNV}/titles/{ulid} | Get comic chapter title.
*ComicChapterApi* | [**list_comic_chapter**](docs/ComicChapterApi.md#list_comic_chapter) | **GET** /rest/comics/{comicCode}/chapters | List comic chapter.
*ComicChapterApi* | [**list_comic_chapter_title**](docs/ComicChapterApi.md#list_comic_chapter_title) | **GET** /rest/comics/{comicCode}/chapters/{chapterNV}/titles | List comic chapter title.
*ComicChapterApi* | [**update_comic_chapter**](docs/ComicChapterApi.md#update_comic_chapter) | **PATCH** /rest/comics/{comicCode}/chapters/{nv} | Update comic chapter.
*ComicChapterApi* | [**update_comic_chapter_title**](docs/ComicChapterApi.md#update_comic_chapter_title) | **PATCH** /rest/comics/{comicCode}/chapters/{chapterNV}/titles/{ulid} | Update comic chapter title.
*ComicVolumeApi* | [**add_comic_volume**](docs/ComicVolumeApi.md#add_comic_volume) | **POST** /rest/comics/{comicCode}/volumes | Add comic volume.
*ComicVolumeApi* | [**add_comic_volume_cover**](docs/ComicVolumeApi.md#add_comic_volume_cover) | **POST** /rest/comics/{comicCode}/volumes/{volumeNumber}/covers | Add comic volume cover.
*ComicVolumeApi* | [**add_comic_volume_title**](docs/ComicVolumeApi.md#add_comic_volume_title) | **POST** /rest/comics/{comicCode}/volumes/{volumeNumber}/titles | Add comic volume title.
*ComicVolumeApi* | [**delete_comic_volume**](docs/ComicVolumeApi.md#delete_comic_volume) | **DELETE** /rest/comics/{comicCode}/volumes/{volume} | Delete comic volume.
*ComicVolumeApi* | [**delete_comic_volume_cover**](docs/ComicVolumeApi.md#delete_comic_volume_cover) | **DELETE** /rest/comics/{comicCode}/volumes/{volumeNumber}/covers/{ulid} | Delete comic volume cover.
*ComicVolumeApi* | [**delete_comic_volume_title**](docs/ComicVolumeApi.md#delete_comic_volume_title) | **DELETE** /rest/comics/{comicCode}/volumes/{volumeNumber}/titles/{ulid} | Delete comic volume title.
*ComicVolumeApi* | [**get_comic_volume**](docs/ComicVolumeApi.md#get_comic_volume) | **GET** /rest/comics/{comicCode}/volumes/{volume} | Get comic volume.
*ComicVolumeApi* | [**get_comic_volume_cover**](docs/ComicVolumeApi.md#get_comic_volume_cover) | **GET** /rest/comics/{comicCode}/volumes/{volumeNumber}/covers/{ulid} | Get comic volume cover.
*ComicVolumeApi* | [**get_comic_volume_title**](docs/ComicVolumeApi.md#get_comic_volume_title) | **GET** /rest/comics/{comicCode}/volumes/{volumeNumber}/titles/{ulid} | Get comic volume title.
*ComicVolumeApi* | [**list_comic_volume**](docs/ComicVolumeApi.md#list_comic_volume) | **GET** /rest/comics/{comicCode}/volumes | List comic volume.
*ComicVolumeApi* | [**list_comic_volume_cover**](docs/ComicVolumeApi.md#list_comic_volume_cover) | **GET** /rest/comics/{comicCode}/volumes/{volumeNumber}/covers | List comic volume cover.
*ComicVolumeApi* | [**list_comic_volume_title**](docs/ComicVolumeApi.md#list_comic_volume_title) | **GET** /rest/comics/{comicCode}/volumes/{volumeNumber}/titles | List comic volume title.
*ComicVolumeApi* | [**update_comic_volume**](docs/ComicVolumeApi.md#update_comic_volume) | **PATCH** /rest/comics/{comicCode}/volumes/{volume} | Update comic volume.
*ComicVolumeApi* | [**update_comic_volume_cover**](docs/ComicVolumeApi.md#update_comic_volume_cover) | **PATCH** /rest/comics/{comicCode}/volumes/{volumeNumber}/covers/{ulid} | Update volume comic cover.
*ComicVolumeApi* | [**update_comic_volume_title**](docs/ComicVolumeApi.md#update_comic_volume_title) | **PATCH** /rest/comics/{comicCode}/volumes/{volumeNumber}/titles/{ulid} | Update comic volume title.
*LanguageApi* | [**add_language**](docs/LanguageApi.md#add_language) | **POST** /rest/languages | Add language.
*LanguageApi* | [**delete_language**](docs/LanguageApi.md#delete_language) | **DELETE** /rest/languages/{lang} | Delete language.
*LanguageApi* | [**get_language**](docs/LanguageApi.md#get_language) | **GET** /rest/languages/{lang} | Get language.
*LanguageApi* | [**list_language**](docs/LanguageApi.md#list_language) | **GET** /rest/languages | List language.
*LanguageApi* | [**update_language**](docs/LanguageApi.md#update_language) | **PATCH** /rest/languages/{lang} | Update language.
*LinkApi* | [**add_link**](docs/LinkApi.md#add_link) | **POST** /rest/links | Add link.
*LinkApi* | [**delete_link**](docs/LinkApi.md#delete_link) | **DELETE** /rest/links/{href} | Delete link.
*LinkApi* | [**get_link**](docs/LinkApi.md#get_link) | **GET** /rest/links/{href} | Get link.
*LinkApi* | [**list_link**](docs/LinkApi.md#list_link) | **GET** /rest/links | List link.
*LinkApi* | [**update_link**](docs/LinkApi.md#update_link) | **PATCH** /rest/links/{href} | Update link.
*MagazineApi* | [**add_magazine**](docs/MagazineApi.md#add_magazine) | **POST** /rest/magazines | Add magazine.
*MagazineApi* | [**delete_magazine**](docs/MagazineApi.md#delete_magazine) | **DELETE** /rest/magazines/{code} | Delete magazine.
*MagazineApi* | [**get_magazine**](docs/MagazineApi.md#get_magazine) | **GET** /rest/magazines/{code} | Get magazine.
*MagazineApi* | [**list_magazine**](docs/MagazineApi.md#list_magazine) | **GET** /rest/magazines | List magazine.
*MagazineApi* | [**update_magazine**](docs/MagazineApi.md#update_magazine) | **PATCH** /rest/magazines/{code} | Update magazine.
*PersonApi* | [**add_person**](docs/PersonApi.md#add_person) | **POST** /rest/people | Add person.
*PersonApi* | [**delete_person**](docs/PersonApi.md#delete_person) | **DELETE** /rest/people/{code} | Delete person.
*PersonApi* | [**get_person**](docs/PersonApi.md#get_person) | **GET** /rest/people/{code} | Get person.
*PersonApi* | [**list_person**](docs/PersonApi.md#list_person) | **GET** /rest/people | List person.
*PersonApi* | [**update_person**](docs/PersonApi.md#update_person) | **PATCH** /rest/people/{code} | Update person.
*TagApi* | [**add_tag**](docs/TagApi.md#add_tag) | **POST** /rest/tags | Add tag.
*TagApi* | [**add_tag_type**](docs/TagApi.md#add_tag_type) | **POST** /rest/tag-types | Add tag type.
*TagApi* | [**delete_tag**](docs/TagApi.md#delete_tag) | **DELETE** /rest/tags/{typeCode}:{code} | Delete tag.
*TagApi* | [**delete_tag_type**](docs/TagApi.md#delete_tag_type) | **DELETE** /rest/tag-types/{code} | Delete tag type.
*TagApi* | [**get_tag**](docs/TagApi.md#get_tag) | **GET** /rest/tags/{typeCode}:{code} | Get tag.
*TagApi* | [**get_tag_type**](docs/TagApi.md#get_tag_type) | **GET** /rest/tag-types/{code} | Get tag type.
*TagApi* | [**list_tag**](docs/TagApi.md#list_tag) | **GET** /rest/tags | List tag.
*TagApi* | [**list_tag_type**](docs/TagApi.md#list_tag_type) | **GET** /rest/tag-types | List tag type.
*TagApi* | [**update_tag**](docs/TagApi.md#update_tag) | **PATCH** /rest/tags/{typeCode}:{code} | Update tag.
*TagApi* | [**update_tag_type**](docs/TagApi.md#update_tag_type) | **PATCH** /rest/tag-types/{code} | Update tag type.
*WebsiteApi* | [**add_website**](docs/WebsiteApi.md#add_website) | **POST** /rest/websites | Add website.
*WebsiteApi* | [**delete_website**](docs/WebsiteApi.md#delete_website) | **DELETE** /rest/websites/{host} | Delete website.
*WebsiteApi* | [**get_website**](docs/WebsiteApi.md#get_website) | **GET** /rest/websites/{host} | Get website.
*WebsiteApi* | [**list_website**](docs/WebsiteApi.md#list_website) | **GET** /rest/websites | List website.
*WebsiteApi* | [**update_website**](docs/WebsiteApi.md#update_website) | **PATCH** /rest/websites/{host} | Update website.


## Documentation For Models

 - [Category](docs/Category.md)
 - [Character](docs/Character.md)
 - [Comic](docs/Comic.md)
 - [ComicAuthor](docs/ComicAuthor.md)
 - [ComicAuthorNote](docs/ComicAuthorNote.md)
 - [ComicCategory](docs/ComicCategory.md)
 - [ComicChapter](docs/ComicChapter.md)
 - [ComicChapterTitle](docs/ComicChapterTitle.md)
 - [ComicCharacter](docs/ComicCharacter.md)
 - [ComicCover](docs/ComicCover.md)
 - [ComicExternal](docs/ComicExternal.md)
 - [ComicRelation](docs/ComicRelation.md)
 - [ComicSerialization](docs/ComicSerialization.md)
 - [ComicSynopsis](docs/ComicSynopsis.md)
 - [ComicTag](docs/ComicTag.md)
 - [ComicTitle](docs/ComicTitle.md)
 - [ComicVolume](docs/ComicVolume.md)
 - [ComicVolumeCover](docs/ComicVolumeCover.md)
 - [ComicVolumeTitle](docs/ComicVolumeTitle.md)
 - [Error](docs/Error.md)
 - [GenericType](docs/GenericType.md)
 - [Language](docs/Language.md)
 - [Link](docs/Link.md)
 - [Magazine](docs/Magazine.md)
 - [NewCategory](docs/NewCategory.md)
 - [NewCharacter](docs/NewCharacter.md)
 - [NewComic](docs/NewComic.md)
 - [NewComicAuthor](docs/NewComicAuthor.md)
 - [NewComicAuthorNote](docs/NewComicAuthorNote.md)
 - [NewComicCategory](docs/NewComicCategory.md)
 - [NewComicChapter](docs/NewComicChapter.md)
 - [NewComicChapterTitle](docs/NewComicChapterTitle.md)
 - [NewComicCharacter](docs/NewComicCharacter.md)
 - [NewComicCover](docs/NewComicCover.md)
 - [NewComicExternal](docs/NewComicExternal.md)
 - [NewComicRelation](docs/NewComicRelation.md)
 - [NewComicSerialization](docs/NewComicSerialization.md)
 - [NewComicSynopsis](docs/NewComicSynopsis.md)
 - [NewComicTag](docs/NewComicTag.md)
 - [NewComicTitle](docs/NewComicTitle.md)
 - [NewComicVolume](docs/NewComicVolume.md)
 - [NewComicVolumeCover](docs/NewComicVolumeCover.md)
 - [NewComicVolumeTitle](docs/NewComicVolumeTitle.md)
 - [NewGenericType](docs/NewGenericType.md)
 - [NewLanguage](docs/NewLanguage.md)
 - [NewLink](docs/NewLink.md)
 - [NewMagazine](docs/NewMagazine.md)
 - [NewPerson](docs/NewPerson.md)
 - [NewTag](docs/NewTag.md)
 - [NewWebsite](docs/NewWebsite.md)
 - [Person](docs/Person.md)
 - [SetCategory](docs/SetCategory.md)
 - [SetCharacter](docs/SetCharacter.md)
 - [SetComic](docs/SetComic.md)
 - [SetComicAuthor](docs/SetComicAuthor.md)
 - [SetComicAuthorNote](docs/SetComicAuthorNote.md)
 - [SetComicCategory](docs/SetComicCategory.md)
 - [SetComicChapter](docs/SetComicChapter.md)
 - [SetComicChapterTitle](docs/SetComicChapterTitle.md)
 - [SetComicCharacter](docs/SetComicCharacter.md)
 - [SetComicCover](docs/SetComicCover.md)
 - [SetComicExternal](docs/SetComicExternal.md)
 - [SetComicRelation](docs/SetComicRelation.md)
 - [SetComicSerialization](docs/SetComicSerialization.md)
 - [SetComicSynopsis](docs/SetComicSynopsis.md)
 - [SetComicTag](docs/SetComicTag.md)
 - [SetComicTitle](docs/SetComicTitle.md)
 - [SetComicVolume](docs/SetComicVolume.md)
 - [SetComicVolumeCover](docs/SetComicVolumeCover.md)
 - [SetComicVolumeTitle](docs/SetComicVolumeTitle.md)
 - [SetGenericType](docs/SetGenericType.md)
 - [SetLanguage](docs/SetLanguage.md)
 - [SetLink](docs/SetLink.md)
 - [SetMagazine](docs/SetMagazine.md)
 - [SetPerson](docs/SetPerson.md)
 - [SetTag](docs/SetTag.md)
 - [SetWebsite](docs/SetWebsite.md)
 - [Tag](docs/Tag.md)
 - [Website](docs/Website.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization


Authentication schemes defined for the API:
<a id="BearerAuth"></a>
### BearerAuth

- **Type**: Bearer authentication (JWT)


## Author




