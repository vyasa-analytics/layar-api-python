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

class ReconcileToOntologyResultResultsMatch(object):
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
        'db_id': 'str',
        'name': 'str',
        'synonyms': 'str',
        'id': 'str'
    }

    attribute_map = {
        'db_id': 'dbId',
        'name': 'name',
        'synonyms': 'synonyms',
        'id': 'id'
    }

    def __init__(self, db_id=None, name=None, synonyms=None, id=None):  # noqa: E501
        """ReconcileToOntologyResultResultsMatch - a model defined in Swagger"""  # noqa: E501
        self._db_id = None
        self._name = None
        self._synonyms = None
        self._id = None
        self.discriminator = None
        if db_id is not None:
            self.db_id = db_id
        if name is not None:
            self.name = name
        if synonyms is not None:
            self.synonyms = synonyms
        if id is not None:
            self.id = id

    @property
    def db_id(self):
        """Gets the db_id of this ReconcileToOntologyResultResultsMatch.  # noqa: E501


        :return: The db_id of this ReconcileToOntologyResultResultsMatch.  # noqa: E501
        :rtype: str
        """
        return self._db_id

    @db_id.setter
    def db_id(self, db_id):
        """Sets the db_id of this ReconcileToOntologyResultResultsMatch.


        :param db_id: The db_id of this ReconcileToOntologyResultResultsMatch.  # noqa: E501
        :type: str
        """

        self._db_id = db_id

    @property
    def name(self):
        """Gets the name of this ReconcileToOntologyResultResultsMatch.  # noqa: E501


        :return: The name of this ReconcileToOntologyResultResultsMatch.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ReconcileToOntologyResultResultsMatch.


        :param name: The name of this ReconcileToOntologyResultResultsMatch.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def synonyms(self):
        """Gets the synonyms of this ReconcileToOntologyResultResultsMatch.  # noqa: E501


        :return: The synonyms of this ReconcileToOntologyResultResultsMatch.  # noqa: E501
        :rtype: str
        """
        return self._synonyms

    @synonyms.setter
    def synonyms(self, synonyms):
        """Sets the synonyms of this ReconcileToOntologyResultResultsMatch.


        :param synonyms: The synonyms of this ReconcileToOntologyResultResultsMatch.  # noqa: E501
        :type: str
        """

        self._synonyms = synonyms

    @property
    def id(self):
        """Gets the id of this ReconcileToOntologyResultResultsMatch.  # noqa: E501


        :return: The id of this ReconcileToOntologyResultResultsMatch.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ReconcileToOntologyResultResultsMatch.


        :param id: The id of this ReconcileToOntologyResultResultsMatch.  # noqa: E501
        :type: str
        """

        self._id = id

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
        if issubclass(ReconcileToOntologyResultResultsMatch, dict):
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
        if not isinstance(other, ReconcileToOntologyResultResultsMatch):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
