# NewComicExternal


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link_website_host** | **str** |  | 
**link_relative_reference** | **str** |  | [optional] 
**is_official** | **bool** |  | [optional] 
**is_community** | **bool** |  | [optional] 

## Example

```python
from comicking_openapi.models.new_comic_external import NewComicExternal

# TODO update the JSON string below
json = "{}"
# create an instance of NewComicExternal from a JSON string
new_comic_external_instance = NewComicExternal.from_json(json)
# print the JSON string representation of the object
print(NewComicExternal.to_json())

# convert the object into a dict
new_comic_external_dict = new_comic_external_instance.to_dict()
# create an instance of NewComicExternal from a dict
new_comic_external_form_dict = new_comic_external.from_dict(new_comic_external_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


