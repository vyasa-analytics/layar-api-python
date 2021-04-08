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

class AskQuestionResponseNbestPredictions(object):
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
        'text': 'str',
        'probability': 'float',
        'start_logit': 'float',
        'end_logit': 'float',
        'start_offset': 'int',
        'end_offset': 'int'
    }

    attribute_map = {
        'text': 'text',
        'probability': 'probability',
        'start_logit': 'start_logit',
        'end_logit': 'end_logit',
        'start_offset': 'start_offset',
        'end_offset': 'end_offset'
    }

    def __init__(self, text=None, probability=None, start_logit=None, end_logit=None, start_offset=None, end_offset=None):  # noqa: E501
        """AskQuestionResponseNbestPredictions - a model defined in Swagger"""  # noqa: E501
        self._text = None
        self._probability = None
        self._start_logit = None
        self._end_logit = None
        self._start_offset = None
        self._end_offset = None
        self.discriminator = None
        if text is not None:
            self.text = text
        if probability is not None:
            self.probability = probability
        if start_logit is not None:
            self.start_logit = start_logit
        if end_logit is not None:
            self.end_logit = end_logit
        if start_offset is not None:
            self.start_offset = start_offset
        if end_offset is not None:
            self.end_offset = end_offset

    @property
    def text(self):
        """Gets the text of this AskQuestionResponseNbestPredictions.  # noqa: E501


        :return: The text of this AskQuestionResponseNbestPredictions.  # noqa: E501
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this AskQuestionResponseNbestPredictions.


        :param text: The text of this AskQuestionResponseNbestPredictions.  # noqa: E501
        :type: str
        """

        self._text = text

    @property
    def probability(self):
        """Gets the probability of this AskQuestionResponseNbestPredictions.  # noqa: E501


        :return: The probability of this AskQuestionResponseNbestPredictions.  # noqa: E501
        :rtype: float
        """
        return self._probability

    @probability.setter
    def probability(self, probability):
        """Sets the probability of this AskQuestionResponseNbestPredictions.


        :param probability: The probability of this AskQuestionResponseNbestPredictions.  # noqa: E501
        :type: float
        """

        self._probability = probability

    @property
    def start_logit(self):
        """Gets the start_logit of this AskQuestionResponseNbestPredictions.  # noqa: E501


        :return: The start_logit of this AskQuestionResponseNbestPredictions.  # noqa: E501
        :rtype: float
        """
        return self._start_logit

    @start_logit.setter
    def start_logit(self, start_logit):
        """Sets the start_logit of this AskQuestionResponseNbestPredictions.


        :param start_logit: The start_logit of this AskQuestionResponseNbestPredictions.  # noqa: E501
        :type: float
        """

        self._start_logit = start_logit

    @property
    def end_logit(self):
        """Gets the end_logit of this AskQuestionResponseNbestPredictions.  # noqa: E501


        :return: The end_logit of this AskQuestionResponseNbestPredictions.  # noqa: E501
        :rtype: float
        """
        return self._end_logit

    @end_logit.setter
    def end_logit(self, end_logit):
        """Sets the end_logit of this AskQuestionResponseNbestPredictions.


        :param end_logit: The end_logit of this AskQuestionResponseNbestPredictions.  # noqa: E501
        :type: float
        """

        self._end_logit = end_logit

    @property
    def start_offset(self):
        """Gets the start_offset of this AskQuestionResponseNbestPredictions.  # noqa: E501


        :return: The start_offset of this AskQuestionResponseNbestPredictions.  # noqa: E501
        :rtype: int
        """
        return self._start_offset

    @start_offset.setter
    def start_offset(self, start_offset):
        """Sets the start_offset of this AskQuestionResponseNbestPredictions.


        :param start_offset: The start_offset of this AskQuestionResponseNbestPredictions.  # noqa: E501
        :type: int
        """

        self._start_offset = start_offset

    @property
    def end_offset(self):
        """Gets the end_offset of this AskQuestionResponseNbestPredictions.  # noqa: E501


        :return: The end_offset of this AskQuestionResponseNbestPredictions.  # noqa: E501
        :rtype: int
        """
        return self._end_offset

    @end_offset.setter
    def end_offset(self, end_offset):
        """Sets the end_offset of this AskQuestionResponseNbestPredictions.


        :param end_offset: The end_offset of this AskQuestionResponseNbestPredictions.  # noqa: E501
        :type: int
        """

        self._end_offset = end_offset

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
        if issubclass(AskQuestionResponseNbestPredictions, dict):
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
        if not isinstance(other, AskQuestionResponseNbestPredictions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
