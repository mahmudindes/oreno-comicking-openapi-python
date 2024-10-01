# Comic


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | [optional] 
**code** | **str** |  | 
**published_from** | **datetime** |  | [optional] 
**published_to** | **datetime** |  | [optional] 
**total_chapter** | **int** |  | [optional] 
**total_volume** | **int** |  | [optional] 
**nsfw** | **int** |  | [optional] 
**nsfl** | **int** |  | [optional] 
**title_count** | **int** |  | 
**cover_count** | **int** |  | 
**synopsis_count** | **int** |  | 
**character_count** | **int** |  | 
**author_count** | **int** |  | 
**serialization_count** | **int** |  | 
**external_count** | **int** |  | 
**chapter_count** | **int** |  | 
**volume_count** | **int** |  | 
**category_count** | **int** |  | 
**tag_count** | **int** |  | 
**relation_count** | **int** |  | 

## Example

```python
from comicking_openapi.models.comic import Comic

# TODO update the JSON string below
json = "{}"
# create an instance of Comic from a JSON string
comic_instance = Comic.from_json(json)
# print the JSON string representation of the object
print(Comic.to_json())

# convert the object into a dict
comic_dict = comic_instance.to_dict()
# create an instance of Comic from a dict
comic_form_dict = comic.from_dict(comic_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


