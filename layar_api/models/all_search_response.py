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

class AllSearchResponse(object):
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
        'id': 'str',
        'type': 'str',
        'score': 'float',
        'source': 'object'
    }

    attribute_map = {
        'id': 'id',
        'type': 'type',
        'score': 'score',
        'source': 'source'
    }

    def __init__(self, id=None, type=None, score=None, source=None):  # noqa: E501
        """AllSearchResponse - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._type = None
        self._score = None
        self._source = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if type is not None:
            self.type = type
        if score is not None:
            self.score = score
        if source is not None:
            self.source = source

    @property
    def id(self):
        """Gets the id of this AllSearchResponse.  # noqa: E501


        :return: The id of this AllSearchResponse.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AllSearchResponse.


        :param id: The id of this AllSearchResponse.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def type(self):
        """Gets the type of this AllSearchResponse.  # noqa: E501


        :return: The type of this AllSearchResponse.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this AllSearchResponse.


        :param type: The type of this AllSearchResponse.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def score(self):
        """Gets the score of this AllSearchResponse.  # noqa: E501


        :return: The score of this AllSearchResponse.  # noqa: E501
        :rtype: float
        """
        return self._score

    @score.setter
    def score(self, score):
        """Sets the score of this AllSearchResponse.


        :param score: The score of this AllSearchResponse.  # noqa: E501
        :type: float
        """

        self._score = score

    @property
    def source(self):
        """Gets the source of this AllSearchResponse.  # noqa: E501


        :return: The source of this AllSearchResponse.  # noqa: E501
        :rtype: object
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this AllSearchResponse.


        :param source: The source of this AllSearchResponse.  # noqa: E501
        :type: object
        """

        self._source = source

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
        if issubclass(AllSearchResponse, dict):
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
        if not isinstance(other, AllSearchResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
