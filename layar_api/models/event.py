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

class Event(object):
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
        'attributes': 'object',
        'created_by_user': 'int',
        'date_indexed': 'datetime',
        'id': 'str',
        'message': 'str',
        'name': 'str',
        'project_id': 'str',
        'subject_id': 'str',
        'user_id': 'int'
    }

    attribute_map = {
        'attributes': 'attributes',
        'created_by_user': 'createdByUser',
        'date_indexed': 'dateIndexed',
        'id': 'id',
        'message': 'message',
        'name': 'name',
        'project_id': 'projectId',
        'subject_id': 'subjectId',
        'user_id': 'userId'
    }

    def __init__(self, attributes=None, created_by_user=None, date_indexed=None, id=None, message=None, name=None, project_id=None, subject_id=None, user_id=None):  # noqa: E501
        """Event - a model defined in Swagger"""  # noqa: E501
        self._attributes = None
        self._created_by_user = None
        self._date_indexed = None
        self._id = None
        self._message = None
        self._name = None
        self._project_id = None
        self._subject_id = None
        self._user_id = None
        self.discriminator = None
        if attributes is not None:
            self.attributes = attributes
        if created_by_user is not None:
            self.created_by_user = created_by_user
        if date_indexed is not None:
            self.date_indexed = date_indexed
        if id is not None:
            self.id = id
        if message is not None:
            self.message = message
        if name is not None:
            self.name = name
        if project_id is not None:
            self.project_id = project_id
        if subject_id is not None:
            self.subject_id = subject_id
        if user_id is not None:
            self.user_id = user_id

    @property
    def attributes(self):
        """Gets the attributes of this Event.  # noqa: E501


        :return: The attributes of this Event.  # noqa: E501
        :rtype: object
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """Sets the attributes of this Event.


        :param attributes: The attributes of this Event.  # noqa: E501
        :type: object
        """

        self._attributes = attributes

    @property
    def created_by_user(self):
        """Gets the created_by_user of this Event.  # noqa: E501


        :return: The created_by_user of this Event.  # noqa: E501
        :rtype: int
        """
        return self._created_by_user

    @created_by_user.setter
    def created_by_user(self, created_by_user):
        """Sets the created_by_user of this Event.


        :param created_by_user: The created_by_user of this Event.  # noqa: E501
        :type: int
        """

        self._created_by_user = created_by_user

    @property
    def date_indexed(self):
        """Gets the date_indexed of this Event.  # noqa: E501


        :return: The date_indexed of this Event.  # noqa: E501
        :rtype: datetime
        """
        return self._date_indexed

    @date_indexed.setter
    def date_indexed(self, date_indexed):
        """Sets the date_indexed of this Event.


        :param date_indexed: The date_indexed of this Event.  # noqa: E501
        :type: datetime
        """

        self._date_indexed = date_indexed

    @property
    def id(self):
        """Gets the id of this Event.  # noqa: E501


        :return: The id of this Event.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Event.


        :param id: The id of this Event.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def message(self):
        """Gets the message of this Event.  # noqa: E501


        :return: The message of this Event.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this Event.


        :param message: The message of this Event.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def name(self):
        """Gets the name of this Event.  # noqa: E501


        :return: The name of this Event.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Event.


        :param name: The name of this Event.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def project_id(self):
        """Gets the project_id of this Event.  # noqa: E501


        :return: The project_id of this Event.  # noqa: E501
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this Event.


        :param project_id: The project_id of this Event.  # noqa: E501
        :type: str
        """

        self._project_id = project_id

    @property
    def subject_id(self):
        """Gets the subject_id of this Event.  # noqa: E501


        :return: The subject_id of this Event.  # noqa: E501
        :rtype: str
        """
        return self._subject_id

    @subject_id.setter
    def subject_id(self, subject_id):
        """Sets the subject_id of this Event.


        :param subject_id: The subject_id of this Event.  # noqa: E501
        :type: str
        """

        self._subject_id = subject_id

    @property
    def user_id(self):
        """Gets the user_id of this Event.  # noqa: E501


        :return: The user_id of this Event.  # noqa: E501
        :rtype: int
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this Event.


        :param user_id: The user_id of this Event.  # noqa: E501
        :type: int
        """

        self._user_id = user_id

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
        if issubclass(Event, dict):
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
        if not isinstance(other, Event):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
