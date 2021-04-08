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

class Module(object):
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
        'module_type': 'str',
        'date_indexed': 'datetime',
        'description': 'str',
        'enabled': 'bool',
        'id': 'str',
        'input_types': 'list[SourceDocumentType]',
        'name': 'str'
    }

    attribute_map = {
        'module_type': 'moduleType',
        'date_indexed': 'dateIndexed',
        'description': 'description',
        'enabled': 'enabled',
        'id': 'id',
        'input_types': 'inputTypes',
        'name': 'name'
    }

    def __init__(self, module_type=None, date_indexed=None, description=None, enabled=None, id=None, input_types=None, name=None):  # noqa: E501
        """Module - a model defined in Swagger"""  # noqa: E501
        self._module_type = None
        self._date_indexed = None
        self._description = None
        self._enabled = None
        self._id = None
        self._input_types = None
        self._name = None
        self.discriminator = None
        if module_type is not None:
            self.module_type = module_type
        if date_indexed is not None:
            self.date_indexed = date_indexed
        if description is not None:
            self.description = description
        if enabled is not None:
            self.enabled = enabled
        if id is not None:
            self.id = id
        if input_types is not None:
            self.input_types = input_types
        if name is not None:
            self.name = name

    @property
    def module_type(self):
        """Gets the module_type of this Module.  # noqa: E501


        :return: The module_type of this Module.  # noqa: E501
        :rtype: str
        """
        return self._module_type

    @module_type.setter
    def module_type(self, module_type):
        """Sets the module_type of this Module.


        :param module_type: The module_type of this Module.  # noqa: E501
        :type: str
        """

        self._module_type = module_type

    @property
    def date_indexed(self):
        """Gets the date_indexed of this Module.  # noqa: E501


        :return: The date_indexed of this Module.  # noqa: E501
        :rtype: datetime
        """
        return self._date_indexed

    @date_indexed.setter
    def date_indexed(self, date_indexed):
        """Sets the date_indexed of this Module.


        :param date_indexed: The date_indexed of this Module.  # noqa: E501
        :type: datetime
        """

        self._date_indexed = date_indexed

    @property
    def description(self):
        """Gets the description of this Module.  # noqa: E501


        :return: The description of this Module.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Module.


        :param description: The description of this Module.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def enabled(self):
        """Gets the enabled of this Module.  # noqa: E501


        :return: The enabled of this Module.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this Module.


        :param enabled: The enabled of this Module.  # noqa: E501
        :type: bool
        """

        self._enabled = enabled

    @property
    def id(self):
        """Gets the id of this Module.  # noqa: E501


        :return: The id of this Module.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Module.


        :param id: The id of this Module.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def input_types(self):
        """Gets the input_types of this Module.  # noqa: E501


        :return: The input_types of this Module.  # noqa: E501
        :rtype: list[SourceDocumentType]
        """
        return self._input_types

    @input_types.setter
    def input_types(self, input_types):
        """Sets the input_types of this Module.


        :param input_types: The input_types of this Module.  # noqa: E501
        :type: list[SourceDocumentType]
        """

        self._input_types = input_types

    @property
    def name(self):
        """Gets the name of this Module.  # noqa: E501


        :return: The name of this Module.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Module.


        :param name: The name of this Module.  # noqa: E501
        :type: str
        """

        self._name = name

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
        if issubclass(Module, dict):
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
        if not isinstance(other, Module):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
