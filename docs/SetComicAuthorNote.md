# SetComicAuthorNote


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**language_lang** | **str** |  | [optional] 
**content** | **str** |  | [optional] 

## Example

```python
from comicking_openapi.models.set_comic_author_note import SetComicAuthorNote

# TODO update the JSON string below
json = "{}"
# create an instance of SetComicAuthorNote from a JSON string
set_comic_author_note_instance = SetComicAuthorNote.from_json(json)
# print the JSON string representation of the object
print(SetComicAuthorNote.to_json())

# convert the object into a dict
set_comic_author_note_dict = set_comic_author_note_instance.to_dict()
# create an instance of SetComicAuthorNote from a dict
set_comic_author_note_form_dict = set_comic_author_note.from_dict(set_comic_author_note_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


