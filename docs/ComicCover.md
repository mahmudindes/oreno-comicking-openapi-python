# ComicCover


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | [optional] 
**ulid** | **str** |  | 
**link_website_host** | **str** |  | 
**link_relative_reference** | **str** |  | [optional] 
**hint** | **str** |  | [optional] 

## Example

```python
from comicking_openapi.models.comic_cover import ComicCover

# TODO update the JSON string below
json = "{}"
# create an instance of ComicCover from a JSON string
comic_cover_instance = ComicCover.from_json(json)
# print the JSON string representation of the object
print(ComicCover.to_json())

# convert the object into a dict
comic_cover_dict = comic_cover_instance.to_dict()
# create an instance of ComicCover from a dict
comic_cover_form_dict = comic_cover.from_dict(comic_cover_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


