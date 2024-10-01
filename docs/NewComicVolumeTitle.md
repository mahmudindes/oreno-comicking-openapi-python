# NewComicVolumeTitle


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**language_lang** | **str** |  | 
**content** | **str** |  | 
**is_synonym** | **bool** |  | [optional] 
**is_latinized** | **bool** |  | [optional] 

## Example

```python
from comicking_openapi.models.new_comic_volume_title import NewComicVolumeTitle

# TODO update the JSON string below
json = "{}"
# create an instance of NewComicVolumeTitle from a JSON string
new_comic_volume_title_instance = NewComicVolumeTitle.from_json(json)
# print the JSON string representation of the object
print(NewComicVolumeTitle.to_json())

# convert the object into a dict
new_comic_volume_title_dict = new_comic_volume_title_instance.to_dict()
# create an instance of NewComicVolumeTitle from a dict
new_comic_volume_title_form_dict = new_comic_volume_title.from_dict(new_comic_volume_title_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


