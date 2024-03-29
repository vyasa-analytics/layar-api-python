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

class ConceptAssignment(object):
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
        'backup_column_key': 'str',
        'column_key': 'str',
        'concept_type_id': 'str',
        'date_indexed': 'datetime',
        'document_id': 'str',
        'external_ids': 'dict(str, str)',
        'id': 'str',
        'link_to_tabluar_data': 'str',
        'user_id': 'int'
    }

    attribute_map = {
        'backup_column_key': 'backupColumnKey',
        'column_key': 'columnKey',
        'concept_type_id': 'conceptTypeId',
        'date_indexed': 'dateIndexed',
        'document_id': 'documentId',
        'external_ids': 'externalIds',
        'id': 'id',
        'link_to_tabluar_data': 'linkToTabluarData',
        'user_id': 'userId'
    }

    def __init__(self, backup_column_key=None, column_key=None, concept_type_id=None, date_indexed=None, document_id=None, external_ids=None, id=None, link_to_tabluar_data=None, user_id=None):  # noqa: E501
        """ConceptAssignment - a model defined in Swagger"""  # noqa: E501
        self._backup_column_key = None
        self._column_key = None
        self._concept_type_id = None
        self._date_indexed = None
        self._document_id = None
        self._external_ids = None
        self._id = None
        self._link_to_tabluar_data = None
        self._user_id = None
        self.discriminator = None
        if backup_column_key is not None:
            self.backup_column_key = backup_column_key
        if column_key is not None:
            self.column_key = column_key
        if concept_type_id is not None:
            self.concept_type_id = concept_type_id
        if date_indexed is not None:
            self.date_indexed = date_indexed
        if document_id is not None:
            self.document_id = document_id
        if external_ids is not None:
            self.external_ids = external_ids
        if id is not None:
            self.id = id
        if link_to_tabluar_data is not None:
            self.link_to_tabluar_data = link_to_tabluar_data
        if user_id is not None:
            self.user_id = user_id

    @property
    def backup_column_key(self):
        """Gets the backup_column_key of this ConceptAssignment.  # noqa: E501


        :return: The backup_column_key of this ConceptAssignment.  # noqa: E501
        :rtype: str
        """
        return self._backup_column_key

    @backup_column_key.setter
    def backup_column_key(self, backup_column_key):
        """Sets the backup_column_key of this ConceptAssignment.


        :param backup_column_key: The backup_column_key of this ConceptAssignment.  # noqa: E501
        :type: str
        """

        self._backup_column_key = backup_column_key

    @property
    def column_key(self):
        """Gets the column_key of this ConceptAssignment.  # noqa: E501


        :return: The column_key of this ConceptAssignment.  # noqa: E501
        :rtype: str
        """
        return self._column_key

    @column_key.setter
    def column_key(self, column_key):
        """Sets the column_key of this ConceptAssignment.


        :param column_key: The column_key of this ConceptAssignment.  # noqa: E501
        :type: str
        """

        self._column_key = column_key

    @property
    def concept_type_id(self):
        """Gets the concept_type_id of this ConceptAssignment.  # noqa: E501


        :return: The concept_type_id of this ConceptAssignment.  # noqa: E501
        :rtype: str
        """
        return self._concept_type_id

    @concept_type_id.setter
    def concept_type_id(self, concept_type_id):
        """Sets the concept_type_id of this ConceptAssignment.


        :param concept_type_id: The concept_type_id of this ConceptAssignment.  # noqa: E501
        :type: str
        """

        self._concept_type_id = concept_type_id

    @property
    def date_indexed(self):
        """Gets the date_indexed of this ConceptAssignment.  # noqa: E501


        :return: The date_indexed of this ConceptAssignment.  # noqa: E501
        :rtype: datetime
        """
        return self._date_indexed

    @date_indexed.setter
    def date_indexed(self, date_indexed):
        """Sets the date_indexed of this ConceptAssignment.


        :param date_indexed: The date_indexed of this ConceptAssignment.  # noqa: E501
        :type: datetime
        """

        self._date_indexed = date_indexed

    @property
    def document_id(self):
        """Gets the document_id of this ConceptAssignment.  # noqa: E501


        :return: The document_id of this ConceptAssignment.  # noqa: E501
        :rtype: str
        """
        return self._document_id

    @document_id.setter
    def document_id(self, document_id):
        """Sets the document_id of this ConceptAssignment.


        :param document_id: The document_id of this ConceptAssignment.  # noqa: E501
        :type: str
        """

        self._document_id = document_id

    @property
    def external_ids(self):
        """Gets the external_ids of this ConceptAssignment.  # noqa: E501


        :return: The external_ids of this ConceptAssignment.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._external_ids

    @external_ids.setter
    def external_ids(self, external_ids):
        """Sets the external_ids of this ConceptAssignment.


        :param external_ids: The external_ids of this ConceptAssignment.  # noqa: E501
        :type: dict(str, str)
        """

        self._external_ids = external_ids

    @property
    def id(self):
        """Gets the id of this ConceptAssignment.  # noqa: E501


        :return: The id of this ConceptAssignment.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ConceptAssignment.


        :param id: The id of this ConceptAssignment.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def link_to_tabluar_data(self):
        """Gets the link_to_tabluar_data of this ConceptAssignment.  # noqa: E501


        :return: The link_to_tabluar_data of this ConceptAssignment.  # noqa: E501
        :rtype: str
        """
        return self._link_to_tabluar_data

    @link_to_tabluar_data.setter
    def link_to_tabluar_data(self, link_to_tabluar_data):
        """Sets the link_to_tabluar_data of this ConceptAssignment.


        :param link_to_tabluar_data: The link_to_tabluar_data of this ConceptAssignment.  # noqa: E501
        :type: str
        """

        self._link_to_tabluar_data = link_to_tabluar_data

    @property
    def user_id(self):
        """Gets the user_id of this ConceptAssignment.  # noqa: E501


        :return: The user_id of this ConceptAssignment.  # noqa: E501
        :rtype: int
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this ConceptAssignment.


        :param user_id: The user_id of this ConceptAssignment.  # noqa: E501
        :type: int
        """

        self._user_id = user_id

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
        if issubclass(ConceptAssignment, dict):
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
        if not isinstance(other, ConceptAssignment):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
