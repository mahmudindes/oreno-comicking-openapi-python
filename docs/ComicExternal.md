# ComicExternal


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | [optional] 
**ulid** | **str** |  | 
**link_website_host** | **str** |  | 
**link_website_name** | **str** |  | 
**link_relative_reference** | **str** |  | [optional] 
**is_official** | **bool** |  | [optional] 
**is_community** | **bool** |  | [optional] 

## Example

```python
from comicking_openapi.models.comic_external import ComicExternal

# TODO update the JSON string below
json = "{}"
# create an instance of ComicExternal from a JSON string
comic_external_instance = ComicExternal.from_json(json)
# print the JSON string representation of the object
print(ComicExternal.to_json())

# convert the object into a dict
comic_external_dict = comic_external_instance.to_dict()
# create an instance of ComicExternal from a dict
comic_external_form_dict = comic_external.from_dict(comic_external_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


