# SetComicTag


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tag_type_code** | **str** |  | [optional] 
**tag_code** | **str** |  | [optional] 

## Example

```python
from comicking_openapi.models.set_comic_tag import SetComicTag

# TODO update the JSON string below
json = "{}"
# create an instance of SetComicTag from a JSON string
set_comic_tag_instance = SetComicTag.from_json(json)
# print the JSON string representation of the object
print(SetComicTag.to_json())

# convert the object into a dict
set_comic_tag_dict = set_comic_tag_instance.to_dict()
# create an instance of SetComicTag from a dict
set_comic_tag_form_dict = set_comic_tag.from_dict(set_comic_tag_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


