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

class RelationshipQuery(object):
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
        'concept_ids': 'list[str]',
        'related_concept_ids': 'list[str]',
        'relationships': 'list[str]',
        'rows': 'int'
    }

    attribute_map = {
        'concept_ids': 'conceptIds',
        'related_concept_ids': 'relatedConceptIds',
        'relationships': 'relationships',
        'rows': 'rows'
    }

    def __init__(self, concept_ids=None, related_concept_ids=None, relationships=None, rows=None):  # noqa: E501
        """RelationshipQuery - a model defined in Swagger"""  # noqa: E501
        self._concept_ids = None
        self._related_concept_ids = None
        self._relationships = None
        self._rows = None
        self.discriminator = None
        if concept_ids is not None:
            self.concept_ids = concept_ids
        if related_concept_ids is not None:
            self.related_concept_ids = related_concept_ids
        if relationships is not None:
            self.relationships = relationships
        if rows is not None:
            self.rows = rows

    @property
    def concept_ids(self):
        """Gets the concept_ids of this RelationshipQuery.  # noqa: E501


        :return: The concept_ids of this RelationshipQuery.  # noqa: E501
        :rtype: list[str]
        """
        return self._concept_ids

    @concept_ids.setter
    def concept_ids(self, concept_ids):
        """Sets the concept_ids of this RelationshipQuery.


        :param concept_ids: The concept_ids of this RelationshipQuery.  # noqa: E501
        :type: list[str]
        """

        self._concept_ids = concept_ids

    @property
    def related_concept_ids(self):
        """Gets the related_concept_ids of this RelationshipQuery.  # noqa: E501


        :return: The related_concept_ids of this RelationshipQuery.  # noqa: E501
        :rtype: list[str]
        """
        return self._related_concept_ids

    @related_concept_ids.setter
    def related_concept_ids(self, related_concept_ids):
        """Sets the related_concept_ids of this RelationshipQuery.


        :param related_concept_ids: The related_concept_ids of this RelationshipQuery.  # noqa: E501
        :type: list[str]
        """

        self._related_concept_ids = related_concept_ids

    @property
    def relationships(self):
        """Gets the relationships of this RelationshipQuery.  # noqa: E501


        :return: The relationships of this RelationshipQuery.  # noqa: E501
        :rtype: list[str]
        """
        return self._relationships

    @relationships.setter
    def relationships(self, relationships):
        """Sets the relationships of this RelationshipQuery.


        :param relationships: The relationships of this RelationshipQuery.  # noqa: E501
        :type: list[str]
        """

        self._relationships = relationships

    @property
    def rows(self):
        """Gets the rows of this RelationshipQuery.  # noqa: E501


        :return: The rows of this RelationshipQuery.  # noqa: E501
        :rtype: int
        """
        return self._rows

    @rows.setter
    def rows(self, rows):
        """Sets the rows of this RelationshipQuery.


        :param rows: The rows of this RelationshipQuery.  # noqa: E501
        :type: int
        """

        self._rows = rows

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
        if issubclass(RelationshipQuery, dict):
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
        if not isinstance(other, RelationshipQuery):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
