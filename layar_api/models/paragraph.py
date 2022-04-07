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
from layar_api.models.domain_object import DomainObject  # noqa: F401,E501

class Paragraph(DomainObject):
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
        'raw_text': 'str',
        'source': 'str',
        'provider': 'str',
        'paragraph_number': 'int',
        'starts_onpage_number': 'int',
        'belongs_to_section_heading': 'str',
        'paragraph_indexing_version': 'list[str]',
        'highlighted_text': 'list[str]'
    }
    if hasattr(DomainObject, "swagger_types"):
        swagger_types.update(DomainObject.swagger_types)

    attribute_map = {
        'document_id': 'documentId',
        'raw_text': 'rawText',
        'source': 'source',
        'provider': 'provider',
        'paragraph_number': 'paragraphNumber',
        'starts_onpage_number': 'startsOnpageNumber',
        'belongs_to_section_heading': 'belongsToSectionHeading',
        'paragraph_indexing_version': 'paragraphIndexingVersion',
        'highlighted_text': 'highlightedText'
    }
    if hasattr(DomainObject, "attribute_map"):
        attribute_map.update(DomainObject.attribute_map)

    def __init__(self, document_id=None, raw_text=None, source=None, provider=None, paragraph_number=None, starts_onpage_number=None, belongs_to_section_heading=None, paragraph_indexing_version=None, highlighted_text=None, *args, **kwargs):  # noqa: E501
        """Paragraph - a model defined in Swagger"""  # noqa: E501
        self._document_id = None
        self._raw_text = None
        self._source = None
        self._provider = None
        self._paragraph_number = None
        self._starts_onpage_number = None
        self._belongs_to_section_heading = None
        self._paragraph_indexing_version = None
        self._highlighted_text = None
        self.discriminator = None
        if document_id is not None:
            self.document_id = document_id
        if raw_text is not None:
            self.raw_text = raw_text
        if source is not None:
            self.source = source
        if provider is not None:
            self.provider = provider
        if paragraph_number is not None:
            self.paragraph_number = paragraph_number
        if starts_onpage_number is not None:
            self.starts_onpage_number = starts_onpage_number
        if belongs_to_section_heading is not None:
            self.belongs_to_section_heading = belongs_to_section_heading
        if paragraph_indexing_version is not None:
            self.paragraph_indexing_version = paragraph_indexing_version
        if highlighted_text is not None:
            self.highlighted_text = highlighted_text
        DomainObject.__init__(self, *args, **kwargs)

    @property
    def document_id(self):
        """Gets the document_id of this Paragraph.  # noqa: E501


        :return: The document_id of this Paragraph.  # noqa: E501
        :rtype: str
        """
        return self._document_id

    @document_id.setter
    def document_id(self, document_id):
        """Sets the document_id of this Paragraph.


        :param document_id: The document_id of this Paragraph.  # noqa: E501
        :type: str
        """

        self._document_id = document_id

    @property
    def raw_text(self):
        """Gets the raw_text of this Paragraph.  # noqa: E501


        :return: The raw_text of this Paragraph.  # noqa: E501
        :rtype: str
        """
        return self._raw_text

    @raw_text.setter
    def raw_text(self, raw_text):
        """Sets the raw_text of this Paragraph.


        :param raw_text: The raw_text of this Paragraph.  # noqa: E501
        :type: str
        """

        self._raw_text = raw_text

    @property
    def source(self):
        """Gets the source of this Paragraph.  # noqa: E501


        :return: The source of this Paragraph.  # noqa: E501
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this Paragraph.


        :param source: The source of this Paragraph.  # noqa: E501
        :type: str
        """

        self._source = source

    @property
    def provider(self):
        """Gets the provider of this Paragraph.  # noqa: E501


        :return: The provider of this Paragraph.  # noqa: E501
        :rtype: str
        """
        return self._provider

    @provider.setter
    def provider(self, provider):
        """Sets the provider of this Paragraph.


        :param provider: The provider of this Paragraph.  # noqa: E501
        :type: str
        """

        self._provider = provider

    @property
    def paragraph_number(self):
        """Gets the paragraph_number of this Paragraph.  # noqa: E501


        :return: The paragraph_number of this Paragraph.  # noqa: E501
        :rtype: int
        """
        return self._paragraph_number

    @paragraph_number.setter
    def paragraph_number(self, paragraph_number):
        """Sets the paragraph_number of this Paragraph.


        :param paragraph_number: The paragraph_number of this Paragraph.  # noqa: E501
        :type: int
        """

        self._paragraph_number = paragraph_number

    @property
    def starts_onpage_number(self):
        """Gets the starts_onpage_number of this Paragraph.  # noqa: E501


        :return: The starts_onpage_number of this Paragraph.  # noqa: E501
        :rtype: int
        """
        return self._starts_onpage_number

    @starts_onpage_number.setter
    def starts_onpage_number(self, starts_onpage_number):
        """Sets the starts_onpage_number of this Paragraph.


        :param starts_onpage_number: The starts_onpage_number of this Paragraph.  # noqa: E501
        :type: int
        """

        self._starts_onpage_number = starts_onpage_number

    @property
    def belongs_to_section_heading(self):
        """Gets the belongs_to_section_heading of this Paragraph.  # noqa: E501


        :return: The belongs_to_section_heading of this Paragraph.  # noqa: E501
        :rtype: str
        """
        return self._belongs_to_section_heading

    @belongs_to_section_heading.setter
    def belongs_to_section_heading(self, belongs_to_section_heading):
        """Sets the belongs_to_section_heading of this Paragraph.


        :param belongs_to_section_heading: The belongs_to_section_heading of this Paragraph.  # noqa: E501
        :type: str
        """

        self._belongs_to_section_heading = belongs_to_section_heading

    @property
    def paragraph_indexing_version(self):
        """Gets the paragraph_indexing_version of this Paragraph.  # noqa: E501


        :return: The paragraph_indexing_version of this Paragraph.  # noqa: E501
        :rtype: list[str]
        """
        return self._paragraph_indexing_version

    @paragraph_indexing_version.setter
    def paragraph_indexing_version(self, paragraph_indexing_version):
        """Sets the paragraph_indexing_version of this Paragraph.


        :param paragraph_indexing_version: The paragraph_indexing_version of this Paragraph.  # noqa: E501
        :type: list[str]
        """

        self._paragraph_indexing_version = paragraph_indexing_version

    @property
    def highlighted_text(self):
        """Gets the highlighted_text of this Paragraph.  # noqa: E501


        :return: The highlighted_text of this Paragraph.  # noqa: E501
        :rtype: list[str]
        """
        return self._highlighted_text

    @highlighted_text.setter
    def highlighted_text(self, highlighted_text):
        """Sets the highlighted_text of this Paragraph.


        :param highlighted_text: The highlighted_text of this Paragraph.  # noqa: E501
        :type: list[str]
        """

        self._highlighted_text = highlighted_text

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
        if issubclass(Paragraph, dict):
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
        if not isinstance(other, Paragraph):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
