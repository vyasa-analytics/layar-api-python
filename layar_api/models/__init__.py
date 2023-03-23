# coding: utf-8

# flake8: noqa
"""
    Layar API Documentation

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: VERSION_PLACEHOLDER
    Contact: support@vyasa.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

# import models into model package
from layar_api.models.add_column_command import AddColumnCommand
from layar_api.models.add_documents_response import AddDocumentsResponse
from layar_api.models.all_search_response import AllSearchResponse
from layar_api.models.annotation import Annotation
from layar_api.models.annotation_search import AnnotationSearch
from layar_api.models.answer import Answer
from layar_api.models.answer_array import AnswerArray
from layar_api.models.answer_evidence import AnswerEvidence
from layar_api.models.answer_exclude_search_command import AnswerExcludeSearchCommand
from layar_api.models.answer_search_command import AnswerSearchCommand
from layar_api.models.ask_question_command import AskQuestionCommand
from layar_api.models.ask_question_response import AskQuestionResponse
from layar_api.models.ask_question_response_answers import AskQuestionResponseAnswers
from layar_api.models.ask_question_response_nbest_predictions import AskQuestionResponseNbestPredictions
from layar_api.models.autocomplete_item import AutocompleteItem
from layar_api.models.autocomplete_result import AutocompleteResult
from layar_api.models.base_search_command import BaseSearchCommand
from layar_api.models.body import Body
from layar_api.models.body1 import Body1
from layar_api.models.body2 import Body2
from layar_api.models.body3 import Body3
from layar_api.models.body4 import Body4
from layar_api.models.body5 import Body5
from layar_api.models.body6 import Body6
from layar_api.models.body7 import Body7
from layar_api.models.body8 import Body8
from layar_api.models.bulk_question import BulkQuestion
from layar_api.models.bulk_question_command import BulkQuestionCommand
from layar_api.models.bulk_question_search_command import BulkQuestionSearchCommand
from layar_api.models.column_definition import ColumnDefinition
from layar_api.models.column_filter import ColumnFilter
from layar_api.models.column_filter_condition import ColumnFilterCondition
from layar_api.models.column_filter_condition_type import ColumnFilterConditionType
from layar_api.models.column_filter_operator import ColumnFilterOperator
from layar_api.models.column_filter_type import ColumnFilterType
from layar_api.models.concept import Concept
from layar_api.models.concept_assignment import ConceptAssignment
from layar_api.models.concept_count_command import ConceptCountCommand
from layar_api.models.concept_counts_in_statements_over_time import ConceptCountsInStatementsOverTime
from layar_api.models.concept_query_params import ConceptQueryParams
from layar_api.models.concept_relationship import ConceptRelationship
from layar_api.models.concept_set import ConceptSet
from layar_api.models.concept_synonym_assignment_response import ConceptSynonymAssignmentResponse
from layar_api.models.concept_term_assignment import ConceptTermAssignment
from layar_api.models.concept_type import ConceptType
from layar_api.models.concept_type_relationship_template import ConceptTypeRelationshipTemplate
from layar_api.models.connector import Connector
from layar_api.models.coordinates import Coordinates
from layar_api.models.cortex_setting import CortexSetting
from layar_api.models.count_command import CountCommand
from layar_api.models.cross_query import CrossQuery
from layar_api.models.curation import Curation
from layar_api.models.curation_custom_string_context import CurationCustomStringContext
from layar_api.models.curation_type import CurationType
from layar_api.models.deep_learning_model import DeepLearningModel
from layar_api.models.deep_learning_task_update import DeepLearningTaskUpdate
from layar_api.models.detected_concept import DetectedConcept
from layar_api.models.distributed_source_document_search_command import DistributedSourceDocumentSearchCommand
from layar_api.models.doc_counts_in_statements_over_time import DocCountsInStatementsOverTime
from layar_api.models.domain_object import DomainObject
from layar_api.models.dynamic_column_type import DynamicColumnType
from layar_api.models.error import Error
from layar_api.models.event import Event
from layar_api.models.extract_tables_command import ExtractTablesCommand
from layar_api.models.field_count import FieldCount
from layar_api.models.field_filter import FieldFilter
from layar_api.models.field_filter_conditions import FieldFilterConditions
from layar_api.models.inline_response200 import InlineResponse200
from layar_api.models.inline_response2001 import InlineResponse2001
from layar_api.models.inline_response2002 import InlineResponse2002
from layar_api.models.inline_response2003 import InlineResponse2003
from layar_api.models.inline_response2004 import InlineResponse2004
from layar_api.models.inline_response201 import InlineResponse201
from layar_api.models.inline_response2011 import InlineResponse2011
from layar_api.models.list_of_annotations import ListOfAnnotations
from layar_api.models.list_of_ids import ListOfIds
from layar_api.models.list_of_item_ids import ListOfItemIds
from layar_api.models.list_of_source_ids import ListOfSourceIds
from layar_api.models.live_source import LiveSource
from layar_api.models.live_source_import_status import LiveSourceImportStatus
from layar_api.models.live_source_job_status import LiveSourceJobStatus
from layar_api.models.live_source_type import LiveSourceType
from layar_api.models.log_stash import LogStash
from layar_api.models.map_string_object import MapStringObject
from layar_api.models.module import Module
from layar_api.models.named_entity import NamedEntity
from layar_api.models.named_entity_request import NamedEntityRequest
from layar_api.models.named_entity_response import NamedEntityResponse
from layar_api.models.named_entity_response_named_entities import NamedEntityResponseNamedEntities
from layar_api.models.one_of_annotation_search_values_items import OneOfAnnotationSearchValuesItems
from layar_api.models.one_ofbody1 import OneOfbody1
from layar_api.models.one_ofbody2 import OneOfbody2
from layar_api.models.one_ofbody4 import OneOfbody4
from layar_api.models.one_ofbody5 import OneOfbody5
from layar_api.models.one_ofinline_response201 import OneOfinlineResponse201
from layar_api.models.one_ofinline_response2011 import OneOfinlineResponse2011
from layar_api.models.ontology_search_command import OntologySearchCommand
from layar_api.models.ontology_term import OntologyTerm
from layar_api.models.paragraph import Paragraph
from layar_api.models.paragraph_exclude_search_command import ParagraphExcludeSearchCommand
from layar_api.models.paragraph_question_search_command import ParagraphQuestionSearchCommand
from layar_api.models.paragraph_search_command import ParagraphSearchCommand
from layar_api.models.part_of_speech_command import PartOfSpeechCommand
from layar_api.models.part_of_speech_response import PartOfSpeechResponse
from layar_api.models.part_of_speech_token import PartOfSpeechToken
from layar_api.models.patch_command import PatchCommand
from layar_api.models.project import Project
from layar_api.models.project_computation import ProjectComputation
from layar_api.models.query_expansion_request import QueryExpansionRequest
from layar_api.models.query_expansion_request_synonym_expansion import QueryExpansionRequestSynonymExpansion
from layar_api.models.query_expansion_response import QueryExpansionResponse
from layar_api.models.question import Question
from layar_api.models.question_answer_response import QuestionAnswerResponse
from layar_api.models.question_answer_response_query_results import QuestionAnswerResponseQueryResults
from layar_api.models.question_answer_type_of_search import QuestionAnswerTypeOfSearch
from layar_api.models.question_batch import QuestionBatch
from layar_api.models.question_search_command import QuestionSearchCommand
from layar_api.models.radar import Radar
from layar_api.models.radar_exclude_search_command import RadarExcludeSearchCommand
from layar_api.models.restart_services_request import RestartServicesRequest
from layar_api.models.som_request import SOMRequest
from layar_api.models.saved_list import SavedList
from layar_api.models.section_search import SectionSearch
from layar_api.models.similar_column import SimilarColumn
from layar_api.models.source_document import SourceDocument
from layar_api.models.source_document_exclude_search_command import SourceDocumentExcludeSearchCommand
from layar_api.models.source_document_import_status import SourceDocumentImportStatus
from layar_api.models.source_document_search_command import SourceDocumentSearchCommand
from layar_api.models.source_document_similarity_command import SourceDocumentSimilarityCommand
from layar_api.models.source_document_type import SourceDocumentType
from layar_api.models.source_document_viewer import SourceDocumentViewer
from layar_api.models.source_documents_assignment import SourceDocumentsAssignment
from layar_api.models.statement import Statement
from layar_api.models.statement_named_entity_command import StatementNamedEntityCommand
from layar_api.models.statement_search_command import StatementSearchCommand
from layar_api.models.statement_similarity import StatementSimilarity
from layar_api.models.stop_training import StopTraining
from layar_api.models.table_similarity import TableSimilarity
from layar_api.models.tagged_concept import TaggedConcept
from layar_api.models.tagged_relationship import TaggedRelationship
from layar_api.models.user_curation import UserCuration
from layar_api.models.vector_similarity_request import VectorSimilarityRequest
from layar_api.models.version_info_result import VersionInfoResult
