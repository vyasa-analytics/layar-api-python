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

class DeepLearningTaskUpdate(object):
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
        'acc_value': 'str',
        'current_step': 'int',
        'file_list': 'list[str]',
        'job_id': 'str',
        'message': 'str',
        'state': 'str',
        'total_steps': 'int'
    }

    attribute_map = {
        'acc_value': 'accValue',
        'current_step': 'currentStep',
        'file_list': 'fileList',
        'job_id': 'jobID',
        'message': 'message',
        'state': 'state',
        'total_steps': 'totalSteps'
    }

    def __init__(self, acc_value=None, current_step=None, file_list=None, job_id=None, message=None, state=None, total_steps=None):  # noqa: E501
        """DeepLearningTaskUpdate - a model defined in Swagger"""  # noqa: E501
        self._acc_value = None
        self._current_step = None
        self._file_list = None
        self._job_id = None
        self._message = None
        self._state = None
        self._total_steps = None
        self.discriminator = None
        if acc_value is not None:
            self.acc_value = acc_value
        if current_step is not None:
            self.current_step = current_step
        if file_list is not None:
            self.file_list = file_list
        if job_id is not None:
            self.job_id = job_id
        if message is not None:
            self.message = message
        if state is not None:
            self.state = state
        if total_steps is not None:
            self.total_steps = total_steps

    @property
    def acc_value(self):
        """Gets the acc_value of this DeepLearningTaskUpdate.  # noqa: E501


        :return: The acc_value of this DeepLearningTaskUpdate.  # noqa: E501
        :rtype: str
        """
        return self._acc_value

    @acc_value.setter
    def acc_value(self, acc_value):
        """Sets the acc_value of this DeepLearningTaskUpdate.


        :param acc_value: The acc_value of this DeepLearningTaskUpdate.  # noqa: E501
        :type: str
        """

        self._acc_value = acc_value

    @property
    def current_step(self):
        """Gets the current_step of this DeepLearningTaskUpdate.  # noqa: E501


        :return: The current_step of this DeepLearningTaskUpdate.  # noqa: E501
        :rtype: int
        """
        return self._current_step

    @current_step.setter
    def current_step(self, current_step):
        """Sets the current_step of this DeepLearningTaskUpdate.


        :param current_step: The current_step of this DeepLearningTaskUpdate.  # noqa: E501
        :type: int
        """

        self._current_step = current_step

    @property
    def file_list(self):
        """Gets the file_list of this DeepLearningTaskUpdate.  # noqa: E501


        :return: The file_list of this DeepLearningTaskUpdate.  # noqa: E501
        :rtype: list[str]
        """
        return self._file_list

    @file_list.setter
    def file_list(self, file_list):
        """Sets the file_list of this DeepLearningTaskUpdate.


        :param file_list: The file_list of this DeepLearningTaskUpdate.  # noqa: E501
        :type: list[str]
        """

        self._file_list = file_list

    @property
    def job_id(self):
        """Gets the job_id of this DeepLearningTaskUpdate.  # noqa: E501


        :return: The job_id of this DeepLearningTaskUpdate.  # noqa: E501
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this DeepLearningTaskUpdate.


        :param job_id: The job_id of this DeepLearningTaskUpdate.  # noqa: E501
        :type: str
        """

        self._job_id = job_id

    @property
    def message(self):
        """Gets the message of this DeepLearningTaskUpdate.  # noqa: E501


        :return: The message of this DeepLearningTaskUpdate.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this DeepLearningTaskUpdate.


        :param message: The message of this DeepLearningTaskUpdate.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def state(self):
        """Gets the state of this DeepLearningTaskUpdate.  # noqa: E501


        :return: The state of this DeepLearningTaskUpdate.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this DeepLearningTaskUpdate.


        :param state: The state of this DeepLearningTaskUpdate.  # noqa: E501
        :type: str
        """

        self._state = state

    @property
    def total_steps(self):
        """Gets the total_steps of this DeepLearningTaskUpdate.  # noqa: E501


        :return: The total_steps of this DeepLearningTaskUpdate.  # noqa: E501
        :rtype: int
        """
        return self._total_steps

    @total_steps.setter
    def total_steps(self, total_steps):
        """Sets the total_steps of this DeepLearningTaskUpdate.


        :param total_steps: The total_steps of this DeepLearningTaskUpdate.  # noqa: E501
        :type: int
        """

        self._total_steps = total_steps

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
        if issubclass(DeepLearningTaskUpdate, dict):
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
        if not isinstance(other, DeepLearningTaskUpdate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
