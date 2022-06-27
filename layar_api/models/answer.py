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
from layar_api.models.domain_object import DomainObject  # noqa: F401,E501

class Answer(DomainObject):
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
        'concepts': 'list[Concept]',
        'date_accepted': 'datetime',
        'evidence': 'list[AnswerEvidence]',
        'question_id': 'str',
        'question_key': 'str',
        'question_query_string': 'str',
        'single_doc_question_document_id': 'str',
        'rejected': 'bool',
        'text': 'str'
    }
    if hasattr(DomainObject, "swagger_types"):
        swagger_types.update(DomainObject.swagger_types)

    attribute_map = {
        'batch_grouping_key': 'batchGroupingKey',
        'concepts': 'concepts',
        'date_accepted': 'dateAccepted',
        'evidence': 'evidence',
        'question_id': 'questionId',
        'question_key': 'questionKey',
        'question_query_string': 'questionQueryString',
        'single_doc_question_document_id': 'singleDocQuestionDocumentId',
        'rejected': 'rejected',
        'text': 'text'
    }
    if hasattr(DomainObject, "attribute_map"):
        attribute_map.update(DomainObject.attribute_map)

    def __init__(self, batch_grouping_key=None, concepts=None, date_accepted=None, evidence=None, question_id=None, question_key=None, question_query_string=None, single_doc_question_document_id=None, rejected=None, text=None, *args, **kwargs):  # noqa: E501
        """Answer - a model defined in Swagger"""  # noqa: E501
        self._batch_grouping_key = None
        self._concepts = None
        self._date_accepted = None
        self._evidence = None
        self._question_id = None
        self._question_key = None
        self._question_query_string = None
        self._single_doc_question_document_id = None
        self._rejected = None
        self._text = None
        self.discriminator = None
        if batch_grouping_key is not None:
            self.batch_grouping_key = batch_grouping_key
        if concepts is not None:
            self.concepts = concepts
        if date_accepted is not None:
            self.date_accepted = date_accepted
        if evidence is not None:
            self.evidence = evidence
        if question_id is not None:
            self.question_id = question_id
        if question_key is not None:
            self.question_key = question_key
        if question_query_string is not None:
            self.question_query_string = question_query_string
        if single_doc_question_document_id is not None:
            self.single_doc_question_document_id = single_doc_question_document_id
        if rejected is not None:
            self.rejected = rejected
        if text is not None:
            self.text = text
        DomainObject.__init__(self, *args, **kwargs)

    @property
    def batch_grouping_key(self):
        """Gets the batch_grouping_key of this Answer.  # noqa: E501


        :return: The batch_grouping_key of this Answer.  # noqa: E501
        :rtype: str
        """
        return self._batch_grouping_key

    @batch_grouping_key.setter
    def batch_grouping_key(self, batch_grouping_key):
        """Sets the batch_grouping_key of this Answer.


        :param batch_grouping_key: The batch_grouping_key of this Answer.  # noqa: E501
        :type: str
        """

        self._batch_grouping_key = batch_grouping_key

    @property
    def concepts(self):
        """Gets the concepts of this Answer.  # noqa: E501


        :return: The concepts of this Answer.  # noqa: E501
        :rtype: list[Concept]
        """
        return self._concepts

    @concepts.setter
    def concepts(self, concepts):
        """Sets the concepts of this Answer.


        :param concepts: The concepts of this Answer.  # noqa: E501
        :type: list[Concept]
        """

        self._concepts = concepts

    @property
    def date_accepted(self):
        """Gets the date_accepted of this Answer.  # noqa: E501


        :return: The date_accepted of this Answer.  # noqa: E501
        :rtype: datetime
        """
        return self._date_accepted

    @date_accepted.setter
    def date_accepted(self, date_accepted):
        """Sets the date_accepted of this Answer.


        :param date_accepted: The date_accepted of this Answer.  # noqa: E501
        :type: datetime
        """

        self._date_accepted = date_accepted

    @property
    def evidence(self):
        """Gets the evidence of this Answer.  # noqa: E501


        :return: The evidence of this Answer.  # noqa: E501
        :rtype: list[AnswerEvidence]
        """
        return self._evidence

    @evidence.setter
    def evidence(self, evidence):
        """Sets the evidence of this Answer.


        :param evidence: The evidence of this Answer.  # noqa: E501
        :type: list[AnswerEvidence]
        """

        self._evidence = evidence

    @property
    def question_id(self):
        """Gets the question_id of this Answer.  # noqa: E501


        :return: The question_id of this Answer.  # noqa: E501
        :rtype: str
        """
        return self._question_id

    @question_id.setter
    def question_id(self, question_id):
        """Sets the question_id of this Answer.


        :param question_id: The question_id of this Answer.  # noqa: E501
        :type: str
        """

        self._question_id = question_id

    @property
    def question_key(self):
        """Gets the question_key of this Answer.  # noqa: E501


        :return: The question_key of this Answer.  # noqa: E501
        :rtype: str
        """
        return self._question_key

    @question_key.setter
    def question_key(self, question_key):
        """Sets the question_key of this Answer.


        :param question_key: The question_key of this Answer.  # noqa: E501
        :type: str
        """

        self._question_key = question_key

    @property
    def question_query_string(self):
        """Gets the question_query_string of this Answer.  # noqa: E501


        :return: The question_query_string of this Answer.  # noqa: E501
        :rtype: str
        """
        return self._question_query_string

    @question_query_string.setter
    def question_query_string(self, question_query_string):
        """Sets the question_query_string of this Answer.


        :param question_query_string: The question_query_string of this Answer.  # noqa: E501
        :type: str
        """

        self._question_query_string = question_query_string

    @property
    def single_doc_question_document_id(self):
        """Gets the single_doc_question_document_id of this Answer.  # noqa: E501


        :return: The single_doc_question_document_id of this Answer.  # noqa: E501
        :rtype: str
        """
        return self._single_doc_question_document_id

    @single_doc_question_document_id.setter
    def single_doc_question_document_id(self, single_doc_question_document_id):
        """Sets the single_doc_question_document_id of this Answer.


        :param single_doc_question_document_id: The single_doc_question_document_id of this Answer.  # noqa: E501
        :type: str
        """

        self._single_doc_question_document_id = single_doc_question_document_id

    @property
    def rejected(self):
        """Gets the rejected of this Answer.  # noqa: E501


        :return: The rejected of this Answer.  # noqa: E501
        :rtype: bool
        """
        return self._rejected

    @rejected.setter
    def rejected(self, rejected):
        """Sets the rejected of this Answer.


        :param rejected: The rejected of this Answer.  # noqa: E501
        :type: bool
        """

        self._rejected = rejected

    @property
    def text(self):
        """Gets the text of this Answer.  # noqa: E501


        :return: The text of this Answer.  # noqa: E501
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this Answer.


        :param text: The text of this Answer.  # noqa: E501
        :type: str
        """

        self._text = text

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
        if issubclass(Answer, dict):
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
        if not isinstance(other, Answer):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
