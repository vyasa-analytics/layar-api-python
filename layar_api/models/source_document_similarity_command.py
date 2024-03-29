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

class SourceDocumentSimilarityCommand(object):
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
        'table1_id': 'str',
        'table1_data_provider': 'str',
        'table2_id': 'str',
        'table2_data_provider': 'str'
    }

    attribute_map = {
        'table1_id': 'table1Id',
        'table1_data_provider': 'table1DataProvider',
        'table2_id': 'table2Id',
        'table2_data_provider': 'table2DataProvider'
    }

    def __init__(self, table1_id=None, table1_data_provider=None, table2_id=None, table2_data_provider=None):  # noqa: E501
        """SourceDocumentSimilarityCommand - a model defined in Swagger"""  # noqa: E501
        self._table1_id = None
        self._table1_data_provider = None
        self._table2_id = None
        self._table2_data_provider = None
        self.discriminator = None
        self.table1_id = table1_id
        self.table1_data_provider = table1_data_provider
        self.table2_id = table2_id
        self.table2_data_provider = table2_data_provider

    @property
    def table1_id(self):
        """Gets the table1_id of this SourceDocumentSimilarityCommand.  # noqa: E501


        :return: The table1_id of this SourceDocumentSimilarityCommand.  # noqa: E501
        :rtype: str
        """
        return self._table1_id

    @table1_id.setter
    def table1_id(self, table1_id):
        """Sets the table1_id of this SourceDocumentSimilarityCommand.


        :param table1_id: The table1_id of this SourceDocumentSimilarityCommand.  # noqa: E501
        :type: str
        """
        if table1_id is None:
            raise ValueError("Invalid value for `table1_id`, must not be `None`")  # noqa: E501

        self._table1_id = table1_id

    @property
    def table1_data_provider(self):
        """Gets the table1_data_provider of this SourceDocumentSimilarityCommand.  # noqa: E501


        :return: The table1_data_provider of this SourceDocumentSimilarityCommand.  # noqa: E501
        :rtype: str
        """
        return self._table1_data_provider

    @table1_data_provider.setter
    def table1_data_provider(self, table1_data_provider):
        """Sets the table1_data_provider of this SourceDocumentSimilarityCommand.


        :param table1_data_provider: The table1_data_provider of this SourceDocumentSimilarityCommand.  # noqa: E501
        :type: str
        """
        if table1_data_provider is None:
            raise ValueError("Invalid value for `table1_data_provider`, must not be `None`")  # noqa: E501

        self._table1_data_provider = table1_data_provider

    @property
    def table2_id(self):
        """Gets the table2_id of this SourceDocumentSimilarityCommand.  # noqa: E501


        :return: The table2_id of this SourceDocumentSimilarityCommand.  # noqa: E501
        :rtype: str
        """
        return self._table2_id

    @table2_id.setter
    def table2_id(self, table2_id):
        """Sets the table2_id of this SourceDocumentSimilarityCommand.


        :param table2_id: The table2_id of this SourceDocumentSimilarityCommand.  # noqa: E501
        :type: str
        """
        if table2_id is None:
            raise ValueError("Invalid value for `table2_id`, must not be `None`")  # noqa: E501

        self._table2_id = table2_id

    @property
    def table2_data_provider(self):
        """Gets the table2_data_provider of this SourceDocumentSimilarityCommand.  # noqa: E501


        :return: The table2_data_provider of this SourceDocumentSimilarityCommand.  # noqa: E501
        :rtype: str
        """
        return self._table2_data_provider

    @table2_data_provider.setter
    def table2_data_provider(self, table2_data_provider):
        """Sets the table2_data_provider of this SourceDocumentSimilarityCommand.


        :param table2_data_provider: The table2_data_provider of this SourceDocumentSimilarityCommand.  # noqa: E501
        :type: str
        """
        if table2_data_provider is None:
            raise ValueError("Invalid value for `table2_data_provider`, must not be `None`")  # noqa: E501

        self._table2_data_provider = table2_data_provider

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
        if issubclass(SourceDocumentSimilarityCommand, dict):
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
        if not isinstance(other, SourceDocumentSimilarityCommand):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
