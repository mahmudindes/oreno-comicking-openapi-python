# NewComicCategory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category_type_code** | **str** |  | 
**category_code** | **str** |  | 

## Example

```python
from comicking_openapi.models.new_comic_category import NewComicCategory

# TODO update the JSON string below
json = "{}"
# create an instance of NewComicCategory from a JSON string
new_comic_category_instance = NewComicCategory.from_json(json)
# print the JSON string representation of the object
print(NewComicCategory.to_json())

# convert the object into a dict
new_comic_category_dict = new_comic_category_instance.to_dict()
# create an instance of NewComicCategory from a dict
new_comic_category_form_dict = new_comic_category.from_dict(new_comic_category_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


