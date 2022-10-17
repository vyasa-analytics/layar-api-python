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

class Body7(object):
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
        'file': 'str',
        'name': 'str',
        'cortex_document_type': 'str'
    }

    attribute_map = {
        'file': 'file',
        'name': 'name',
        'cortex_document_type': 'cortexDocumentType'
    }

    def __init__(self, file=None, name=None, cortex_document_type=None):  # noqa: E501
        """Body7 - a model defined in Swagger"""  # noqa: E501
        self._file = None
        self._name = None
        self._cortex_document_type = None
        self.discriminator = None
        if file is not None:
            self.file = file
        if name is not None:
            self.name = name
        if cortex_document_type is not None:
            self.cortex_document_type = cortex_document_type

    @property
    def file(self):
        """Gets the file of this Body7.  # noqa: E501


        :return: The file of this Body7.  # noqa: E501
        :rtype: str
        """
        return self._file

    @file.setter
    def file(self, file):
        """Sets the file of this Body7.


        :param file: The file of this Body7.  # noqa: E501
        :type: str
        """

        self._file = file

    @property
    def name(self):
        """Gets the name of this Body7.  # noqa: E501


        :return: The name of this Body7.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Body7.


        :param name: The name of this Body7.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def cortex_document_type(self):
        """Gets the cortex_document_type of this Body7.  # noqa: E501


        :return: The cortex_document_type of this Body7.  # noqa: E501
        :rtype: str
        """
        return self._cortex_document_type

    @cortex_document_type.setter
    def cortex_document_type(self, cortex_document_type):
        """Sets the cortex_document_type of this Body7.


        :param cortex_document_type: The cortex_document_type of this Body7.  # noqa: E501
        :type: str
        """
        allowed_values = ["IMAGE", "DOCUMENT", "TABLE"]  # noqa: E501
        if cortex_document_type not in allowed_values:
            raise ValueError(
                "Invalid value for `cortex_document_type` ({0}), must be one of {1}"  # noqa: E501
                .format(cortex_document_type, allowed_values)
            )

        self._cortex_document_type = cortex_document_type

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
        if issubclass(Body7, dict):
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
        if not isinstance(other, Body7):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other