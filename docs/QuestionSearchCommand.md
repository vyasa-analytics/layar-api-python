# QuestionSearchCommand

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**batch_grouping_key** | **str** | limit results to answers from a batch query | [optional] 
**batch_grouping_keys** | **list[str]** | limit results to answers from a list of batch queries | [optional] 
**complete** | **list[str]** | limit results to questions that have finished being answered | [optional] 
**data_providers** | **list[str]** | limit results to questions that contain specified data providers (host names) | [optional] 
**query_strings** | **list[str]** | limit results to questions that contain specified query strings | [optional] 
**question_ids** | **list[str]** | limit results to questions that have specified identifiers | [optional] 
**assigned_user_ids** | **list[int]** | limit results to questions assigned to the given user ids | [optional] 
**moderator_user_ids** | **list[int]** | limit results to questions assigned to user IDs with the moderator curation role | [optional] 
**question_key** | **str** | limit results to answers with a specific question key | [optional] 
**question_keys** | **list[str]** | limit results to answers from a list of question keys | [optional] 
**search** | [**ParagraphQuestionSearchCommand**](ParagraphQuestionSearchCommand.md) |  | [optional] 
**single_doc_question_document_id** | **str** | include answers that were asked of a single document | [optional] 
**single_doc_question_document_ids** | **list[str]** | include answers that were asked from a list of documents | [optional] 
**source_fields** | **object** |  | [optional] 
**type_of_search** | [**QuestionAnswerTypeOfSearch**](QuestionAnswerTypeOfSearch.md) |  | [optional] 
**curation_complete** | **list[str]** | determine whether every user has (not) provided an answer for a given document curation | [optional] 
**curation_discord** | **list[str]** | determine whether there is (not) a discrepancy between users&#x27; answers for a given document curation | [optional] 
**moderated** | **list[str]** | determine whether a user with the moderator curation role has (not) added a curated answer | [optional] 
**has_assigned_users** | **list[str]** | a question has (doesn&#x27;t have) assignedUserIds | [optional] 
**has_moderator_users** | **list[str]** | a question has (doesn&#x27;t have) moderatorUserIds | [optional] 
**has_user_curations** | **list[str]** | a question has (doesn&#x27;t have) any user provided curations | [optional] 
**curation_complete_for_assigned_user_ids** | **list[str]** | a question has (doesn&#x27;t have) all assigned user provided curations | [optional] 
**has_answers** | **list[str]** | a question has a model generated answer | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

