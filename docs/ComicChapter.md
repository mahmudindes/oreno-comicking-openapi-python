# ComicChapter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | [optional] 
**number** | **float** |  | 
**version** | **str** |  | [optional] 
**released_at** | **datetime** |  | [optional] 
**thumbnail_link_website_host** | **str** |  | [optional] 
**thumbnail_link_relative_reference** | **str** |  | [optional] 
**volume_number** | **str** |  | [optional] 
**title_count** | **int** |  | 

## Example

```python
from comicking_openapi.models.comic_chapter import ComicChapter

# TODO update the JSON string below
json = "{}"
# create an instance of ComicChapter from a JSON string
comic_chapter_instance = ComicChapter.from_json(json)
# print the JSON string representation of the object
print(ComicChapter.to_json())

# convert the object into a dict
comic_chapter_dict = comic_chapter_instance.to_dict()
# create an instance of ComicChapter from a dict
comic_chapter_form_dict = comic_chapter.from_dict(comic_chapter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


