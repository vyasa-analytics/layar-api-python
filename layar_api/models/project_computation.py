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

class ProjectComputation(object):
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
        'computation_mode': 'str',
        'computation_parameters': 'object',
        'created_by_user': 'int',
        'date_indexed': 'datetime',
        'id': 'str',
        'model_id': 'str',
        'name': 'str',
        'project_id': 'str',
        'source_document': 'SourceDocument',
        'status': 'str'
    }

    attribute_map = {
        'computation_mode': 'computationMode',
        'computation_parameters': 'computationParameters',
        'created_by_user': 'createdByUser',
        'date_indexed': 'dateIndexed',
        'id': 'id',
        'model_id': 'modelId',
        'name': 'name',
        'project_id': 'projectId',
        'source_document': 'sourceDocument',
        'status': 'status'
    }

    def __init__(self, computation_mode=None, computation_parameters=None, created_by_user=None, date_indexed=None, id=None, model_id=None, name=None, project_id=None, source_document=None, status=None):  # noqa: E501
        """ProjectComputation - a model defined in Swagger"""  # noqa: E501
        self._computation_mode = None
        self._computation_parameters = None
        self._created_by_user = None
        self._date_indexed = None
        self._id = None
        self._model_id = None
        self._name = None
        self._project_id = None
        self._source_document = None
        self._status = None
        self.discriminator = None
        if computation_mode is not None:
            self.computation_mode = computation_mode
        if computation_parameters is not None:
            self.computation_parameters = computation_parameters
        if created_by_user is not None:
            self.created_by_user = created_by_user
        if date_indexed is not None:
            self.date_indexed = date_indexed
        if id is not None:
            self.id = id
        if model_id is not None:
            self.model_id = model_id
        if name is not None:
            self.name = name
        if project_id is not None:
            self.project_id = project_id
        if source_document is not None:
            self.source_document = source_document
        if status is not None:
            self.status = status

    @property
    def computation_mode(self):
        """Gets the computation_mode of this ProjectComputation.  # noqa: E501


        :return: The computation_mode of this ProjectComputation.  # noqa: E501
        :rtype: str
        """
        return self._computation_mode

    @computation_mode.setter
    def computation_mode(self, computation_mode):
        """Sets the computation_mode of this ProjectComputation.


        :param computation_mode: The computation_mode of this ProjectComputation.  # noqa: E501
        :type: str
        """
        allowed_values = ["TRAINING", "EXECUTING"]  # noqa: E501
        if computation_mode not in allowed_values:
            raise ValueError(
                "Invalid value for `computation_mode` ({0}), must be one of {1}"  # noqa: E501
                .format(computation_mode, allowed_values)
            )

        self._computation_mode = computation_mode

    @property
    def computation_parameters(self):
        """Gets the computation_parameters of this ProjectComputation.  # noqa: E501


        :return: The computation_parameters of this ProjectComputation.  # noqa: E501
        :rtype: object
        """
        return self._computation_parameters

    @computation_parameters.setter
    def computation_parameters(self, computation_parameters):
        """Sets the computation_parameters of this ProjectComputation.


        :param computation_parameters: The computation_parameters of this ProjectComputation.  # noqa: E501
        :type: object
        """

        self._computation_parameters = computation_parameters

    @property
    def created_by_user(self):
        """Gets the created_by_user of this ProjectComputation.  # noqa: E501


        :return: The created_by_user of this ProjectComputation.  # noqa: E501
        :rtype: int
        """
        return self._created_by_user

    @created_by_user.setter
    def created_by_user(self, created_by_user):
        """Sets the created_by_user of this ProjectComputation.


        :param created_by_user: The created_by_user of this ProjectComputation.  # noqa: E501
        :type: int
        """

        self._created_by_user = created_by_user

    @property
    def date_indexed(self):
        """Gets the date_indexed of this ProjectComputation.  # noqa: E501


        :return: The date_indexed of this ProjectComputation.  # noqa: E501
        :rtype: datetime
        """
        return self._date_indexed

    @date_indexed.setter
    def date_indexed(self, date_indexed):
        """Sets the date_indexed of this ProjectComputation.


        :param date_indexed: The date_indexed of this ProjectComputation.  # noqa: E501
        :type: datetime
        """

        self._date_indexed = date_indexed

    @property
    def id(self):
        """Gets the id of this ProjectComputation.  # noqa: E501


        :return: The id of this ProjectComputation.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ProjectComputation.


        :param id: The id of this ProjectComputation.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def model_id(self):
        """Gets the model_id of this ProjectComputation.  # noqa: E501


        :return: The model_id of this ProjectComputation.  # noqa: E501
        :rtype: str
        """
        return self._model_id

    @model_id.setter
    def model_id(self, model_id):
        """Sets the model_id of this ProjectComputation.


        :param model_id: The model_id of this ProjectComputation.  # noqa: E501
        :type: str
        """

        self._model_id = model_id

    @property
    def name(self):
        """Gets the name of this ProjectComputation.  # noqa: E501


        :return: The name of this ProjectComputation.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ProjectComputation.


        :param name: The name of this ProjectComputation.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def project_id(self):
        """Gets the project_id of this ProjectComputation.  # noqa: E501


        :return: The project_id of this ProjectComputation.  # noqa: E501
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this ProjectComputation.


        :param project_id: The project_id of this ProjectComputation.  # noqa: E501
        :type: str
        """

        self._project_id = project_id

    @property
    def source_document(self):
        """Gets the source_document of this ProjectComputation.  # noqa: E501


        :return: The source_document of this ProjectComputation.  # noqa: E501
        :rtype: SourceDocument
        """
        return self._source_document

    @source_document.setter
    def source_document(self, source_document):
        """Sets the source_document of this ProjectComputation.


        :param source_document: The source_document of this ProjectComputation.  # noqa: E501
        :type: SourceDocument
        """

        self._source_document = source_document

    @property
    def status(self):
        """Gets the status of this ProjectComputation.  # noqa: E501


        :return: The status of this ProjectComputation.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ProjectComputation.


        :param status: The status of this ProjectComputation.  # noqa: E501
        :type: str
        """
        allowed_values = ["RUNNING", "COMPLETE", "ERROR"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

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
        if issubclass(ProjectComputation, dict):
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
        if not isinstance(other, ProjectComputation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
