# GenericType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | [optional] 
**code** | **str** |  | 
**name** | **str** |  | 

## Example

```python
from comicking_openapi.models.generic_type import GenericType

# TODO update the JSON string below
json = "{}"
# create an instance of GenericType from a JSON string
generic_type_instance = GenericType.from_json(json)
# print the JSON string representation of the object
print(GenericType.to_json())

# convert the object into a dict
generic_type_dict = generic_type_instance.to_dict()
# create an instance of GenericType from a dict
generic_type_form_dict = generic_type.from_dict(generic_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


