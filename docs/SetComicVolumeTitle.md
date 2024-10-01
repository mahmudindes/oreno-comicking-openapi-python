# SetComicVolumeTitle


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**language_lang** | **str** |  | [optional] 
**content** | **str** |  | [optional] 
**is_synonym** | **bool** |  | [optional] 
**is_latinized** | **bool** |  | [optional] 

## Example

```python
from comicking_openapi.models.set_comic_volume_title import SetComicVolumeTitle

# TODO update the JSON string below
json = "{}"
# create an instance of SetComicVolumeTitle from a JSON string
set_comic_volume_title_instance = SetComicVolumeTitle.from_json(json)
# print the JSON string representation of the object
print(SetComicVolumeTitle.to_json())

# convert the object into a dict
set_comic_volume_title_dict = set_comic_volume_title_instance.to_dict()
# create an instance of SetComicVolumeTitle from a dict
set_comic_volume_title_form_dict = set_comic_volume_title.from_dict(set_comic_volume_title_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


