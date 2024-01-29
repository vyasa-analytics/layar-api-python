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

class Project(object):
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
        'created_by_user': 'int',
        'date_indexed': 'datetime',
        'description': 'str',
        'id': 'str',
        'module': 'Module',
        'module_id': 'str',
        'name': 'str'
    }

    attribute_map = {
        'created_by_user': 'createdByUser',
        'date_indexed': 'dateIndexed',
        'description': 'description',
        'id': 'id',
        'module': 'module',
        'module_id': 'moduleId',
        'name': 'name'
    }

    def __init__(self, created_by_user=None, date_indexed=None, description=None, id=None, module=None, module_id=None, name=None):  # noqa: E501
        """Project - a model defined in Swagger"""  # noqa: E501
        self._created_by_user = None
        self._date_indexed = None
        self._description = None
        self._id = None
        self._module = None
        self._module_id = None
        self._name = None
        self.discriminator = None
        if created_by_user is not None:
            self.created_by_user = created_by_user
        if date_indexed is not None:
            self.date_indexed = date_indexed
        if description is not None:
            self.description = description
        if id is not None:
            self.id = id
        if module is not None:
            self.module = module
        if module_id is not None:
            self.module_id = module_id
        if name is not None:
            self.name = name

    @property
    def created_by_user(self):
        """Gets the created_by_user of this Project.  # noqa: E501


        :return: The created_by_user of this Project.  # noqa: E501
        :rtype: int
        """
        return self._created_by_user

    @created_by_user.setter
    def created_by_user(self, created_by_user):
        """Sets the created_by_user of this Project.


        :param created_by_user: The created_by_user of this Project.  # noqa: E501
        :type: int
        """

        self._created_by_user = created_by_user

    @property
    def date_indexed(self):
        """Gets the date_indexed of this Project.  # noqa: E501


        :return: The date_indexed of this Project.  # noqa: E501
        :rtype: datetime
        """
        return self._date_indexed

    @date_indexed.setter
    def date_indexed(self, date_indexed):
        """Sets the date_indexed of this Project.


        :param date_indexed: The date_indexed of this Project.  # noqa: E501
        :type: datetime
        """

        self._date_indexed = date_indexed

    @property
    def description(self):
        """Gets the description of this Project.  # noqa: E501


        :return: The description of this Project.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Project.


        :param description: The description of this Project.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def id(self):
        """Gets the id of this Project.  # noqa: E501


        :return: The id of this Project.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Project.


        :param id: The id of this Project.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def module(self):
        """Gets the module of this Project.  # noqa: E501


        :return: The module of this Project.  # noqa: E501
        :rtype: Module
        """
        return self._module

    @module.setter
    def module(self, module):
        """Sets the module of this Project.


        :param module: The module of this Project.  # noqa: E501
        :type: Module
        """

        self._module = module

    @property
    def module_id(self):
        """Gets the module_id of this Project.  # noqa: E501


        :return: The module_id of this Project.  # noqa: E501
        :rtype: str
        """
        return self._module_id

    @module_id.setter
    def module_id(self, module_id):
        """Sets the module_id of this Project.


        :param module_id: The module_id of this Project.  # noqa: E501
        :type: str
        """

        self._module_id = module_id

    @property
    def name(self):
        """Gets the name of this Project.  # noqa: E501


        :return: The name of this Project.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Project.


        :param name: The name of this Project.  # noqa: E501
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
        if issubclass(Project, dict):
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
        if not isinstance(other, Project):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
