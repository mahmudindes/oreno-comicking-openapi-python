# NewTag


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type_code** | **str** |  | 
**code** | **str** |  | 
**name** | **str** |  | 
**link_website_host** | **str** |  | [optional] 
**link_relative_reference** | **str** |  | [optional] 

## Example

```python
from comicking_openapi.models.new_tag import NewTag

# TODO update the JSON string below
json = "{}"
# create an instance of NewTag from a JSON string
new_tag_instance = NewTag.from_json(json)
# print the JSON string representation of the object
print(NewTag.to_json())

# convert the object into a dict
new_tag_dict = new_tag_instance.to_dict()
# create an instance of NewTag from a dict
new_tag_form_dict = new_tag.from_dict(new_tag_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


