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

class ClusteredQuery(object):
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
        'clustered_query_type': 'str',
        'created_by_user': 'int',
        'date_indexed': 'datetime',
        'id': 'str',
        'name': 'str',
        'query_string': 'str',
        'status': 'str'
    }

    attribute_map = {
        'clustered_query_type': 'clusteredQueryType',
        'created_by_user': 'createdByUser',
        'date_indexed': 'dateIndexed',
        'id': 'id',
        'name': 'name',
        'query_string': 'queryString',
        'status': 'status'
    }

    def __init__(self, clustered_query_type=None, created_by_user=None, date_indexed=None, id=None, name=None, query_string=None, status=None):  # noqa: E501
        """ClusteredQuery - a model defined in Swagger"""  # noqa: E501
        self._clustered_query_type = None
        self._created_by_user = None
        self._date_indexed = None
        self._id = None
        self._name = None
        self._query_string = None
        self._status = None
        self.discriminator = None
        if clustered_query_type is not None:
            self.clustered_query_type = clustered_query_type
        if created_by_user is not None:
            self.created_by_user = created_by_user
        if date_indexed is not None:
            self.date_indexed = date_indexed
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if query_string is not None:
            self.query_string = query_string
        if status is not None:
            self.status = status

    @property
    def clustered_query_type(self):
        """Gets the clustered_query_type of this ClusteredQuery.  # noqa: E501


        :return: The clustered_query_type of this ClusteredQuery.  # noqa: E501
        :rtype: str
        """
        return self._clustered_query_type

    @clustered_query_type.setter
    def clustered_query_type(self, clustered_query_type):
        """Sets the clustered_query_type of this ClusteredQuery.


        :param clustered_query_type: The clustered_query_type of this ClusteredQuery.  # noqa: E501
        :type: str
        """
        allowed_values = ["STATEMENT", "CONCEPT"]  # noqa: E501
        if clustered_query_type not in allowed_values:
            raise ValueError(
                "Invalid value for `clustered_query_type` ({0}), must be one of {1}"  # noqa: E501
                .format(clustered_query_type, allowed_values)
            )

        self._clustered_query_type = clustered_query_type

    @property
    def created_by_user(self):
        """Gets the created_by_user of this ClusteredQuery.  # noqa: E501


        :return: The created_by_user of this ClusteredQuery.  # noqa: E501
        :rtype: int
        """
        return self._created_by_user

    @created_by_user.setter
    def created_by_user(self, created_by_user):
        """Sets the created_by_user of this ClusteredQuery.


        :param created_by_user: The created_by_user of this ClusteredQuery.  # noqa: E501
        :type: int
        """

        self._created_by_user = created_by_user

    @property
    def date_indexed(self):
        """Gets the date_indexed of this ClusteredQuery.  # noqa: E501


        :return: The date_indexed of this ClusteredQuery.  # noqa: E501
        :rtype: datetime
        """
        return self._date_indexed

    @date_indexed.setter
    def date_indexed(self, date_indexed):
        """Sets the date_indexed of this ClusteredQuery.


        :param date_indexed: The date_indexed of this ClusteredQuery.  # noqa: E501
        :type: datetime
        """

        self._date_indexed = date_indexed

    @property
    def id(self):
        """Gets the id of this ClusteredQuery.  # noqa: E501


        :return: The id of this ClusteredQuery.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ClusteredQuery.


        :param id: The id of this ClusteredQuery.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this ClusteredQuery.  # noqa: E501


        :return: The name of this ClusteredQuery.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ClusteredQuery.


        :param name: The name of this ClusteredQuery.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def query_string(self):
        """Gets the query_string of this ClusteredQuery.  # noqa: E501


        :return: The query_string of this ClusteredQuery.  # noqa: E501
        :rtype: str
        """
        return self._query_string

    @query_string.setter
    def query_string(self, query_string):
        """Sets the query_string of this ClusteredQuery.


        :param query_string: The query_string of this ClusteredQuery.  # noqa: E501
        :type: str
        """

        self._query_string = query_string

    @property
    def status(self):
        """Gets the status of this ClusteredQuery.  # noqa: E501


        :return: The status of this ClusteredQuery.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ClusteredQuery.


        :param status: The status of this ClusteredQuery.  # noqa: E501
        :type: str
        """
        allowed_values = ["RUNNING", "COMPLETE", "ERROR"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

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
        if issubclass(ClusteredQuery, dict):
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
        if not isinstance(other, ClusteredQuery):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
