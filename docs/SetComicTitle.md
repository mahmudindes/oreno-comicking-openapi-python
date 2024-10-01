# SetComicTitle


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**language_lang** | **str** |  | [optional] 
**content** | **str** |  | [optional] 
**is_synonym** | **bool** |  | [optional] 
**is_latinized** | **bool** |  | [optional] 

## Example

```python
from comicking_openapi.models.set_comic_title import SetComicTitle

# TODO update the JSON string below
json = "{}"
# create an instance of SetComicTitle from a JSON string
set_comic_title_instance = SetComicTitle.from_json(json)
# print the JSON string representation of the object
print(SetComicTitle.to_json())

# convert the object into a dict
set_comic_title_dict = set_comic_title_instance.to_dict()
# create an instance of SetComicTitle from a dict
set_comic_title_form_dict = set_comic_title.from_dict(set_comic_title_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


