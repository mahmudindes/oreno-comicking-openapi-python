# NewComicAuthor


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type_code** | **str** |  | 
**person_code** | **str** |  | 

## Example

```python
from comicking_openapi.models.new_comic_author import NewComicAuthor

# TODO update the JSON string below
json = "{}"
# create an instance of NewComicAuthor from a JSON string
new_comic_author_instance = NewComicAuthor.from_json(json)
# print the JSON string representation of the object
print(NewComicAuthor.to_json())

# convert the object into a dict
new_comic_author_dict = new_comic_author_instance.to_dict()
# create an instance of NewComicAuthor from a dict
new_comic_author_form_dict = new_comic_author.from_dict(new_comic_author_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


