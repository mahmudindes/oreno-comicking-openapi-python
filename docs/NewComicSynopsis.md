# NewComicSynopsis


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**language_lang** | **str** |  | 
**content** | **str** |  | 
**source** | **str** |  | [optional] 

## Example

```python
from comicking_openapi.models.new_comic_synopsis import NewComicSynopsis

# TODO update the JSON string below
json = "{}"
# create an instance of NewComicSynopsis from a JSON string
new_comic_synopsis_instance = NewComicSynopsis.from_json(json)
# print the JSON string representation of the object
print(NewComicSynopsis.to_json())

# convert the object into a dict
new_comic_synopsis_dict = new_comic_synopsis_instance.to_dict()
# create an instance of NewComicSynopsis from a dict
new_comic_synopsis_form_dict = new_comic_synopsis.from_dict(new_comic_synopsis_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


