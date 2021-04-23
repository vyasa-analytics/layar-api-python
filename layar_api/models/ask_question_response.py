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

class AskQuestionResponse(object):
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
        'answers': 'list[AskQuestionResponseAnswers]',
        'questions': 'list[str]'
    }

    attribute_map = {
        'answers': 'answers',
        'questions': 'questions'
    }

    def __init__(self, answers=None, questions=None):  # noqa: E501
        """AskQuestionResponse - a model defined in Swagger"""  # noqa: E501
        self._answers = None
        self._questions = None
        self.discriminator = None
        if answers is not None:
            self.answers = answers
        if questions is not None:
            self.questions = questions

    @property
    def answers(self):
        """Gets the answers of this AskQuestionResponse.  # noqa: E501


        :return: The answers of this AskQuestionResponse.  # noqa: E501
        :rtype: list[AskQuestionResponseAnswers]
        """
        return self._answers

    @answers.setter
    def answers(self, answers):
        """Sets the answers of this AskQuestionResponse.


        :param answers: The answers of this AskQuestionResponse.  # noqa: E501
        :type: list[AskQuestionResponseAnswers]
        """

        self._answers = answers

    @property
    def questions(self):
        """Gets the questions of this AskQuestionResponse.  # noqa: E501


        :return: The questions of this AskQuestionResponse.  # noqa: E501
        :rtype: list[str]
        """
        return self._questions

    @questions.setter
    def questions(self, questions):
        """Sets the questions of this AskQuestionResponse.


        :param questions: The questions of this AskQuestionResponse.  # noqa: E501
        :type: list[str]
        """

        self._questions = questions

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
        if issubclass(AskQuestionResponse, dict):
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
        if not isinstance(other, AskQuestionResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
