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

class LayargptgenerateConversation(object):
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
        'chunk_size': 'float',
        'chunk_overlap': 'float'
    }

    attribute_map = {
        'chunk_size': 'chunk_size',
        'chunk_overlap': 'chunk_overlap'
    }

    def __init__(self, chunk_size=None, chunk_overlap=None):  # noqa: E501
        """LayargptgenerateConversation - a model defined in Swagger"""  # noqa: E501
        self._chunk_size = None
        self._chunk_overlap = None
        self.discriminator = None
        if chunk_size is not None:
            self.chunk_size = chunk_size
        if chunk_overlap is not None:
            self.chunk_overlap = chunk_overlap

    @property
    def chunk_size(self):
        """Gets the chunk_size of this LayargptgenerateConversation.  # noqa: E501


        :return: The chunk_size of this LayargptgenerateConversation.  # noqa: E501
        :rtype: float
        """
        return self._chunk_size

    @chunk_size.setter
    def chunk_size(self, chunk_size):
        """Sets the chunk_size of this LayargptgenerateConversation.


        :param chunk_size: The chunk_size of this LayargptgenerateConversation.  # noqa: E501
        :type: float
        """

        self._chunk_size = chunk_size

    @property
    def chunk_overlap(self):
        """Gets the chunk_overlap of this LayargptgenerateConversation.  # noqa: E501


        :return: The chunk_overlap of this LayargptgenerateConversation.  # noqa: E501
        :rtype: float
        """
        return self._chunk_overlap

    @chunk_overlap.setter
    def chunk_overlap(self, chunk_overlap):
        """Sets the chunk_overlap of this LayargptgenerateConversation.


        :param chunk_overlap: The chunk_overlap of this LayargptgenerateConversation.  # noqa: E501
        :type: float
        """

        self._chunk_overlap = chunk_overlap

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
        if issubclass(LayargptgenerateConversation, dict):
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
        if not isinstance(other, LayargptgenerateConversation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
