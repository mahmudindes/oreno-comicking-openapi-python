# ComicAuthor


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | [optional] 
**type_code** | **str** |  | 
**person_code** | **str** |  | 
**note_count** | **int** |  | 

## Example

```python
from comicking_openapi.models.comic_author import ComicAuthor

# TODO update the JSON string below
json = "{}"
# create an instance of ComicAuthor from a JSON string
comic_author_instance = ComicAuthor.from_json(json)
# print the JSON string representation of the object
print(ComicAuthor.to_json())

# convert the object into a dict
comic_author_dict = comic_author_instance.to_dict()
# create an instance of ComicAuthor from a dict
comic_author_form_dict = comic_author.from_dict(comic_author_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


