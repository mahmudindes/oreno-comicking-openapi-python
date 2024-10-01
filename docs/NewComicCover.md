# NewComicCover


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link_website_host** | **str** |  | 
**link_relative_reference** | **str** |  | [optional] 
**hint** | **str** |  | [optional] 

## Example

```python
from comicking_openapi.models.new_comic_cover import NewComicCover

# TODO update the JSON string below
json = "{}"
# create an instance of NewComicCover from a JSON string
new_comic_cover_instance = NewComicCover.from_json(json)
# print the JSON string representation of the object
print(NewComicCover.to_json())

# convert the object into a dict
new_comic_cover_dict = new_comic_cover_instance.to_dict()
# create an instance of NewComicCover from a dict
new_comic_cover_form_dict = new_comic_cover.from_dict(new_comic_cover_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


