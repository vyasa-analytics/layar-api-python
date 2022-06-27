# coding: utf-8

"""
    Layar API Documentation

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: VERSION_PLACEHOLDER
    Contact: support@vyasa.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class SourceDocumentExcludeSearchCommand(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'annotation_searches': 'list[AnnotationSearch]',
        'category_ids': 'list[str]',
        'concept_ids': 'list[str]',
        'connector_id': 'str',
        'connector_ids': 'list[str]',
        'data_source_types': 'list[str]',
        'has_fields': 'list[str]',
        'highlight': 'bool',
        'highlight_fragment_size': 'int',
        'highlight_number_of_fragments': 'int',
        'highlight_post_tag': 'str',
        'highlight_pre_tag': 'str',
        'ids': 'list[str]',
        'live_source_id': 'str',
        'live_source_ids': 'list[str]',
        'live_source_types': 'list[LiveSourceType]',
        'log_search': 'bool',
        'mime_types': 'list[str]',
        'must_have_annotations': 'bool',
        'named_entities': 'list[NamedEntity]',
        'parent_ids': 'list[str]',
        'paths': 'list[str]',
        'project_computation_id': 'str',
        'question': 'str',
        'saved_list_ids': 'list[str]',
        'section_searches': 'list[SectionSearch]',
        'similarity_document_id': 'str',
        'similarity_threshold': 'float',
        'source_fields': 'list[str]',
        'sources': 'list[str]',
        'term_operator': 'str',
        'terms': 'list[str]',
        'trial_data': 'object',
        'type': 'SourceDocumentType',
        'types': 'list[SourceDocumentType]',
        'user_ids': 'list[int]',
        'vyasa_clients': 'list[str]'
    }

    attribute_map = {
        'annotation_searches': 'annotationSearches',
        'category_ids': 'categoryIds',
        'concept_ids': 'conceptIds',
        'connector_id': 'connectorId',
        'connector_ids': 'connectorIds',
        'data_source_types': 'dataSourceTypes',
        'has_fields': 'hasFields',
        'highlight': 'highlight',
        'highlight_fragment_size': 'highlightFragmentSize',
        'highlight_number_of_fragments': 'highlightNumberOfFragments',
        'highlight_post_tag': 'highlightPostTag',
        'highlight_pre_tag': 'highlightPreTag',
        'ids': 'ids',
        'live_source_id': 'liveSourceId',
        'live_source_ids': 'liveSourceIds',
        'live_source_types': 'liveSourceTypes',
        'log_search': 'logSearch',
        'mime_types': 'mimeTypes',
        'must_have_annotations': 'mustHaveAnnotations',
        'named_entities': 'namedEntities',
        'parent_ids': 'parentIds',
        'paths': 'paths',
        'project_computation_id': 'projectComputationId',
        'question': 'question',
        'saved_list_ids': 'savedListIds',
        'section_searches': 'sectionSearches',
        'similarity_document_id': 'similarityDocumentId',
        'similarity_threshold': 'similarityThreshold',
        'source_fields': 'sourceFields',
        'sources': 'sources',
        'term_operator': 'termOperator',
        'terms': 'terms',
        'trial_data': 'trialData',
        'type': 'type',
        'types': 'types',
        'user_ids': 'userIds',
        'vyasa_clients': 'vyasaClients'
    }

    def __init__(self, annotation_searches=None, category_ids=None, concept_ids=None, connector_id=None, connector_ids=None, data_source_types=None, has_fields=None, highlight=None, highlight_fragment_size=None, highlight_number_of_fragments=None, highlight_post_tag=None, highlight_pre_tag=None, ids=None, live_source_id=None, live_source_ids=None, live_source_types=None, log_search=None, mime_types=None, must_have_annotations=None, named_entities=None, parent_ids=None, paths=None, project_computation_id=None, question=None, saved_list_ids=None, section_searches=None, similarity_document_id=None, similarity_threshold=None, source_fields=None, sources=None, term_operator=None, terms=None, trial_data=None, type=None, types=None, user_ids=None, vyasa_clients=None):  # noqa: E501
        """SourceDocumentExcludeSearchCommand - a model defined in Swagger"""  # noqa: E501
        self._annotation_searches = None
        self._category_ids = None
        self._concept_ids = None
        self._connector_id = None
        self._connector_ids = None
        self._data_source_types = None
        self._has_fields = None
        self._highlight = None
        self._highlight_fragment_size = None
        self._highlight_number_of_fragments = None
        self._highlight_post_tag = None
        self._highlight_pre_tag = None
        self._ids = None
        self._live_source_id = None
        self._live_source_ids = None
        self._live_source_types = None
        self._log_search = None
        self._mime_types = None
        self._must_have_annotations = None
        self._named_entities = None
        self._parent_ids = None
        self._paths = None
        self._project_computation_id = None
        self._question = None
        self._saved_list_ids = None
        self._section_searches = None
        self._similarity_document_id = None
        self._similarity_threshold = None
        self._source_fields = None
        self._sources = None
        self._term_operator = None
        self._terms = None
        self._trial_data = None
        self._type = None
        self._types = None
        self._user_ids = None
        self._vyasa_clients = None
        self.discriminator = None
        if annotation_searches is not None:
            self.annotation_searches = annotation_searches
        if category_ids is not None:
            self.category_ids = category_ids
        if concept_ids is not None:
            self.concept_ids = concept_ids
        if connector_id is not None:
            self.connector_id = connector_id
        if connector_ids is not None:
            self.connector_ids = connector_ids
        if data_source_types is not None:
            self.data_source_types = data_source_types
        if has_fields is not None:
            self.has_fields = has_fields
        if highlight is not None:
            self.highlight = highlight
        if highlight_fragment_size is not None:
            self.highlight_fragment_size = highlight_fragment_size
        if highlight_number_of_fragments is not None:
            self.highlight_number_of_fragments = highlight_number_of_fragments
        if highlight_post_tag is not None:
            self.highlight_post_tag = highlight_post_tag
        if highlight_pre_tag is not None:
            self.highlight_pre_tag = highlight_pre_tag
        if ids is not None:
            self.ids = ids
        if live_source_id is not None:
            self.live_source_id = live_source_id
        if live_source_ids is not None:
            self.live_source_ids = live_source_ids
        if live_source_types is not None:
            self.live_source_types = live_source_types
        if log_search is not None:
            self.log_search = log_search
        if mime_types is not None:
            self.mime_types = mime_types
        if must_have_annotations is not None:
            self.must_have_annotations = must_have_annotations
        if named_entities is not None:
            self.named_entities = named_entities
        if parent_ids is not None:
            self.parent_ids = parent_ids
        if paths is not None:
            self.paths = paths
        if project_computation_id is not None:
            self.project_computation_id = project_computation_id
        if question is not None:
            self.question = question
        if saved_list_ids is not None:
            self.saved_list_ids = saved_list_ids
        if section_searches is not None:
            self.section_searches = section_searches
        if similarity_document_id is not None:
            self.similarity_document_id = similarity_document_id
        if similarity_threshold is not None:
            self.similarity_threshold = similarity_threshold
        if source_fields is not None:
            self.source_fields = source_fields
        if sources is not None:
            self.sources = sources
        if term_operator is not None:
            self.term_operator = term_operator
        if terms is not None:
            self.terms = terms
        if trial_data is not None:
            self.trial_data = trial_data
        if type is not None:
            self.type = type
        if types is not None:
            self.types = types
        if user_ids is not None:
            self.user_ids = user_ids
        if vyasa_clients is not None:
            self.vyasa_clients = vyasa_clients

    @property
    def annotation_searches(self):
        """Gets the annotation_searches of this SourceDocumentExcludeSearchCommand.  # noqa: E501


        :return: The annotation_searches of this SourceDocumentExcludeSearchCommand.  # noqa: E501
        :rtype: list[AnnotationSearch]
        """
        return self._annotation_searches

    @annotation_searches.setter
    def annotation_searches(self, annotation_searches):
        """Sets the annotation_searches of this SourceDocumentExcludeSearchCommand.


        :param annotation_searches: The annotation_searches of this SourceDocumentExcludeSearchCommand.  # noqa: E501
        :type: list[AnnotationSearch]
        """

        self._annotation_searches = annotation_searches

    @property
    def category_ids(self):
        """Gets the category_ids of this SourceDocumentExcludeSearchCommand.  # noqa: E501


        :return: The category_ids of this SourceDocumentExcludeSearchCommand.  # noqa: E501
        :rtype: list[str]
        """
        return self._category_ids

    @category_ids.setter
    def category_ids(self, category_ids):
        """Sets the category_ids of this SourceDocumentExcludeSearchCommand.


        :param category_ids: The category_ids of this SourceDocumentExcludeSearchCommand.  # noqa: E501
        :type: list[str]
        """

        self._category_ids = category_ids

    @property
    def concept_ids(self):
        """Gets the concept_ids of this SourceDocumentExcludeSearchCommand.  # noqa: E501


        :return: The concept_ids of this SourceDocumentExcludeSearchCommand.  # noqa: E501
        :rtype: list[str]
        """
        return self._concept_ids

    @concept_ids.setter
    def concept_ids(self, concept_ids):
        """Sets the concept_ids of this SourceDocumentExcludeSearchCommand.


        :param concept_ids: The concept_ids of this SourceDocumentExcludeSearchCommand.  # noqa: E501
        :type: list[str]
        """

        self._concept_ids = concept_ids

    @property
    def connector_id(self):
        """Gets the connector_id of this SourceDocumentExcludeSearchCommand.  # noqa: E501


        :return: The connector_id of this SourceDocumentExcludeSearchCommand.  # noqa: E501
        :rtype: str
        """
        return self._connector_id

    @connector_id.setter
    def connector_id(self, connector_id):
        """Sets the connector_id of this SourceDocumentExcludeSearchCommand.


        :param connector_id: The connector_id of this SourceDocumentExcludeSearchCommand.  # noqa: E501
        :type: str
        """

        self._connector_id = connector_id

    @property
    def connector_ids(self):
        """Gets the connector_ids of this SourceDocumentExcludeSearchCommand.  # noqa: E501


        :return: The connector_ids of this SourceDocumentExcludeSearchCommand.  # noqa: E501
        :rtype: list[str]
        """
        return self._connector_ids

    @connector_ids.setter
    def connector_ids(self, connector_ids):
        """Sets the connector_ids of this SourceDocumentExcludeSearchCommand.


        :param connector_ids: The connector_ids of this SourceDocumentExcludeSearchCommand.  # noqa: E501
        :type: list[str]
        """

        self._connector_ids = connector_ids

    @property
    def data_source_types(self):
        """Gets the data_source_types of this SourceDocumentExcludeSearchCommand.  # noqa: E501


        :return: The data_source_types of this SourceDocumentExcludeSearchCommand.  # noqa: E501
        :rtype: list[str]
        """
        return self._data_source_types

    @data_source_types.setter
    def data_source_types(self, data_source_types):
        """Sets the data_source_types of this SourceDocumentExcludeSearchCommand.


        :param data_source_types: The data_source_types of this SourceDocumentExcludeSearchCommand.  # noqa: E501
        :type: list[str]
        """

        self._data_source_types = data_source_types

    @property
    def has_fields(self):
        """Gets the has_fields of this SourceDocumentExcludeSearchCommand.  # noqa: E501


        :return: The has_fields of this SourceDocumentExcludeSearchCommand.  # noqa: E501
        :rtype: list[str]
        """
        return self._has_fields

    @has_fields.setter
    def has_fields(self, has_fields):
        """Sets the has_fields of this SourceDocumentExcludeSearchCommand.


        :param has_fields: The has_fields of this SourceDocumentExcludeSearchCommand.  # noqa: E501
        :type: list[str]
        """

        self._has_fields = has_fields

    @property
    def highlight(self):
        """Gets the highlight of this SourceDocumentExcludeSearchCommand.  # noqa: E501


        :return: The highlight of this SourceDocumentExcludeSearchCommand.  # noqa: E501
        :rtype: bool
        """
        return self._highlight

    @highlight.setter
    def highlight(self, highlight):
        """Sets the highlight of this SourceDocumentExcludeSearchCommand.


        :param highlight: The highlight of this SourceDocumentExcludeSearchCommand.  # noqa: E501
        :type: bool
        """

        self._highlight = highlight

    @property
    def highlight_fragment_size(self):
        """Gets the highlight_fragment_size of this SourceDocumentExcludeSearchCommand.  # noqa: E501


        :return: The highlight_fragment_size of this SourceDocumentExcludeSearchCommand.  # noqa: E501
        :rtype: int
        """
        return self._highlight_fragment_size

    @highlight_fragment_size.setter
    def highlight_fragment_size(self, highlight_fragment_size):
        """Sets the highlight_fragment_size of this SourceDocumentExcludeSearchCommand.


        :param highlight_fragment_size: The highlight_fragment_size of this SourceDocumentExcludeSearchCommand.  # noqa: E501
        :type: int
        """

        self._highlight_fragment_size = highlight_fragment_size

    @property
    def highlight_number_of_fragments(self):
        """Gets the highlight_number_of_fragments of this SourceDocumentExcludeSearchCommand.  # noqa: E501


        :return: The highlight_number_of_fragments of this SourceDocumentExcludeSearchCommand.  # noqa: E501
        :rtype: int
        """
        return self._highlight_number_of_fragments

    @highlight_number_of_fragments.setter
    def highlight_number_of_fragments(self, highlight_number_of_fragments):
        """Sets the highlight_number_of_fragments of this SourceDocumentExcludeSearchCommand.


        :param highlight_number_of_fragments: The highlight_number_of_fragments of this SourceDocumentExcludeSearchCommand.  # noqa: E501
        :type: int
        """

        self._highlight_number_of_fragments = highlight_number_of_fragments

    @property
    def highlight_post_tag(self):
        """Gets the highlight_post_tag of this SourceDocumentExcludeSearchCommand.  # noqa: E501


        :return: The highlight_post_tag of this SourceDocumentExcludeSearchCommand.  # noqa: E501
        :rtype: str
        """
        return self._highlight_post_tag

    @highlight_post_tag.setter
    def highlight_post_tag(self, highlight_post_tag):
        """Sets the highlight_post_tag of this SourceDocumentExcludeSearchCommand.


        :param highlight_post_tag: The highlight_post_tag of this SourceDocumentExcludeSearchCommand.  # noqa: E501
        :type: str
        """

        self._highlight_post_tag = highlight_post_tag

    @property
    def highlight_pre_tag(self):
        """Gets the highlight_pre_tag of this SourceDocumentExcludeSearchCommand.  # noqa: E501


        :return: The highlight_pre_tag of this SourceDocumentExcludeSearchCommand.  # noqa: E501
        :rtype: str
        """
        return self._highlight_pre_tag

    @highlight_pre_tag.setter
    def highlight_pre_tag(self, highlight_pre_tag):
        """Sets the highlight_pre_tag of this SourceDocumentExcludeSearchCommand.


        :param highlight_pre_tag: The highlight_pre_tag of this SourceDocumentExcludeSearchCommand.  # noqa: E501
        :type: str
        """

        self._highlight_pre_tag = highlight_pre_tag

    @property
    def ids(self):
        """Gets the ids of this SourceDocumentExcludeSearchCommand.  # noqa: E501


        :return: The ids of this SourceDocumentExcludeSearchCommand.  # noqa: E501
        :rtype: list[str]
        """
        return self._ids

    @ids.setter
    def ids(self, ids):
        """Sets the ids of this SourceDocumentExcludeSearchCommand.


        :param ids: The ids of this SourceDocumentExcludeSearchCommand.  # noqa: E501
        :type: list[str]
        """

        self._ids = ids

    @property
    def live_source_id(self):
        """Gets the live_source_id of this SourceDocumentExcludeSearchCommand.  # noqa: E501


        :return: The live_source_id of this SourceDocumentExcludeSearchCommand.  # noqa: E501
        :rtype: str
        """
        return self._live_source_id

    @live_source_id.setter
    def live_source_id(self, live_source_id):
        """Sets the live_source_id of this SourceDocumentExcludeSearchCommand.


        :param live_source_id: The live_source_id of this SourceDocumentExcludeSearchCommand.  # noqa: E501
        :type: str
        """

        self._live_source_id = live_source_id

    @property
    def live_source_ids(self):
        """Gets the live_source_ids of this SourceDocumentExcludeSearchCommand.  # noqa: E501


        :return: The live_source_ids of this SourceDocumentExcludeSearchCommand.  # noqa: E501
        :rtype: list[str]
        """
        return self._live_source_ids

    @live_source_ids.setter
    def live_source_ids(self, live_source_ids):
        """Sets the live_source_ids of this SourceDocumentExcludeSearchCommand.


        :param live_source_ids: The live_source_ids of this SourceDocumentExcludeSearchCommand.  # noqa: E501
        :type: list[str]
        """

        self._live_source_ids = live_source_ids

    @property
    def live_source_types(self):
        """Gets the live_source_types of this SourceDocumentExcludeSearchCommand.  # noqa: E501


        :return: The live_source_types of this SourceDocumentExcludeSearchCommand.  # noqa: E501
        :rtype: list[LiveSourceType]
        """
        return self._live_source_types

    @live_source_types.setter
    def live_source_types(self, live_source_types):
        """Sets the live_source_types of this SourceDocumentExcludeSearchCommand.


        :param live_source_types: The live_source_types of this SourceDocumentExcludeSearchCommand.  # noqa: E501
        :type: list[LiveSourceType]
        """

        self._live_source_types = live_source_types

    @property
    def log_search(self):
        """Gets the log_search of this SourceDocumentExcludeSearchCommand.  # noqa: E501


        :return: The log_search of this SourceDocumentExcludeSearchCommand.  # noqa: E501
        :rtype: bool
        """
        return self._log_search

    @log_search.setter
    def log_search(self, log_search):
        """Sets the log_search of this SourceDocumentExcludeSearchCommand.


        :param log_search: The log_search of this SourceDocumentExcludeSearchCommand.  # noqa: E501
        :type: bool
        """

        self._log_search = log_search

    @property
    def mime_types(self):
        """Gets the mime_types of this SourceDocumentExcludeSearchCommand.  # noqa: E501


        :return: The mime_types of this SourceDocumentExcludeSearchCommand.  # noqa: E501
        :rtype: list[str]
        """
        return self._mime_types

    @mime_types.setter
    def mime_types(self, mime_types):
        """Sets the mime_types of this SourceDocumentExcludeSearchCommand.


        :param mime_types: The mime_types of this SourceDocumentExcludeSearchCommand.  # noqa: E501
        :type: list[str]
        """

        self._mime_types = mime_types

    @property
    def must_have_annotations(self):
        """Gets the must_have_annotations of this SourceDocumentExcludeSearchCommand.  # noqa: E501


        :return: The must_have_annotations of this SourceDocumentExcludeSearchCommand.  # noqa: E501
        :rtype: bool
        """
        return self._must_have_annotations

    @must_have_annotations.setter
    def must_have_annotations(self, must_have_annotations):
        """Sets the must_have_annotations of this SourceDocumentExcludeSearchCommand.


        :param must_have_annotations: The must_have_annotations of this SourceDocumentExcludeSearchCommand.  # noqa: E501
        :type: bool
        """

        self._must_have_annotations = must_have_annotations

    @property
    def named_entities(self):
        """Gets the named_entities of this SourceDocumentExcludeSearchCommand.  # noqa: E501


        :return: The named_entities of this SourceDocumentExcludeSearchCommand.  # noqa: E501
        :rtype: list[NamedEntity]
        """
        return self._named_entities

    @named_entities.setter
    def named_entities(self, named_entities):
        """Sets the named_entities of this SourceDocumentExcludeSearchCommand.


        :param named_entities: The named_entities of this SourceDocumentExcludeSearchCommand.  # noqa: E501
        :type: list[NamedEntity]
        """

        self._named_entities = named_entities

    @property
    def parent_ids(self):
        """Gets the parent_ids of this SourceDocumentExcludeSearchCommand.  # noqa: E501


        :return: The parent_ids of this SourceDocumentExcludeSearchCommand.  # noqa: E501
        :rtype: list[str]
        """
        return self._parent_ids

    @parent_ids.setter
    def parent_ids(self, parent_ids):
        """Sets the parent_ids of this SourceDocumentExcludeSearchCommand.


        :param parent_ids: The parent_ids of this SourceDocumentExcludeSearchCommand.  # noqa: E501
        :type: list[str]
        """

        self._parent_ids = parent_ids

    @property
    def paths(self):
        """Gets the paths of this SourceDocumentExcludeSearchCommand.  # noqa: E501


        :return: The paths of this SourceDocumentExcludeSearchCommand.  # noqa: E501
        :rtype: list[str]
        """
        return self._paths

    @paths.setter
    def paths(self, paths):
        """Sets the paths of this SourceDocumentExcludeSearchCommand.


        :param paths: The paths of this SourceDocumentExcludeSearchCommand.  # noqa: E501
        :type: list[str]
        """

        self._paths = paths

    @property
    def project_computation_id(self):
        """Gets the project_computation_id of this SourceDocumentExcludeSearchCommand.  # noqa: E501


        :return: The project_computation_id of this SourceDocumentExcludeSearchCommand.  # noqa: E501
        :rtype: str
        """
        return self._project_computation_id

    @project_computation_id.setter
    def project_computation_id(self, project_computation_id):
        """Sets the project_computation_id of this SourceDocumentExcludeSearchCommand.


        :param project_computation_id: The project_computation_id of this SourceDocumentExcludeSearchCommand.  # noqa: E501
        :type: str
        """

        self._project_computation_id = project_computation_id

    @property
    def question(self):
        """Gets the question of this SourceDocumentExcludeSearchCommand.  # noqa: E501


        :return: The question of this SourceDocumentExcludeSearchCommand.  # noqa: E501
        :rtype: str
        """
        return self._question

    @question.setter
    def question(self, question):
        """Sets the question of this SourceDocumentExcludeSearchCommand.


        :param question: The question of this SourceDocumentExcludeSearchCommand.  # noqa: E501
        :type: str
        """

        self._question = question

    @property
    def saved_list_ids(self):
        """Gets the saved_list_ids of this SourceDocumentExcludeSearchCommand.  # noqa: E501


        :return: The saved_list_ids of this SourceDocumentExcludeSearchCommand.  # noqa: E501
        :rtype: list[str]
        """
        return self._saved_list_ids

    @saved_list_ids.setter
    def saved_list_ids(self, saved_list_ids):
        """Sets the saved_list_ids of this SourceDocumentExcludeSearchCommand.


        :param saved_list_ids: The saved_list_ids of this SourceDocumentExcludeSearchCommand.  # noqa: E501
        :type: list[str]
        """

        self._saved_list_ids = saved_list_ids

    @property
    def section_searches(self):
        """Gets the section_searches of this SourceDocumentExcludeSearchCommand.  # noqa: E501


        :return: The section_searches of this SourceDocumentExcludeSearchCommand.  # noqa: E501
        :rtype: list[SectionSearch]
        """
        return self._section_searches

    @section_searches.setter
    def section_searches(self, section_searches):
        """Sets the section_searches of this SourceDocumentExcludeSearchCommand.


        :param section_searches: The section_searches of this SourceDocumentExcludeSearchCommand.  # noqa: E501
        :type: list[SectionSearch]
        """

        self._section_searches = section_searches

    @property
    def similarity_document_id(self):
        """Gets the similarity_document_id of this SourceDocumentExcludeSearchCommand.  # noqa: E501


        :return: The similarity_document_id of this SourceDocumentExcludeSearchCommand.  # noqa: E501
        :rtype: str
        """
        return self._similarity_document_id

    @similarity_document_id.setter
    def similarity_document_id(self, similarity_document_id):
        """Sets the similarity_document_id of this SourceDocumentExcludeSearchCommand.


        :param similarity_document_id: The similarity_document_id of this SourceDocumentExcludeSearchCommand.  # noqa: E501
        :type: str
        """

        self._similarity_document_id = similarity_document_id

    @property
    def similarity_threshold(self):
        """Gets the similarity_threshold of this SourceDocumentExcludeSearchCommand.  # noqa: E501


        :return: The similarity_threshold of this SourceDocumentExcludeSearchCommand.  # noqa: E501
        :rtype: float
        """
        return self._similarity_threshold

    @similarity_threshold.setter
    def similarity_threshold(self, similarity_threshold):
        """Sets the similarity_threshold of this SourceDocumentExcludeSearchCommand.


        :param similarity_threshold: The similarity_threshold of this SourceDocumentExcludeSearchCommand.  # noqa: E501
        :type: float
        """

        self._similarity_threshold = similarity_threshold

    @property
    def source_fields(self):
        """Gets the source_fields of this SourceDocumentExcludeSearchCommand.  # noqa: E501


        :return: The source_fields of this SourceDocumentExcludeSearchCommand.  # noqa: E501
        :rtype: list[str]
        """
        return self._source_fields

    @source_fields.setter
    def source_fields(self, source_fields):
        """Sets the source_fields of this SourceDocumentExcludeSearchCommand.


        :param source_fields: The source_fields of this SourceDocumentExcludeSearchCommand.  # noqa: E501
        :type: list[str]
        """

        self._source_fields = source_fields

    @property
    def sources(self):
        """Gets the sources of this SourceDocumentExcludeSearchCommand.  # noqa: E501


        :return: The sources of this SourceDocumentExcludeSearchCommand.  # noqa: E501
        :rtype: list[str]
        """
        return self._sources

    @sources.setter
    def sources(self, sources):
        """Sets the sources of this SourceDocumentExcludeSearchCommand.


        :param sources: The sources of this SourceDocumentExcludeSearchCommand.  # noqa: E501
        :type: list[str]
        """

        self._sources = sources

    @property
    def term_operator(self):
        """Gets the term_operator of this SourceDocumentExcludeSearchCommand.  # noqa: E501


        :return: The term_operator of this SourceDocumentExcludeSearchCommand.  # noqa: E501
        :rtype: str
        """
        return self._term_operator

    @term_operator.setter
    def term_operator(self, term_operator):
        """Sets the term_operator of this SourceDocumentExcludeSearchCommand.


        :param term_operator: The term_operator of this SourceDocumentExcludeSearchCommand.  # noqa: E501
        :type: str
        """
        allowed_values = ["AND", "OR"]  # noqa: E501
        if term_operator not in allowed_values:
            raise ValueError(
                "Invalid value for `term_operator` ({0}), must be one of {1}"  # noqa: E501
                .format(term_operator, allowed_values)
            )

        self._term_operator = term_operator

    @property
    def terms(self):
        """Gets the terms of this SourceDocumentExcludeSearchCommand.  # noqa: E501


        :return: The terms of this SourceDocumentExcludeSearchCommand.  # noqa: E501
        :rtype: list[str]
        """
        return self._terms

    @terms.setter
    def terms(self, terms):
        """Sets the terms of this SourceDocumentExcludeSearchCommand.


        :param terms: The terms of this SourceDocumentExcludeSearchCommand.  # noqa: E501
        :type: list[str]
        """

        self._terms = terms

    @property
    def trial_data(self):
        """Gets the trial_data of this SourceDocumentExcludeSearchCommand.  # noqa: E501


        :return: The trial_data of this SourceDocumentExcludeSearchCommand.  # noqa: E501
        :rtype: object
        """
        return self._trial_data

    @trial_data.setter
    def trial_data(self, trial_data):
        """Sets the trial_data of this SourceDocumentExcludeSearchCommand.


        :param trial_data: The trial_data of this SourceDocumentExcludeSearchCommand.  # noqa: E501
        :type: object
        """

        self._trial_data = trial_data

    @property
    def type(self):
        """Gets the type of this SourceDocumentExcludeSearchCommand.  # noqa: E501


        :return: The type of this SourceDocumentExcludeSearchCommand.  # noqa: E501
        :rtype: SourceDocumentType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this SourceDocumentExcludeSearchCommand.


        :param type: The type of this SourceDocumentExcludeSearchCommand.  # noqa: E501
        :type: SourceDocumentType
        """

        self._type = type

    @property
    def types(self):
        """Gets the types of this SourceDocumentExcludeSearchCommand.  # noqa: E501


        :return: The types of this SourceDocumentExcludeSearchCommand.  # noqa: E501
        :rtype: list[SourceDocumentType]
        """
        return self._types

    @types.setter
    def types(self, types):
        """Sets the types of this SourceDocumentExcludeSearchCommand.


        :param types: The types of this SourceDocumentExcludeSearchCommand.  # noqa: E501
        :type: list[SourceDocumentType]
        """

        self._types = types

    @property
    def user_ids(self):
        """Gets the user_ids of this SourceDocumentExcludeSearchCommand.  # noqa: E501


        :return: The user_ids of this SourceDocumentExcludeSearchCommand.  # noqa: E501
        :rtype: list[int]
        """
        return self._user_ids

    @user_ids.setter
    def user_ids(self, user_ids):
        """Sets the user_ids of this SourceDocumentExcludeSearchCommand.


        :param user_ids: The user_ids of this SourceDocumentExcludeSearchCommand.  # noqa: E501
        :type: list[int]
        """

        self._user_ids = user_ids

    @property
    def vyasa_clients(self):
        """Gets the vyasa_clients of this SourceDocumentExcludeSearchCommand.  # noqa: E501


        :return: The vyasa_clients of this SourceDocumentExcludeSearchCommand.  # noqa: E501
        :rtype: list[str]
        """
        return self._vyasa_clients

    @vyasa_clients.setter
    def vyasa_clients(self, vyasa_clients):
        """Sets the vyasa_clients of this SourceDocumentExcludeSearchCommand.


        :param vyasa_clients: The vyasa_clients of this SourceDocumentExcludeSearchCommand.  # noqa: E501
        :type: list[str]
        """

        self._vyasa_clients = vyasa_clients

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(SourceDocumentExcludeSearchCommand, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, SourceDocumentExcludeSearchCommand):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
