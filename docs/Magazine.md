# Magazine


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | [optional] 
**code** | **str** |  | 

## Example

```python
from comicking_openapi.models.magazine import Magazine

# TODO update the JSON string below
json = "{}"
# create an instance of Magazine from a JSON string
magazine_instance = Magazine.from_json(json)
# print the JSON string representation of the object
print(Magazine.to_json())

# convert the object into a dict
magazine_dict = magazine_instance.to_dict()
# create an instance of Magazine from a dict
magazine_form_dict = magazine.from_dict(magazine_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


