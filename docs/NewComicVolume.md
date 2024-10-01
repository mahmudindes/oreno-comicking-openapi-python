# NewComicVolume


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**number** | **float** |  | 
**released_at** | **datetime** |  | [optional] 

## Example

```python
from comicking_openapi.models.new_comic_volume import NewComicVolume

# TODO update the JSON string below
json = "{}"
# create an instance of NewComicVolume from a JSON string
new_comic_volume_instance = NewComicVolume.from_json(json)
# print the JSON string representation of the object
print(NewComicVolume.to_json())

# convert the object into a dict
new_comic_volume_dict = new_comic_volume_instance.to_dict()
# create an instance of NewComicVolume from a dict
new_comic_volume_form_dict = new_comic_volume.from_dict(new_comic_volume_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


