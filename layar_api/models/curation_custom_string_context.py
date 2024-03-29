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

class CurationCustomStringContext(object):
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
        'document_id': 'str',
        'paragraph_id': 'str',
        'section_heading': 'str',
        'text_field': 'str',
        'provider': 'str',
        'start_offset': 'int',
        'end_offset': 'int',
        'starts_on_page_number': 'int'
    }

    attribute_map = {
        'document_id': 'documentId',
        'paragraph_id': 'paragraphId',
        'section_heading': 'sectionHeading',
        'text_field': 'textField',
        'provider': 'provider',
        'start_offset': 'startOffset',
        'end_offset': 'endOffset',
        'starts_on_page_number': 'startsOnPageNumber'
    }

    def __init__(self, document_id=None, paragraph_id=None, section_heading=None, text_field=None, provider=None, start_offset=None, end_offset=None, starts_on_page_number=None):  # noqa: E501
        """CurationCustomStringContext - a model defined in Swagger"""  # noqa: E501
        self._document_id = None
        self._paragraph_id = None
        self._section_heading = None
        self._text_field = None
        self._provider = None
        self._start_offset = None
        self._end_offset = None
        self._starts_on_page_number = None
        self.discriminator = None
        if document_id is not None:
            self.document_id = document_id
        if paragraph_id is not None:
            self.paragraph_id = paragraph_id
        if section_heading is not None:
            self.section_heading = section_heading
        if text_field is not None:
            self.text_field = text_field
        if provider is not None:
            self.provider = provider
        if start_offset is not None:
            self.start_offset = start_offset
        if end_offset is not None:
            self.end_offset = end_offset
        if starts_on_page_number is not None:
            self.starts_on_page_number = starts_on_page_number

    @property
    def document_id(self):
        """Gets the document_id of this CurationCustomStringContext.  # noqa: E501


        :return: The document_id of this CurationCustomStringContext.  # noqa: E501
        :rtype: str
        """
        return self._document_id

    @document_id.setter
    def document_id(self, document_id):
        """Sets the document_id of this CurationCustomStringContext.


        :param document_id: The document_id of this CurationCustomStringContext.  # noqa: E501
        :type: str
        """

        self._document_id = document_id

    @property
    def paragraph_id(self):
        """Gets the paragraph_id of this CurationCustomStringContext.  # noqa: E501


        :return: The paragraph_id of this CurationCustomStringContext.  # noqa: E501
        :rtype: str
        """
        return self._paragraph_id

    @paragraph_id.setter
    def paragraph_id(self, paragraph_id):
        """Sets the paragraph_id of this CurationCustomStringContext.


        :param paragraph_id: The paragraph_id of this CurationCustomStringContext.  # noqa: E501
        :type: str
        """

        self._paragraph_id = paragraph_id

    @property
    def section_heading(self):
        """Gets the section_heading of this CurationCustomStringContext.  # noqa: E501


        :return: The section_heading of this CurationCustomStringContext.  # noqa: E501
        :rtype: str
        """
        return self._section_heading

    @section_heading.setter
    def section_heading(self, section_heading):
        """Sets the section_heading of this CurationCustomStringContext.


        :param section_heading: The section_heading of this CurationCustomStringContext.  # noqa: E501
        :type: str
        """

        self._section_heading = section_heading

    @property
    def text_field(self):
        """Gets the text_field of this CurationCustomStringContext.  # noqa: E501


        :return: The text_field of this CurationCustomStringContext.  # noqa: E501
        :rtype: str
        """
        return self._text_field

    @text_field.setter
    def text_field(self, text_field):
        """Sets the text_field of this CurationCustomStringContext.


        :param text_field: The text_field of this CurationCustomStringContext.  # noqa: E501
        :type: str
        """

        self._text_field = text_field

    @property
    def provider(self):
        """Gets the provider of this CurationCustomStringContext.  # noqa: E501


        :return: The provider of this CurationCustomStringContext.  # noqa: E501
        :rtype: str
        """
        return self._provider

    @provider.setter
    def provider(self, provider):
        """Sets the provider of this CurationCustomStringContext.


        :param provider: The provider of this CurationCustomStringContext.  # noqa: E501
        :type: str
        """

        self._provider = provider

    @property
    def start_offset(self):
        """Gets the start_offset of this CurationCustomStringContext.  # noqa: E501


        :return: The start_offset of this CurationCustomStringContext.  # noqa: E501
        :rtype: int
        """
        return self._start_offset

    @start_offset.setter
    def start_offset(self, start_offset):
        """Sets the start_offset of this CurationCustomStringContext.


        :param start_offset: The start_offset of this CurationCustomStringContext.  # noqa: E501
        :type: int
        """

        self._start_offset = start_offset

    @property
    def end_offset(self):
        """Gets the end_offset of this CurationCustomStringContext.  # noqa: E501


        :return: The end_offset of this CurationCustomStringContext.  # noqa: E501
        :rtype: int
        """
        return self._end_offset

    @end_offset.setter
    def end_offset(self, end_offset):
        """Sets the end_offset of this CurationCustomStringContext.


        :param end_offset: The end_offset of this CurationCustomStringContext.  # noqa: E501
        :type: int
        """

        self._end_offset = end_offset

    @property
    def starts_on_page_number(self):
        """Gets the starts_on_page_number of this CurationCustomStringContext.  # noqa: E501


        :return: The starts_on_page_number of this CurationCustomStringContext.  # noqa: E501
        :rtype: int
        """
        return self._starts_on_page_number

    @starts_on_page_number.setter
    def starts_on_page_number(self, starts_on_page_number):
        """Sets the starts_on_page_number of this CurationCustomStringContext.


        :param starts_on_page_number: The starts_on_page_number of this CurationCustomStringContext.  # noqa: E501
        :type: int
        """

        self._starts_on_page_number = starts_on_page_number

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
        if issubclass(CurationCustomStringContext, dict):
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
        if not isinstance(other, CurationCustomStringContext):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
