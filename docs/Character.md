# Character


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | [optional] 
**code** | **str** |  | 

## Example

```python
from comicking_openapi.models.character import Character

# TODO update the JSON string below
json = "{}"
# create an instance of Character from a JSON string
character_instance = Character.from_json(json)
# print the JSON string representation of the object
print(Character.to_json())

# convert the object into a dict
character_dict = character_instance.to_dict()
# create an instance of Character from a dict
character_form_dict = character.from_dict(character_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


