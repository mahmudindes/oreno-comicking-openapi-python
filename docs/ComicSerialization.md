# ComicSerialization


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | [optional] 
**magazine_code** | **str** |  | 

## Example

```python
from comicking_openapi.models.comic_serialization import ComicSerialization

# TODO update the JSON string below
json = "{}"
# create an instance of ComicSerialization from a JSON string
comic_serialization_instance = ComicSerialization.from_json(json)
# print the JSON string representation of the object
print(ComicSerialization.to_json())

# convert the object into a dict
comic_serialization_dict = comic_serialization_instance.to_dict()
# create an instance of ComicSerialization from a dict
comic_serialization_form_dict = comic_serialization.from_dict(comic_serialization_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


