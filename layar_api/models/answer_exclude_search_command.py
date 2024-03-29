# coding: utf-8

"""
    Layar API Documentation

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: VERSION_PLACEHOLDER
    Contact: AI-Support@Certara.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class AnswerExcludeSearchCommand(object):
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
        'batch_grouping_key': 'str',
        'question_ids': 'list[str]',
        'question_key': 'str',
        'rejected': 'bool',
        'show_accepted_first': 'bool',
        'single_doc_question_document_id': 'str',
        'with_concepts': 'bool'
    }

    attribute_map = {
        'batch_grouping_key': 'batchGroupingKey',
        'question_ids': 'questionIds',
        'question_key': 'questionKey',
        'rejected': 'rejected',
        'show_accepted_first': 'showAcceptedFirst',
        'single_doc_question_document_id': 'singleDocQuestionDocumentId',
        'with_concepts': 'withConcepts'
    }

    def __init__(self, batch_grouping_key=None, question_ids=None, question_key=None, rejected=None, show_accepted_first=None, single_doc_question_document_id=None, with_concepts=None):  # noqa: E501
        """AnswerExcludeSearchCommand - a model defined in Swagger"""  # noqa: E501
        self._batch_grouping_key = None
        self._question_ids = None
        self._question_key = None
        self._rejected = None
        self._show_accepted_first = None
        self._single_doc_question_document_id = None
        self._with_concepts = None
        self.discriminator = None
        if batch_grouping_key is not None:
            self.batch_grouping_key = batch_grouping_key
        if question_ids is not None:
            self.question_ids = question_ids
        if question_key is not None:
            self.question_key = question_key
        if rejected is not None:
            self.rejected = rejected
        if show_accepted_first is not None:
            self.show_accepted_first = show_accepted_first
        if single_doc_question_document_id is not None:
            self.single_doc_question_document_id = single_doc_question_document_id
        if with_concepts is not None:
            self.with_concepts = with_concepts

    @property
    def batch_grouping_key(self):
        """Gets the batch_grouping_key of this AnswerExcludeSearchCommand.  # noqa: E501

        limit results to answers from a batch query  # noqa: E501

        :return: The batch_grouping_key of this AnswerExcludeSearchCommand.  # noqa: E501
        :rtype: str
        """
        return self._batch_grouping_key

    @batch_grouping_key.setter
    def batch_grouping_key(self, batch_grouping_key):
        """Sets the batch_grouping_key of this AnswerExcludeSearchCommand.

        limit results to answers from a batch query  # noqa: E501

        :param batch_grouping_key: The batch_grouping_key of this AnswerExcludeSearchCommand.  # noqa: E501
        :type: str
        """

        self._batch_grouping_key = batch_grouping_key

    @property
    def question_ids(self):
        """Gets the question_ids of this AnswerExcludeSearchCommand.  # noqa: E501

        limit results to answers that came from specific questions  # noqa: E501

        :return: The question_ids of this AnswerExcludeSearchCommand.  # noqa: E501
        :rtype: list[str]
        """
        return self._question_ids

    @question_ids.setter
    def question_ids(self, question_ids):
        """Sets the question_ids of this AnswerExcludeSearchCommand.

        limit results to answers that came from specific questions  # noqa: E501

        :param question_ids: The question_ids of this AnswerExcludeSearchCommand.  # noqa: E501
        :type: list[str]
        """

        self._question_ids = question_ids

    @property
    def question_key(self):
        """Gets the question_key of this AnswerExcludeSearchCommand.  # noqa: E501

        limit results to answers with a specific question key  # noqa: E501

        :return: The question_key of this AnswerExcludeSearchCommand.  # noqa: E501
        :rtype: str
        """
        return self._question_key

    @question_key.setter
    def question_key(self, question_key):
        """Sets the question_key of this AnswerExcludeSearchCommand.

        limit results to answers with a specific question key  # noqa: E501

        :param question_key: The question_key of this AnswerExcludeSearchCommand.  # noqa: E501
        :type: str
        """

        self._question_key = question_key

    @property
    def rejected(self):
        """Gets the rejected of this AnswerExcludeSearchCommand.  # noqa: E501

        include results that have been rejected  # noqa: E501

        :return: The rejected of this AnswerExcludeSearchCommand.  # noqa: E501
        :rtype: bool
        """
        return self._rejected

    @rejected.setter
    def rejected(self, rejected):
        """Sets the rejected of this AnswerExcludeSearchCommand.

        include results that have been rejected  # noqa: E501

        :param rejected: The rejected of this AnswerExcludeSearchCommand.  # noqa: E501
        :type: bool
        """

        self._rejected = rejected

    @property
    def show_accepted_first(self):
        """Gets the show_accepted_first of this AnswerExcludeSearchCommand.  # noqa: E501

        order results with accepted answers first  # noqa: E501

        :return: The show_accepted_first of this AnswerExcludeSearchCommand.  # noqa: E501
        :rtype: bool
        """
        return self._show_accepted_first

    @show_accepted_first.setter
    def show_accepted_first(self, show_accepted_first):
        """Sets the show_accepted_first of this AnswerExcludeSearchCommand.

        order results with accepted answers first  # noqa: E501

        :param show_accepted_first: The show_accepted_first of this AnswerExcludeSearchCommand.  # noqa: E501
        :type: bool
        """

        self._show_accepted_first = show_accepted_first

    @property
    def single_doc_question_document_id(self):
        """Gets the single_doc_question_document_id of this AnswerExcludeSearchCommand.  # noqa: E501

        include answers that were asked of a single document  # noqa: E501

        :return: The single_doc_question_document_id of this AnswerExcludeSearchCommand.  # noqa: E501
        :rtype: str
        """
        return self._single_doc_question_document_id

    @single_doc_question_document_id.setter
    def single_doc_question_document_id(self, single_doc_question_document_id):
        """Sets the single_doc_question_document_id of this AnswerExcludeSearchCommand.

        include answers that were asked of a single document  # noqa: E501

        :param single_doc_question_document_id: The single_doc_question_document_id of this AnswerExcludeSearchCommand.  # noqa: E501
        :type: str
        """

        self._single_doc_question_document_id = single_doc_question_document_id

    @property
    def with_concepts(self):
        """Gets the with_concepts of this AnswerExcludeSearchCommand.  # noqa: E501

        return concept matches for each answer  # noqa: E501

        :return: The with_concepts of this AnswerExcludeSearchCommand.  # noqa: E501
        :rtype: bool
        """
        return self._with_concepts

    @with_concepts.setter
    def with_concepts(self, with_concepts):
        """Sets the with_concepts of this AnswerExcludeSearchCommand.

        return concept matches for each answer  # noqa: E501

        :param with_concepts: The with_concepts of this AnswerExcludeSearchCommand.  # noqa: E501
        :type: bool
        """

        self._with_concepts = with_concepts

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
        if issubclass(AnswerExcludeSearchCommand, dict):
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
        if not isinstance(other, AnswerExcludeSearchCommand):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
