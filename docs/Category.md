# Category


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | [optional] 
**type_code** | **str** |  | 
**code** | **str** |  | 
**name** | **str** |  | 
**link_website_host** | **str** |  | [optional] 
**link_relative_reference** | **str** |  | [optional] 
**parent_code** | **str** |  | [optional] 
**child_count** | **int** |  | 

## Example

```python
from comicking_openapi.models.category import Category

# TODO update the JSON string below
json = "{}"
# create an instance of Category from a JSON string
category_instance = Category.from_json(json)
# print the JSON string representation of the object
print(Category.to_json())

# convert the object into a dict
category_dict = category_instance.to_dict()
# create an instance of Category from a dict
category_form_dict = category.from_dict(category_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


