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

class LiveSource(object):
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
        'description': 'str',
        'id': 'str',
        'live_source_type': 'str',
        'manifold_id': 'str',
        'name': 'str',
        'run_mode': 'str',
        'url': 'str'
    }

    attribute_map = {
        'created_by_user': 'createdByUser',
        'date_indexed': 'dateIndexed',
        'description': 'description',
        'id': 'id',
        'live_source_type': 'liveSourceType',
        'manifold_id': 'manifoldId',
        'name': 'name',
        'run_mode': 'runMode',
        'url': 'url'
    }

    def __init__(self, created_by_user=None, date_indexed=None, description=None, id=None, live_source_type=None, manifold_id=None, name=None, run_mode=None, url=None):  # noqa: E501
        """LiveSource - a model defined in Swagger"""  # noqa: E501
        self._created_by_user = None
        self._date_indexed = None
        self._description = None
        self._id = None
        self._live_source_type = None
        self._manifold_id = None
        self._name = None
        self._run_mode = None
        self._url = None
        self.discriminator = None
        if created_by_user is not None:
            self.created_by_user = created_by_user
        if date_indexed is not None:
            self.date_indexed = date_indexed
        if description is not None:
            self.description = description
        if id is not None:
            self.id = id
        if live_source_type is not None:
            self.live_source_type = live_source_type
        if manifold_id is not None:
            self.manifold_id = manifold_id
        if name is not None:
            self.name = name
        if run_mode is not None:
            self.run_mode = run_mode
        if url is not None:
            self.url = url

    @property
    def created_by_user(self):
        """Gets the created_by_user of this LiveSource.  # noqa: E501


        :return: The created_by_user of this LiveSource.  # noqa: E501
        :rtype: int
        """
        return self._created_by_user

    @created_by_user.setter
    def created_by_user(self, created_by_user):
        """Sets the created_by_user of this LiveSource.


        :param created_by_user: The created_by_user of this LiveSource.  # noqa: E501
        :type: int
        """

        self._created_by_user = created_by_user

    @property
    def date_indexed(self):
        """Gets the date_indexed of this LiveSource.  # noqa: E501


        :return: The date_indexed of this LiveSource.  # noqa: E501
        :rtype: datetime
        """
        return self._date_indexed

    @date_indexed.setter
    def date_indexed(self, date_indexed):
        """Sets the date_indexed of this LiveSource.


        :param date_indexed: The date_indexed of this LiveSource.  # noqa: E501
        :type: datetime
        """

        self._date_indexed = date_indexed

    @property
    def description(self):
        """Gets the description of this LiveSource.  # noqa: E501


        :return: The description of this LiveSource.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this LiveSource.


        :param description: The description of this LiveSource.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def id(self):
        """Gets the id of this LiveSource.  # noqa: E501


        :return: The id of this LiveSource.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this LiveSource.


        :param id: The id of this LiveSource.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def live_source_type(self):
        """Gets the live_source_type of this LiveSource.  # noqa: E501


        :return: The live_source_type of this LiveSource.  # noqa: E501
        :rtype: str
        """
        return self._live_source_type

    @live_source_type.setter
    def live_source_type(self, live_source_type):
        """Sets the live_source_type of this LiveSource.


        :param live_source_type: The live_source_type of this LiveSource.  # noqa: E501
        :type: str
        """
        allowed_values = ["RSS", "WEBSITE"]  # noqa: E501
        if live_source_type not in allowed_values:
            raise ValueError(
                "Invalid value for `live_source_type` ({0}), must be one of {1}"  # noqa: E501
                .format(live_source_type, allowed_values)
            )

        self._live_source_type = live_source_type

    @property
    def manifold_id(self):
        """Gets the manifold_id of this LiveSource.  # noqa: E501


        :return: The manifold_id of this LiveSource.  # noqa: E501
        :rtype: str
        """
        return self._manifold_id

    @manifold_id.setter
    def manifold_id(self, manifold_id):
        """Sets the manifold_id of this LiveSource.


        :param manifold_id: The manifold_id of this LiveSource.  # noqa: E501
        :type: str
        """

        self._manifold_id = manifold_id

    @property
    def name(self):
        """Gets the name of this LiveSource.  # noqa: E501


        :return: The name of this LiveSource.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this LiveSource.


        :param name: The name of this LiveSource.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def run_mode(self):
        """Gets the run_mode of this LiveSource.  # noqa: E501


        :return: The run_mode of this LiveSource.  # noqa: E501
        :rtype: str
        """
        return self._run_mode

    @run_mode.setter
    def run_mode(self, run_mode):
        """Sets the run_mode of this LiveSource.


        :param run_mode: The run_mode of this LiveSource.  # noqa: E501
        :type: str
        """
        allowed_values = ["SCAN_ONCE", "CONTINUOUS"]  # noqa: E501
        if run_mode not in allowed_values:
            raise ValueError(
                "Invalid value for `run_mode` ({0}), must be one of {1}"  # noqa: E501
                .format(run_mode, allowed_values)
            )

        self._run_mode = run_mode

    @property
    def url(self):
        """Gets the url of this LiveSource.  # noqa: E501


        :return: The url of this LiveSource.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this LiveSource.


        :param url: The url of this LiveSource.  # noqa: E501
        :type: str
        """

        self._url = url

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
        if issubclass(LiveSource, dict):
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
        if not isinstance(other, LiveSource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
