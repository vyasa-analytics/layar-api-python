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

class SourceDocumentViewer(object):
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
        'date_indexed': 'datetime',
        'created_by_user': 'int',
        'document_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'date_indexed': 'dateIndexed',
        'created_by_user': 'createdByUser',
        'document_id': 'documentId'
    }

    def __init__(self, id=None, date_indexed=None, created_by_user=None, document_id=None):  # noqa: E501
        """SourceDocumentViewer - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._date_indexed = None
        self._created_by_user = None
        self._document_id = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if date_indexed is not None:
            self.date_indexed = date_indexed
        if created_by_user is not None:
            self.created_by_user = created_by_user
        if document_id is not None:
            self.document_id = document_id

    @property
    def id(self):
        """Gets the id of this SourceDocumentViewer.  # noqa: E501


        :return: The id of this SourceDocumentViewer.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SourceDocumentViewer.


        :param id: The id of this SourceDocumentViewer.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def date_indexed(self):
        """Gets the date_indexed of this SourceDocumentViewer.  # noqa: E501


        :return: The date_indexed of this SourceDocumentViewer.  # noqa: E501
        :rtype: datetime
        """
        return self._date_indexed

    @date_indexed.setter
    def date_indexed(self, date_indexed):
        """Sets the date_indexed of this SourceDocumentViewer.


        :param date_indexed: The date_indexed of this SourceDocumentViewer.  # noqa: E501
        :type: datetime
        """

        self._date_indexed = date_indexed

    @property
    def created_by_user(self):
        """Gets the created_by_user of this SourceDocumentViewer.  # noqa: E501


        :return: The created_by_user of this SourceDocumentViewer.  # noqa: E501
        :rtype: int
        """
        return self._created_by_user

    @created_by_user.setter
    def created_by_user(self, created_by_user):
        """Sets the created_by_user of this SourceDocumentViewer.


        :param created_by_user: The created_by_user of this SourceDocumentViewer.  # noqa: E501
        :type: int
        """

        self._created_by_user = created_by_user

    @property
    def document_id(self):
        """Gets the document_id of this SourceDocumentViewer.  # noqa: E501


        :return: The document_id of this SourceDocumentViewer.  # noqa: E501
        :rtype: str
        """
        return self._document_id

    @document_id.setter
    def document_id(self, document_id):
        """Sets the document_id of this SourceDocumentViewer.


        :param document_id: The document_id of this SourceDocumentViewer.  # noqa: E501
        :type: str
        """

        self._document_id = document_id

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
        if issubclass(SourceDocumentViewer, dict):
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
        if not isinstance(other, SourceDocumentViewer):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
