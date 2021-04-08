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

class ExtractTablesCommand(object):
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
        'pages': 'list[int]',
        'search_terms': 'list[str]'
    }

    attribute_map = {
        'pages': 'pages',
        'search_terms': 'searchTerms'
    }

    def __init__(self, pages=None, search_terms=None):  # noqa: E501
        """ExtractTablesCommand - a model defined in Swagger"""  # noqa: E501
        self._pages = None
        self._search_terms = None
        self.discriminator = None
        if pages is not None:
            self.pages = pages
        if search_terms is not None:
            self.search_terms = search_terms

    @property
    def pages(self):
        """Gets the pages of this ExtractTablesCommand.  # noqa: E501

        pages from which tables will be extracted  # noqa: E501

        :return: The pages of this ExtractTablesCommand.  # noqa: E501
        :rtype: list[int]
        """
        return self._pages

    @pages.setter
    def pages(self, pages):
        """Sets the pages of this ExtractTablesCommand.

        pages from which tables will be extracted  # noqa: E501

        :param pages: The pages of this ExtractTablesCommand.  # noqa: E501
        :type: list[int]
        """

        self._pages = pages

    @property
    def search_terms(self):
        """Gets the search_terms of this ExtractTablesCommand.  # noqa: E501

        search terms that must exist on any page with a table  # noqa: E501

        :return: The search_terms of this ExtractTablesCommand.  # noqa: E501
        :rtype: list[str]
        """
        return self._search_terms

    @search_terms.setter
    def search_terms(self, search_terms):
        """Sets the search_terms of this ExtractTablesCommand.

        search terms that must exist on any page with a table  # noqa: E501

        :param search_terms: The search_terms of this ExtractTablesCommand.  # noqa: E501
        :type: list[str]
        """

        self._search_terms = search_terms

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
        if issubclass(ExtractTablesCommand, dict):
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
        if not isinstance(other, ExtractTablesCommand):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
