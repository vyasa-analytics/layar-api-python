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

class ClusteredConcepts(object):
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
        'cluster_id': 'str',
        'clustered_query_id': 'str',
        'concept_count': 'int',
        'concept_ids': 'list[str]',
        'created_by_user': 'int',
        'date_indexed': 'datetime',
        'id': 'str',
        'name': 'str'
    }

    attribute_map = {
        'cluster_id': 'clusterId',
        'clustered_query_id': 'clusteredQueryId',
        'concept_count': 'conceptCount',
        'concept_ids': 'conceptIds',
        'created_by_user': 'createdByUser',
        'date_indexed': 'dateIndexed',
        'id': 'id',
        'name': 'name'
    }

    def __init__(self, cluster_id=None, clustered_query_id=None, concept_count=None, concept_ids=None, created_by_user=None, date_indexed=None, id=None, name=None):  # noqa: E501
        """ClusteredConcepts - a model defined in Swagger"""  # noqa: E501
        self._cluster_id = None
        self._clustered_query_id = None
        self._concept_count = None
        self._concept_ids = None
        self._created_by_user = None
        self._date_indexed = None
        self._id = None
        self._name = None
        self.discriminator = None
        if cluster_id is not None:
            self.cluster_id = cluster_id
        if clustered_query_id is not None:
            self.clustered_query_id = clustered_query_id
        if concept_count is not None:
            self.concept_count = concept_count
        if concept_ids is not None:
            self.concept_ids = concept_ids
        if created_by_user is not None:
            self.created_by_user = created_by_user
        if date_indexed is not None:
            self.date_indexed = date_indexed
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name

    @property
    def cluster_id(self):
        """Gets the cluster_id of this ClusteredConcepts.  # noqa: E501


        :return: The cluster_id of this ClusteredConcepts.  # noqa: E501
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        """Sets the cluster_id of this ClusteredConcepts.


        :param cluster_id: The cluster_id of this ClusteredConcepts.  # noqa: E501
        :type: str
        """

        self._cluster_id = cluster_id

    @property
    def clustered_query_id(self):
        """Gets the clustered_query_id of this ClusteredConcepts.  # noqa: E501


        :return: The clustered_query_id of this ClusteredConcepts.  # noqa: E501
        :rtype: str
        """
        return self._clustered_query_id

    @clustered_query_id.setter
    def clustered_query_id(self, clustered_query_id):
        """Sets the clustered_query_id of this ClusteredConcepts.


        :param clustered_query_id: The clustered_query_id of this ClusteredConcepts.  # noqa: E501
        :type: str
        """

        self._clustered_query_id = clustered_query_id

    @property
    def concept_count(self):
        """Gets the concept_count of this ClusteredConcepts.  # noqa: E501


        :return: The concept_count of this ClusteredConcepts.  # noqa: E501
        :rtype: int
        """
        return self._concept_count

    @concept_count.setter
    def concept_count(self, concept_count):
        """Sets the concept_count of this ClusteredConcepts.


        :param concept_count: The concept_count of this ClusteredConcepts.  # noqa: E501
        :type: int
        """

        self._concept_count = concept_count

    @property
    def concept_ids(self):
        """Gets the concept_ids of this ClusteredConcepts.  # noqa: E501


        :return: The concept_ids of this ClusteredConcepts.  # noqa: E501
        :rtype: list[str]
        """
        return self._concept_ids

    @concept_ids.setter
    def concept_ids(self, concept_ids):
        """Sets the concept_ids of this ClusteredConcepts.


        :param concept_ids: The concept_ids of this ClusteredConcepts.  # noqa: E501
        :type: list[str]
        """

        self._concept_ids = concept_ids

    @property
    def created_by_user(self):
        """Gets the created_by_user of this ClusteredConcepts.  # noqa: E501


        :return: The created_by_user of this ClusteredConcepts.  # noqa: E501
        :rtype: int
        """
        return self._created_by_user

    @created_by_user.setter
    def created_by_user(self, created_by_user):
        """Sets the created_by_user of this ClusteredConcepts.


        :param created_by_user: The created_by_user of this ClusteredConcepts.  # noqa: E501
        :type: int
        """

        self._created_by_user = created_by_user

    @property
    def date_indexed(self):
        """Gets the date_indexed of this ClusteredConcepts.  # noqa: E501


        :return: The date_indexed of this ClusteredConcepts.  # noqa: E501
        :rtype: datetime
        """
        return self._date_indexed

    @date_indexed.setter
    def date_indexed(self, date_indexed):
        """Sets the date_indexed of this ClusteredConcepts.


        :param date_indexed: The date_indexed of this ClusteredConcepts.  # noqa: E501
        :type: datetime
        """

        self._date_indexed = date_indexed

    @property
    def id(self):
        """Gets the id of this ClusteredConcepts.  # noqa: E501


        :return: The id of this ClusteredConcepts.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ClusteredConcepts.


        :param id: The id of this ClusteredConcepts.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this ClusteredConcepts.  # noqa: E501


        :return: The name of this ClusteredConcepts.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ClusteredConcepts.


        :param name: The name of this ClusteredConcepts.  # noqa: E501
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
        if issubclass(ClusteredConcepts, dict):
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
        if not isinstance(other, ClusteredConcepts):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
