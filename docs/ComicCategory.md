# ComicCategory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | [optional] 
**category_type_code** | **str** |  | 
**category_code** | **str** |  | 

## Example

```python
from comicking_openapi.models.comic_category import ComicCategory

# TODO update the JSON string below
json = "{}"
# create an instance of ComicCategory from a JSON string
comic_category_instance = ComicCategory.from_json(json)
# print the JSON string representation of the object
print(ComicCategory.to_json())

# convert the object into a dict
comic_category_dict = comic_category_instance.to_dict()
# create an instance of ComicCategory from a dict
comic_category_form_dict = comic_category.from_dict(comic_category_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


