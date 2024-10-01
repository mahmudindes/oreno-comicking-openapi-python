# SetComicAuthor


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type_code** | **str** |  | [optional] 
**person_code** | **str** |  | [optional] 

## Example

```python
from comicking_openapi.models.set_comic_author import SetComicAuthor

# TODO update the JSON string below
json = "{}"
# create an instance of SetComicAuthor from a JSON string
set_comic_author_instance = SetComicAuthor.from_json(json)
# print the JSON string representation of the object
print(SetComicAuthor.to_json())

# convert the object into a dict
set_comic_author_dict = set_comic_author_instance.to_dict()
# create an instance of SetComicAuthor from a dict
set_comic_author_form_dict = set_comic_author.from_dict(set_comic_author_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


