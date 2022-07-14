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
*AllApi* | [**search_all**](docs/AllApi.md#search_all) | **GET** /layar/all | Search across all domain objects
*AnswerApi* | [**get_answer**](docs/AnswerApi.md#get_answer) | **GET** /layar/answer/{id} | Get answer details
*AnswerApi* | [**layar_answer_get**](docs/AnswerApi.md#layar_answer_get) | **GET** /layar/answer | 
*AnswerApi* | [**search_answer**](docs/AnswerApi.md#search_answer) | **POST** /layar/answer/search | Search for answers
*AnswerApi* | [**update_answer**](docs/AnswerApi.md#update_answer) | **PUT** /layar/answer/{id} | Update answer details
*AutocompleteApi* | [**delete_search_history**](docs/AutocompleteApi.md#delete_search_history) | **DELETE** /layar/autocomplete/searchHistory/{term} | Delete a search request
*AutocompleteApi* | [**get_search_history**](docs/AutocompleteApi.md#get_search_history) | **GET** /layar/autocomplete/searchHistory | Get search history
*AutocompleteApi* | [**layar_autocomplete_get**](docs/AutocompleteApi.md#layar_autocomplete_get) | **GET** /layar/autocomplete | Get search history for all domain objects
*CompoundApi* | [**render**](docs/CompoundApi.md#render) | **GET** /layar/compound/render | Render SMILES into an SVG
*ConceptApi* | [**assign_from_term**](docs/ConceptApi.md#assign_from_term) | **POST** /layar/concept/assignTerm | Create a new term for a concept
*ConceptApi* | [**create_concept**](docs/ConceptApi.md#create_concept) | **POST** /layar/concept | Create a new concept
*ConceptApi* | [**delete_concept**](docs/ConceptApi.md#delete_concept) | **DELETE** /layar/concept/{id} | Delete a concept
*ConceptApi* | [**delete_concepts**](docs/ConceptApi.md#delete_concepts) | **DELETE** /layar/concept/deleteMany | Delete multiple concepts
*ConceptApi* | [**demote_concept**](docs/ConceptApi.md#demote_concept) | **PUT** /layar/concept/{id}/demote | Demote a relationship with another concept
*ConceptApi* | [**get_concept**](docs/ConceptApi.md#get_concept) | **GET** /layar/concept/{id} | Get concept details
*ConceptApi* | [**get_external_concepts**](docs/ConceptApi.md#get_external_concepts) | **GET** /layar/concept/external/{idKey}/{idValue} | Search for concepts by external ID
*ConceptApi* | [**get_related_concepts**](docs/ConceptApi.md#get_related_concepts) | **GET** /layar/concept/{id}/related | Find related concepts
*ConceptApi* | [**get_statement_counts_over_time**](docs/ConceptApi.md#get_statement_counts_over_time) | **GET** /layar/concept/{id}/statementCountsOverTime | Get statement counts over time
*ConceptApi* | [**make_primary_synonym**](docs/ConceptApi.md#make_primary_synonym) | **PUT** /layar/concept/{id}/makePrimarySynonym | Set as primary synonym
*ConceptApi* | [**make_synonyms**](docs/ConceptApi.md#make_synonyms) | **PUT** /layar/concept/makeSynonyms | Set as synonyms
*ConceptApi* | [**patch_concept**](docs/ConceptApi.md#patch_concept) | **PATCH** /layar/concept/{id} | Update specific details for a concept
*ConceptApi* | [**remove_synonym**](docs/ConceptApi.md#remove_synonym) | **DELETE** /layar/concept/{id}/removeAsSynonym | Remove as synonym
*ConceptApi* | [**search_concept**](docs/ConceptApi.md#search_concept) | **POST** /layar/concept/search | Search for concepts
*ConceptApi* | [**update_concept**](docs/ConceptApi.md#update_concept) | **PUT** /layar/concept/{id} | Update all details for a concept
*ConceptTypeApi* | [**create_concept_type**](docs/ConceptTypeApi.md#create_concept_type) | **POST** /layar/conceptType | Create a new concept type
*ConceptTypeApi* | [**delete_concept_type**](docs/ConceptTypeApi.md#delete_concept_type) | **DELETE** /layar/conceptType/{id} | Delete a concept type
*ConceptTypeApi* | [**delete_concept_types**](docs/ConceptTypeApi.md#delete_concept_types) | **DELETE** /layar/conceptType/deleteMany | Delete multiple concept types
*ConceptTypeApi* | [**get_concept_type**](docs/ConceptTypeApi.md#get_concept_type) | **GET** /layar/conceptType/{id} | Get concept type details
*ConceptTypeApi* | [**get_counts**](docs/ConceptTypeApi.md#get_counts) | **GET** /layar/concept/type/counts | Get concept type counts
*ConceptTypeApi* | [**get_relationship_templates**](docs/ConceptTypeApi.md#get_relationship_templates) | **GET** /layar/concept/type/relationshipTemplates | Get concept relationship details
*ConceptTypeApi* | [**search_concept_types**](docs/ConceptTypeApi.md#search_concept_types) | **GET** /layar/conceptType | Search for concept types
*ConceptTypeApi* | [**update_concept_type**](docs/ConceptTypeApi.md#update_concept_type) | **PUT** /layar/conceptType/{id} | Update concept type details
*ConnectorApi* | [**create_connector**](docs/ConnectorApi.md#create_connector) | **POST** /layar/connector | Create a new Twitter connector
*ConnectorApi* | [**delete_connector**](docs/ConnectorApi.md#delete_connector) | **DELETE** /layar/connector/{id} | Delete a Twitter connector
*ConnectorApi* | [**delete_connectors**](docs/ConnectorApi.md#delete_connectors) | **DELETE** /layar/connector/deleteMany | Delete multiple Twitter connectors
*ConnectorApi* | [**get_connector**](docs/ConnectorApi.md#get_connector) | **GET** /layar/connector/{id} | Get Twitter connector details
*ConnectorApi* | [**patch_connector**](docs/ConnectorApi.md#patch_connector) | **PATCH** /layar/connector/{id} | Update a specific attribute
*ConnectorApi* | [**search_connectors**](docs/ConnectorApi.md#search_connectors) | **GET** /layar/connector | Search for Twitter connectors
*ConnectorApi* | [**update_connector**](docs/ConnectorApi.md#update_connector) | **PUT** /layar/connector/{id} | Update Twitter connector details
*DataFabricApi* | [**get_data_providers**](docs/DataFabricApi.md#get_data_providers) | **GET** /layar/node | Search for data providers
*DataFabricApi* | [**get_fabrics**](docs/DataFabricApi.md#get_fabrics) | **GET** /layar/fabric | Search for data fabrics
*EventApi* | [**get_event**](docs/EventApi.md#get_event) | **GET** /layar/event/{id} | Get event details
*EventApi* | [**search_events**](docs/EventApi.md#search_events) | **GET** /layar/event | Search for events
*GroupApi* | [**group_terms**](docs/GroupApi.md#group_terms) | **POST** /layar/group/terms | Group similar terms
*LiveSourceApi* | [**create_feeds**](docs/LiveSourceApi.md#create_feeds) | **POST** /layar/liveSource | Create a new connector
*LiveSourceApi* | [**create_feeds_from_column**](docs/LiveSourceApi.md#create_feeds_from_column) | **POST** /layar/liveSource/createFeedsFromColumn | Create new RSS connectors from a spreadsheet of URLs
*LiveSourceApi* | [**delete_feed**](docs/LiveSourceApi.md#delete_feed) | **DELETE** /layar/liveSource/{id} | Delete a connector
*LiveSourceApi* | [**delete_feeds**](docs/LiveSourceApi.md#delete_feeds) | **DELETE** /layar/liveSource/deleteMany | Delete multiple connectors
*LiveSourceApi* | [**get_feed**](docs/LiveSourceApi.md#get_feed) | **GET** /layar/liveSource/{id} | Get connector details
*LiveSourceApi* | [**get_import_status**](docs/LiveSourceApi.md#get_import_status) | **GET** /layar/liveSource/{id}/importStatus | Get percent completed for a live indexing job
*LiveSourceApi* | [**get_job_status**](docs/LiveSourceApi.md#get_job_status) | **GET** /layar/liveSource/{id}/jobStatus | Get job status details
*LiveSourceApi* | [**get_source_document_url**](docs/LiveSourceApi.md#get_source_document_url) | **GET** /layar/liveSource/{id}/sourceDocuments | Get the documents from a given connector
*LiveSourceApi* | [**search_feeds**](docs/LiveSourceApi.md#search_feeds) | **GET** /layar/liveSource | Search for connectors
*LiveSourceApi* | [**unschedule_job**](docs/LiveSourceApi.md#unschedule_job) | **PUT** /layar/liveSource/{id}/jobStatus/unschedule | Change job status schedule
*LiveSourceApi* | [**update_feed**](docs/LiveSourceApi.md#update_feed) | **PUT** /layar/liveSource/{id} | Update connector details
*LiveSourceApi* | [**update_job**](docs/LiveSourceApi.md#update_job) | **PUT** /layar/liveSource/{id}/{jobAction} | Update a job with a new action
*ModelApi* | [**download_model**](docs/ModelApi.md#download_model) | **GET** /layar/model/{id}/download | Download a model by ID
*ModelApi* | [**search_models_by_computation_id**](docs/ModelApi.md#search_models_by_computation_id) | **GET** /layar/projectComputation/{id}/models | Find models by project computation ID
*ModelApi* | [**search_models_by_module_id**](docs/ModelApi.md#search_models_by_module_id) | **GET** /layar/module/{moduleId}/models | Find models by module ID
*ModelApi* | [**search_models_by_project_id**](docs/ModelApi.md#search_models_by_project_id) | **GET** /layar/project/{projectId}/models | Find models by project ID
*ModuleApi* | [**create_module**](docs/ModuleApi.md#create_module) | **POST** /layar/module | Create a new module
*ModuleApi* | [**get_module**](docs/ModuleApi.md#get_module) | **GET** /layar/module/{id} | Get module details
*ModuleApi* | [**search_modules**](docs/ModuleApi.md#search_modules) | **GET** /layar/module | Search for modules
*NamedEntityApi* | [**get_types**](docs/NamedEntityApi.md#get_types) | **GET** /layar/namedEntity/types | Retrieve a list of available named entity types
*NamedEntityApi* | [**named_entity_tag**](docs/NamedEntityApi.md#named_entity_tag) | **POST** /layar/statement/{id}/namedEntity/tag | Tag named entities within specific columns of a table
*NamedEntityApi* | [**tag_ner**](docs/NamedEntityApi.md#tag_ner) | **POST** /layar/namedEntity/tag | Tag named entities
*OntologyApi* | [**create_table_ontology**](docs/OntologyApi.md#create_table_ontology) | **POST** /layar/sourceDocument/{id}/createOntology | Create an ontology from a table
*OntologyTermApi* | [**create_term**](docs/OntologyTermApi.md#create_term) | **POST** /layar/ontologyTerm | Create a new ontology term
*OntologyTermApi* | [**delete_term**](docs/OntologyTermApi.md#delete_term) | **DELETE** /layar/ontologyTerm/{id} | Delete an ontology term
*OntologyTermApi* | [**get_term**](docs/OntologyTermApi.md#get_term) | **GET** /layar/ontologyTerm/{id} | Get ontology term details
*OntologyTermApi* | [**layar_ontology_term_get**](docs/OntologyTermApi.md#layar_ontology_term_get) | **GET** /layar/ontologyTerm | Search for ontology terms
*OntologyTermApi* | [**search_term**](docs/OntologyTermApi.md#search_term) | **POST** /layar/ontologyTerm/search | 
*OntologyTermApi* | [**update_term**](docs/OntologyTermApi.md#update_term) | **PUT** /layar/ontologyTerm/{id} | Update ontology term details
*ParagraphApi* | [**get_paragraph**](docs/ParagraphApi.md#get_paragraph) | **GET** /layar/paragraph/{id} | Get paragraph details
*ParagraphApi* | [**layar_paragraph_get**](docs/ParagraphApi.md#layar_paragraph_get) | **GET** /layar/paragraph | Search for paragraphs
*ParagraphApi* | [**parse_text**](docs/ParagraphApi.md#parse_text) | **POST** /layar/partOfSpeech/parseText | Parse text into part-of-speech components
*ParagraphApi* | [**search_paragraph**](docs/ParagraphApi.md#search_paragraph) | **POST** /layar/paragraph/search | 
*ProjectApi* | [**add_input**](docs/ProjectApi.md#add_input) | **PUT** /layar/project/{id}/addInput | Add items to a project
*ProjectApi* | [**create_project**](docs/ProjectApi.md#create_project) | **POST** /layar/project | Create a new project
*ProjectApi* | [**delete_project**](docs/ProjectApi.md#delete_project) | **DELETE** /layar/project/{id} | Delete a project
*ProjectApi* | [**delete_projects**](docs/ProjectApi.md#delete_projects) | **DELETE** /layar/project/deleteMany | Delete multiple projects
*ProjectApi* | [**download_results**](docs/ProjectApi.md#download_results) | **GET** /layar/project/{id}/results/download | Download project results as zip file
*ProjectApi* | [**get_project**](docs/ProjectApi.md#get_project) | **GET** /layar/project/{id} | Get project details
*ProjectApi* | [**get_results**](docs/ProjectApi.md#get_results) | **GET** /layar/project/{id}/results | Get project results details
*ProjectApi* | [**get_results_som**](docs/ProjectApi.md#get_results_som) | **GET** /layar/project/{id}/results/som | Download project results as SOM
*ProjectApi* | [**remove_input**](docs/ProjectApi.md#remove_input) | **PUT** /layar/project/{id}/removeInput | Remove items from a project
*ProjectApi* | [**run_project**](docs/ProjectApi.md#run_project) | **POST** /layar/project/{id}/run | Run a new project
*ProjectApi* | [**search_projects**](docs/ProjectApi.md#search_projects) | **GET** /layar/project | Search for projects
*ProjectApi* | [**update_project**](docs/ProjectApi.md#update_project) | **PUT** /layar/project/{id} | Update project details
*ProjectComputationApi* | [**cancel_computation**](docs/ProjectComputationApi.md#cancel_computation) | **POST** /layar/projectComputation/{id}/cancel | Cancel a project computation job (hard stop)
*ProjectComputationApi* | [**download_computation**](docs/ProjectComputationApi.md#download_computation) | **GET** /layar/projectComputation/{id}/downloadZipResults | Download computation job documents as zip file
*ProjectComputationApi* | [**download_logs**](docs/ProjectComputationApi.md#download_logs) | **GET** /layar/projectComputation/{id}/downloadLogs | Download all computation job logs
*ProjectComputationApi* | [**get_logs**](docs/ProjectComputationApi.md#get_logs) | **GET** /layar/projectComputation/{id}/logs | Retrieve logs for computation job
*ProjectComputationApi* | [**get_project_computation**](docs/ProjectComputationApi.md#get_project_computation) | **GET** /layar/projectComputation/{id} | Get project computation details
*ProjectComputationApi* | [**stop_job**](docs/ProjectComputationApi.md#stop_job) | **POST** /layar/projectComputation/{id}/stopTraining | Stop a computation job (soft stop)
*QuestionApi* | [**ask**](docs/QuestionApi.md#ask) | **POST** /layar/question/ask | Ask a new question
*QuestionApi* | [**cancel_batch**](docs/QuestionApi.md#cancel_batch) | **PUT** /layar/question/cancelBulkQuestionAnswerJob/{jobID} | Cancel a bulk QA job request
*QuestionApi* | [**create_question**](docs/QuestionApi.md#create_question) | **POST** /layar/question | Create a new question
*QuestionApi* | [**delete_question**](docs/QuestionApi.md#delete_question) | **DELETE** /layar/question/{id} | Delete a question
*QuestionApi* | [**delete_questions**](docs/QuestionApi.md#delete_questions) | **DELETE** /layar/question/deleteMany | Delete multiple questions
*QuestionApi* | [**find_more_answers**](docs/QuestionApi.md#find_more_answers) | **POST** /layar/question/{id}/answers/more | Find more answers to a question
*QuestionApi* | [**get_question**](docs/QuestionApi.md#get_question) | **GET** /layar/question/{id} | Get question details
*QuestionApi* | [**get_question_field_counts**](docs/QuestionApi.md#get_question_field_counts) | **POST** /layar/question/{field}/counts | Get curation details by field type
*QuestionApi* | [**patch_question**](docs/QuestionApi.md#patch_question) | **PATCH** /layar/question/{id} | Update specific details for a question
*QuestionApi* | [**query_expansion**](docs/QuestionApi.md#query_expansion) | **POST** /layar/question/queryExpansion | Enable query expansion
*QuestionApi* | [**refresh_answers**](docs/QuestionApi.md#refresh_answers) | **POST** /layar/question/{id}/answers/refresh | Search for answers in new documents
*QuestionApi* | [**search_question_batch**](docs/QuestionApi.md#search_question_batch) | **POST** /layar/question/searchQuestionBatch | Search for question batches
*QuestionApi* | [**search_questions**](docs/QuestionApi.md#search_questions) | **POST** /layar/question/search | Search for questions
*QuestionApi* | [**start_batch**](docs/QuestionApi.md#start_batch) | **POST** /layar/question/startBulkQuestionAnswerJob | Submit a bulk QA job request
*QuestionApi* | [**update_question**](docs/QuestionApi.md#update_question) | **PUT** /layar/question/{id} | Update a saved question
*RadarApi* | [**get_nearest_neighbor_count**](docs/RadarApi.md#get_nearest_neighbor_count) | **GET** /layar/radar/count | Get nearest neighbor counts
*RadarApi* | [**get_radar**](docs/RadarApi.md#get_radar) | **GET** /layar/radar | Get Radar results
*RadarApi* | [**get_radar_by_concept_id**](docs/RadarApi.md#get_radar_by_concept_id) | **GET** /layar/radar/byConceptId | Find semantically similar terms for a concept
*RadarApi* | [**get_radar_by_query_string**](docs/RadarApi.md#get_radar_by_query_string) | **GET** /layar/radar/byQueryString | Find semantically similar terms for a string
*SavedListApi* | [**add_items**](docs/SavedListApi.md#add_items) | **PUT** /layar/savedList/{id}/addItem | Add items to a set
*SavedListApi* | [**add_items_by_search**](docs/SavedListApi.md#add_items_by_search) | **PUT** /layar/savedList/{id}/add | Add items to a set
*SavedListApi* | [**create_saved_list**](docs/SavedListApi.md#create_saved_list) | **POST** /layar/savedList | Create a new set
*SavedListApi* | [**delete_saved_list**](docs/SavedListApi.md#delete_saved_list) | **DELETE** /layar/savedList/{id} | Delete a set
*SavedListApi* | [**delete_saved_lists**](docs/SavedListApi.md#delete_saved_lists) | **DELETE** /layar/savedList/deleteMany | Delete multiple sets
*SavedListApi* | [**download_saved_list**](docs/SavedListApi.md#download_saved_list) | **GET** /layar/savedList/{id}/downloadCsv | Download set contents to a CSV
*SavedListApi* | [**get_saved_list**](docs/SavedListApi.md#get_saved_list) | **GET** /layar/savedList/{id} | Get set details
*SavedListApi* | [**remove_items**](docs/SavedListApi.md#remove_items) | **DELETE** /layar/savedList/{id}/removeItem | Remove items from a Layar set
*SavedListApi* | [**search_saved_list**](docs/SavedListApi.md#search_saved_list) | **GET** /layar/savedList | Search for sets
*SavedListApi* | [**update_saved_list**](docs/SavedListApi.md#update_saved_list) | **PUT** /layar/savedList/{id} | Update set details
*SmilesApi* | [**create_tox_csv**](docs/SmilesApi.md#create_tox_csv) | **POST** /layar/smiles/createTox21CSV | Run the Tox21 model and download the results to a CSV
*SmilesApi* | [**create_tox_som**](docs/SmilesApi.md#create_tox_som) | **POST** /layar/smiles/createTox21SOM | Run the Tox21 model and download the results to a SOM
*SourceDocumentApi* | [**add_annotation**](docs/SourceDocumentApi.md#add_annotation) | **POST** /layar/sourceDocument/{id}/addAnnotation | Add an annotation to a document
*SourceDocumentApi* | [**add_annotations**](docs/SourceDocumentApi.md#add_annotations) | **POST** /layar/sourceDocument/{id}/addAnnotations | Add a list of annotations to a document
*SourceDocumentApi* | [**add_column**](docs/SourceDocumentApi.md#add_column) | **PUT** /layar/sourceDocument/{id}/addColumn | Add a column to a table document
*SourceDocumentApi* | [**add_viewer**](docs/SourceDocumentApi.md#add_viewer) | **POST** /layar/sourceDocument/{id}/viewers | Authorize a viewer for the source document
*SourceDocumentApi* | [**create_document**](docs/SourceDocumentApi.md#create_document) | **POST** /layar/sourceDocument | Create a source document
*SourceDocumentApi* | [**create_table_ontology**](docs/SourceDocumentApi.md#create_table_ontology) | **POST** /layar/sourceDocument/{id}/createOntology | Create an ontology from a table
*SourceDocumentApi* | [**delete_document**](docs/SourceDocumentApi.md#delete_document) | **DELETE** /layar/sourceDocument/{id} | Delete a document
*SourceDocumentApi* | [**delete_documents**](docs/SourceDocumentApi.md#delete_documents) | **DELETE** /layar/sourceDocument/deleteMany | Delete multiple documents
*SourceDocumentApi* | [**download_annotations**](docs/SourceDocumentApi.md#download_annotations) | **GET** /layar/sourceDocument/downloadAnnotations | Download document annotations to a CSV
*SourceDocumentApi* | [**download_document**](docs/SourceDocumentApi.md#download_document) | **GET** /layar/sourceDocument/{id}/download | Download document by ID
*SourceDocumentApi* | [**extract_table_by_page**](docs/SourceDocumentApi.md#extract_table_by_page) | **POST** /layar/sourceDocument/{id}/page/{page}/extractTable | Extract table from a specific page
*SourceDocumentApi* | [**extract_tables**](docs/SourceDocumentApi.md#extract_tables) | **POST** /layar/sourceDocument/{id}/extractTables | Extract tables from a document
*SourceDocumentApi* | [**get_counts_by_suggested_category**](docs/SourceDocumentApi.md#get_counts_by_suggested_category) | **GET** /layar/sourceDocument/{projectComputationId}/countBySuggestedCategory | Get document counts for suggested concept type by computation id
*SourceDocumentApi* | [**get_counts_by_type**](docs/SourceDocumentApi.md#get_counts_by_type) | **GET** /layar/sourceDocument/countByType | Get document counts by type
*SourceDocumentApi* | [**get_counts_over_time**](docs/SourceDocumentApi.md#get_counts_over_time) | **GET** /layar/sourceDocument/docCountsOverTime | Get document counts over time
*SourceDocumentApi* | [**get_doc_field_counts**](docs/SourceDocumentApi.md#get_doc_field_counts) | **POST** /layar/sourceDocument/{field}/counts | Get document counts by field type
*SourceDocumentApi* | [**get_document**](docs/SourceDocumentApi.md#get_document) | **GET** /layar/sourceDocument/{id} | Get source document details
*SourceDocumentApi* | [**get_document_concepts**](docs/SourceDocumentApi.md#get_document_concepts) | **GET** /layar/sourceDocument/{id}/concepts | Get concept counts by document ID
*SourceDocumentApi* | [**get_document_statements**](docs/SourceDocumentApi.md#get_document_statements) | **GET** /layar/sourceDocument/{id}/statements | Get statement counts by document ID
*SourceDocumentApi* | [**get_document_status**](docs/SourceDocumentApi.md#get_document_status) | **GET** /layar/sourceDocument/{id}/status | Get the import status for a document
*SourceDocumentApi* | [**get_page_preview**](docs/SourceDocumentApi.md#get_page_preview) | **GET** /layar/sourceDocument/{id}/page/{page}/preview | Get a document preview for a specific page
*SourceDocumentApi* | [**get_preview**](docs/SourceDocumentApi.md#get_preview) | **GET** /layar/sourceDocument/{id}/preview | Get a document preview
*SourceDocumentApi* | [**get_statement_counts**](docs/SourceDocumentApi.md#get_statement_counts) | **GET** /layar/sourceDocument/{id}/statementCount | Get a count of all statements in a document
*SourceDocumentApi* | [**get_viewers**](docs/SourceDocumentApi.md#get_viewers) | **GET** /layar/sourceDocument/{id}/viewers | Get a list of all viewers of the source document
*SourceDocumentApi* | [**remove_annotation**](docs/SourceDocumentApi.md#remove_annotation) | **DELETE** /layar/sourceDocument/{id}/annotations/{annotationId} | Delete annotations by annotation ID
*SourceDocumentApi* | [**render_pdf**](docs/SourceDocumentApi.md#render_pdf) | **GET** /layar/sourceDocument/{id}/renderPdf | Render a PDF of a document
*SourceDocumentApi* | [**search_documents**](docs/SourceDocumentApi.md#search_documents) | **POST** /layar/sourceDocument/search | Search for documents
*SourceDocumentApi* | [**table_similarity**](docs/SourceDocumentApi.md#table_similarity) | **POST** /layar/sourceDocument/similarity | Calculate table similarity
*SourceDocumentApi* | [**update_annotation**](docs/SourceDocumentApi.md#update_annotation) | **PUT** /layar/sourceDocument/{id}/annotations | Update annotation details
*SourceDocumentApi* | [**update_document**](docs/SourceDocumentApi.md#update_document) | **PUT** /layar/sourceDocument/{id} | Update document details
*StatementApi* | [**aggregate_values**](docs/StatementApi.md#aggregate_values) | **POST** /layar/statement/aggs | Return distinct values in columns
*StatementApi* | [**create_statement**](docs/StatementApi.md#create_statement) | **POST** /layar/statement | Create a new statement
*StatementApi* | [**delete_statement**](docs/StatementApi.md#delete_statement) | **DELETE** /layar/statement/{id} | Delete a statement
*StatementApi* | [**delete_statements**](docs/StatementApi.md#delete_statements) | **DELETE** /layar/statement/deleteMany | Delete multiple statements
*StatementApi* | [**get_relationship_evidence**](docs/StatementApi.md#get_relationship_evidence) | **GET** /layar/statement/relationshipEvidence/{conceptId1}/{relationship}/{conceptId2} | Get existing relationships between two given concepts
*StatementApi* | [**get_statement**](docs/StatementApi.md#get_statement) | **GET** /layar/statement/{id} | Get statement details
*StatementApi* | [**get_statement_field_counts**](docs/StatementApi.md#get_statement_field_counts) | **POST** /layar/statement/{field}/counts | Get statement counts for a table column
*StatementApi* | [**named_entity_tag**](docs/StatementApi.md#named_entity_tag) | **POST** /layar/statement/{id}/namedEntity/tag | Tag named entities within specific columns of a table
*StatementApi* | [**search_statements**](docs/StatementApi.md#search_statements) | **POST** /layar/statement/search | Search for statements
*StatementApi* | [**update_statement**](docs/StatementApi.md#update_statement) | **PUT** /layar/statement/{id} | Update statement details
*StatusApi* | [**get_app_status**](docs/StatusApi.md#get_app_status) | **GET** /layar/app | Get app uptime status
*VectorSimilarityApi* | [**create_vector_similarity**](docs/VectorSimilarityApi.md#create_vector_similarity) | **POST** /layar/vectorSimilarity | Create a new vector embedding
*VectorSimilarityApi* | [**get_similar_statements**](docs/VectorSimilarityApi.md#get_similar_statements) | **GET** /layar/vectorSimilarity/{similarityRequestId}/statements | Find similar statements by statement ID
*VectorSimilarityApi* | [**get_vector_similarity**](docs/VectorSimilarityApi.md#get_vector_similarity) | **GET** /layar/vectorSimilarity/{id} | Get vector details
*VectorSimilarityApi* | [**get_vectors_by_query_string**](docs/VectorSimilarityApi.md#get_vectors_by_query_string) | **GET** /layar/vectorSimilarity/byQueryString | Find similar embeddings by query string
