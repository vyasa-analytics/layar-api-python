# coding: utf-8

"""
    Layar API Documentation

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: VERSION_PLACEHOLDER
    Contact: support@vyasa.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class Curation(object):
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
        'answer_id': 'str',
        'custom_string': 'str',
        'custom_string_context': 'CurationCustomStringContext',
        'notes': 'str',
        'curation_type': 'CurationType'
    }

    attribute_map = {
        'answer_id': 'answerId',
        'custom_string': 'customString',
        'custom_string_context': 'customStringContext',
        'notes': 'notes',
        'curation_type': 'curationType'
    }

    def __init__(self, answer_id=None, custom_string=None, custom_string_context=None, notes=None, curation_type=None):  # noqa: E501
        """Curation - a model defined in Swagger"""  # noqa: E501
        self._answer_id = None
        self._custom_string = None
        self._custom_string_context = None
        self._notes = None
        self._curation_type = None
        self.discriminator = None
        if answer_id is not None:
            self.answer_id = answer_id
        if custom_string is not None:
            self.custom_string = custom_string
        if custom_string_context is not None:
            self.custom_string_context = custom_string_context
        if notes is not None:
            self.notes = notes
        if curation_type is not None:
            self.curation_type = curation_type

    @property
    def answer_id(self):
        """Gets the answer_id of this Curation.  # noqa: E501


        :return: The answer_id of this Curation.  # noqa: E501
        :rtype: str
        """
        return self._answer_id

    @answer_id.setter
    def answer_id(self, answer_id):
        """Sets the answer_id of this Curation.


        :param answer_id: The answer_id of this Curation.  # noqa: E501
        :type: str
        """

        self._answer_id = answer_id

    @property
    def custom_string(self):
        """Gets the custom_string of this Curation.  # noqa: E501


        :return: The custom_string of this Curation.  # noqa: E501
        :rtype: str
        """
        return self._custom_string

    @custom_string.setter
    def custom_string(self, custom_string):
        """Sets the custom_string of this Curation.


        :param custom_string: The custom_string of this Curation.  # noqa: E501
        :type: str
        """

        self._custom_string = custom_string

    @property
    def custom_string_context(self):
        """Gets the custom_string_context of this Curation.  # noqa: E501


        :return: The custom_string_context of this Curation.  # noqa: E501
        :rtype: CurationCustomStringContext
        """
        return self._custom_string_context

    @custom_string_context.setter
    def custom_string_context(self, custom_string_context):
        """Sets the custom_string_context of this Curation.


        :param custom_string_context: The custom_string_context of this Curation.  # noqa: E501
        :type: CurationCustomStringContext
        """

        self._custom_string_context = custom_string_context

    @property
    def notes(self):
        """Gets the notes of this Curation.  # noqa: E501


        :return: The notes of this Curation.  # noqa: E501
        :rtype: str
        """
        return self._notes

    @notes.setter
    def notes(self, notes):
        """Sets the notes of this Curation.


        :param notes: The notes of this Curation.  # noqa: E501
        :type: str
        """

        self._notes = notes

    @property
    def curation_type(self):
        """Gets the curation_type of this Curation.  # noqa: E501


        :return: The curation_type of this Curation.  # noqa: E501
        :rtype: CurationType
        """
        return self._curation_type

    @curation_type.setter
    def curation_type(self, curation_type):
        """Sets the curation_type of this Curation.


        :param curation_type: The curation_type of this Curation.  # noqa: E501
        :type: CurationType
        """

        self._curation_type = curation_type

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
        if issubclass(Curation, dict):
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
        if not isinstance(other, Curation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other