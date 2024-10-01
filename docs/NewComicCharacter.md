# NewComicCharacter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**person_code** | **str** |  | 
**is_main** | **bool** |  | [optional] 

## Example

```python
from comicking_openapi.models.new_comic_character import NewComicCharacter

# TODO update the JSON string below
json = "{}"
# create an instance of NewComicCharacter from a JSON string
new_comic_character_instance = NewComicCharacter.from_json(json)
# print the JSON string representation of the object
print(NewComicCharacter.to_json())

# convert the object into a dict
new_comic_character_dict = new_comic_character_instance.to_dict()
# create an instance of NewComicCharacter from a dict
new_comic_character_form_dict = new_comic_character.from_dict(new_comic_character_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


