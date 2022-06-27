# QuestionBatch

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | A unique identifier for the questionBatch object | [optional] 
**job_id** | **str** | A unique identifier programmatically assigned to the Bulk QA job | [optional] 
**batch_grouping_key** | **str** | User assigned key for a QA batch (e.g. \&quot;Batch_QA_V1\&quot;) | [optional] 
**question_keys** | **list[str]** | User assigned key for a question within the QA batch (e.g. \&quot;Study Drug\&quot;) | [optional] 
**saved_list_ids** | **list[str]** | IDs of the Layar Sets used when submitting a Bulk QA job | [optional] 
**question_count** | **int** | The total number of questions in this batch. Sum of queued and completed. | [optional] 
**questions_queued** | **int** | Questions yet to be answered | [optional] 
**questions_completed** | **int** | Should always be the sum of answered, skipped, and failed | [optional] 
**questions_answered** | **int** | Successfully submitted to the QA service and a response received | [optional] 
**questions_skipped** | **int** | Skipped because the batch was cancelled | [optional] 
**questions_failed** | **int** | Error submitting to QA service or processing the response | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

