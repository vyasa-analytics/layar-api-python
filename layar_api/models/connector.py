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

class Connector(object):
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
        'connector_type': 'str',
        'created_by_user': 'str',
        'date_indexed': 'datetime',
        'id': 'str',
        'name': 'str'
    }

    attribute_map = {
        'connector_type': 'connectorType',
        'created_by_user': 'createdByUser',
        'date_indexed': 'dateIndexed',
        'id': 'id',
        'name': 'name'
    }

    discriminator_value_class_map = {
            'TWITTER'.lower(): 'TwitterConnector',
    }

    def __init__(self, connector_type=None, created_by_user=None, date_indexed=None, id=None, name=None):  # noqa: E501
        """Connector - a model defined in Swagger"""  # noqa: E501
        self._connector_type = None
        self._created_by_user = None
        self._date_indexed = None
        self._id = None
        self._name = None
        self.discriminator = 'connectorType'
        if connector_type is not None:
            self.connector_type = connector_type
        if created_by_user is not None:
            self.created_by_user = created_by_user
        if date_indexed is not None:
            self.date_indexed = date_indexed
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name

    @property
    def connector_type(self):
        """Gets the connector_type of this Connector.  # noqa: E501


        :return: The connector_type of this Connector.  # noqa: E501
        :rtype: str
        """
        return self._connector_type

    @connector_type.setter
    def connector_type(self, connector_type):
        """Sets the connector_type of this Connector.


        :param connector_type: The connector_type of this Connector.  # noqa: E501
        :type: str
        """
        allowed_values = ["TWITTER"]  # noqa: E501
        if connector_type not in allowed_values:
            raise ValueError(
                "Invalid value for `connector_type` ({0}), must be one of {1}"  # noqa: E501
                .format(connector_type, allowed_values)
            )

        self._connector_type = connector_type

    @property
    def created_by_user(self):
        """Gets the created_by_user of this Connector.  # noqa: E501


        :return: The created_by_user of this Connector.  # noqa: E501
        :rtype: str
        """
        return self._created_by_user

    @created_by_user.setter
    def created_by_user(self, created_by_user):
        """Sets the created_by_user of this Connector.


        :param created_by_user: The created_by_user of this Connector.  # noqa: E501
        :type: str
        """

        self._created_by_user = created_by_user

    @property
    def date_indexed(self):
        """Gets the date_indexed of this Connector.  # noqa: E501


        :return: The date_indexed of this Connector.  # noqa: E501
        :rtype: datetime
        """
        return self._date_indexed

    @date_indexed.setter
    def date_indexed(self, date_indexed):
        """Sets the date_indexed of this Connector.


        :param date_indexed: The date_indexed of this Connector.  # noqa: E501
        :type: datetime
        """

        self._date_indexed = date_indexed

    @property
    def id(self):
        """Gets the id of this Connector.  # noqa: E501

        Layar Connector ID  # noqa: E501

        :return: The id of this Connector.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Connector.

        Layar Connector ID  # noqa: E501

        :param id: The id of this Connector.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this Connector.  # noqa: E501

        Name provided by a user to a given Layar Connector  # noqa: E501

        :return: The name of this Connector.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Connector.

        Name provided by a user to a given Layar Connector  # noqa: E501

        :param name: The name of this Connector.  # noqa: E501
        :type: str
        """

        self._name = name

    def get_real_child_model(self, data):
        """Returns the real base class specified by the discriminator"""
        discriminator_value = data[self.discriminator].lower()
        return self.discriminator_value_class_map.get(discriminator_value)

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
        if issubclass(Connector, dict):
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
        if not isinstance(other, Connector):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
