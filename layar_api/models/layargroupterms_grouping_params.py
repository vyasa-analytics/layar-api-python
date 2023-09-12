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

class LayargrouptermsGroupingParams(object):
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
        'close_match_cutoff': 'float',
        'split_up_lists': 'bool',
        'ngram_size': 'float'
    }

    attribute_map = {
        'close_match_cutoff': 'close_match_cutoff',
        'split_up_lists': 'split_up_lists',
        'ngram_size': 'ngram_size'
    }

    def __init__(self, close_match_cutoff=None, split_up_lists=None, ngram_size=None):  # noqa: E501
        """LayargrouptermsGroupingParams - a model defined in Swagger"""  # noqa: E501
        self._close_match_cutoff = None
        self._split_up_lists = None
        self._ngram_size = None
        self.discriminator = None
        if close_match_cutoff is not None:
            self.close_match_cutoff = close_match_cutoff
        if split_up_lists is not None:
            self.split_up_lists = split_up_lists
        if ngram_size is not None:
            self.ngram_size = ngram_size

    @property
    def close_match_cutoff(self):
        """Gets the close_match_cutoff of this LayargrouptermsGroupingParams.  # noqa: E501


        :return: The close_match_cutoff of this LayargrouptermsGroupingParams.  # noqa: E501
        :rtype: float
        """
        return self._close_match_cutoff

    @close_match_cutoff.setter
    def close_match_cutoff(self, close_match_cutoff):
        """Sets the close_match_cutoff of this LayargrouptermsGroupingParams.


        :param close_match_cutoff: The close_match_cutoff of this LayargrouptermsGroupingParams.  # noqa: E501
        :type: float
        """

        self._close_match_cutoff = close_match_cutoff

    @property
    def split_up_lists(self):
        """Gets the split_up_lists of this LayargrouptermsGroupingParams.  # noqa: E501


        :return: The split_up_lists of this LayargrouptermsGroupingParams.  # noqa: E501
        :rtype: bool
        """
        return self._split_up_lists

    @split_up_lists.setter
    def split_up_lists(self, split_up_lists):
        """Sets the split_up_lists of this LayargrouptermsGroupingParams.


        :param split_up_lists: The split_up_lists of this LayargrouptermsGroupingParams.  # noqa: E501
        :type: bool
        """

        self._split_up_lists = split_up_lists

    @property
    def ngram_size(self):
        """Gets the ngram_size of this LayargrouptermsGroupingParams.  # noqa: E501


        :return: The ngram_size of this LayargrouptermsGroupingParams.  # noqa: E501
        :rtype: float
        """
        return self._ngram_size

    @ngram_size.setter
    def ngram_size(self, ngram_size):
        """Sets the ngram_size of this LayargrouptermsGroupingParams.


        :param ngram_size: The ngram_size of this LayargrouptermsGroupingParams.  # noqa: E501
        :type: float
        """

        self._ngram_size = ngram_size

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
        if issubclass(LayargrouptermsGroupingParams, dict):
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
        if not isinstance(other, LayargrouptermsGroupingParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other