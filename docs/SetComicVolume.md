# SetComicVolume


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**number** | **float** |  | [optional] 
**released_at** | **datetime** |  | [optional] 

## Example

```python
from comicking_openapi.models.set_comic_volume import SetComicVolume

# TODO update the JSON string below
json = "{}"
# create an instance of SetComicVolume from a JSON string
set_comic_volume_instance = SetComicVolume.from_json(json)
# print the JSON string representation of the object
print(SetComicVolume.to_json())

# convert the object into a dict
set_comic_volume_dict = set_comic_volume_instance.to_dict()
# create an instance of SetComicVolume from a dict
set_comic_volume_form_dict = set_comic_volume.from_dict(set_comic_volume_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


