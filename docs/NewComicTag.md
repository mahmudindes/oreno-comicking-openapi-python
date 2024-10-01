# NewComicTag


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tag_type_code** | **str** |  | 
**tag_code** | **str** |  | 

## Example

```python
from comicking_openapi.models.new_comic_tag import NewComicTag

# TODO update the JSON string below
json = "{}"
# create an instance of NewComicTag from a JSON string
new_comic_tag_instance = NewComicTag.from_json(json)
# print the JSON string representation of the object
print(NewComicTag.to_json())

# convert the object into a dict
new_comic_tag_dict = new_comic_tag_instance.to_dict()
# create an instance of NewComicTag from a dict
new_comic_tag_form_dict = new_comic_tag.from_dict(new_comic_tag_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


