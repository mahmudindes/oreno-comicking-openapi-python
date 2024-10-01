# ComicVolume


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | [optional] 
**number** | **float** |  | 
**released_at** | **datetime** |  | [optional] 
**title_count** | **str** |  | 
**cover_count** | **str** |  | 
**chapter_count** | **str** |  | 

## Example

```python
from comicking_openapi.models.comic_volume import ComicVolume

# TODO update the JSON string below
json = "{}"
# create an instance of ComicVolume from a JSON string
comic_volume_instance = ComicVolume.from_json(json)
# print the JSON string representation of the object
print(ComicVolume.to_json())

# convert the object into a dict
comic_volume_dict = comic_volume_instance.to_dict()
# create an instance of ComicVolume from a dict
comic_volume_form_dict = comic_volume.from_dict(comic_volume_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


