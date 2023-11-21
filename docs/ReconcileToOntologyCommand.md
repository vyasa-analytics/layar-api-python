# ReconcileToOntologyCommand

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ontology_id** | **str** | the ID of the ontology file (sourceDocument) the terms will be reconciled against | 
**terms** | **list[str]** | terms to reconcile against the ontology (maximum 500) | 
**max_predictions** | **int** | the maximum number of predicted results to return per reconciled term | [optional] 
**threshold** | **float** | the minimum confidence threshold (range is 0-1) | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

