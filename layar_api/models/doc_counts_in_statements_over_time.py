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

class DocCountsInStatementsOverTime(object):
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
        'date_epoch': 'str',
        'date_string': 'str',
        '_date': 'str',
        'count': 'float'
    }

    attribute_map = {
        'date_epoch': 'dateEpoch',
        'date_string': 'dateString',
        '_date': 'date',
        'count': 'count'
    }

    def __init__(self, date_epoch=None, date_string=None, _date=None, count=None):  # noqa: E501
        """DocCountsInStatementsOverTime - a model defined in Swagger"""  # noqa: E501
        self._date_epoch = None
        self._date_string = None
        self.__date = None
        self._count = None
        self.discriminator = None
        if date_epoch is not None:
            self.date_epoch = date_epoch
        if date_string is not None:
            self.date_string = date_string
        if _date is not None:
            self._date = _date
        if count is not None:
            self.count = count

    @property
    def date_epoch(self):
        """Gets the date_epoch of this DocCountsInStatementsOverTime.  # noqa: E501


        :return: The date_epoch of this DocCountsInStatementsOverTime.  # noqa: E501
        :rtype: str
        """
        return self._date_epoch

    @date_epoch.setter
    def date_epoch(self, date_epoch):
        """Sets the date_epoch of this DocCountsInStatementsOverTime.


        :param date_epoch: The date_epoch of this DocCountsInStatementsOverTime.  # noqa: E501
        :type: str
        """

        self._date_epoch = date_epoch

    @property
    def date_string(self):
        """Gets the date_string of this DocCountsInStatementsOverTime.  # noqa: E501


        :return: The date_string of this DocCountsInStatementsOverTime.  # noqa: E501
        :rtype: str
        """
        return self._date_string

    @date_string.setter
    def date_string(self, date_string):
        """Sets the date_string of this DocCountsInStatementsOverTime.


        :param date_string: The date_string of this DocCountsInStatementsOverTime.  # noqa: E501
        :type: str
        """

        self._date_string = date_string

    @property
    def _date(self):
        """Gets the _date of this DocCountsInStatementsOverTime.  # noqa: E501


        :return: The _date of this DocCountsInStatementsOverTime.  # noqa: E501
        :rtype: str
        """
        return self.__date

    @_date.setter
    def _date(self, _date):
        """Sets the _date of this DocCountsInStatementsOverTime.


        :param _date: The _date of this DocCountsInStatementsOverTime.  # noqa: E501
        :type: str
        """

        self.__date = _date

    @property
    def count(self):
        """Gets the count of this DocCountsInStatementsOverTime.  # noqa: E501


        :return: The count of this DocCountsInStatementsOverTime.  # noqa: E501
        :rtype: float
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this DocCountsInStatementsOverTime.


        :param count: The count of this DocCountsInStatementsOverTime.  # noqa: E501
        :type: float
        """

        self._count = count

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
        if issubclass(DocCountsInStatementsOverTime, dict):
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
        if not isinstance(other, DocCountsInStatementsOverTime):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
