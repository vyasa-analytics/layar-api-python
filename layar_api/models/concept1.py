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

class Concept1(object):
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
        'assignments': 'list[str]',
        'column_definitions': 'list[ColumnDefinition]',
        'columns': 'object',
        'concept_name_query_term_vector_similarity': 'dict(str, float)',
        'concept_source': 'str',
        'concept_type': 'ConceptType',
        'concept_type_id': 'str',
        'concept_vector': 'list[float]',
        'cortex_relevance_score': 'float',
        'cross_query_counts': 'dict(str, int)',
        'date_updated': 'datetime',
        'document_id': 'str',
        'external_ids': 'object',
        'is_primary_synonym': 'bool',
        'name': 'str',
        'saved_lists': 'list[str]',
        'source_count': 'int',
        'statement_count': 'int',
        'suggested_concept_type': 'ConceptType',
        'suggested_concept_type_id': 'str',
        'suggested_concept_type_rankings': 'object',
        'synonym_of_id': 'str',
        'synonym_source_count': 'int',
        'synonym_statement_count': 'int'
    }

    attribute_map = {
        'assignments': 'assignments',
        'column_definitions': 'columnDefinitions',
        'columns': 'columns',
        'concept_name_query_term_vector_similarity': 'conceptNameQueryTermVectorSimilarity',
        'concept_source': 'conceptSource',
        'concept_type': 'conceptType',
        'concept_type_id': 'conceptTypeId',
        'concept_vector': 'conceptVector',
        'cortex_relevance_score': 'cortexRelevanceScore',
        'cross_query_counts': 'crossQueryCounts',
        'date_updated': 'dateUpdated',
        'document_id': 'documentId',
        'external_ids': 'externalIds',
        'is_primary_synonym': 'isPrimarySynonym',
        'name': 'name',
        'saved_lists': 'savedLists',
        'source_count': 'sourceCount',
        'statement_count': 'statementCount',
        'suggested_concept_type': 'suggestedConceptType',
        'suggested_concept_type_id': 'suggestedConceptTypeId',
        'suggested_concept_type_rankings': 'suggestedConceptTypeRankings',
        'synonym_of_id': 'synonymOfId',
        'synonym_source_count': 'synonymSourceCount',
        'synonym_statement_count': 'synonymStatementCount'
    }

    def __init__(self, assignments=None, column_definitions=None, columns=None, concept_name_query_term_vector_similarity=None, concept_source=None, concept_type=None, concept_type_id=None, concept_vector=None, cortex_relevance_score=None, cross_query_counts=None, date_updated=None, document_id=None, external_ids=None, is_primary_synonym=None, name=None, saved_lists=None, source_count=None, statement_count=None, suggested_concept_type=None, suggested_concept_type_id=None, suggested_concept_type_rankings=None, synonym_of_id=None, synonym_source_count=None, synonym_statement_count=None):  # noqa: E501
        """Concept1 - a model defined in Swagger"""  # noqa: E501
        self._assignments = None
        self._column_definitions = None
        self._columns = None
        self._concept_name_query_term_vector_similarity = None
        self._concept_source = None
        self._concept_type = None
        self._concept_type_id = None
        self._concept_vector = None
        self._cortex_relevance_score = None
        self._cross_query_counts = None
        self._date_updated = None
        self._document_id = None
        self._external_ids = None
        self._is_primary_synonym = None
        self._name = None
        self._saved_lists = None
        self._source_count = None
        self._statement_count = None
        self._suggested_concept_type = None
        self._suggested_concept_type_id = None
        self._suggested_concept_type_rankings = None
        self._synonym_of_id = None
        self._synonym_source_count = None
        self._synonym_statement_count = None
        self.discriminator = None
        if assignments is not None:
            self.assignments = assignments
        if column_definitions is not None:
            self.column_definitions = column_definitions
        if columns is not None:
            self.columns = columns
        if concept_name_query_term_vector_similarity is not None:
            self.concept_name_query_term_vector_similarity = concept_name_query_term_vector_similarity
        if concept_source is not None:
            self.concept_source = concept_source
        if concept_type is not None:
            self.concept_type = concept_type
        if concept_type_id is not None:
            self.concept_type_id = concept_type_id
        if concept_vector is not None:
            self.concept_vector = concept_vector
        if cortex_relevance_score is not None:
            self.cortex_relevance_score = cortex_relevance_score
        if cross_query_counts is not None:
            self.cross_query_counts = cross_query_counts
        if date_updated is not None:
            self.date_updated = date_updated
        if document_id is not None:
            self.document_id = document_id
        if external_ids is not None:
            self.external_ids = external_ids
        if is_primary_synonym is not None:
            self.is_primary_synonym = is_primary_synonym
        if name is not None:
            self.name = name
        if saved_lists is not None:
            self.saved_lists = saved_lists
        if source_count is not None:
            self.source_count = source_count
        if statement_count is not None:
            self.statement_count = statement_count
        if suggested_concept_type is not None:
            self.suggested_concept_type = suggested_concept_type
        if suggested_concept_type_id is not None:
            self.suggested_concept_type_id = suggested_concept_type_id
        if suggested_concept_type_rankings is not None:
            self.suggested_concept_type_rankings = suggested_concept_type_rankings
        if synonym_of_id is not None:
            self.synonym_of_id = synonym_of_id
        if synonym_source_count is not None:
            self.synonym_source_count = synonym_source_count
        if synonym_statement_count is not None:
            self.synonym_statement_count = synonym_statement_count

    @property
    def assignments(self):
        """Gets the assignments of this Concept1.  # noqa: E501


        :return: The assignments of this Concept1.  # noqa: E501
        :rtype: list[str]
        """
        return self._assignments

    @assignments.setter
    def assignments(self, assignments):
        """Sets the assignments of this Concept1.


        :param assignments: The assignments of this Concept1.  # noqa: E501
        :type: list[str]
        """

        self._assignments = assignments

    @property
    def column_definitions(self):
        """Gets the column_definitions of this Concept1.  # noqa: E501


        :return: The column_definitions of this Concept1.  # noqa: E501
        :rtype: list[ColumnDefinition]
        """
        return self._column_definitions

    @column_definitions.setter
    def column_definitions(self, column_definitions):
        """Sets the column_definitions of this Concept1.


        :param column_definitions: The column_definitions of this Concept1.  # noqa: E501
        :type: list[ColumnDefinition]
        """

        self._column_definitions = column_definitions

    @property
    def columns(self):
        """Gets the columns of this Concept1.  # noqa: E501


        :return: The columns of this Concept1.  # noqa: E501
        :rtype: object
        """
        return self._columns

    @columns.setter
    def columns(self, columns):
        """Sets the columns of this Concept1.


        :param columns: The columns of this Concept1.  # noqa: E501
        :type: object
        """

        self._columns = columns

    @property
    def concept_name_query_term_vector_similarity(self):
        """Gets the concept_name_query_term_vector_similarity of this Concept1.  # noqa: E501


        :return: The concept_name_query_term_vector_similarity of this Concept1.  # noqa: E501
        :rtype: dict(str, float)
        """
        return self._concept_name_query_term_vector_similarity

    @concept_name_query_term_vector_similarity.setter
    def concept_name_query_term_vector_similarity(self, concept_name_query_term_vector_similarity):
        """Sets the concept_name_query_term_vector_similarity of this Concept1.


        :param concept_name_query_term_vector_similarity: The concept_name_query_term_vector_similarity of this Concept1.  # noqa: E501
        :type: dict(str, float)
        """

        self._concept_name_query_term_vector_similarity = concept_name_query_term_vector_similarity

    @property
    def concept_source(self):
        """Gets the concept_source of this Concept1.  # noqa: E501


        :return: The concept_source of this Concept1.  # noqa: E501
        :rtype: str
        """
        return self._concept_source

    @concept_source.setter
    def concept_source(self, concept_source):
        """Sets the concept_source of this Concept1.


        :param concept_source: The concept_source of this Concept1.  # noqa: E501
        :type: str
        """
        allowed_values = ["USER_DEFINED", "FAST_TEXT", "LEVENSHTEIN_DISTANCE", "WIKIDATA", "NEAREST_NEIGHBOR"]  # noqa: E501
        if concept_source not in allowed_values:
            raise ValueError(
                "Invalid value for `concept_source` ({0}), must be one of {1}"  # noqa: E501
                .format(concept_source, allowed_values)
            )

        self._concept_source = concept_source

    @property
    def concept_type(self):
        """Gets the concept_type of this Concept1.  # noqa: E501


        :return: The concept_type of this Concept1.  # noqa: E501
        :rtype: ConceptType
        """
        return self._concept_type

    @concept_type.setter
    def concept_type(self, concept_type):
        """Sets the concept_type of this Concept1.


        :param concept_type: The concept_type of this Concept1.  # noqa: E501
        :type: ConceptType
        """

        self._concept_type = concept_type

    @property
    def concept_type_id(self):
        """Gets the concept_type_id of this Concept1.  # noqa: E501


        :return: The concept_type_id of this Concept1.  # noqa: E501
        :rtype: str
        """
        return self._concept_type_id

    @concept_type_id.setter
    def concept_type_id(self, concept_type_id):
        """Sets the concept_type_id of this Concept1.


        :param concept_type_id: The concept_type_id of this Concept1.  # noqa: E501
        :type: str
        """

        self._concept_type_id = concept_type_id

    @property
    def concept_vector(self):
        """Gets the concept_vector of this Concept1.  # noqa: E501


        :return: The concept_vector of this Concept1.  # noqa: E501
        :rtype: list[float]
        """
        return self._concept_vector

    @concept_vector.setter
    def concept_vector(self, concept_vector):
        """Sets the concept_vector of this Concept1.


        :param concept_vector: The concept_vector of this Concept1.  # noqa: E501
        :type: list[float]
        """

        self._concept_vector = concept_vector

    @property
    def cortex_relevance_score(self):
        """Gets the cortex_relevance_score of this Concept1.  # noqa: E501


        :return: The cortex_relevance_score of this Concept1.  # noqa: E501
        :rtype: float
        """
        return self._cortex_relevance_score

    @cortex_relevance_score.setter
    def cortex_relevance_score(self, cortex_relevance_score):
        """Sets the cortex_relevance_score of this Concept1.


        :param cortex_relevance_score: The cortex_relevance_score of this Concept1.  # noqa: E501
        :type: float
        """

        self._cortex_relevance_score = cortex_relevance_score

    @property
    def cross_query_counts(self):
        """Gets the cross_query_counts of this Concept1.  # noqa: E501


        :return: The cross_query_counts of this Concept1.  # noqa: E501
        :rtype: dict(str, int)
        """
        return self._cross_query_counts

    @cross_query_counts.setter
    def cross_query_counts(self, cross_query_counts):
        """Sets the cross_query_counts of this Concept1.


        :param cross_query_counts: The cross_query_counts of this Concept1.  # noqa: E501
        :type: dict(str, int)
        """

        self._cross_query_counts = cross_query_counts

    @property
    def date_updated(self):
        """Gets the date_updated of this Concept1.  # noqa: E501


        :return: The date_updated of this Concept1.  # noqa: E501
        :rtype: datetime
        """
        return self._date_updated

    @date_updated.setter
    def date_updated(self, date_updated):
        """Sets the date_updated of this Concept1.


        :param date_updated: The date_updated of this Concept1.  # noqa: E501
        :type: datetime
        """

        self._date_updated = date_updated

    @property
    def document_id(self):
        """Gets the document_id of this Concept1.  # noqa: E501


        :return: The document_id of this Concept1.  # noqa: E501
        :rtype: str
        """
        return self._document_id

    @document_id.setter
    def document_id(self, document_id):
        """Sets the document_id of this Concept1.


        :param document_id: The document_id of this Concept1.  # noqa: E501
        :type: str
        """

        self._document_id = document_id

    @property
    def external_ids(self):
        """Gets the external_ids of this Concept1.  # noqa: E501


        :return: The external_ids of this Concept1.  # noqa: E501
        :rtype: object
        """
        return self._external_ids

    @external_ids.setter
    def external_ids(self, external_ids):
        """Sets the external_ids of this Concept1.


        :param external_ids: The external_ids of this Concept1.  # noqa: E501
        :type: object
        """

        self._external_ids = external_ids

    @property
    def is_primary_synonym(self):
        """Gets the is_primary_synonym of this Concept1.  # noqa: E501


        :return: The is_primary_synonym of this Concept1.  # noqa: E501
        :rtype: bool
        """
        return self._is_primary_synonym

    @is_primary_synonym.setter
    def is_primary_synonym(self, is_primary_synonym):
        """Sets the is_primary_synonym of this Concept1.


        :param is_primary_synonym: The is_primary_synonym of this Concept1.  # noqa: E501
        :type: bool
        """

        self._is_primary_synonym = is_primary_synonym

    @property
    def name(self):
        """Gets the name of this Concept1.  # noqa: E501


        :return: The name of this Concept1.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Concept1.


        :param name: The name of this Concept1.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def saved_lists(self):
        """Gets the saved_lists of this Concept1.  # noqa: E501


        :return: The saved_lists of this Concept1.  # noqa: E501
        :rtype: list[str]
        """
        return self._saved_lists

    @saved_lists.setter
    def saved_lists(self, saved_lists):
        """Sets the saved_lists of this Concept1.


        :param saved_lists: The saved_lists of this Concept1.  # noqa: E501
        :type: list[str]
        """

        self._saved_lists = saved_lists

    @property
    def source_count(self):
        """Gets the source_count of this Concept1.  # noqa: E501


        :return: The source_count of this Concept1.  # noqa: E501
        :rtype: int
        """
        return self._source_count

    @source_count.setter
    def source_count(self, source_count):
        """Sets the source_count of this Concept1.


        :param source_count: The source_count of this Concept1.  # noqa: E501
        :type: int
        """

        self._source_count = source_count

    @property
    def statement_count(self):
        """Gets the statement_count of this Concept1.  # noqa: E501


        :return: The statement_count of this Concept1.  # noqa: E501
        :rtype: int
        """
        return self._statement_count

    @statement_count.setter
    def statement_count(self, statement_count):
        """Sets the statement_count of this Concept1.


        :param statement_count: The statement_count of this Concept1.  # noqa: E501
        :type: int
        """

        self._statement_count = statement_count

    @property
    def suggested_concept_type(self):
        """Gets the suggested_concept_type of this Concept1.  # noqa: E501


        :return: The suggested_concept_type of this Concept1.  # noqa: E501
        :rtype: ConceptType
        """
        return self._suggested_concept_type

    @suggested_concept_type.setter
    def suggested_concept_type(self, suggested_concept_type):
        """Sets the suggested_concept_type of this Concept1.


        :param suggested_concept_type: The suggested_concept_type of this Concept1.  # noqa: E501
        :type: ConceptType
        """

        self._suggested_concept_type = suggested_concept_type

    @property
    def suggested_concept_type_id(self):
        """Gets the suggested_concept_type_id of this Concept1.  # noqa: E501


        :return: The suggested_concept_type_id of this Concept1.  # noqa: E501
        :rtype: str
        """
        return self._suggested_concept_type_id

    @suggested_concept_type_id.setter
    def suggested_concept_type_id(self, suggested_concept_type_id):
        """Sets the suggested_concept_type_id of this Concept1.


        :param suggested_concept_type_id: The suggested_concept_type_id of this Concept1.  # noqa: E501
        :type: str
        """

        self._suggested_concept_type_id = suggested_concept_type_id

    @property
    def suggested_concept_type_rankings(self):
        """Gets the suggested_concept_type_rankings of this Concept1.  # noqa: E501


        :return: The suggested_concept_type_rankings of this Concept1.  # noqa: E501
        :rtype: object
        """
        return self._suggested_concept_type_rankings

    @suggested_concept_type_rankings.setter
    def suggested_concept_type_rankings(self, suggested_concept_type_rankings):
        """Sets the suggested_concept_type_rankings of this Concept1.


        :param suggested_concept_type_rankings: The suggested_concept_type_rankings of this Concept1.  # noqa: E501
        :type: object
        """

        self._suggested_concept_type_rankings = suggested_concept_type_rankings

    @property
    def synonym_of_id(self):
        """Gets the synonym_of_id of this Concept1.  # noqa: E501


        :return: The synonym_of_id of this Concept1.  # noqa: E501
        :rtype: str
        """
        return self._synonym_of_id

    @synonym_of_id.setter
    def synonym_of_id(self, synonym_of_id):
        """Sets the synonym_of_id of this Concept1.


        :param synonym_of_id: The synonym_of_id of this Concept1.  # noqa: E501
        :type: str
        """

        self._synonym_of_id = synonym_of_id

    @property
    def synonym_source_count(self):
        """Gets the synonym_source_count of this Concept1.  # noqa: E501


        :return: The synonym_source_count of this Concept1.  # noqa: E501
        :rtype: int
        """
        return self._synonym_source_count

    @synonym_source_count.setter
    def synonym_source_count(self, synonym_source_count):
        """Sets the synonym_source_count of this Concept1.


        :param synonym_source_count: The synonym_source_count of this Concept1.  # noqa: E501
        :type: int
        """

        self._synonym_source_count = synonym_source_count

    @property
    def synonym_statement_count(self):
        """Gets the synonym_statement_count of this Concept1.  # noqa: E501


        :return: The synonym_statement_count of this Concept1.  # noqa: E501
        :rtype: int
        """
        return self._synonym_statement_count

    @synonym_statement_count.setter
    def synonym_statement_count(self, synonym_statement_count):
        """Sets the synonym_statement_count of this Concept1.


        :param synonym_statement_count: The synonym_statement_count of this Concept1.  # noqa: E501
        :type: int
        """

        self._synonym_statement_count = synonym_statement_count

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
        if issubclass(Concept1, dict):
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
        if not isinstance(other, Concept1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other