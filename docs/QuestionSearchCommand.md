# QuestionSearchCommand

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**batch_grouping_key** | **str** | limit results to answers from a batch query | [optional] 
**complete** | **list[str]** | limit results to questions that have finished being answered | [optional] 
**data_providers** | **list[str]** | limit results to questions that contain specified data providers (host names) | [optional] 
**query_strings** | **list[str]** | limit results to questions that contain specified query strings | [optional] 
**question_ids** | **list[str]** | limit results to questions that have specifified identifiers | [optional] 
**assigned_user_ids** | **list[int]** | limit results to questions assigned to the given user ids | [optional] 
**question_key** | **str** | limit results to answers with a specific question key | [optional] 
**search** | [**ParagraphQuestionSearchCommand**](ParagraphQuestionSearchCommand.md) |  | [optional] 
**single_doc_question_document_id** | **str** | include answers that were asked of a single document | [optional] 
**source_fields** | **object** |  | [optional] 
**type_of_search** | [**QuestionAnswerTypeOfSearch**](QuestionAnswerTypeOfSearch.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

