# SetTag


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type_code** | **str** |  | [optional] 
**code** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**link_website_host** | **str** |  | [optional] 
**link_relative_reference** | **str** |  | [optional] 

## Example

```python
from comicking_openapi.models.set_tag import SetTag

# TODO update the JSON string below
json = "{}"
# create an instance of SetTag from a JSON string
set_tag_instance = SetTag.from_json(json)
# print the JSON string representation of the object
print(SetTag.to_json())

# convert the object into a dict
set_tag_dict = set_tag_instance.to_dict()
# create an instance of SetTag from a dict
set_tag_form_dict = set_tag.from_dict(set_tag_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


