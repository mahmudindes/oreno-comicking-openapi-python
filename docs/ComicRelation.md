# ComicRelation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | [optional] 
**type_code** | **str** |  | 
**child_code** | **str** |  | 

## Example

```python
from comicking_openapi.models.comic_relation import ComicRelation

# TODO update the JSON string below
json = "{}"
# create an instance of ComicRelation from a JSON string
comic_relation_instance = ComicRelation.from_json(json)
# print the JSON string representation of the object
print(ComicRelation.to_json())

# convert the object into a dict
comic_relation_dict = comic_relation_instance.to_dict()
# create an instance of ComicRelation from a dict
comic_relation_form_dict = comic_relation.from_dict(comic_relation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


