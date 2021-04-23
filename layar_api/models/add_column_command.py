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

class AddColumnCommand(object):
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
        'name': 'str',
        'search_command': 'SourceDocumentSearchCommand',
        'column_type': 'DynamicColumnType',
        'ref_column_id': 'str'
    }

    attribute_map = {
        'name': 'name',
        'search_command': 'searchCommand',
        'column_type': 'columnType',
        'ref_column_id': 'refColumnId'
    }

    def __init__(self, name=None, search_command=None, column_type=None, ref_column_id=None):  # noqa: E501
        """AddColumnCommand - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._search_command = None
        self._column_type = None
        self._ref_column_id = None
        self.discriminator = None
        if name is not None:
            self.name = name
        if search_command is not None:
            self.search_command = search_command
        if column_type is not None:
            self.column_type = column_type
        if ref_column_id is not None:
            self.ref_column_id = ref_column_id

    @property
    def name(self):
        """Gets the name of this AddColumnCommand.  # noqa: E501


        :return: The name of this AddColumnCommand.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AddColumnCommand.


        :param name: The name of this AddColumnCommand.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def search_command(self):
        """Gets the search_command of this AddColumnCommand.  # noqa: E501


        :return: The search_command of this AddColumnCommand.  # noqa: E501
        :rtype: SourceDocumentSearchCommand
        """
        return self._search_command

    @search_command.setter
    def search_command(self, search_command):
        """Sets the search_command of this AddColumnCommand.


        :param search_command: The search_command of this AddColumnCommand.  # noqa: E501
        :type: SourceDocumentSearchCommand
        """

        self._search_command = search_command

    @property
    def column_type(self):
        """Gets the column_type of this AddColumnCommand.  # noqa: E501


        :return: The column_type of this AddColumnCommand.  # noqa: E501
        :rtype: DynamicColumnType
        """
        return self._column_type

    @column_type.setter
    def column_type(self, column_type):
        """Sets the column_type of this AddColumnCommand.


        :param column_type: The column_type of this AddColumnCommand.  # noqa: E501
        :type: DynamicColumnType
        """

        self._column_type = column_type

    @property
    def ref_column_id(self):
        """Gets the ref_column_id of this AddColumnCommand.  # noqa: E501


        :return: The ref_column_id of this AddColumnCommand.  # noqa: E501
        :rtype: str
        """
        return self._ref_column_id

    @ref_column_id.setter
    def ref_column_id(self, ref_column_id):
        """Sets the ref_column_id of this AddColumnCommand.


        :param ref_column_id: The ref_column_id of this AddColumnCommand.  # noqa: E501
        :type: str
        """

        self._ref_column_id = ref_column_id

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
        if issubclass(AddColumnCommand, dict):
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
        if not isinstance(other, AddColumnCommand):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
