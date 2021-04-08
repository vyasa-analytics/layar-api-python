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

class Body1(object):
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
        'terms': 'list[str]',
        'cutoff': 'float'
    }

    attribute_map = {
        'terms': 'terms',
        'cutoff': 'cutoff'
    }

    def __init__(self, terms=None, cutoff=None):  # noqa: E501
        """Body1 - a model defined in Swagger"""  # noqa: E501
        self._terms = None
        self._cutoff = None
        self.discriminator = None
        if terms is not None:
            self.terms = terms
        if cutoff is not None:
            self.cutoff = cutoff

    @property
    def terms(self):
        """Gets the terms of this Body1.  # noqa: E501


        :return: The terms of this Body1.  # noqa: E501
        :rtype: list[str]
        """
        return self._terms

    @terms.setter
    def terms(self, terms):
        """Sets the terms of this Body1.


        :param terms: The terms of this Body1.  # noqa: E501
        :type: list[str]
        """

        self._terms = terms

    @property
    def cutoff(self):
        """Gets the cutoff of this Body1.  # noqa: E501


        :return: The cutoff of this Body1.  # noqa: E501
        :rtype: float
        """
        return self._cutoff

    @cutoff.setter
    def cutoff(self, cutoff):
        """Sets the cutoff of this Body1.


        :param cutoff: The cutoff of this Body1.  # noqa: E501
        :type: float
        """

        self._cutoff = cutoff

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
        if issubclass(Body1, dict):
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
        if not isinstance(other, Body1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
