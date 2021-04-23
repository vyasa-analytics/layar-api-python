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
from layar_api.models.source_document_search_command import SourceDocumentSearchCommand  # noqa: F401,E501

class DistributedSourceDocumentSearchCommand(SourceDocumentSearchCommand):
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
        'data_providers': 'list[str]'
    }
    if hasattr(SourceDocumentSearchCommand, "swagger_types"):
        swagger_types.update(SourceDocumentSearchCommand.swagger_types)

    attribute_map = {
        'data_providers': 'dataProviders'
    }
    if hasattr(SourceDocumentSearchCommand, "attribute_map"):
        attribute_map.update(SourceDocumentSearchCommand.attribute_map)

    def __init__(self, data_providers=None, *args, **kwargs):  # noqa: E501
        """DistributedSourceDocumentSearchCommand - a model defined in Swagger"""  # noqa: E501
        self._data_providers = None
        self.discriminator = None
        if data_providers is not None:
            self.data_providers = data_providers
        SourceDocumentSearchCommand.__init__(self, *args, **kwargs)

    @property
    def data_providers(self):
        """Gets the data_providers of this DistributedSourceDocumentSearchCommand.  # noqa: E501


        :return: The data_providers of this DistributedSourceDocumentSearchCommand.  # noqa: E501
        :rtype: list[str]
        """
        return self._data_providers

    @data_providers.setter
    def data_providers(self, data_providers):
        """Sets the data_providers of this DistributedSourceDocumentSearchCommand.


        :param data_providers: The data_providers of this DistributedSourceDocumentSearchCommand.  # noqa: E501
        :type: list[str]
        """

        self._data_providers = data_providers

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
        if issubclass(DistributedSourceDocumentSearchCommand, dict):
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
        if not isinstance(other, DistributedSourceDocumentSearchCommand):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
