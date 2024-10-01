# ComicCharacter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | [optional] 
**character_code** | **str** |  | 
**is_main** | **bool** |  | [optional] 

## Example

```python
from comicking_openapi.models.comic_character import ComicCharacter

# TODO update the JSON string below
json = "{}"
# create an instance of ComicCharacter from a JSON string
comic_character_instance = ComicCharacter.from_json(json)
# print the JSON string representation of the object
print(ComicCharacter.to_json())

# convert the object into a dict
comic_character_dict = comic_character_instance.to_dict()
# create an instance of ComicCharacter from a dict
comic_character_form_dict = comic_character.from_dict(comic_character_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


