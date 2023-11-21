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

class AsyncJob(object):
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
        'status': 'JobStatus',
        'status_message': 'str',
        'percent_complete': 'float',
        'attributes': 'object'
    }

    attribute_map = {
        'status': 'status',
        'status_message': 'statusMessage',
        'percent_complete': 'percentComplete',
        'attributes': 'attributes'
    }

    def __init__(self, status=None, status_message=None, percent_complete=None, attributes=None):  # noqa: E501
        """AsyncJob - a model defined in Swagger"""  # noqa: E501
        self._status = None
        self._status_message = None
        self._percent_complete = None
        self._attributes = None
        self.discriminator = None
        if status is not None:
            self.status = status
        if status_message is not None:
            self.status_message = status_message
        if percent_complete is not None:
            self.percent_complete = percent_complete
        if attributes is not None:
            self.attributes = attributes

    @property
    def status(self):
        """Gets the status of this AsyncJob.  # noqa: E501


        :return: The status of this AsyncJob.  # noqa: E501
        :rtype: JobStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this AsyncJob.


        :param status: The status of this AsyncJob.  # noqa: E501
        :type: JobStatus
        """

        self._status = status

    @property
    def status_message(self):
        """Gets the status_message of this AsyncJob.  # noqa: E501


        :return: The status_message of this AsyncJob.  # noqa: E501
        :rtype: str
        """
        return self._status_message

    @status_message.setter
    def status_message(self, status_message):
        """Sets the status_message of this AsyncJob.


        :param status_message: The status_message of this AsyncJob.  # noqa: E501
        :type: str
        """

        self._status_message = status_message

    @property
    def percent_complete(self):
        """Gets the percent_complete of this AsyncJob.  # noqa: E501


        :return: The percent_complete of this AsyncJob.  # noqa: E501
        :rtype: float
        """
        return self._percent_complete

    @percent_complete.setter
    def percent_complete(self, percent_complete):
        """Sets the percent_complete of this AsyncJob.


        :param percent_complete: The percent_complete of this AsyncJob.  # noqa: E501
        :type: float
        """

        self._percent_complete = percent_complete

    @property
    def attributes(self):
        """Gets the attributes of this AsyncJob.  # noqa: E501


        :return: The attributes of this AsyncJob.  # noqa: E501
        :rtype: object
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """Sets the attributes of this AsyncJob.


        :param attributes: The attributes of this AsyncJob.  # noqa: E501
        :type: object
        """

        self._attributes = attributes

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
        if issubclass(AsyncJob, dict):
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
        if not isinstance(other, AsyncJob):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other