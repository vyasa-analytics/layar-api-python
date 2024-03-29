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
from layar_api.models.domain_object import DomainObject  # noqa: F401,E501

class QuestionBatch(DomainObject):
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
        'job_id': 'str',
        'batch_grouping_key': 'str',
        'question_keys': 'list[str]',
        'saved_list_ids': 'list[str]',
        'question_count': 'int',
        'questions_queued': 'int',
        'questions_completed': 'int',
        'questions_answered': 'int',
        'questions_skipped': 'int',
        'questions_failed': 'int'
    }
    if hasattr(DomainObject, "swagger_types"):
        swagger_types.update(DomainObject.swagger_types)

    attribute_map = {
        'id': 'id',
        'job_id': 'jobID',
        'batch_grouping_key': 'batchGroupingKey',
        'question_keys': 'questionKeys',
        'saved_list_ids': 'savedListIds',
        'question_count': 'questionCount',
        'questions_queued': 'questionsQueued',
        'questions_completed': 'questionsCompleted',
        'questions_answered': 'questionsAnswered',
        'questions_skipped': 'questionsSkipped',
        'questions_failed': 'questionsFailed'
    }
    if hasattr(DomainObject, "attribute_map"):
        attribute_map.update(DomainObject.attribute_map)

    def __init__(self, id=None, job_id=None, batch_grouping_key=None, question_keys=None, saved_list_ids=None, question_count=None, questions_queued=None, questions_completed=None, questions_answered=None, questions_skipped=None, questions_failed=None, *args, **kwargs):  # noqa: E501
        """QuestionBatch - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._job_id = None
        self._batch_grouping_key = None
        self._question_keys = None
        self._saved_list_ids = None
        self._question_count = None
        self._questions_queued = None
        self._questions_completed = None
        self._questions_answered = None
        self._questions_skipped = None
        self._questions_failed = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if job_id is not None:
            self.job_id = job_id
        if batch_grouping_key is not None:
            self.batch_grouping_key = batch_grouping_key
        if question_keys is not None:
            self.question_keys = question_keys
        if saved_list_ids is not None:
            self.saved_list_ids = saved_list_ids
        if question_count is not None:
            self.question_count = question_count
        if questions_queued is not None:
            self.questions_queued = questions_queued
        if questions_completed is not None:
            self.questions_completed = questions_completed
        if questions_answered is not None:
            self.questions_answered = questions_answered
        if questions_skipped is not None:
            self.questions_skipped = questions_skipped
        if questions_failed is not None:
            self.questions_failed = questions_failed
        DomainObject.__init__(self, *args, **kwargs)

    @property
    def id(self):
        """Gets the id of this QuestionBatch.  # noqa: E501

        A unique identifier for the questionBatch object  # noqa: E501

        :return: The id of this QuestionBatch.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this QuestionBatch.

        A unique identifier for the questionBatch object  # noqa: E501

        :param id: The id of this QuestionBatch.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def job_id(self):
        """Gets the job_id of this QuestionBatch.  # noqa: E501

        A unique identifier programmatically assigned to the Bulk QA job  # noqa: E501

        :return: The job_id of this QuestionBatch.  # noqa: E501
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this QuestionBatch.

        A unique identifier programmatically assigned to the Bulk QA job  # noqa: E501

        :param job_id: The job_id of this QuestionBatch.  # noqa: E501
        :type: str
        """

        self._job_id = job_id

    @property
    def batch_grouping_key(self):
        """Gets the batch_grouping_key of this QuestionBatch.  # noqa: E501

        User assigned key for a QA batch (e.g. \"Batch_QA_V1\")  # noqa: E501

        :return: The batch_grouping_key of this QuestionBatch.  # noqa: E501
        :rtype: str
        """
        return self._batch_grouping_key

    @batch_grouping_key.setter
    def batch_grouping_key(self, batch_grouping_key):
        """Sets the batch_grouping_key of this QuestionBatch.

        User assigned key for a QA batch (e.g. \"Batch_QA_V1\")  # noqa: E501

        :param batch_grouping_key: The batch_grouping_key of this QuestionBatch.  # noqa: E501
        :type: str
        """

        self._batch_grouping_key = batch_grouping_key

    @property
    def question_keys(self):
        """Gets the question_keys of this QuestionBatch.  # noqa: E501

        User assigned key for a question within the QA batch (e.g. \"Study Drug\")  # noqa: E501

        :return: The question_keys of this QuestionBatch.  # noqa: E501
        :rtype: list[str]
        """
        return self._question_keys

    @question_keys.setter
    def question_keys(self, question_keys):
        """Sets the question_keys of this QuestionBatch.

        User assigned key for a question within the QA batch (e.g. \"Study Drug\")  # noqa: E501

        :param question_keys: The question_keys of this QuestionBatch.  # noqa: E501
        :type: list[str]
        """

        self._question_keys = question_keys

    @property
    def saved_list_ids(self):
        """Gets the saved_list_ids of this QuestionBatch.  # noqa: E501

        IDs of the Layar Sets used when submitting a Bulk QA job  # noqa: E501

        :return: The saved_list_ids of this QuestionBatch.  # noqa: E501
        :rtype: list[str]
        """
        return self._saved_list_ids

    @saved_list_ids.setter
    def saved_list_ids(self, saved_list_ids):
        """Sets the saved_list_ids of this QuestionBatch.

        IDs of the Layar Sets used when submitting a Bulk QA job  # noqa: E501

        :param saved_list_ids: The saved_list_ids of this QuestionBatch.  # noqa: E501
        :type: list[str]
        """

        self._saved_list_ids = saved_list_ids

    @property
    def question_count(self):
        """Gets the question_count of this QuestionBatch.  # noqa: E501

        The total number of questions in this batch. Sum of queued and completed.  # noqa: E501

        :return: The question_count of this QuestionBatch.  # noqa: E501
        :rtype: int
        """
        return self._question_count

    @question_count.setter
    def question_count(self, question_count):
        """Sets the question_count of this QuestionBatch.

        The total number of questions in this batch. Sum of queued and completed.  # noqa: E501

        :param question_count: The question_count of this QuestionBatch.  # noqa: E501
        :type: int
        """

        self._question_count = question_count

    @property
    def questions_queued(self):
        """Gets the questions_queued of this QuestionBatch.  # noqa: E501

        Questions yet to be answered  # noqa: E501

        :return: The questions_queued of this QuestionBatch.  # noqa: E501
        :rtype: int
        """
        return self._questions_queued

    @questions_queued.setter
    def questions_queued(self, questions_queued):
        """Sets the questions_queued of this QuestionBatch.

        Questions yet to be answered  # noqa: E501

        :param questions_queued: The questions_queued of this QuestionBatch.  # noqa: E501
        :type: int
        """

        self._questions_queued = questions_queued

    @property
    def questions_completed(self):
        """Gets the questions_completed of this QuestionBatch.  # noqa: E501

        Should always be the sum of answered, skipped, and failed  # noqa: E501

        :return: The questions_completed of this QuestionBatch.  # noqa: E501
        :rtype: int
        """
        return self._questions_completed

    @questions_completed.setter
    def questions_completed(self, questions_completed):
        """Sets the questions_completed of this QuestionBatch.

        Should always be the sum of answered, skipped, and failed  # noqa: E501

        :param questions_completed: The questions_completed of this QuestionBatch.  # noqa: E501
        :type: int
        """

        self._questions_completed = questions_completed

    @property
    def questions_answered(self):
        """Gets the questions_answered of this QuestionBatch.  # noqa: E501

        Successfully submitted to the QA service and a response received  # noqa: E501

        :return: The questions_answered of this QuestionBatch.  # noqa: E501
        :rtype: int
        """
        return self._questions_answered

    @questions_answered.setter
    def questions_answered(self, questions_answered):
        """Sets the questions_answered of this QuestionBatch.

        Successfully submitted to the QA service and a response received  # noqa: E501

        :param questions_answered: The questions_answered of this QuestionBatch.  # noqa: E501
        :type: int
        """

        self._questions_answered = questions_answered

    @property
    def questions_skipped(self):
        """Gets the questions_skipped of this QuestionBatch.  # noqa: E501

        Skipped because the batch was cancelled  # noqa: E501

        :return: The questions_skipped of this QuestionBatch.  # noqa: E501
        :rtype: int
        """
        return self._questions_skipped

    @questions_skipped.setter
    def questions_skipped(self, questions_skipped):
        """Sets the questions_skipped of this QuestionBatch.

        Skipped because the batch was cancelled  # noqa: E501

        :param questions_skipped: The questions_skipped of this QuestionBatch.  # noqa: E501
        :type: int
        """

        self._questions_skipped = questions_skipped

    @property
    def questions_failed(self):
        """Gets the questions_failed of this QuestionBatch.  # noqa: E501

        Error submitting to QA service or processing the response  # noqa: E501

        :return: The questions_failed of this QuestionBatch.  # noqa: E501
        :rtype: int
        """
        return self._questions_failed

    @questions_failed.setter
    def questions_failed(self, questions_failed):
        """Sets the questions_failed of this QuestionBatch.

        Error submitting to QA service or processing the response  # noqa: E501

        :param questions_failed: The questions_failed of this QuestionBatch.  # noqa: E501
        :type: int
        """

        self._questions_failed = questions_failed

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
        if issubclass(QuestionBatch, dict):
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
        if not isinstance(other, QuestionBatch):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
