# SetComicRelation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type_code** | **str** |  | [optional] 
**child_code** | **str** |  | [optional] 

## Example

```python
from comicking_openapi.models.set_comic_relation import SetComicRelation

# TODO update the JSON string below
json = "{}"
# create an instance of SetComicRelation from a JSON string
set_comic_relation_instance = SetComicRelation.from_json(json)
# print the JSON string representation of the object
print(SetComicRelation.to_json())

# convert the object into a dict
set_comic_relation_dict = set_comic_relation_instance.to_dict()
# create an instance of SetComicRelation from a dict
set_comic_relation_form_dict = set_comic_relation.from_dict(set_comic_relation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


