# SetComicVolumeCover


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link_website_host** | **str** |  | [optional] 
**link_relative_reference** | **str** |  | [optional] 
**hint** | **str** |  | [optional] 

## Example

```python
from comicking_openapi.models.set_comic_volume_cover import SetComicVolumeCover

# TODO update the JSON string below
json = "{}"
# create an instance of SetComicVolumeCover from a JSON string
set_comic_volume_cover_instance = SetComicVolumeCover.from_json(json)
# print the JSON string representation of the object
print(SetComicVolumeCover.to_json())

# convert the object into a dict
set_comic_volume_cover_dict = set_comic_volume_cover_instance.to_dict()
# create an instance of SetComicVolumeCover from a dict
set_comic_volume_cover_form_dict = set_comic_volume_cover.from_dict(set_comic_volume_cover_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


