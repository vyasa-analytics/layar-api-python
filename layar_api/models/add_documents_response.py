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

class AddDocumentsResponse(object):
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
        'not_found_names': 'list[str]',
        'added_documents': 'list[SourceDocument]'
    }

    attribute_map = {
        'not_found_names': 'notFoundNames',
        'added_documents': 'addedDocuments'
    }

    def __init__(self, not_found_names=None, added_documents=None):  # noqa: E501
        """AddDocumentsResponse - a model defined in Swagger"""  # noqa: E501
        self._not_found_names = None
        self._added_documents = None
        self.discriminator = None
        if not_found_names is not None:
            self.not_found_names = not_found_names
        if added_documents is not None:
            self.added_documents = added_documents

    @property
    def not_found_names(self):
        """Gets the not_found_names of this AddDocumentsResponse.  # noqa: E501


        :return: The not_found_names of this AddDocumentsResponse.  # noqa: E501
        :rtype: list[str]
        """
        return self._not_found_names

    @not_found_names.setter
    def not_found_names(self, not_found_names):
        """Sets the not_found_names of this AddDocumentsResponse.


        :param not_found_names: The not_found_names of this AddDocumentsResponse.  # noqa: E501
        :type: list[str]
        """

        self._not_found_names = not_found_names

    @property
    def added_documents(self):
        """Gets the added_documents of this AddDocumentsResponse.  # noqa: E501


        :return: The added_documents of this AddDocumentsResponse.  # noqa: E501
        :rtype: list[SourceDocument]
        """
        return self._added_documents

    @added_documents.setter
    def added_documents(self, added_documents):
        """Sets the added_documents of this AddDocumentsResponse.


        :param added_documents: The added_documents of this AddDocumentsResponse.  # noqa: E501
        :type: list[SourceDocument]
        """

        self._added_documents = added_documents

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
        if issubclass(AddDocumentsResponse, dict):
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
        if not isinstance(other, AddDocumentsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
