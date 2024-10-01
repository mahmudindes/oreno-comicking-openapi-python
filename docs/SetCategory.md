# SetCategory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type_code** | **str** |  | [optional] 
**code** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**link_website_host** | **str** |  | [optional] 
**link_relative_reference** | **str** |  | [optional] 
**parent_code** | **str** |  | [optional] 

## Example

```python
from comicking_openapi.models.set_category import SetCategory

# TODO update the JSON string below
json = "{}"
# create an instance of SetCategory from a JSON string
set_category_instance = SetCategory.from_json(json)
# print the JSON string representation of the object
print(SetCategory.to_json())

# convert the object into a dict
set_category_dict = set_category_instance.to_dict()
# create an instance of SetCategory from a dict
set_category_form_dict = set_category.from_dict(set_category_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


