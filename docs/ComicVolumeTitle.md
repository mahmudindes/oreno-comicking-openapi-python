# ComicVolumeTitle


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | [optional] 
**ulid** | **str** |  | 
**language_lang** | **str** |  | 
**content** | **str** |  | 
**is_synonym** | **bool** |  | [optional] 
**is_latinized** | **bool** |  | [optional] 

## Example

```python
from comicking_openapi.models.comic_volume_title import ComicVolumeTitle

# TODO update the JSON string below
json = "{}"
# create an instance of ComicVolumeTitle from a JSON string
comic_volume_title_instance = ComicVolumeTitle.from_json(json)
# print the JSON string representation of the object
print(ComicVolumeTitle.to_json())

# convert the object into a dict
comic_volume_title_dict = comic_volume_title_instance.to_dict()
# create an instance of ComicVolumeTitle from a dict
comic_volume_title_form_dict = comic_volume_title.from_dict(comic_volume_title_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


