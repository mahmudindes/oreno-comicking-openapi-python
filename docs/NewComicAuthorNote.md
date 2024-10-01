# NewComicAuthorNote


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**language_lang** | **str** |  | 
**content** | **str** |  | 

## Example

```python
from comicking_openapi.models.new_comic_author_note import NewComicAuthorNote

# TODO update the JSON string below
json = "{}"
# create an instance of NewComicAuthorNote from a JSON string
new_comic_author_note_instance = NewComicAuthorNote.from_json(json)
# print the JSON string representation of the object
print(NewComicAuthorNote.to_json())

# convert the object into a dict
new_comic_author_note_dict = new_comic_author_note_instance.to_dict()
# create an instance of NewComicAuthorNote from a dict
new_comic_author_note_form_dict = new_comic_author_note.from_dict(new_comic_author_note_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


