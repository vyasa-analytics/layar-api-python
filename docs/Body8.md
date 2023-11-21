# Body8

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Provide a name for the new ontology | 
**label** | **str** | The column key to use when creating term labels | 
**parent** | **str** | The column key to use for creating hierarchical relationships. The value in this cell should match the ID value of another row in the table. | [optional] 
**synonyms** | **list[str]** | The column key(s) to use when creating term synonyms | [optional] 
**properties** | **list[str]** | The column keys(s) to use when creating term properties | [optional] 
**delimiter** | **str** | If term synonyms are collected in a single column, please provide a delimiter to separate each one | [optional] 
**start_row** | **int** | The first row with ontology term data (and not a header row). Defaults to 0. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

