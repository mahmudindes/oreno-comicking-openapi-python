# ComicTag


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | [optional] 
**tag_type_code** | **str** |  | 
**tag_code** | **str** |  | 

## Example

```python
from comicking_openapi.models.comic_tag import ComicTag

# TODO update the JSON string below
json = "{}"
# create an instance of ComicTag from a JSON string
comic_tag_instance = ComicTag.from_json(json)
# print the JSON string representation of the object
print(ComicTag.to_json())

# convert the object into a dict
comic_tag_dict = comic_tag_instance.to_dict()
# create an instance of ComicTag from a dict
comic_tag_form_dict = comic_tag.from_dict(comic_tag_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


