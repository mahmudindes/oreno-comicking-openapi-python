# SetComic


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**published_from** | **datetime** |  | [optional] 
**published_to** | **datetime** |  | [optional] 
**total_chapter** | **int** |  | [optional] 
**total_volume** | **int** |  | [optional] 
**nsfw** | **int** |  | [optional] 
**nsfl** | **int** |  | [optional] 

## Example

```python
from comicking_openapi.models.set_comic import SetComic

# TODO update the JSON string below
json = "{}"
# create an instance of SetComic from a JSON string
set_comic_instance = SetComic.from_json(json)
# print the JSON string representation of the object
print(SetComic.to_json())

# convert the object into a dict
set_comic_dict = set_comic_instance.to_dict()
# create an instance of SetComic from a dict
set_comic_form_dict = set_comic.from_dict(set_comic_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


