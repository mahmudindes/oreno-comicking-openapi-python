# NewComicRelation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type_code** | **str** |  | 
**child_code** | **str** |  | 

## Example

```python
from comicking_openapi.models.new_comic_relation import NewComicRelation

# TODO update the JSON string below
json = "{}"
# create an instance of NewComicRelation from a JSON string
new_comic_relation_instance = NewComicRelation.from_json(json)
# print the JSON string representation of the object
print(NewComicRelation.to_json())

# convert the object into a dict
new_comic_relation_dict = new_comic_relation_instance.to_dict()
# create an instance of NewComicRelation from a dict
new_comic_relation_form_dict = new_comic_relation.from_dict(new_comic_relation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


