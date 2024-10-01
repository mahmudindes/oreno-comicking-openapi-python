# ComicAuthorNote


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | [optional] 
**ulid** | **str** |  | 
**language_lang** | **str** |  | 
**content** | **str** |  | 

## Example

```python
from comicking_openapi.models.comic_author_note import ComicAuthorNote

# TODO update the JSON string below
json = "{}"
# create an instance of ComicAuthorNote from a JSON string
comic_author_note_instance = ComicAuthorNote.from_json(json)
# print the JSON string representation of the object
print(ComicAuthorNote.to_json())

# convert the object into a dict
comic_author_note_dict = comic_author_note_instance.to_dict()
# create an instance of ComicAuthorNote from a dict
comic_author_note_form_dict = comic_author_note.from_dict(comic_author_note_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


