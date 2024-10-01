# ComicVolumeCover


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
from comicking_openapi.models.comic_volume_cover import ComicVolumeCover

# TODO update the JSON string below
json = "{}"
# create an instance of ComicVolumeCover from a JSON string
comic_volume_cover_instance = ComicVolumeCover.from_json(json)
# print the JSON string representation of the object
print(ComicVolumeCover.to_json())

# convert the object into a dict
comic_volume_cover_dict = comic_volume_cover_instance.to_dict()
# create an instance of ComicVolumeCover from a dict
comic_volume_cover_form_dict = comic_volume_cover.from_dict(comic_volume_cover_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


