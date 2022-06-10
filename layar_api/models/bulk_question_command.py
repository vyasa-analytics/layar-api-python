# coding: utf-8

"""
    Layar API Documentation

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 2.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class BulkQuestionCommand(object):
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
        'bulk_questions': 'list[BulkQuestion]',
        'source_document_search_command': 'SourceDocumentSearchCommand',
        'question_grouping_key': 'str'
    }

    attribute_map = {
        'bulk_questions': 'bulkQuestions',
        'source_document_search_command': 'sourceDocumentSearchCommand',
        'question_grouping_key': 'questionGroupingKey'
    }

    def __init__(self, bulk_questions=None, source_document_search_command=None, question_grouping_key=None):  # noqa: E501
        """BulkQuestionCommand - a model defined in Swagger"""  # noqa: E501
        self._bulk_questions = None
        self._source_document_search_command = None
        self._question_grouping_key = None
        self.discriminator = None
        if bulk_questions is not None:
            self.bulk_questions = bulk_questions
        if source_document_search_command is not None:
            self.source_document_search_command = source_document_search_command
        if question_grouping_key is not None:
            self.question_grouping_key = question_grouping_key

    @property
    def bulk_questions(self):
        """Gets the bulk_questions of this BulkQuestionCommand.  # noqa: E501

        A list of bulk question IDs to be asked  # noqa: E501

        :return: The bulk_questions of this BulkQuestionCommand.  # noqa: E501
        :rtype: list[BulkQuestion]
        """
        return self._bulk_questions

    @bulk_questions.setter
    def bulk_questions(self, bulk_questions):
        """Sets the bulk_questions of this BulkQuestionCommand.

        A list of bulk question IDs to be asked  # noqa: E501

        :param bulk_questions: The bulk_questions of this BulkQuestionCommand.  # noqa: E501
        :type: list[BulkQuestion]
        """

        self._bulk_questions = bulk_questions

    @property
    def source_document_search_command(self):
        """Gets the source_document_search_command of this BulkQuestionCommand.  # noqa: E501


        :return: The source_document_search_command of this BulkQuestionCommand.  # noqa: E501
        :rtype: SourceDocumentSearchCommand
        """
        return self._source_document_search_command

    @source_document_search_command.setter
    def source_document_search_command(self, source_document_search_command):
        """Sets the source_document_search_command of this BulkQuestionCommand.


        :param source_document_search_command: The source_document_search_command of this BulkQuestionCommand.  # noqa: E501
        :type: SourceDocumentSearchCommand
        """

        self._source_document_search_command = source_document_search_command

    @property
    def question_grouping_key(self):
        """Gets the question_grouping_key of this BulkQuestionCommand.  # noqa: E501

        The grouping ID for this bulk question record  # noqa: E501

        :return: The question_grouping_key of this BulkQuestionCommand.  # noqa: E501
        :rtype: str
        """
        return self._question_grouping_key

    @question_grouping_key.setter
    def question_grouping_key(self, question_grouping_key):
        """Sets the question_grouping_key of this BulkQuestionCommand.

        The grouping ID for this bulk question record  # noqa: E501

        :param question_grouping_key: The question_grouping_key of this BulkQuestionCommand.  # noqa: E501
        :type: str
        """

        self._question_grouping_key = question_grouping_key

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
        if issubclass(BulkQuestionCommand, dict):
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
        if not isinstance(other, BulkQuestionCommand):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
