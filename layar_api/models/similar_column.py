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

class SimilarColumn(object):
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
        'key': 'str',
        'name': 'str',
        'top_values': 'list[str]'
    }

    attribute_map = {
        'key': 'key',
        'name': 'name',
        'top_values': 'topValues'
    }

    def __init__(self, key=None, name=None, top_values=None):  # noqa: E501
        """SimilarColumn - a model defined in Swagger"""  # noqa: E501
        self._key = None
        self._name = None
        self._top_values = None
        self.discriminator = None
        if key is not None:
            self.key = key
        if name is not None:
            self.name = name
        if top_values is not None:
            self.top_values = top_values

    @property
    def key(self):
        """Gets the key of this SimilarColumn.  # noqa: E501


        :return: The key of this SimilarColumn.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this SimilarColumn.


        :param key: The key of this SimilarColumn.  # noqa: E501
        :type: str
        """

        self._key = key

    @property
    def name(self):
        """Gets the name of this SimilarColumn.  # noqa: E501


        :return: The name of this SimilarColumn.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SimilarColumn.


        :param name: The name of this SimilarColumn.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def top_values(self):
        """Gets the top_values of this SimilarColumn.  # noqa: E501


        :return: The top_values of this SimilarColumn.  # noqa: E501
        :rtype: list[str]
        """
        return self._top_values

    @top_values.setter
    def top_values(self, top_values):
        """Sets the top_values of this SimilarColumn.


        :param top_values: The top_values of this SimilarColumn.  # noqa: E501
        :type: list[str]
        """

        self._top_values = top_values

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
        if issubclass(SimilarColumn, dict):
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
        if not isinstance(other, SimilarColumn):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
