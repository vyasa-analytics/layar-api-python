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

class ConceptTypeRelationshipTemplate(object):
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
        'id': 'str',
        'label': 'str',
        'left_concept_type_ids': 'list[str]',
        'name': 'str',
        'relationships': 'list[str]',
        'right_concept_type_ids': 'list[str]'
    }

    attribute_map = {
        'created_by_user': 'createdByUser',
        'date_indexed': 'dateIndexed',
        'id': 'id',
        'label': 'label',
        'left_concept_type_ids': 'leftConceptTypeIds',
        'name': 'name',
        'relationships': 'relationships',
        'right_concept_type_ids': 'rightConceptTypeIds'
    }

    def __init__(self, created_by_user=None, date_indexed=None, id=None, label=None, left_concept_type_ids=None, name=None, relationships=None, right_concept_type_ids=None):  # noqa: E501
        """ConceptTypeRelationshipTemplate - a model defined in Swagger"""  # noqa: E501
        self._created_by_user = None
        self._date_indexed = None
        self._id = None
        self._label = None
        self._left_concept_type_ids = None
        self._name = None
        self._relationships = None
        self._right_concept_type_ids = None
        self.discriminator = None
        if created_by_user is not None:
            self.created_by_user = created_by_user
        if date_indexed is not None:
            self.date_indexed = date_indexed
        if id is not None:
            self.id = id
        if label is not None:
            self.label = label
        if left_concept_type_ids is not None:
            self.left_concept_type_ids = left_concept_type_ids
        if name is not None:
            self.name = name
        if relationships is not None:
            self.relationships = relationships
        if right_concept_type_ids is not None:
            self.right_concept_type_ids = right_concept_type_ids

    @property
    def created_by_user(self):
        """Gets the created_by_user of this ConceptTypeRelationshipTemplate.  # noqa: E501


        :return: The created_by_user of this ConceptTypeRelationshipTemplate.  # noqa: E501
        :rtype: int
        """
        return self._created_by_user

    @created_by_user.setter
    def created_by_user(self, created_by_user):
        """Sets the created_by_user of this ConceptTypeRelationshipTemplate.


        :param created_by_user: The created_by_user of this ConceptTypeRelationshipTemplate.  # noqa: E501
        :type: int
        """

        self._created_by_user = created_by_user

    @property
    def date_indexed(self):
        """Gets the date_indexed of this ConceptTypeRelationshipTemplate.  # noqa: E501


        :return: The date_indexed of this ConceptTypeRelationshipTemplate.  # noqa: E501
        :rtype: datetime
        """
        return self._date_indexed

    @date_indexed.setter
    def date_indexed(self, date_indexed):
        """Sets the date_indexed of this ConceptTypeRelationshipTemplate.


        :param date_indexed: The date_indexed of this ConceptTypeRelationshipTemplate.  # noqa: E501
        :type: datetime
        """

        self._date_indexed = date_indexed

    @property
    def id(self):
        """Gets the id of this ConceptTypeRelationshipTemplate.  # noqa: E501


        :return: The id of this ConceptTypeRelationshipTemplate.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ConceptTypeRelationshipTemplate.


        :param id: The id of this ConceptTypeRelationshipTemplate.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def label(self):
        """Gets the label of this ConceptTypeRelationshipTemplate.  # noqa: E501


        :return: The label of this ConceptTypeRelationshipTemplate.  # noqa: E501
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this ConceptTypeRelationshipTemplate.


        :param label: The label of this ConceptTypeRelationshipTemplate.  # noqa: E501
        :type: str
        """

        self._label = label

    @property
    def left_concept_type_ids(self):
        """Gets the left_concept_type_ids of this ConceptTypeRelationshipTemplate.  # noqa: E501


        :return: The left_concept_type_ids of this ConceptTypeRelationshipTemplate.  # noqa: E501
        :rtype: list[str]
        """
        return self._left_concept_type_ids

    @left_concept_type_ids.setter
    def left_concept_type_ids(self, left_concept_type_ids):
        """Sets the left_concept_type_ids of this ConceptTypeRelationshipTemplate.


        :param left_concept_type_ids: The left_concept_type_ids of this ConceptTypeRelationshipTemplate.  # noqa: E501
        :type: list[str]
        """

        self._left_concept_type_ids = left_concept_type_ids

    @property
    def name(self):
        """Gets the name of this ConceptTypeRelationshipTemplate.  # noqa: E501


        :return: The name of this ConceptTypeRelationshipTemplate.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ConceptTypeRelationshipTemplate.


        :param name: The name of this ConceptTypeRelationshipTemplate.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def relationships(self):
        """Gets the relationships of this ConceptTypeRelationshipTemplate.  # noqa: E501


        :return: The relationships of this ConceptTypeRelationshipTemplate.  # noqa: E501
        :rtype: list[str]
        """
        return self._relationships

    @relationships.setter
    def relationships(self, relationships):
        """Sets the relationships of this ConceptTypeRelationshipTemplate.


        :param relationships: The relationships of this ConceptTypeRelationshipTemplate.  # noqa: E501
        :type: list[str]
        """

        self._relationships = relationships

    @property
    def right_concept_type_ids(self):
        """Gets the right_concept_type_ids of this ConceptTypeRelationshipTemplate.  # noqa: E501


        :return: The right_concept_type_ids of this ConceptTypeRelationshipTemplate.  # noqa: E501
        :rtype: list[str]
        """
        return self._right_concept_type_ids

    @right_concept_type_ids.setter
    def right_concept_type_ids(self, right_concept_type_ids):
        """Sets the right_concept_type_ids of this ConceptTypeRelationshipTemplate.


        :param right_concept_type_ids: The right_concept_type_ids of this ConceptTypeRelationshipTemplate.  # noqa: E501
        :type: list[str]
        """

        self._right_concept_type_ids = right_concept_type_ids

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
        if issubclass(ConceptTypeRelationshipTemplate, dict):
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
        if not isinstance(other, ConceptTypeRelationshipTemplate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
