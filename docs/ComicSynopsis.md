# ComicSynopsis


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | [optional] 
**ulid** | **str** |  | 
**language_lang** | **str** |  | 
**content** | **str** |  | 
**source** | **str** |  | [optional] 

## Example

```python
from comicking_openapi.models.comic_synopsis import ComicSynopsis

# TODO update the JSON string below
json = "{}"
# create an instance of ComicSynopsis from a JSON string
comic_synopsis_instance = ComicSynopsis.from_json(json)
# print the JSON string representation of the object
print(ComicSynopsis.to_json())

# convert the object into a dict
comic_synopsis_dict = comic_synopsis_instance.to_dict()
# create an instance of ComicSynopsis from a dict
comic_synopsis_form_dict = comic_synopsis.from_dict(comic_synopsis_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


