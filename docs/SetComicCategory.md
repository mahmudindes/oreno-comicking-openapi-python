# SetComicCategory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category_type_code** | **str** |  | [optional] 
**category_code** | **str** |  | [optional] 

## Example

```python
from comicking_openapi.models.set_comic_category import SetComicCategory

# TODO update the JSON string below
json = "{}"
# create an instance of SetComicCategory from a JSON string
set_comic_category_instance = SetComicCategory.from_json(json)
# print the JSON string representation of the object
print(SetComicCategory.to_json())

# convert the object into a dict
set_comic_category_dict = set_comic_category_instance.to_dict()
# create an instance of SetComicCategory from a dict
set_comic_category_form_dict = set_comic_category.from_dict(set_comic_category_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


