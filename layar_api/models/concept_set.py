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

class ConceptSet(object):
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
        'concept_count': 'int',
        'concept_ids': 'list[str]',
        'created_by_user': 'int',
        'date_indexed': 'datetime',
        'id': 'str',
        'name': 'str',
        'q': 'str',
        'related_set_id': 'str',
        'relationships': 'list[str]'
    }

    attribute_map = {
        'concept_count': 'conceptCount',
        'concept_ids': 'conceptIds',
        'created_by_user': 'createdByUser',
        'date_indexed': 'dateIndexed',
        'id': 'id',
        'name': 'name',
        'q': 'q',
        'related_set_id': 'relatedSetId',
        'relationships': 'relationships'
    }

    def __init__(self, concept_count=None, concept_ids=None, created_by_user=None, date_indexed=None, id=None, name=None, q=None, related_set_id=None, relationships=None):  # noqa: E501
        """ConceptSet - a model defined in Swagger"""  # noqa: E501
        self._concept_count = None
        self._concept_ids = None
        self._created_by_user = None
        self._date_indexed = None
        self._id = None
        self._name = None
        self._q = None
        self._related_set_id = None
        self._relationships = None
        self.discriminator = None
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
        if q is not None:
            self.q = q
        if related_set_id is not None:
            self.related_set_id = related_set_id
        if relationships is not None:
            self.relationships = relationships

    @property
    def concept_count(self):
        """Gets the concept_count of this ConceptSet.  # noqa: E501


        :return: The concept_count of this ConceptSet.  # noqa: E501
        :rtype: int
        """
        return self._concept_count

    @concept_count.setter
    def concept_count(self, concept_count):
        """Sets the concept_count of this ConceptSet.


        :param concept_count: The concept_count of this ConceptSet.  # noqa: E501
        :type: int
        """

        self._concept_count = concept_count

    @property
    def concept_ids(self):
        """Gets the concept_ids of this ConceptSet.  # noqa: E501


        :return: The concept_ids of this ConceptSet.  # noqa: E501
        :rtype: list[str]
        """
        return self._concept_ids

    @concept_ids.setter
    def concept_ids(self, concept_ids):
        """Sets the concept_ids of this ConceptSet.


        :param concept_ids: The concept_ids of this ConceptSet.  # noqa: E501
        :type: list[str]
        """

        self._concept_ids = concept_ids

    @property
    def created_by_user(self):
        """Gets the created_by_user of this ConceptSet.  # noqa: E501


        :return: The created_by_user of this ConceptSet.  # noqa: E501
        :rtype: int
        """
        return self._created_by_user

    @created_by_user.setter
    def created_by_user(self, created_by_user):
        """Sets the created_by_user of this ConceptSet.


        :param created_by_user: The created_by_user of this ConceptSet.  # noqa: E501
        :type: int
        """

        self._created_by_user = created_by_user

    @property
    def date_indexed(self):
        """Gets the date_indexed of this ConceptSet.  # noqa: E501


        :return: The date_indexed of this ConceptSet.  # noqa: E501
        :rtype: datetime
        """
        return self._date_indexed

    @date_indexed.setter
    def date_indexed(self, date_indexed):
        """Sets the date_indexed of this ConceptSet.


        :param date_indexed: The date_indexed of this ConceptSet.  # noqa: E501
        :type: datetime
        """

        self._date_indexed = date_indexed

    @property
    def id(self):
        """Gets the id of this ConceptSet.  # noqa: E501


        :return: The id of this ConceptSet.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ConceptSet.


        :param id: The id of this ConceptSet.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this ConceptSet.  # noqa: E501


        :return: The name of this ConceptSet.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ConceptSet.


        :param name: The name of this ConceptSet.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def q(self):
        """Gets the q of this ConceptSet.  # noqa: E501


        :return: The q of this ConceptSet.  # noqa: E501
        :rtype: str
        """
        return self._q

    @q.setter
    def q(self, q):
        """Sets the q of this ConceptSet.


        :param q: The q of this ConceptSet.  # noqa: E501
        :type: str
        """

        self._q = q

    @property
    def related_set_id(self):
        """Gets the related_set_id of this ConceptSet.  # noqa: E501


        :return: The related_set_id of this ConceptSet.  # noqa: E501
        :rtype: str
        """
        return self._related_set_id

    @related_set_id.setter
    def related_set_id(self, related_set_id):
        """Sets the related_set_id of this ConceptSet.


        :param related_set_id: The related_set_id of this ConceptSet.  # noqa: E501
        :type: str
        """

        self._related_set_id = related_set_id

    @property
    def relationships(self):
        """Gets the relationships of this ConceptSet.  # noqa: E501


        :return: The relationships of this ConceptSet.  # noqa: E501
        :rtype: list[str]
        """
        return self._relationships

    @relationships.setter
    def relationships(self, relationships):
        """Sets the relationships of this ConceptSet.


        :param relationships: The relationships of this ConceptSet.  # noqa: E501
        :type: list[str]
        """

        self._relationships = relationships

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
        if issubclass(ConceptSet, dict):
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
        if not isinstance(other, ConceptSet):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
