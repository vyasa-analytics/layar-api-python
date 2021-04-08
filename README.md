# Layar API Python Client

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

Install this package using pip:
```sh
pip install git+https://github.com/vyasa-analytics/layar-api-python.git
```

Then import the package:
```python
import layar_api 
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import layar_api
from layar_api.rest import ApiException
from pprint import pprint

# configure oauth access token for authorization
configuration = layar_api.Configuration()
configuration.host = 'HOST_NAME'
configuration.access_token = configuration.fetch_access_token('CLIENT_ID', 'CLIENT_SECRET')

# create an instance of the api class
api_instance = layar_api.SourceDocumentApi(layar_api.ApiClient(configuration))
body = layar_api.SourceDocumentSearchCommand() 
x_vyasa_data_providers = 'x_vyasa_data_providers_example' 

try:
    api_response = api_instance.search(body, x_vyasa_data_providers)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SourceDocumentApi->search: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *BASE_PATH*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AllApi* | [**search**](docs/AllApi.md#search) | **GET** /all | 
*AnswerApi* | [**get**](docs/AnswerApi.md#get) | **GET** /answer/{id} | QA answer details
*AnswerApi* | [**search**](docs/AnswerApi.md#search) | **POST** /answer/search | QA answer search
*AnswerApi* | [**update**](docs/AnswerApi.md#update) | **PUT** /answer/{id} | QA answer update
*AutocompleteApi* | [**delete**](docs/AutocompleteApi.md#delete) | **DELETE** /autocomplete/searchHistory/{term} | delete a previous search request
*AutocompleteApi* | [**get**](docs/AutocompleteApi.md#get) | **GET** /autocomplete | search for names used in various cortex domain objects
*AutocompleteApi* | [**search**](docs/AutocompleteApi.md#search) | **GET** /autocomplete/searchHistory | find previous search requests
*ClusteredConceptsApi* | [**get**](docs/ClusteredConceptsApi.md#get) | **GET** /clusteredConcepts/{id} | clustered concept details
*ClusteredConceptsApi* | [**get_concepts**](docs/ClusteredConceptsApi.md#get_concepts) | **GET** /clusteredConcepts/{clusteredQueryId}/{clusterId}/concepts | concepts
*ClusteredConceptsApi* | [**get_graph**](docs/ClusteredConceptsApi.md#get_graph) | **GET** /clusteredConcepts/{clusteredQueryId}/graph | graph
*ClusteredConceptsApi* | [**get_relationships**](docs/ClusteredConceptsApi.md#get_relationships) | **GET** /clusteredConcepts/{clusteredQueryId}/relationships | relationships
*ClusteredQueryApi* | [**create**](docs/ClusteredQueryApi.md#create) | **POST** /clusteredQuery | create a new clustered query request
*ClusteredQueryApi* | [**get**](docs/ClusteredQueryApi.md#get) | **GET** /clusteredQuery/{id} | clustered query details
*ClusteredQueryApi* | [**get_by_query_string**](docs/ClusteredQueryApi.md#get_by_query_string) | **GET** /clusteredQuery/byQueryString | find clustered query by query string
*ClusteredQueryApi* | [**get_clusters**](docs/ClusteredQueryApi.md#get_clusters) | **GET** /clusteredQuery/{clusteredQueryId}/clusters | getClusters
*ClusteredQueryApi* | [**update**](docs/ClusteredQueryApi.md#update) | **PUT** /clusteredQuery/{id} | update
*ClusteredStatementsApi* | [**create**](docs/ClusteredStatementsApi.md#create) | **POST** /clusteredStatements | create a new clustered statement request
*ClusteredStatementsApi* | [**get**](docs/ClusteredStatementsApi.md#get) | **GET** /clusteredStatements/{id} | clustered statements details
*ClusteredStatementsApi* | [**get_statements**](docs/ClusteredStatementsApi.md#get_statements) | **GET** /clusteredStatements/{clusteredStatementsId}/statements | statements
*CompoundApi* | [**render**](docs/CompoundApi.md#render) | **GET** /compound/render | render
*ConceptApi* | [**assign_from_column**](docs/ConceptApi.md#assign_from_column) | **POST** /concept/assign | start an async process to create concepts from a column in an uploaded spreadsheet
*ConceptApi* | [**assign_from_term**](docs/ConceptApi.md#assign_from_term) | **POST** /concept/assignTerm | create a concept from an arbitrary text string
*ConceptApi* | [**create**](docs/ConceptApi.md#create) | **POST** /concept | save a new concept
*ConceptApi* | [**delete**](docs/ConceptApi.md#delete) | **DELETE** /concept/{id} | delete
*ConceptApi* | [**delete_many**](docs/ConceptApi.md#delete_many) | **DELETE** /concept/deleteMany | delete all the records with the given IDs
*ConceptApi* | [**demote**](docs/ConceptApi.md#demote) | **PUT** /concept/{id}/demote | demote concept
*ConceptApi* | [**get**](docs/ConceptApi.md#get) | **GET** /concept/{id} | concept details
*ConceptApi* | [**get_external_concepts**](docs/ConceptApi.md#get_external_concepts) | **GET** /concept/external/{idKey}/{idValue} | find concepts by external id
*ConceptApi* | [**get_related_concepts**](docs/ConceptApi.md#get_related_concepts) | **GET** /concept/{id}/related | find related concepts
*ConceptApi* | [**get_statement_counts_over_time**](docs/ConceptApi.md#get_statement_counts_over_time) | **GET** /concept/{id}/statementCountsOverTime | statement counts over time for concept id
*ConceptApi* | [**make_primary_synonym**](docs/ConceptApi.md#make_primary_synonym) | **PUT** /concept/{id}/makePrimarySynonym | Make Primary Synonym
*ConceptApi* | [**make_synonyms**](docs/ConceptApi.md#make_synonyms) | **PUT** /concept/makeSynonyms | set all the concept ids as synonyms of each other
*ConceptApi* | [**patch**](docs/ConceptApi.md#patch) | **PATCH** /concept/{id} | patch
*ConceptApi* | [**remove_synonym**](docs/ConceptApi.md#remove_synonym) | **DELETE** /concept/{id}/removeAsSynonym | Remove As Synonym
*ConceptApi* | [**search**](docs/ConceptApi.md#search) | **POST** /concept/search | search for concepts
*ConceptApi* | [**update**](docs/ConceptApi.md#update) | **PUT** /concept/{id} | update
*ConceptTypeApi* | [**create**](docs/ConceptTypeApi.md#create) | **POST** /conceptType | save
*ConceptTypeApi* | [**delete**](docs/ConceptTypeApi.md#delete) | **DELETE** /conceptType/{id} | delete
*ConceptTypeApi* | [**delete_many**](docs/ConceptTypeApi.md#delete_many) | **DELETE** /conceptType/deleteMany | delete all the records with the given IDs
*ConceptTypeApi* | [**get**](docs/ConceptTypeApi.md#get) | **GET** /conceptType/{id} | concept type details
*ConceptTypeApi* | [**get_counts**](docs/ConceptTypeApi.md#get_counts) | **GET** /concept/type/counts | get counts concepts broken down by concept type
*ConceptTypeApi* | [**get_relationship_templates**](docs/ConceptTypeApi.md#get_relationship_templates) | **GET** /concept/type/relationshipTemplates | Relationship Templates
*ConceptTypeApi* | [**search**](docs/ConceptTypeApi.md#search) | **GET** /conceptType | search for concept types
*ConceptTypeApi* | [**update**](docs/ConceptTypeApi.md#update) | **PUT** /conceptType/{id} | update
*ConnectorApi* | [**create**](docs/ConnectorApi.md#create) | **POST** /connector | save
*ConnectorApi* | [**delete**](docs/ConnectorApi.md#delete) | **DELETE** /connector/{id} | delete
*ConnectorApi* | [**delete_many**](docs/ConnectorApi.md#delete_many) | **DELETE** /connector/deleteMany | delete all the records with the given IDs
*ConnectorApi* | [**get**](docs/ConnectorApi.md#get) | **GET** /connector/{id} | connector details
*ConnectorApi* | [**patch**](docs/ConnectorApi.md#patch) | **PATCH** /connector/{id} | patch
*ConnectorApi* | [**search**](docs/ConnectorApi.md#search) | **GET** /connector | 
*ConnectorApi* | [**update**](docs/ConnectorApi.md#update) | **PUT** /connector/{id} | update
*EventApi* | [**get**](docs/EventApi.md#get) | **GET** /event/{id} | event details
*EventApi* | [**search**](docs/EventApi.md#search) | **GET** /event | search for events
*GroupApi* | [**group_terms**](docs/GroupApi.md#group_terms) | **POST** /group/terms | group similar terms (eg, &#x27;Vyasa Analytics&#x27; and &#x27;Vyasa Analytics, LLC&#x27;)
*LiveSourceApi* | [**create**](docs/LiveSourceApi.md#create) | **POST** /liveSource | save
*LiveSourceApi* | [**create_feeds_from_column**](docs/LiveSourceApi.md#create_feeds_from_column) | **POST** /liveSource/createFeedsFromColumn | create live source feeds from column of a spreadsheet containing URLs
*LiveSourceApi* | [**delete**](docs/LiveSourceApi.md#delete) | **DELETE** /liveSource/{id} | delete
*LiveSourceApi* | [**delete_many**](docs/LiveSourceApi.md#delete_many) | **DELETE** /liveSource/deleteMany | delete the set of ids
*LiveSourceApi* | [**get**](docs/LiveSourceApi.md#get) | **GET** /liveSource/{id} | live source details
*LiveSourceApi* | [**get_import_status**](docs/LiveSourceApi.md#get_import_status) | **GET** /liveSource/{id}/importStatus | percent completion information
*LiveSourceApi* | [**get_job_status**](docs/LiveSourceApi.md#get_job_status) | **GET** /liveSource/{id}/jobStatus | jobStatus
*LiveSourceApi* | [**get_source_documents**](docs/LiveSourceApi.md#get_source_documents) | **GET** /liveSource/{id}/sourceDocuments | sourceDocuments
*LiveSourceApi* | [**search**](docs/LiveSourceApi.md#search) | **GET** /liveSource | 
*LiveSourceApi* | [**unschedule_job**](docs/LiveSourceApi.md#unschedule_job) | **PUT** /liveSource/{id}/jobStatus/unschedule | unschedule
*LiveSourceApi* | [**update**](docs/LiveSourceApi.md#update) | **PUT** /liveSource/{id} | update
*LiveSourceApi* | [**update_job**](docs/LiveSourceApi.md#update_job) | **PUT** /liveSource/{id}/{jobAction} | jobAction
*ModelApi* | [**download**](docs/ModelApi.md#download) | **GET** /model/{id}/download | download
*ModelApi* | [**search_by_computation_id**](docs/ModelApi.md#search_by_computation_id) | **GET** /projectComputation/{computationId}/models | find deep learning models by project computation
*ModelApi* | [**search_by_module_id**](docs/ModelApi.md#search_by_module_id) | **GET** /module/{moduleId}/models | find deep learning models by module
*ModelApi* | [**search_by_project_id**](docs/ModelApi.md#search_by_project_id) | **GET** /project/{projectId}/models | find deep learning models by project
*ModuleApi* | [**create**](docs/ModuleApi.md#create) | **POST** /module | save
*ModuleApi* | [**get**](docs/ModuleApi.md#get) | **GET** /module/{id} | module details
*ModuleApi* | [**search**](docs/ModuleApi.md#search) | **GET** /module | search for modules
*NamedEntityApi* | [**get_types**](docs/NamedEntityApi.md#get_types) | **GET** /namedEntity/types | A list of the available Named Entity Types
*NamedEntityApi* | [**tag**](docs/NamedEntityApi.md#tag) | **POST** /namedEntity/tag | 
*ProjectApi* | [**add_input**](docs/ProjectApi.md#add_input) | **PUT** /project/{id}/addInput | addInput
*ProjectApi* | [**create**](docs/ProjectApi.md#create) | **POST** /project | save
*ProjectApi* | [**delete**](docs/ProjectApi.md#delete) | **DELETE** /project/{id} | delete
*ProjectApi* | [**delete_many**](docs/ProjectApi.md#delete_many) | **DELETE** /project/deleteMany | deleteMany
*ProjectApi* | [**download_results**](docs/ProjectApi.md#download_results) | **GET** /project/{id}/results/download | downloadResults
*ProjectApi* | [**get**](docs/ProjectApi.md#get) | **GET** /project/{id} | project details
*ProjectApi* | [**get_results**](docs/ProjectApi.md#get_results) | **GET** /project/{id}/results | results
*ProjectApi* | [**get_results_som**](docs/ProjectApi.md#get_results_som) | **GET** /project/{id}/results/som | results SOM
*ProjectApi* | [**remove_input**](docs/ProjectApi.md#remove_input) | **PUT** /project/{id}/removeInput | removeInput
*ProjectApi* | [**run**](docs/ProjectApi.md#run) | **POST** /project/{id}/run | run
*ProjectApi* | [**search**](docs/ProjectApi.md#search) | **GET** /project | 
*ProjectApi* | [**update**](docs/ProjectApi.md#update) | **PUT** /project/{id} | update
*ProjectComputationApi* | [**cancel**](docs/ProjectComputationApi.md#cancel) | **POST** /projectComputation/{computationId}/cancel | cancel and shut down project computation without expecting any results back
*ProjectComputationApi* | [**download_logs**](docs/ProjectComputationApi.md#download_logs) | **GET** /projectComputation/{computationId}/downloadLogs | download full logs for computation job
*ProjectComputationApi* | [**download_results**](docs/ProjectComputationApi.md#download_results) | **GET** /projectComputation/{computationId}/downloadZipResults | download zip of documents created during computation
*ProjectComputationApi* | [**get**](docs/ProjectComputationApi.md#get) | **GET** /projectComputation/{id} | project computation details
*ProjectComputationApi* | [**get_logs**](docs/ProjectComputationApi.md#get_logs) | **GET** /projectComputation/{computationId}/logs | retrieve logs for computation job
*ProjectComputationApi* | [**stop**](docs/ProjectComputationApi.md#stop) | **POST** /projectComputation/{computationId}/stopTraining | send computation job a stop message encouraging it to stop and send any results back
*QuestionApi* | [**ask**](docs/QuestionApi.md#ask) | **POST** /question/ask | 
*QuestionApi* | [**cancel_batch**](docs/QuestionApi.md#cancel_batch) | **PUT** /question/cancelBulkQuestionAnswerJob/{jobID} | cancel an existing request to ask a batch of questions
*QuestionApi* | [**create**](docs/QuestionApi.md#create) | **POST** /question | save a new question
*QuestionApi* | [**delete**](docs/QuestionApi.md#delete) | **DELETE** /question/{id} | delete
*QuestionApi* | [**delete_many**](docs/QuestionApi.md#delete_many) | **DELETE** /question/deleteMany | delete all the records with the given IDs
*QuestionApi* | [**find_more_answers**](docs/QuestionApi.md#find_more_answers) | **POST** /question/{id}/answers/more | look for more answers to this question
*QuestionApi* | [**get**](docs/QuestionApi.md#get) | **GET** /question/{id} | question details
*QuestionApi* | [**patch**](docs/QuestionApi.md#patch) | **PATCH** /question/{id} | patch
*QuestionApi* | [**query_expansion**](docs/QuestionApi.md#query_expansion) | **POST** /question/queryExpansion | 
*QuestionApi* | [**refresh_answers**](docs/QuestionApi.md#refresh_answers) | **POST** /question/{id}/answers/refresh | look for answers in new documents
*QuestionApi* | [**search**](docs/QuestionApi.md#search) | **POST** /question/search | search for questions
*QuestionApi* | [**start_batch**](docs/QuestionApi.md#start_batch) | **POST** /question/startBulkQuestionAnswerJob | submit a request to ask a batch of questions
*QuestionApi* | [**update**](docs/QuestionApi.md#update) | **PUT** /question/{id} | update
*RadarApi* | [**get**](docs/RadarApi.md#get) | **GET** /radar | 
*RadarApi* | [**get_by_concept_id**](docs/RadarApi.md#get_by_concept_id) | **GET** /radar/byConceptId | find semantically similar terms
*RadarApi* | [**get_by_query_string**](docs/RadarApi.md#get_by_query_string) | **GET** /radar/byQueryString | find semantically similar terms
*RadarApi* | [**get_count**](docs/RadarApi.md#get_count) | **GET** /radar/count | count of nearest neighbor terms that match the term in the query string
*SavedListApi* | [**add_items**](docs/SavedListApi.md#add_items) | **PUT** /savedList/{id}/addItem | addItem
*SavedListApi* | [**add_items_by_search**](docs/SavedListApi.md#add_items_by_search) | **PUT** /savedList/{id}/add | addItem
*SavedListApi* | [**create**](docs/SavedListApi.md#create) | **POST** /savedList | save
*SavedListApi* | [**delete**](docs/SavedListApi.md#delete) | **DELETE** /savedList/{id} | delete
*SavedListApi* | [**delete_many**](docs/SavedListApi.md#delete_many) | **DELETE** /savedList/deleteMany | delete all the given ids
*SavedListApi* | [**download_csv**](docs/SavedListApi.md#download_csv) | **GET** /savedList/{id}/downloadCsv | downloadCsv
*SavedListApi* | [**get**](docs/SavedListApi.md#get) | **GET** /savedList/{id} | saved list details
*SavedListApi* | [**remove_items**](docs/SavedListApi.md#remove_items) | **DELETE** /savedList/{id}/removeItem | removeItem
*SavedListApi* | [**search**](docs/SavedListApi.md#search) | **GET** /savedList | 
*SavedListApi* | [**update**](docs/SavedListApi.md#update) | **PUT** /savedList/{id} | update
*SetAnalyticsApi* | [**download**](docs/SetAnalyticsApi.md#download) | **GET** /set/analytics/download | download
*SetAnalyticsApi* | [**get_concepts**](docs/SetAnalyticsApi.md#get_concepts) | **POST** /set/analytics/concepts | concepts
*SetAnalyticsApi* | [**get_concepts_tree**](docs/SetAnalyticsApi.md#get_concepts_tree) | **POST** /set/analytics/concepts/tree | conceptTree
*SetAnalyticsApi* | [**get_relationships**](docs/SetAnalyticsApi.md#get_relationships) | **POST** /set/analytics/concepts/relationships | relationships
*SetAnalyticsApi* | [**get_summary**](docs/SetAnalyticsApi.md#get_summary) | **POST** /set/analytics/summary | summary
*SmilesApi* | [**create_tox21_csv**](docs/SmilesApi.md#create_tox21_csv) | **POST** /smiles/createTox21CSV | Runs Tox21 toxicity analysis against list of smiles and returns the results in a CSV file.
*SmilesApi* | [**create_tox21_som**](docs/SmilesApi.md#create_tox21_som) | **POST** /smiles/createTox21SOM | Runs Tox21 toxicity analysis against list of smiles and returns the results in a Self Organizing Map (SOM)
*SourceDocumentApi* | [**add_annotation**](docs/SourceDocumentApi.md#add_annotation) | **POST** /sourceDocument/{id}/addAnnotation | bySource
*SourceDocumentApi* | [**add_annotations**](docs/SourceDocumentApi.md#add_annotations) | **POST** /sourceDocument/{id}/addAnnotations | bySource
*SourceDocumentApi* | [**add_column**](docs/SourceDocumentApi.md#add_column) | **PUT** /sourceDocument/{id}/addColumn | addColumn
*SourceDocumentApi* | [**add_viewer**](docs/SourceDocumentApi.md#add_viewer) | **POST** /sourceDocument/{id}/viewers | add a viewer to the source document
*SourceDocumentApi* | [**create**](docs/SourceDocumentApi.md#create) | **POST** /sourceDocument | save
*SourceDocumentApi* | [**delete**](docs/SourceDocumentApi.md#delete) | **DELETE** /sourceDocument/{id} | delete
*SourceDocumentApi* | [**delete_many**](docs/SourceDocumentApi.md#delete_many) | **DELETE** /sourceDocument/deleteMany | deleteMany
*SourceDocumentApi* | [**download**](docs/SourceDocumentApi.md#download) | **GET** /sourceDocument/{id}/download | download
*SourceDocumentApi* | [**download_annotations**](docs/SourceDocumentApi.md#download_annotations) | **GET** /sourceDocument/downloadAnnotations | downloads annotations as csv of one or more source document
*SourceDocumentApi* | [**extract_table_by_page**](docs/SourceDocumentApi.md#extract_table_by_page) | **POST** /sourceDocument/{id}/page/{page}/extractTable | extract a table from a specific page
*SourceDocumentApi* | [**extract_tables**](docs/SourceDocumentApi.md#extract_tables) | **POST** /sourceDocument/{id}/extractTables | extract tables from a document
*SourceDocumentApi* | [**get**](docs/SourceDocumentApi.md#get) | **GET** /sourceDocument/{id} | source document details
*SourceDocumentApi* | [**get_concepts**](docs/SourceDocumentApi.md#get_concepts) | **GET** /sourceDocument/{id}/concepts | count concepts by source document
*SourceDocumentApi* | [**get_counts_by_suggested_category**](docs/SourceDocumentApi.md#get_counts_by_suggested_category) | **GET** /sourceDocument/{projectComputationId}/countBySuggestedCategory | countBySuggestedCategory
*SourceDocumentApi* | [**get_counts_by_type**](docs/SourceDocumentApi.md#get_counts_by_type) | **GET** /sourceDocument/countByType | countByType
*SourceDocumentApi* | [**get_counts_over_time**](docs/SourceDocumentApi.md#get_counts_over_time) | **GET** /sourceDocument/docCountsOverTime | doc counts over time for term
*SourceDocumentApi* | [**get_field_counts**](docs/SourceDocumentApi.md#get_field_counts) | **POST** /sourceDocument/{field}/counts | 
*SourceDocumentApi* | [**get_page_preview**](docs/SourceDocumentApi.md#get_page_preview) | **GET** /sourceDocument/{id}/page/{page}/preview | preview of a specific page
*SourceDocumentApi* | [**get_preview**](docs/SourceDocumentApi.md#get_preview) | **GET** /sourceDocument/{id}/preview | preview
*SourceDocumentApi* | [**get_statement_counts**](docs/SourceDocumentApi.md#get_statement_counts) | **GET** /sourceDocument/{id}/statementCount | get statement counts
*SourceDocumentApi* | [**get_statements**](docs/SourceDocumentApi.md#get_statements) | **GET** /sourceDocument/{id}/statements | bySource
*SourceDocumentApi* | [**get_status**](docs/SourceDocumentApi.md#get_status) | **GET** /sourceDocument/{id}/status | status
*SourceDocumentApi* | [**get_viewers**](docs/SourceDocumentApi.md#get_viewers) | **GET** /sourceDocument/{id}/viewers | get a list of all viewers of the source document
*SourceDocumentApi* | [**render_pdf**](docs/SourceDocumentApi.md#render_pdf) | **GET** /sourceDocument/{id}/renderPdf | renderPdf
*SourceDocumentApi* | [**search**](docs/SourceDocumentApi.md#search) | **POST** /sourceDocument/search | 
*SourceDocumentApi* | [**update**](docs/SourceDocumentApi.md#update) | **PUT** /sourceDocument/{id} | update
*StatementApi* | [**create**](docs/StatementApi.md#create) | **POST** /statement | save
*StatementApi* | [**delete**](docs/StatementApi.md#delete) | **DELETE** /statement/{id} | delete
*StatementApi* | [**delete_many**](docs/StatementApi.md#delete_many) | **DELETE** /statement/deleteMany | deleteMany
*StatementApi* | [**get**](docs/StatementApi.md#get) | **GET** /statement/{id} | statement details
*StatementApi* | [**get_field_counts**](docs/StatementApi.md#get_field_counts) | **POST** /statement/{field}/counts | 
*StatementApi* | [**get_relationship_evidence**](docs/StatementApi.md#get_relationship_evidence) | **GET** /statement/relationshipEvidence/{conceptId1}/{relationship}/{conceptId2} | relationshipEvidence
*StatementApi* | [**search**](docs/StatementApi.md#search) | **POST** /statement/search | search for statements
*StatementApi* | [**update**](docs/StatementApi.md#update) | **PUT** /statement/{id} | update
*StatusApi* | [**get**](docs/StatusApi.md#get) | **GET** /app | 
*VectorSimilarityApi* | [**create**](docs/VectorSimilarityApi.md#create) | **POST** /vectorSimilarity | save
*VectorSimilarityApi* | [**get**](docs/VectorSimilarityApi.md#get) | **GET** /vectorSimilarity/{id} | vector similarity details
*VectorSimilarityApi* | [**get_by_query_string**](docs/VectorSimilarityApi.md#get_by_query_string) | **GET** /vectorSimilarity/byQueryString | byQueryString
*VectorSimilarityApi* | [**get_similar_statements**](docs/VectorSimilarityApi.md#get_similar_statements) | **GET** /vectorSimilarity/{similarityRequestId}/statements | similarStatements
