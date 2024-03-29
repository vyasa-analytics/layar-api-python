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

class AnnotationSearch(object):
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
        'key': 'str',
        'value_type': 'str',
        'values': 'list[OneOfAnnotationSearchValuesItems]',
        'min_value': 'int',
        'max_value': 'int',
        'min_date_value': 'datetime',
        'max_date_value': 'datetime'
    }

    attribute_map = {
        'key': 'key',
        'value_type': 'valueType',
        'values': 'values',
        'min_value': 'minValue',
        'max_value': 'maxValue',
        'min_date_value': 'minDateValue',
        'max_date_value': 'maxDateValue'
    }

    def __init__(self, key=None, value_type=None, values=None, min_value=None, max_value=None, min_date_value=None, max_date_value=None):  # noqa: E501
        """AnnotationSearch - a model defined in Swagger"""  # noqa: E501
        self._key = None
        self._value_type = None
        self._values = None
        self._min_value = None
        self._max_value = None
        self._min_date_value = None
        self._max_date_value = None
        self.discriminator = None
        if key is not None:
            self.key = key
        if value_type is not None:
            self.value_type = value_type
        if values is not None:
            self.values = values
        if min_value is not None:
            self.min_value = min_value
        if max_value is not None:
            self.max_value = max_value
        if min_date_value is not None:
            self.min_date_value = min_date_value
        if max_date_value is not None:
            self.max_date_value = max_date_value

    @property
    def key(self):
        """Gets the key of this AnnotationSearch.  # noqa: E501


        :return: The key of this AnnotationSearch.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this AnnotationSearch.


        :param key: The key of this AnnotationSearch.  # noqa: E501
        :type: str
        """

        self._key = key

    @property
    def value_type(self):
        """Gets the value_type of this AnnotationSearch.  # noqa: E501


        :return: The value_type of this AnnotationSearch.  # noqa: E501
        :rtype: str
        """
        return self._value_type

    @value_type.setter
    def value_type(self, value_type):
        """Sets the value_type of this AnnotationSearch.


        :param value_type: The value_type of this AnnotationSearch.  # noqa: E501
        :type: str
        """
        allowed_values = ["STRING", "BOOLEAN", "INTEGER", "DOUBLE", "DATE"]  # noqa: E501
        if value_type not in allowed_values:
            raise ValueError(
                "Invalid value for `value_type` ({0}), must be one of {1}"  # noqa: E501
                .format(value_type, allowed_values)
            )

        self._value_type = value_type

    @property
    def values(self):
        """Gets the values of this AnnotationSearch.  # noqa: E501


        :return: The values of this AnnotationSearch.  # noqa: E501
        :rtype: list[OneOfAnnotationSearchValuesItems]
        """
        return self._values

    @values.setter
    def values(self, values):
        """Sets the values of this AnnotationSearch.


        :param values: The values of this AnnotationSearch.  # noqa: E501
        :type: list[OneOfAnnotationSearchValuesItems]
        """

        self._values = values

    @property
    def min_value(self):
        """Gets the min_value of this AnnotationSearch.  # noqa: E501


        :return: The min_value of this AnnotationSearch.  # noqa: E501
        :rtype: int
        """
        return self._min_value

    @min_value.setter
    def min_value(self, min_value):
        """Sets the min_value of this AnnotationSearch.


        :param min_value: The min_value of this AnnotationSearch.  # noqa: E501
        :type: int
        """

        self._min_value = min_value

    @property
    def max_value(self):
        """Gets the max_value of this AnnotationSearch.  # noqa: E501


        :return: The max_value of this AnnotationSearch.  # noqa: E501
        :rtype: int
        """
        return self._max_value

    @max_value.setter
    def max_value(self, max_value):
        """Sets the max_value of this AnnotationSearch.


        :param max_value: The max_value of this AnnotationSearch.  # noqa: E501
        :type: int
        """

        self._max_value = max_value

    @property
    def min_date_value(self):
        """Gets the min_date_value of this AnnotationSearch.  # noqa: E501


        :return: The min_date_value of this AnnotationSearch.  # noqa: E501
        :rtype: datetime
        """
        return self._min_date_value

    @min_date_value.setter
    def min_date_value(self, min_date_value):
        """Sets the min_date_value of this AnnotationSearch.


        :param min_date_value: The min_date_value of this AnnotationSearch.  # noqa: E501
        :type: datetime
        """

        self._min_date_value = min_date_value

    @property
    def max_date_value(self):
        """Gets the max_date_value of this AnnotationSearch.  # noqa: E501


        :return: The max_date_value of this AnnotationSearch.  # noqa: E501
        :rtype: datetime
        """
        return self._max_date_value

    @max_date_value.setter
    def max_date_value(self, max_date_value):
        """Sets the max_date_value of this AnnotationSearch.


        :param max_date_value: The max_date_value of this AnnotationSearch.  # noqa: E501
        :type: datetime
        """

        self._max_date_value = max_date_value

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
        if issubclass(AnnotationSearch, dict):
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
        if not isinstance(other, AnnotationSearch):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
