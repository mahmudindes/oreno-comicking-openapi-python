# NewCategory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type_code** | **str** |  | 
**code** | **str** |  | 
**name** | **str** |  | 
**link_website_host** | **str** |  | [optional] 
**link_relative_reference** | **str** |  | [optional] 
**parent_code** | **str** |  | [optional] 

## Example

```python
from comicking_openapi.models.new_category import NewCategory

# TODO update the JSON string below
json = "{}"
# create an instance of NewCategory from a JSON string
new_category_instance = NewCategory.from_json(json)
# print the JSON string representation of the object
print(NewCategory.to_json())

# convert the object into a dict
new_category_dict = new_category_instance.to_dict()
# create an instance of NewCategory from a dict
new_category_form_dict = new_category.from_dict(new_category_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


