# coding: utf-8

"""
    Layar API Documentation

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class AnswerEvidence(object):
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
        'answer_ranking_score': 'float',
        'context': 'str',
        'document_id': 'str',
        'document_uri': 'str',
        'end_offset': 'float',
        'name': 'str',
        'named_entities': 'list[NamedEntity]',
        'passage_ranking_score': 'float',
        'probability': 'float',
        'provider': 'str',
        'start_offset': 'float',
        'whole_document_end_offset': 'float',
        'whole_document_start_offset': 'float'
    }

    attribute_map = {
        'answer_ranking_score': 'answerRankingScore',
        'context': 'context',
        'document_id': 'documentId',
        'document_uri': 'documentURI',
        'end_offset': 'endOffset',
        'name': 'name',
        'named_entities': 'namedEntities',
        'passage_ranking_score': 'passageRankingScore',
        'probability': 'probability',
        'provider': 'provider',
        'start_offset': 'startOffset',
        'whole_document_end_offset': 'wholeDocumentEndOffset',
        'whole_document_start_offset': 'wholeDocumentStartOffset'
    }

    def __init__(self, answer_ranking_score=None, context=None, document_id=None, document_uri=None, end_offset=None, name=None, named_entities=None, passage_ranking_score=None, probability=None, provider=None, start_offset=None, whole_document_end_offset=None, whole_document_start_offset=None):  # noqa: E501
        """AnswerEvidence - a model defined in Swagger"""  # noqa: E501
        self._answer_ranking_score = None
        self._context = None
        self._document_id = None
        self._document_uri = None
        self._end_offset = None
        self._name = None
        self._named_entities = None
        self._passage_ranking_score = None
        self._probability = None
        self._provider = None
        self._start_offset = None
        self._whole_document_end_offset = None
        self._whole_document_start_offset = None
        self.discriminator = None
        if answer_ranking_score is not None:
            self.answer_ranking_score = answer_ranking_score
        if context is not None:
            self.context = context
        if document_id is not None:
            self.document_id = document_id
        if document_uri is not None:
            self.document_uri = document_uri
        if end_offset is not None:
            self.end_offset = end_offset
        if name is not None:
            self.name = name
        if named_entities is not None:
            self.named_entities = named_entities
        if passage_ranking_score is not None:
            self.passage_ranking_score = passage_ranking_score
        if probability is not None:
            self.probability = probability
        if provider is not None:
            self.provider = provider
        if start_offset is not None:
            self.start_offset = start_offset
        if whole_document_end_offset is not None:
            self.whole_document_end_offset = whole_document_end_offset
        if whole_document_start_offset is not None:
            self.whole_document_start_offset = whole_document_start_offset

    @property
    def answer_ranking_score(self):
        """Gets the answer_ranking_score of this AnswerEvidence.  # noqa: E501


        :return: The answer_ranking_score of this AnswerEvidence.  # noqa: E501
        :rtype: float
        """
        return self._answer_ranking_score

    @answer_ranking_score.setter
    def answer_ranking_score(self, answer_ranking_score):
        """Sets the answer_ranking_score of this AnswerEvidence.


        :param answer_ranking_score: The answer_ranking_score of this AnswerEvidence.  # noqa: E501
        :type: float
        """

        self._answer_ranking_score = answer_ranking_score

    @property
    def context(self):
        """Gets the context of this AnswerEvidence.  # noqa: E501


        :return: The context of this AnswerEvidence.  # noqa: E501
        :rtype: str
        """
        return self._context

    @context.setter
    def context(self, context):
        """Sets the context of this AnswerEvidence.


        :param context: The context of this AnswerEvidence.  # noqa: E501
        :type: str
        """

        self._context = context

    @property
    def document_id(self):
        """Gets the document_id of this AnswerEvidence.  # noqa: E501


        :return: The document_id of this AnswerEvidence.  # noqa: E501
        :rtype: str
        """
        return self._document_id

    @document_id.setter
    def document_id(self, document_id):
        """Sets the document_id of this AnswerEvidence.


        :param document_id: The document_id of this AnswerEvidence.  # noqa: E501
        :type: str
        """

        self._document_id = document_id

    @property
    def document_uri(self):
        """Gets the document_uri of this AnswerEvidence.  # noqa: E501


        :return: The document_uri of this AnswerEvidence.  # noqa: E501
        :rtype: str
        """
        return self._document_uri

    @document_uri.setter
    def document_uri(self, document_uri):
        """Sets the document_uri of this AnswerEvidence.


        :param document_uri: The document_uri of this AnswerEvidence.  # noqa: E501
        :type: str
        """

        self._document_uri = document_uri

    @property
    def end_offset(self):
        """Gets the end_offset of this AnswerEvidence.  # noqa: E501


        :return: The end_offset of this AnswerEvidence.  # noqa: E501
        :rtype: float
        """
        return self._end_offset

    @end_offset.setter
    def end_offset(self, end_offset):
        """Sets the end_offset of this AnswerEvidence.


        :param end_offset: The end_offset of this AnswerEvidence.  # noqa: E501
        :type: float
        """

        self._end_offset = end_offset

    @property
    def name(self):
        """Gets the name of this AnswerEvidence.  # noqa: E501


        :return: The name of this AnswerEvidence.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AnswerEvidence.


        :param name: The name of this AnswerEvidence.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def named_entities(self):
        """Gets the named_entities of this AnswerEvidence.  # noqa: E501


        :return: The named_entities of this AnswerEvidence.  # noqa: E501
        :rtype: list[NamedEntity]
        """
        return self._named_entities

    @named_entities.setter
    def named_entities(self, named_entities):
        """Sets the named_entities of this AnswerEvidence.


        :param named_entities: The named_entities of this AnswerEvidence.  # noqa: E501
        :type: list[NamedEntity]
        """

        self._named_entities = named_entities

    @property
    def passage_ranking_score(self):
        """Gets the passage_ranking_score of this AnswerEvidence.  # noqa: E501


        :return: The passage_ranking_score of this AnswerEvidence.  # noqa: E501
        :rtype: float
        """
        return self._passage_ranking_score

    @passage_ranking_score.setter
    def passage_ranking_score(self, passage_ranking_score):
        """Sets the passage_ranking_score of this AnswerEvidence.


        :param passage_ranking_score: The passage_ranking_score of this AnswerEvidence.  # noqa: E501
        :type: float
        """

        self._passage_ranking_score = passage_ranking_score

    @property
    def probability(self):
        """Gets the probability of this AnswerEvidence.  # noqa: E501


        :return: The probability of this AnswerEvidence.  # noqa: E501
        :rtype: float
        """
        return self._probability

    @probability.setter
    def probability(self, probability):
        """Sets the probability of this AnswerEvidence.


        :param probability: The probability of this AnswerEvidence.  # noqa: E501
        :type: float
        """

        self._probability = probability

    @property
    def provider(self):
        """Gets the provider of this AnswerEvidence.  # noqa: E501


        :return: The provider of this AnswerEvidence.  # noqa: E501
        :rtype: str
        """
        return self._provider

    @provider.setter
    def provider(self, provider):
        """Sets the provider of this AnswerEvidence.


        :param provider: The provider of this AnswerEvidence.  # noqa: E501
        :type: str
        """

        self._provider = provider

    @property
    def start_offset(self):
        """Gets the start_offset of this AnswerEvidence.  # noqa: E501


        :return: The start_offset of this AnswerEvidence.  # noqa: E501
        :rtype: float
        """
        return self._start_offset

    @start_offset.setter
    def start_offset(self, start_offset):
        """Sets the start_offset of this AnswerEvidence.


        :param start_offset: The start_offset of this AnswerEvidence.  # noqa: E501
        :type: float
        """

        self._start_offset = start_offset

    @property
    def whole_document_end_offset(self):
        """Gets the whole_document_end_offset of this AnswerEvidence.  # noqa: E501


        :return: The whole_document_end_offset of this AnswerEvidence.  # noqa: E501
        :rtype: float
        """
        return self._whole_document_end_offset

    @whole_document_end_offset.setter
    def whole_document_end_offset(self, whole_document_end_offset):
        """Sets the whole_document_end_offset of this AnswerEvidence.


        :param whole_document_end_offset: The whole_document_end_offset of this AnswerEvidence.  # noqa: E501
        :type: float
        """

        self._whole_document_end_offset = whole_document_end_offset

    @property
    def whole_document_start_offset(self):
        """Gets the whole_document_start_offset of this AnswerEvidence.  # noqa: E501


        :return: The whole_document_start_offset of this AnswerEvidence.  # noqa: E501
        :rtype: float
        """
        return self._whole_document_start_offset

    @whole_document_start_offset.setter
    def whole_document_start_offset(self, whole_document_start_offset):
        """Sets the whole_document_start_offset of this AnswerEvidence.


        :param whole_document_start_offset: The whole_document_start_offset of this AnswerEvidence.  # noqa: E501
        :type: float
        """

        self._whole_document_start_offset = whole_document_start_offset

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
        if issubclass(AnswerEvidence, dict):
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
        if not isinstance(other, AnswerEvidence):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
