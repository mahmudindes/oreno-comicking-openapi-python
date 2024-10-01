# NewComicChapter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**number** | **float** |  | 
**version** | **str** |  | [optional] 
**released_at** | **datetime** |  | [optional] 
**thumbnail_link_website_host** | **str** |  | [optional] 
**thumbnail_link_relative_reference** | **str** |  | [optional] 
**volume_number** | **str** |  | [optional] 

## Example

```python
from comicking_openapi.models.new_comic_chapter import NewComicChapter

# TODO update the JSON string below
json = "{}"
# create an instance of NewComicChapter from a JSON string
new_comic_chapter_instance = NewComicChapter.from_json(json)
# print the JSON string representation of the object
print(NewComicChapter.to_json())

# convert the object into a dict
new_comic_chapter_dict = new_comic_chapter_instance.to_dict()
# create an instance of NewComicChapter from a dict
new_comic_chapter_form_dict = new_comic_chapter.from_dict(new_comic_chapter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


