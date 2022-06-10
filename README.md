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
*AllApi* | [**search_all**](docs/AllApi.md#search_all) | **GET** /all | 
*AnswerApi* | [**get_answer**](docs/AnswerApi.md#get_answer) | **GET** /answer/{id} | Get details for a QA Answer in your Layar instance
*AnswerApi* | [**search_answer**](docs/AnswerApi.md#search_answer) | **POST** /answer/search | Search for previously found QA answers
*AnswerApi* | [**update_answer**](docs/AnswerApi.md#update_answer) | **PUT** /answer/{id} | Update answer details
*AutocompleteApi* | [**autocomplete_get**](docs/AutocompleteApi.md#autocomplete_get) | **GET** /autocomplete | search for names used in various cortex domain objects
*AutocompleteApi* | [**delete_search_history**](docs/AutocompleteApi.md#delete_search_history) | **DELETE** /autocomplete/searchHistory/{term} | delete a previous search request
*AutocompleteApi* | [**get_search_history**](docs/AutocompleteApi.md#get_search_history) | **GET** /autocomplete/searchHistory | find previous search requests
*CompoundApi* | [**render**](docs/CompoundApi.md#render) | **GET** /compound/render | Render a SMILES compound string. Returns an SVG of the render.
*ConceptApi* | [**assign_from_term**](docs/ConceptApi.md#assign_from_term) | **POST** /concept/assignTerm | create a concept from an arbitrary text string
*ConceptApi* | [**create_concept**](docs/ConceptApi.md#create_concept) | **POST** /concept | Save a new concept
*ConceptApi* | [**delete_concept**](docs/ConceptApi.md#delete_concept) | **DELETE** /concept/{id} | Delete a concept from Layar
*ConceptApi* | [**delete_concepts**](docs/ConceptApi.md#delete_concepts) | **DELETE** /concept/deleteMany | delete all the records with the given IDs
*ConceptApi* | [**demote_concept**](docs/ConceptApi.md#demote_concept) | **PUT** /concept/{id}/demote | Remove relationship with a concept
*ConceptApi* | [**get_concept**](docs/ConceptApi.md#get_concept) | **GET** /concept/{id} | Get concept details
*ConceptApi* | [**get_external_concepts**](docs/ConceptApi.md#get_external_concepts) | **GET** /concept/external/{idKey}/{idValue} | find concepts by external id
*ConceptApi* | [**get_related_concepts**](docs/ConceptApi.md#get_related_concepts) | **GET** /concept/{id}/related | Returns a list of concepts related to the original concept.
*ConceptApi* | [**get_statement_counts_over_time**](docs/ConceptApi.md#get_statement_counts_over_time) | **GET** /concept/{id}/statementCountsOverTime | statement counts over time for concept id
*ConceptApi* | [**make_primary_synonym**](docs/ConceptApi.md#make_primary_synonym) | **PUT** /concept/{id}/makePrimarySynonym | Set a concept as the primary in its group of synonyms
*ConceptApi* | [**make_synonyms**](docs/ConceptApi.md#make_synonyms) | **PUT** /concept/makeSynonyms | Set all of the provided concept ids as synonyms of each other
*ConceptApi* | [**patch_concept**](docs/ConceptApi.md#patch_concept) | **PATCH** /concept/{id} | patch
*ConceptApi* | [**remove_synonym**](docs/ConceptApi.md#remove_synonym) | **DELETE** /concept/{id}/removeAsSynonym | Remove a concept from its group of synonyms
*ConceptApi* | [**search_concept**](docs/ConceptApi.md#search_concept) | **POST** /concept/search | search for concepts
*ConceptApi* | [**update_concept**](docs/ConceptApi.md#update_concept) | **PUT** /concept/{id} | Update concept details
*ConceptTypeApi* | [**create_concept_type**](docs/ConceptTypeApi.md#create_concept_type) | **POST** /conceptType | Save new concept types
*ConceptTypeApi* | [**delete_concept_type**](docs/ConceptTypeApi.md#delete_concept_type) | **DELETE** /conceptType/{id} | Delete a single concept type
*ConceptTypeApi* | [**delete_concept_types**](docs/ConceptTypeApi.md#delete_concept_types) | **DELETE** /conceptType/deleteMany | Delete all the records with the given IDs
*ConceptTypeApi* | [**get_concept_type**](docs/ConceptTypeApi.md#get_concept_type) | **GET** /conceptType/{id} | Concept type details
*ConceptTypeApi* | [**get_counts**](docs/ConceptTypeApi.md#get_counts) | **GET** /concept/type/counts | Get result counts by concept type
*ConceptTypeApi* | [**get_relationship_templates**](docs/ConceptTypeApi.md#get_relationship_templates) | **GET** /concept/type/relationshipTemplates | Relationship Templates
*ConceptTypeApi* | [**search_concept_types**](docs/ConceptTypeApi.md#search_concept_types) | **GET** /conceptType | Search for concept types
*ConceptTypeApi* | [**update_concept_type**](docs/ConceptTypeApi.md#update_concept_type) | **PUT** /conceptType/{id} | Update a single concept type
*ConnectorApi* | [**create_connector**](docs/ConnectorApi.md#create_connector) | **POST** /connector | Add a new Layar connector
*ConnectorApi* | [**delete_connector**](docs/ConnectorApi.md#delete_connector) | **DELETE** /connector/{id} | Delete a single Layar connector
*ConnectorApi* | [**delete_connectors**](docs/ConnectorApi.md#delete_connectors) | **DELETE** /connector/deleteMany | delete all the records with the given IDs
*ConnectorApi* | [**get_connector**](docs/ConnectorApi.md#get_connector) | **GET** /connector/{id} | Get the details for a single Layar connector
*ConnectorApi* | [**patch_connector**](docs/ConnectorApi.md#patch_connector) | **PATCH** /connector/{id} | patch
*ConnectorApi* | [**search_connectors**](docs/ConnectorApi.md#search_connectors) | **GET** /connector | Get the details for a given Layar connector
*ConnectorApi* | [**update_connector**](docs/ConnectorApi.md#update_connector) | **PUT** /connector/{id} | Update the details for a single Layar connector
*DefaultApi* | [**search_paragraph**](docs/DefaultApi.md#search_paragraph) | **POST** /paragraph/search | 
*DefaultApi* | [**search_term**](docs/DefaultApi.md#search_term) | **POST** /ontologyTerm/search | 
*EventApi* | [**get_event**](docs/EventApi.md#get_event) | **GET** /event/{id} | event details
*EventApi* | [**search_events**](docs/EventApi.md#search_events) | **GET** /event | search for events
*GroupApi* | [**group_terms**](docs/GroupApi.md#group_terms) | **POST** /group/terms | group similar terms (eg, &#x27;Vyasa Analytics&#x27; and &#x27;Vyasa Analytics, LLC&#x27;)
*LiveSourceApi* | [**create_feeds**](docs/LiveSourceApi.md#create_feeds) | **POST** /liveSource | Create a new live source
*LiveSourceApi* | [**create_feeds_from_column**](docs/LiveSourceApi.md#create_feeds_from_column) | **POST** /liveSource/createFeedsFromColumn | create live source feeds from column of a spreadsheet containing URLs
*LiveSourceApi* | [**delete_feed**](docs/LiveSourceApi.md#delete_feed) | **DELETE** /liveSource/{id} | Delete a live source
*LiveSourceApi* | [**delete_feeds**](docs/LiveSourceApi.md#delete_feeds) | **DELETE** /liveSource/deleteMany | delete the set of live source ids
*LiveSourceApi* | [**get_feed**](docs/LiveSourceApi.md#get_feed) | **GET** /liveSource/{id} | Get live source details
*LiveSourceApi* | [**get_import_status**](docs/LiveSourceApi.md#get_import_status) | **GET** /liveSource/{id}/importStatus | Returns the percent completed for a live source import
*LiveSourceApi* | [**get_job_status**](docs/LiveSourceApi.md#get_job_status) | **GET** /liveSource/{id}/jobStatus | Get job status details
*LiveSourceApi* | [**get_source_document_url**](docs/LiveSourceApi.md#get_source_document_url) | **GET** /liveSource/{id}/sourceDocuments | Get the documents from a particular source
*LiveSourceApi* | [**search_feeds**](docs/LiveSourceApi.md#search_feeds) | **GET** /liveSource | Search for live sources
*LiveSourceApi* | [**unschedule_job**](docs/LiveSourceApi.md#unschedule_job) | **PUT** /liveSource/{id}/jobStatus/unschedule | Change a job status to &#x27;Unscheduled&#x27;
*LiveSourceApi* | [**update_feed**](docs/LiveSourceApi.md#update_feed) | **PUT** /liveSource/{id} | Update a live source
*LiveSourceApi* | [**update_job**](docs/LiveSourceApi.md#update_job) | **PUT** /liveSource/{id}/{jobAction} | Update a job with a new action
*ModelApi* | [**download_model**](docs/ModelApi.md#download_model) | **GET** /model/{id}/download | Download a learning model by ID
*ModelApi* | [**search_models_by_computation_id**](docs/ModelApi.md#search_models_by_computation_id) | **GET** /projectComputation/{id}/models | find deep learning models by project computation
*ModelApi* | [**search_models_by_module_id**](docs/ModelApi.md#search_models_by_module_id) | **GET** /module/{moduleId}/models | Find deep learning models by module
*ModelApi* | [**search_models_by_project_id**](docs/ModelApi.md#search_models_by_project_id) | **GET** /project/{projectId}/models | find deep learning models by project
*ModuleApi* | [**create_module**](docs/ModuleApi.md#create_module) | **POST** /module | Save a new module
*ModuleApi* | [**get_module**](docs/ModuleApi.md#get_module) | **GET** /module/{id} | Get module details
*ModuleApi* | [**search_modules**](docs/ModuleApi.md#search_modules) | **GET** /module | search for modules
*NamedEntityApi* | [**get_types**](docs/NamedEntityApi.md#get_types) | **GET** /namedEntity/types | A list of the available Named Entity Types
*NamedEntityApi* | [**named_entity_tag**](docs/NamedEntityApi.md#named_entity_tag) | **POST** /statement/{id}/namedEntity/tag | tag named entities within specific columns of a statement
*NamedEntityApi* | [**tag_ner**](docs/NamedEntityApi.md#tag_ner) | **POST** /namedEntity/tag | Find named entity tags by query term or list of types
*OntologyTermApi* | [**create_term**](docs/OntologyTermApi.md#create_term) | **POST** /ontologyTerm | Save a new ontology term
*OntologyTermApi* | [**delete_term**](docs/OntologyTermApi.md#delete_term) | **DELETE** /ontologyTerm/{id} | Delete a term from the ontology
*OntologyTermApi* | [**get_term**](docs/OntologyTermApi.md#get_term) | **GET** /ontologyTerm/{id} | get the ontology term details
*OntologyTermApi* | [**ontology_term_get**](docs/OntologyTermApi.md#ontology_term_get) | **GET** /ontologyTerm | search for ontology terms
*OntologyTermApi* | [**update_term**](docs/OntologyTermApi.md#update_term) | **PUT** /ontologyTerm/{id} | Update a term in an ontology
*ParagraphApi* | [**get_paragraph**](docs/ParagraphApi.md#get_paragraph) | **GET** /paragraph/{id} | Get details for a single paragraph
*ParagraphApi* | [**paragraph_get**](docs/ParagraphApi.md#paragraph_get) | **GET** /paragraph | search for paragraphs
*ParagraphApi* | [**parse_text**](docs/ParagraphApi.md#parse_text) | **POST** /partOfSpeech/parseText | Parse text into part of speech components and queryable terms
*ProjectApi* | [**add_input**](docs/ProjectApi.md#add_input) | **PUT** /project/{id}/addInput | Add source inputs to a project
*ProjectApi* | [**create_project**](docs/ProjectApi.md#create_project) | **POST** /project | Save a new project
*ProjectApi* | [**delete_project**](docs/ProjectApi.md#delete_project) | **DELETE** /project/{id} | Delete a project
*ProjectApi* | [**delete_projects**](docs/ProjectApi.md#delete_projects) | **DELETE** /project/deleteMany | Delete multiple projects by ID
*ProjectApi* | [**download_results**](docs/ProjectApi.md#download_results) | **GET** /project/{id}/results/download | Download a zip file of a given project&#x27;s results
*ProjectApi* | [**get_project**](docs/ProjectApi.md#get_project) | **GET** /project/{id} | project details
*ProjectApi* | [**get_results**](docs/ProjectApi.md#get_results) | **GET** /project/{id}/results | Get project results details
*ProjectApi* | [**get_results_som**](docs/ProjectApi.md#get_results_som) | **GET** /project/{id}/results/som | results SOM
*ProjectApi* | [**remove_input**](docs/ProjectApi.md#remove_input) | **PUT** /project/{id}/removeInput | Remove source inputs from a project
*ProjectApi* | [**run_project**](docs/ProjectApi.md#run_project) | **POST** /project/{id}/run | Create and run a new project
*ProjectApi* | [**search_projects**](docs/ProjectApi.md#search_projects) | **GET** /project | Get project details
*ProjectApi* | [**update_project**](docs/ProjectApi.md#update_project) | **PUT** /project/{id} | Pdate project
*ProjectComputationApi* | [**cancel_computation**](docs/ProjectComputationApi.md#cancel_computation) | **POST** /projectComputation/{id}/cancel | cancel and shut down project computation without expecting any results back
*ProjectComputationApi* | [**download_computation**](docs/ProjectComputationApi.md#download_computation) | **GET** /projectComputation/{id}/downloadZipResults | download zip of documents created during computation
*ProjectComputationApi* | [**download_logs**](docs/ProjectComputationApi.md#download_logs) | **GET** /projectComputation/{id}/downloadLogs | download full logs for computation job
*ProjectComputationApi* | [**get_logs**](docs/ProjectComputationApi.md#get_logs) | **GET** /projectComputation/{id}/logs | retrieve logs for computation job
*ProjectComputationApi* | [**get_project_computation**](docs/ProjectComputationApi.md#get_project_computation) | **GET** /projectComputation/{id} | project computation details
*ProjectComputationApi* | [**stop_job**](docs/ProjectComputationApi.md#stop_job) | **POST** /projectComputation/{id}/stopTraining | send computation job a stop message encouraging it to stop and send any results back
*QuestionApi* | [**ask**](docs/QuestionApi.md#ask) | **POST** /question/ask | Create and ask a new question in the QA model
*QuestionApi* | [**cancel_batch**](docs/QuestionApi.md#cancel_batch) | **PUT** /question/cancelBulkQuestionAnswerJob/{jobID} | cancel an existing request to ask a batch of questions
*QuestionApi* | [**create_question**](docs/QuestionApi.md#create_question) | **POST** /question | save a new question
*QuestionApi* | [**delete_question**](docs/QuestionApi.md#delete_question) | **DELETE** /question/{id} | Delete a saved question
*QuestionApi* | [**delete_questions**](docs/QuestionApi.md#delete_questions) | **DELETE** /question/deleteMany | delete all the records with the given IDs
*QuestionApi* | [**find_more_answers**](docs/QuestionApi.md#find_more_answers) | **POST** /question/{id}/answers/more | look for more answers to this question
*QuestionApi* | [**get_question**](docs/QuestionApi.md#get_question) | **GET** /question/{id} | Get question details
*QuestionApi* | [**get_question_field_counts**](docs/QuestionApi.md#get_question_field_counts) | **POST** /question/{field}/counts | Get curation counts or progress by field for a QA job
*QuestionApi* | [**patch_question**](docs/QuestionApi.md#patch_question) | **PATCH** /question/{id} | patch
*QuestionApi* | [**query_expansion**](docs/QuestionApi.md#query_expansion) | **POST** /question/queryExpansion | Expand the scope of a particular question
*QuestionApi* | [**refresh_answers**](docs/QuestionApi.md#refresh_answers) | **POST** /question/{id}/answers/refresh | look for answers in new documents
*QuestionApi* | [**search_questions**](docs/QuestionApi.md#search_questions) | **POST** /question/search | search for questions
*QuestionApi* | [**start_batch**](docs/QuestionApi.md#start_batch) | **POST** /question/startBulkQuestionAnswerJob | submit a request to ask a batch of questions
*QuestionApi* | [**update_question**](docs/QuestionApi.md#update_question) | **PUT** /question/{id} | Update a saved question
*RadarApi* | [**get_nearest_neighbor_count**](docs/RadarApi.md#get_nearest_neighbor_count) | **GET** /radar/count | count of nearest neighbor terms that match the term in the query string
*RadarApi* | [**get_radar**](docs/RadarApi.md#get_radar) | **GET** /radar | Get Radar results
*RadarApi* | [**get_radar_by_concept_id**](docs/RadarApi.md#get_radar_by_concept_id) | **GET** /radar/byConceptId | find semantically similar terms
*RadarApi* | [**get_radar_by_query_string**](docs/RadarApi.md#get_radar_by_query_string) | **GET** /radar/byQueryString | find semantically similar terms
*SavedListApi* | [**add_items**](docs/SavedListApi.md#add_items) | **PUT** /savedList/{id}/addItem | Add items to a saved list
*SavedListApi* | [**add_items_by_search**](docs/SavedListApi.md#add_items_by_search) | **PUT** /savedList/{id}/add | Add items to a saved list from a search
*SavedListApi* | [**create_saved_list**](docs/SavedListApi.md#create_saved_list) | **POST** /savedList | Create a new saved list
*SavedListApi* | [**delete_saved_list**](docs/SavedListApi.md#delete_saved_list) | **DELETE** /savedList/{id} | Delete a saved list
*SavedListApi* | [**delete_saved_lists**](docs/SavedListApi.md#delete_saved_lists) | **DELETE** /savedList/deleteMany | delete all the given ids
*SavedListApi* | [**download_saved_list**](docs/SavedListApi.md#download_saved_list) | **GET** /savedList/{id}/downloadCsv | Download the contents of a savedc list as a csv file
*SavedListApi* | [**get_saved_list**](docs/SavedListApi.md#get_saved_list) | **GET** /savedList/{id} | saved list details
*SavedListApi* | [**remove_items**](docs/SavedListApi.md#remove_items) | **DELETE** /savedList/{id}/removeItem | Remove items from a saved list
*SavedListApi* | [**search_saved_list**](docs/SavedListApi.md#search_saved_list) | **GET** /savedList | Search for saved lists
*SavedListApi* | [**update_saved_list**](docs/SavedListApi.md#update_saved_list) | **PUT** /savedList/{id} | Update a saved list
*SmilesApi* | [**create_tox_csv**](docs/SmilesApi.md#create_tox_csv) | **POST** /smiles/createTox21CSV | Runs Tox21 toxicity analysis against list of smiles and returns the results in a CSV file.
*SmilesApi* | [**create_tox_som**](docs/SmilesApi.md#create_tox_som) | **POST** /smiles/createTox21SOM | Runs Tox21 toxicity analysis against list of smiles and returns the results in a Self Organizing Map (SOM)
*SourceDocumentApi* | [**add_annotation**](docs/SourceDocumentApi.md#add_annotation) | **POST** /sourceDocument/{id}/addAnnotation | Add annotation by source
*SourceDocumentApi* | [**add_annotations**](docs/SourceDocumentApi.md#add_annotations) | **POST** /sourceDocument/{id}/addAnnotations | Add a list of annotations to a document
*SourceDocumentApi* | [**add_column**](docs/SourceDocumentApi.md#add_column) | **PUT** /sourceDocument/{id}/addColumn | Add column to table
*SourceDocumentApi* | [**add_viewer**](docs/SourceDocumentApi.md#add_viewer) | **POST** /sourceDocument/{id}/viewers | add a viewer to the source document
*SourceDocumentApi* | [**create_document**](docs/SourceDocumentApi.md#create_document) | **POST** /sourceDocument | Save a source document to Layar
*SourceDocumentApi* | [**delete_document**](docs/SourceDocumentApi.md#delete_document) | **DELETE** /sourceDocument/{id} | Delete a document from Layar
*SourceDocumentApi* | [**delete_documents**](docs/SourceDocumentApi.md#delete_documents) | **DELETE** /sourceDocument/deleteMany | Delete all documents in an array
*SourceDocumentApi* | [**download_annotations**](docs/SourceDocumentApi.md#download_annotations) | **GET** /sourceDocument/downloadAnnotations | downloads annotations as csv of one or more source document
*SourceDocumentApi* | [**download_document**](docs/SourceDocumentApi.md#download_document) | **GET** /sourceDocument/{id}/download | Download a document by ID
*SourceDocumentApi* | [**extract_table_by_page**](docs/SourceDocumentApi.md#extract_table_by_page) | **POST** /sourceDocument/{id}/page/{page}/extractTable | extract a table from a specific page
*SourceDocumentApi* | [**extract_tables**](docs/SourceDocumentApi.md#extract_tables) | **POST** /sourceDocument/{id}/extractTables | extract tables from a document
*SourceDocumentApi* | [**get_counts_by_suggested_category**](docs/SourceDocumentApi.md#get_counts_by_suggested_category) | **GET** /sourceDocument/{projectComputationId}/countBySuggestedCategory | Get document counts by suggested category
*SourceDocumentApi* | [**get_counts_by_type**](docs/SourceDocumentApi.md#get_counts_by_type) | **GET** /sourceDocument/countByType | Get document counts by type
*SourceDocumentApi* | [**get_counts_over_time**](docs/SourceDocumentApi.md#get_counts_over_time) | **GET** /sourceDocument/docCountsOverTime | doc counts over time for term
*SourceDocumentApi* | [**get_doc_field_counts**](docs/SourceDocumentApi.md#get_doc_field_counts) | **POST** /sourceDocument/{field}/counts | Get counts by field type for documents
*SourceDocumentApi* | [**get_document**](docs/SourceDocumentApi.md#get_document) | **GET** /sourceDocument/{id} | source document details
*SourceDocumentApi* | [**get_document_concepts**](docs/SourceDocumentApi.md#get_document_concepts) | **GET** /sourceDocument/{id}/concepts | count concepts by source document
*SourceDocumentApi* | [**get_document_statements**](docs/SourceDocumentApi.md#get_document_statements) | **GET** /sourceDocument/{id}/statements | Get all the statements in a given document
*SourceDocumentApi* | [**get_document_status**](docs/SourceDocumentApi.md#get_document_status) | **GET** /sourceDocument/{id}/status | Get the import status for a document
*SourceDocumentApi* | [**get_page_preview**](docs/SourceDocumentApi.md#get_page_preview) | **GET** /sourceDocument/{id}/page/{page}/preview | Preview of a specific page in a document
*SourceDocumentApi* | [**get_preview**](docs/SourceDocumentApi.md#get_preview) | **GET** /sourceDocument/{id}/preview | Get a document preview
*SourceDocumentApi* | [**get_statement_counts**](docs/SourceDocumentApi.md#get_statement_counts) | **GET** /sourceDocument/{id}/statementCount | get statement counts for a document
*SourceDocumentApi* | [**get_viewers**](docs/SourceDocumentApi.md#get_viewers) | **GET** /sourceDocument/{id}/viewers | get a list of all viewers of the source document
*SourceDocumentApi* | [**remove_annotation**](docs/SourceDocumentApi.md#remove_annotation) | **DELETE** /sourceDocument/{id}/annotations/{annotationId} | Delete annotations by ID
*SourceDocumentApi* | [**render_pdf**](docs/SourceDocumentApi.md#render_pdf) | **GET** /sourceDocument/{id}/renderPdf | Render a PDF of a document
*SourceDocumentApi* | [**search_documents**](docs/SourceDocumentApi.md#search_documents) | **POST** /sourceDocument/search | Search for documents in Layar
*SourceDocumentApi* | [**update_annotation**](docs/SourceDocumentApi.md#update_annotation) | **PUT** /sourceDocument/{id}/annotations | Update document annotations
*SourceDocumentApi* | [**update_document**](docs/SourceDocumentApi.md#update_document) | **PUT** /sourceDocument/{id} | Update document details
*StatementApi* | [**create_statement**](docs/StatementApi.md#create_statement) | **POST** /statement | Create a new statement
*StatementApi* | [**delete_statement**](docs/StatementApi.md#delete_statement) | **DELETE** /statement/{id} | Delete a statement by ID
*StatementApi* | [**delete_statements**](docs/StatementApi.md#delete_statements) | **DELETE** /statement/deleteMany | Delete all the statements in an array
*StatementApi* | [**get_relationship_evidence**](docs/StatementApi.md#get_relationship_evidence) | **GET** /statement/relationshipEvidence/{conceptId1}/{relationship}/{conceptId2} | Get the relationship evidence between two given concepts
*StatementApi* | [**get_statement**](docs/StatementApi.md#get_statement) | **GET** /statement/{id} | Get statement details by ID
*StatementApi* | [**get_statement_field_counts**](docs/StatementApi.md#get_statement_field_counts) | **POST** /statement/{field}/counts | Get statement counts by table column
*StatementApi* | [**named_entity_tag**](docs/StatementApi.md#named_entity_tag) | **POST** /statement/{id}/namedEntity/tag | tag named entities within specific columns of a statement
*StatementApi* | [**search_statements**](docs/StatementApi.md#search_statements) | **POST** /statement/search | search for statements
*StatementApi* | [**update_statement**](docs/StatementApi.md#update_statement) | **PUT** /statement/{id} | Update a statement by ID
*StatusApi* | [**get_app_status**](docs/StatusApi.md#get_app_status) | **GET** /app | 
*VectorSimilarityApi* | [**create_vector_similarity**](docs/VectorSimilarityApi.md#create_vector_similarity) | **POST** /vectorSimilarity | save
*VectorSimilarityApi* | [**get_similar_statements**](docs/VectorSimilarityApi.md#get_similar_statements) | **GET** /vectorSimilarity/{similarityRequestId}/statements | similarStatements
*VectorSimilarityApi* | [**get_vector_similarity**](docs/VectorSimilarityApi.md#get_vector_similarity) | **GET** /vectorSimilarity/{id} | vector similarity details
*VectorSimilarityApi* | [**get_vectors_by_query_string**](docs/VectorSimilarityApi.md#get_vectors_by_query_string) | **GET** /vectorSimilarity/byQueryString | byQueryString
