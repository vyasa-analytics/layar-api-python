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

class ConceptRelationship(object):
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
        'concept_ids': 'list[str]',
        'created_by_user': 'int',
        'date_indexed': 'datetime',
        'id': 'str',
        'left_concept_id': 'str',
        'name': 'str',
        'relationship': 'str',
        'right_concept_id': 'str',
        'verified': 'bool'
    }

    attribute_map = {
        'attributes': 'attributes',
        'concept_ids': 'conceptIds',
        'created_by_user': 'createdByUser',
        'date_indexed': 'dateIndexed',
        'id': 'id',
        'left_concept_id': 'leftConceptId',
        'name': 'name',
        'relationship': 'relationship',
        'right_concept_id': 'rightConceptId',
        'verified': 'verified'
    }

    def __init__(self, attributes=None, concept_ids=None, created_by_user=None, date_indexed=None, id=None, left_concept_id=None, name=None, relationship=None, right_concept_id=None, verified=None):  # noqa: E501
        """ConceptRelationship - a model defined in Swagger"""  # noqa: E501
        self._attributes = None
        self._concept_ids = None
        self._created_by_user = None
        self._date_indexed = None
        self._id = None
        self._left_concept_id = None
        self._name = None
        self._relationship = None
        self._right_concept_id = None
        self._verified = None
        self.discriminator = None
        if attributes is not None:
            self.attributes = attributes
        if concept_ids is not None:
            self.concept_ids = concept_ids
        if created_by_user is not None:
            self.created_by_user = created_by_user
        if date_indexed is not None:
            self.date_indexed = date_indexed
        if id is not None:
            self.id = id
        if left_concept_id is not None:
            self.left_concept_id = left_concept_id
        if name is not None:
            self.name = name
        if relationship is not None:
            self.relationship = relationship
        if right_concept_id is not None:
            self.right_concept_id = right_concept_id
        if verified is not None:
            self.verified = verified

    @property
    def attributes(self):
        """Gets the attributes of this ConceptRelationship.  # noqa: E501


        :return: The attributes of this ConceptRelationship.  # noqa: E501
        :rtype: object
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """Sets the attributes of this ConceptRelationship.


        :param attributes: The attributes of this ConceptRelationship.  # noqa: E501
        :type: object
        """

        self._attributes = attributes

    @property
    def concept_ids(self):
        """Gets the concept_ids of this ConceptRelationship.  # noqa: E501


        :return: The concept_ids of this ConceptRelationship.  # noqa: E501
        :rtype: list[str]
        """
        return self._concept_ids

    @concept_ids.setter
    def concept_ids(self, concept_ids):
        """Sets the concept_ids of this ConceptRelationship.


        :param concept_ids: The concept_ids of this ConceptRelationship.  # noqa: E501
        :type: list[str]
        """

        self._concept_ids = concept_ids

    @property
    def created_by_user(self):
        """Gets the created_by_user of this ConceptRelationship.  # noqa: E501


        :return: The created_by_user of this ConceptRelationship.  # noqa: E501
        :rtype: int
        """
        return self._created_by_user

    @created_by_user.setter
    def created_by_user(self, created_by_user):
        """Sets the created_by_user of this ConceptRelationship.


        :param created_by_user: The created_by_user of this ConceptRelationship.  # noqa: E501
        :type: int
        """

        self._created_by_user = created_by_user

    @property
    def date_indexed(self):
        """Gets the date_indexed of this ConceptRelationship.  # noqa: E501


        :return: The date_indexed of this ConceptRelationship.  # noqa: E501
        :rtype: datetime
        """
        return self._date_indexed

    @date_indexed.setter
    def date_indexed(self, date_indexed):
        """Sets the date_indexed of this ConceptRelationship.


        :param date_indexed: The date_indexed of this ConceptRelationship.  # noqa: E501
        :type: datetime
        """

        self._date_indexed = date_indexed

    @property
    def id(self):
        """Gets the id of this ConceptRelationship.  # noqa: E501


        :return: The id of this ConceptRelationship.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ConceptRelationship.


        :param id: The id of this ConceptRelationship.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def left_concept_id(self):
        """Gets the left_concept_id of this ConceptRelationship.  # noqa: E501


        :return: The left_concept_id of this ConceptRelationship.  # noqa: E501
        :rtype: str
        """
        return self._left_concept_id

    @left_concept_id.setter
    def left_concept_id(self, left_concept_id):
        """Sets the left_concept_id of this ConceptRelationship.


        :param left_concept_id: The left_concept_id of this ConceptRelationship.  # noqa: E501
        :type: str
        """

        self._left_concept_id = left_concept_id

    @property
    def name(self):
        """Gets the name of this ConceptRelationship.  # noqa: E501


        :return: The name of this ConceptRelationship.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ConceptRelationship.


        :param name: The name of this ConceptRelationship.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def relationship(self):
        """Gets the relationship of this ConceptRelationship.  # noqa: E501


        :return: The relationship of this ConceptRelationship.  # noqa: E501
        :rtype: str
        """
        return self._relationship

    @relationship.setter
    def relationship(self, relationship):
        """Sets the relationship of this ConceptRelationship.


        :param relationship: The relationship of this ConceptRelationship.  # noqa: E501
        :type: str
        """

        self._relationship = relationship

    @property
    def right_concept_id(self):
        """Gets the right_concept_id of this ConceptRelationship.  # noqa: E501


        :return: The right_concept_id of this ConceptRelationship.  # noqa: E501
        :rtype: str
        """
        return self._right_concept_id

    @right_concept_id.setter
    def right_concept_id(self, right_concept_id):
        """Sets the right_concept_id of this ConceptRelationship.


        :param right_concept_id: The right_concept_id of this ConceptRelationship.  # noqa: E501
        :type: str
        """

        self._right_concept_id = right_concept_id

    @property
    def verified(self):
        """Gets the verified of this ConceptRelationship.  # noqa: E501


        :return: The verified of this ConceptRelationship.  # noqa: E501
        :rtype: bool
        """
        return self._verified

    @verified.setter
    def verified(self, verified):
        """Sets the verified of this ConceptRelationship.


        :param verified: The verified of this ConceptRelationship.  # noqa: E501
        :type: bool
        """

        self._verified = verified

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
        if issubclass(ConceptRelationship, dict):
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
        if not isinstance(other, ConceptRelationship):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
