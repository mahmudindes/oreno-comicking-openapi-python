# SetComicSynopsis


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**language_lang** | **str** |  | [optional] 
**content** | **str** |  | [optional] 
**source** | **str** |  | [optional] 

## Example

```python
from comicking_openapi.models.set_comic_synopsis import SetComicSynopsis

# TODO update the JSON string below
json = "{}"
# create an instance of SetComicSynopsis from a JSON string
set_comic_synopsis_instance = SetComicSynopsis.from_json(json)
# print the JSON string representation of the object
print(SetComicSynopsis.to_json())

# convert the object into a dict
set_comic_synopsis_dict = set_comic_synopsis_instance.to_dict()
# create an instance of SetComicSynopsis from a dict
set_comic_synopsis_form_dict = set_comic_synopsis.from_dict(set_comic_synopsis_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


