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

class DetectedConcept(object):
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
        'concept': 'Concept',
        'end': 'int',
        'start': 'int'
    }

    attribute_map = {
        'concept': 'concept',
        'end': 'end',
        'start': 'start'
    }

    def __init__(self, concept=None, end=None, start=None):  # noqa: E501
        """DetectedConcept - a model defined in Swagger"""  # noqa: E501
        self._concept = None
        self._end = None
        self._start = None
        self.discriminator = None
        if concept is not None:
            self.concept = concept
        if end is not None:
            self.end = end
        if start is not None:
            self.start = start

    @property
    def concept(self):
        """Gets the concept of this DetectedConcept.  # noqa: E501


        :return: The concept of this DetectedConcept.  # noqa: E501
        :rtype: Concept
        """
        return self._concept

    @concept.setter
    def concept(self, concept):
        """Sets the concept of this DetectedConcept.


        :param concept: The concept of this DetectedConcept.  # noqa: E501
        :type: Concept
        """

        self._concept = concept

    @property
    def end(self):
        """Gets the end of this DetectedConcept.  # noqa: E501


        :return: The end of this DetectedConcept.  # noqa: E501
        :rtype: int
        """
        return self._end

    @end.setter
    def end(self, end):
        """Sets the end of this DetectedConcept.


        :param end: The end of this DetectedConcept.  # noqa: E501
        :type: int
        """

        self._end = end

    @property
    def start(self):
        """Gets the start of this DetectedConcept.  # noqa: E501


        :return: The start of this DetectedConcept.  # noqa: E501
        :rtype: int
        """
        return self._start

    @start.setter
    def start(self, start):
        """Sets the start of this DetectedConcept.


        :param start: The start of this DetectedConcept.  # noqa: E501
        :type: int
        """

        self._start = start

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
        if issubclass(DetectedConcept, dict):
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
        if not isinstance(other, DetectedConcept):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
