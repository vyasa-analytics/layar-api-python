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

class RadarExcludeSearchCommand(object):
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
        'live_source_ids': 'list[str]',
        'concept_type_ids': 'list[str]'
    }

    attribute_map = {
        'live_source_ids': 'liveSourceIds',
        'concept_type_ids': 'conceptTypeIds'
    }

    def __init__(self, live_source_ids=None, concept_type_ids=None):  # noqa: E501
        """RadarExcludeSearchCommand - a model defined in Swagger"""  # noqa: E501
        self._live_source_ids = None
        self._concept_type_ids = None
        self.discriminator = None
        if live_source_ids is not None:
            self.live_source_ids = live_source_ids
        if concept_type_ids is not None:
            self.concept_type_ids = concept_type_ids

    @property
    def live_source_ids(self):
        """Gets the live_source_ids of this RadarExcludeSearchCommand.  # noqa: E501


        :return: The live_source_ids of this RadarExcludeSearchCommand.  # noqa: E501
        :rtype: list[str]
        """
        return self._live_source_ids

    @live_source_ids.setter
    def live_source_ids(self, live_source_ids):
        """Sets the live_source_ids of this RadarExcludeSearchCommand.


        :param live_source_ids: The live_source_ids of this RadarExcludeSearchCommand.  # noqa: E501
        :type: list[str]
        """

        self._live_source_ids = live_source_ids

    @property
    def concept_type_ids(self):
        """Gets the concept_type_ids of this RadarExcludeSearchCommand.  # noqa: E501


        :return: The concept_type_ids of this RadarExcludeSearchCommand.  # noqa: E501
        :rtype: list[str]
        """
        return self._concept_type_ids

    @concept_type_ids.setter
    def concept_type_ids(self, concept_type_ids):
        """Sets the concept_type_ids of this RadarExcludeSearchCommand.


        :param concept_type_ids: The concept_type_ids of this RadarExcludeSearchCommand.  # noqa: E501
        :type: list[str]
        """

        self._concept_type_ids = concept_type_ids

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
        if issubclass(RadarExcludeSearchCommand, dict):
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
        if not isinstance(other, RadarExcludeSearchCommand):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
