# ComicTitle


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
from comicking_openapi.models.comic_title import ComicTitle

# TODO update the JSON string below
json = "{}"
# create an instance of ComicTitle from a JSON string
comic_title_instance = ComicTitle.from_json(json)
# print the JSON string representation of the object
print(ComicTitle.to_json())

# convert the object into a dict
comic_title_dict = comic_title_instance.to_dict()
# create an instance of ComicTitle from a dict
comic_title_form_dict = comic_title.from_dict(comic_title_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


