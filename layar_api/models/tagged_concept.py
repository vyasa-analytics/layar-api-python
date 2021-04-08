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

class TaggedConcept(object):
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
        'concept_type_id': 'str',
        'end_offset': 'int',
        'id': 'str',
        'start_offset': 'int'
    }

    attribute_map = {
        'concept_type_id': 'conceptTypeId',
        'end_offset': 'endOffset',
        'id': 'id',
        'start_offset': 'startOffset'
    }

    def __init__(self, concept_type_id=None, end_offset=None, id=None, start_offset=None):  # noqa: E501
        """TaggedConcept - a model defined in Swagger"""  # noqa: E501
        self._concept_type_id = None
        self._end_offset = None
        self._id = None
        self._start_offset = None
        self.discriminator = None
        if concept_type_id is not None:
            self.concept_type_id = concept_type_id
        if end_offset is not None:
            self.end_offset = end_offset
        if id is not None:
            self.id = id
        if start_offset is not None:
            self.start_offset = start_offset

    @property
    def concept_type_id(self):
        """Gets the concept_type_id of this TaggedConcept.  # noqa: E501


        :return: The concept_type_id of this TaggedConcept.  # noqa: E501
        :rtype: str
        """
        return self._concept_type_id

    @concept_type_id.setter
    def concept_type_id(self, concept_type_id):
        """Sets the concept_type_id of this TaggedConcept.


        :param concept_type_id: The concept_type_id of this TaggedConcept.  # noqa: E501
        :type: str
        """

        self._concept_type_id = concept_type_id

    @property
    def end_offset(self):
        """Gets the end_offset of this TaggedConcept.  # noqa: E501


        :return: The end_offset of this TaggedConcept.  # noqa: E501
        :rtype: int
        """
        return self._end_offset

    @end_offset.setter
    def end_offset(self, end_offset):
        """Sets the end_offset of this TaggedConcept.


        :param end_offset: The end_offset of this TaggedConcept.  # noqa: E501
        :type: int
        """

        self._end_offset = end_offset

    @property
    def id(self):
        """Gets the id of this TaggedConcept.  # noqa: E501


        :return: The id of this TaggedConcept.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TaggedConcept.


        :param id: The id of this TaggedConcept.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def start_offset(self):
        """Gets the start_offset of this TaggedConcept.  # noqa: E501


        :return: The start_offset of this TaggedConcept.  # noqa: E501
        :rtype: int
        """
        return self._start_offset

    @start_offset.setter
    def start_offset(self, start_offset):
        """Sets the start_offset of this TaggedConcept.


        :param start_offset: The start_offset of this TaggedConcept.  # noqa: E501
        :type: int
        """

        self._start_offset = start_offset

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
        if issubclass(TaggedConcept, dict):
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
        if not isinstance(other, TaggedConcept):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
