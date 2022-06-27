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

class VectorSimilarityRequest(object):
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
        'created_by_user': 'int',
        'date_indexed': 'datetime',
        'id': 'str',
        'name': 'str',
        'query_string': 'str',
        'raw_text_vector': 'list[float]',
        'status': 'str',
        'vector_similarity_type': 'str'
    }

    attribute_map = {
        'created_by_user': 'createdByUser',
        'date_indexed': 'dateIndexed',
        'id': 'id',
        'name': 'name',
        'query_string': 'queryString',
        'raw_text_vector': 'rawTextVector',
        'status': 'status',
        'vector_similarity_type': 'vectorSimilarityType'
    }

    def __init__(self, created_by_user=None, date_indexed=None, id=None, name=None, query_string=None, raw_text_vector=None, status=None, vector_similarity_type=None):  # noqa: E501
        """VectorSimilarityRequest - a model defined in Swagger"""  # noqa: E501
        self._created_by_user = None
        self._date_indexed = None
        self._id = None
        self._name = None
        self._query_string = None
        self._raw_text_vector = None
        self._status = None
        self._vector_similarity_type = None
        self.discriminator = None
        if created_by_user is not None:
            self.created_by_user = created_by_user
        if date_indexed is not None:
            self.date_indexed = date_indexed
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if query_string is not None:
            self.query_string = query_string
        if raw_text_vector is not None:
            self.raw_text_vector = raw_text_vector
        if status is not None:
            self.status = status
        if vector_similarity_type is not None:
            self.vector_similarity_type = vector_similarity_type

    @property
    def created_by_user(self):
        """Gets the created_by_user of this VectorSimilarityRequest.  # noqa: E501


        :return: The created_by_user of this VectorSimilarityRequest.  # noqa: E501
        :rtype: int
        """
        return self._created_by_user

    @created_by_user.setter
    def created_by_user(self, created_by_user):
        """Sets the created_by_user of this VectorSimilarityRequest.


        :param created_by_user: The created_by_user of this VectorSimilarityRequest.  # noqa: E501
        :type: int
        """

        self._created_by_user = created_by_user

    @property
    def date_indexed(self):
        """Gets the date_indexed of this VectorSimilarityRequest.  # noqa: E501


        :return: The date_indexed of this VectorSimilarityRequest.  # noqa: E501
        :rtype: datetime
        """
        return self._date_indexed

    @date_indexed.setter
    def date_indexed(self, date_indexed):
        """Sets the date_indexed of this VectorSimilarityRequest.


        :param date_indexed: The date_indexed of this VectorSimilarityRequest.  # noqa: E501
        :type: datetime
        """

        self._date_indexed = date_indexed

    @property
    def id(self):
        """Gets the id of this VectorSimilarityRequest.  # noqa: E501


        :return: The id of this VectorSimilarityRequest.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this VectorSimilarityRequest.


        :param id: The id of this VectorSimilarityRequest.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this VectorSimilarityRequest.  # noqa: E501


        :return: The name of this VectorSimilarityRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this VectorSimilarityRequest.


        :param name: The name of this VectorSimilarityRequest.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def query_string(self):
        """Gets the query_string of this VectorSimilarityRequest.  # noqa: E501


        :return: The query_string of this VectorSimilarityRequest.  # noqa: E501
        :rtype: str
        """
        return self._query_string

    @query_string.setter
    def query_string(self, query_string):
        """Sets the query_string of this VectorSimilarityRequest.


        :param query_string: The query_string of this VectorSimilarityRequest.  # noqa: E501
        :type: str
        """

        self._query_string = query_string

    @property
    def raw_text_vector(self):
        """Gets the raw_text_vector of this VectorSimilarityRequest.  # noqa: E501


        :return: The raw_text_vector of this VectorSimilarityRequest.  # noqa: E501
        :rtype: list[float]
        """
        return self._raw_text_vector

    @raw_text_vector.setter
    def raw_text_vector(self, raw_text_vector):
        """Sets the raw_text_vector of this VectorSimilarityRequest.


        :param raw_text_vector: The raw_text_vector of this VectorSimilarityRequest.  # noqa: E501
        :type: list[float]
        """

        self._raw_text_vector = raw_text_vector

    @property
    def status(self):
        """Gets the status of this VectorSimilarityRequest.  # noqa: E501


        :return: The status of this VectorSimilarityRequest.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this VectorSimilarityRequest.


        :param status: The status of this VectorSimilarityRequest.  # noqa: E501
        :type: str
        """
        allowed_values = ["RUNNING", "COMPLETE", "ERROR"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def vector_similarity_type(self):
        """Gets the vector_similarity_type of this VectorSimilarityRequest.  # noqa: E501


        :return: The vector_similarity_type of this VectorSimilarityRequest.  # noqa: E501
        :rtype: str
        """
        return self._vector_similarity_type

    @vector_similarity_type.setter
    def vector_similarity_type(self, vector_similarity_type):
        """Sets the vector_similarity_type of this VectorSimilarityRequest.


        :param vector_similarity_type: The vector_similarity_type of this VectorSimilarityRequest.  # noqa: E501
        :type: str
        """
        allowed_values = ["STATEMENT", "CONCEPT_NAME_QUERY_TERM"]  # noqa: E501
        if vector_similarity_type not in allowed_values:
            raise ValueError(
                "Invalid value for `vector_similarity_type` ({0}), must be one of {1}"  # noqa: E501
                .format(vector_similarity_type, allowed_values)
            )

        self._vector_similarity_type = vector_similarity_type

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
        if issubclass(VectorSimilarityRequest, dict):
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
        if not isinstance(other, VectorSimilarityRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
