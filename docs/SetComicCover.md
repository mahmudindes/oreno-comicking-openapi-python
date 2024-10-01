# SetComicCover


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link_website_host** | **str** |  | [optional] 
**link_relative_reference** | **str** |  | [optional] 
**hint** | **str** |  | [optional] 

## Example

```python
from comicking_openapi.models.set_comic_cover import SetComicCover

# TODO update the JSON string below
json = "{}"
# create an instance of SetComicCover from a JSON string
set_comic_cover_instance = SetComicCover.from_json(json)
# print the JSON string representation of the object
print(SetComicCover.to_json())

# convert the object into a dict
set_comic_cover_dict = set_comic_cover_instance.to_dict()
# create an instance of SetComicCover from a dict
set_comic_cover_form_dict = set_comic_cover.from_dict(set_comic_cover_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


