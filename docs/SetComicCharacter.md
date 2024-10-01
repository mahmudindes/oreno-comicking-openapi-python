# SetComicCharacter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**person_code** | **str** |  | [optional] 
**is_main** | **bool** |  | [optional] 

## Example

```python
from comicking_openapi.models.set_comic_character import SetComicCharacter

# TODO update the JSON string below
json = "{}"
# create an instance of SetComicCharacter from a JSON string
set_comic_character_instance = SetComicCharacter.from_json(json)
# print the JSON string representation of the object
print(SetComicCharacter.to_json())

# convert the object into a dict
set_comic_character_dict = set_comic_character_instance.to_dict()
# create an instance of SetComicCharacter from a dict
set_comic_character_form_dict = set_comic_character.from_dict(set_comic_character_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


