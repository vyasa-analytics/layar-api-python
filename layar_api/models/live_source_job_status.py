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

class LiveSourceJobStatus(object):
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
        'start_time': 'float',
        'outstanding_exact': 'bool',
        'queue_exact': 'bool',
        'processed_exact': 'bool',
        'job_id': 'str',
        'status': 'str',
        'documents_outstanding': 'float',
        'documents_processed': 'float',
        'documents_in_queue': 'float'
    }

    attribute_map = {
        'start_time': 'startTime',
        'outstanding_exact': 'outstandingExact',
        'queue_exact': 'queueExact',
        'processed_exact': 'processedExact',
        'job_id': 'jobId',
        'status': 'status',
        'documents_outstanding': 'documentsOutstanding',
        'documents_processed': 'documentsProcessed',
        'documents_in_queue': 'documentsInQueue'
    }

    def __init__(self, start_time=None, outstanding_exact=None, queue_exact=None, processed_exact=None, job_id=None, status=None, documents_outstanding=None, documents_processed=None, documents_in_queue=None):  # noqa: E501
        """LiveSourceJobStatus - a model defined in Swagger"""  # noqa: E501
        self._start_time = None
        self._outstanding_exact = None
        self._queue_exact = None
        self._processed_exact = None
        self._job_id = None
        self._status = None
        self._documents_outstanding = None
        self._documents_processed = None
        self._documents_in_queue = None
        self.discriminator = None
        if start_time is not None:
            self.start_time = start_time
        if outstanding_exact is not None:
            self.outstanding_exact = outstanding_exact
        if queue_exact is not None:
            self.queue_exact = queue_exact
        if processed_exact is not None:
            self.processed_exact = processed_exact
        if job_id is not None:
            self.job_id = job_id
        if status is not None:
            self.status = status
        if documents_outstanding is not None:
            self.documents_outstanding = documents_outstanding
        if documents_processed is not None:
            self.documents_processed = documents_processed
        if documents_in_queue is not None:
            self.documents_in_queue = documents_in_queue

    @property
    def start_time(self):
        """Gets the start_time of this LiveSourceJobStatus.  # noqa: E501


        :return: The start_time of this LiveSourceJobStatus.  # noqa: E501
        :rtype: float
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this LiveSourceJobStatus.


        :param start_time: The start_time of this LiveSourceJobStatus.  # noqa: E501
        :type: float
        """

        self._start_time = start_time

    @property
    def outstanding_exact(self):
        """Gets the outstanding_exact of this LiveSourceJobStatus.  # noqa: E501


        :return: The outstanding_exact of this LiveSourceJobStatus.  # noqa: E501
        :rtype: bool
        """
        return self._outstanding_exact

    @outstanding_exact.setter
    def outstanding_exact(self, outstanding_exact):
        """Sets the outstanding_exact of this LiveSourceJobStatus.


        :param outstanding_exact: The outstanding_exact of this LiveSourceJobStatus.  # noqa: E501
        :type: bool
        """

        self._outstanding_exact = outstanding_exact

    @property
    def queue_exact(self):
        """Gets the queue_exact of this LiveSourceJobStatus.  # noqa: E501


        :return: The queue_exact of this LiveSourceJobStatus.  # noqa: E501
        :rtype: bool
        """
        return self._queue_exact

    @queue_exact.setter
    def queue_exact(self, queue_exact):
        """Sets the queue_exact of this LiveSourceJobStatus.


        :param queue_exact: The queue_exact of this LiveSourceJobStatus.  # noqa: E501
        :type: bool
        """

        self._queue_exact = queue_exact

    @property
    def processed_exact(self):
        """Gets the processed_exact of this LiveSourceJobStatus.  # noqa: E501


        :return: The processed_exact of this LiveSourceJobStatus.  # noqa: E501
        :rtype: bool
        """
        return self._processed_exact

    @processed_exact.setter
    def processed_exact(self, processed_exact):
        """Sets the processed_exact of this LiveSourceJobStatus.


        :param processed_exact: The processed_exact of this LiveSourceJobStatus.  # noqa: E501
        :type: bool
        """

        self._processed_exact = processed_exact

    @property
    def job_id(self):
        """Gets the job_id of this LiveSourceJobStatus.  # noqa: E501


        :return: The job_id of this LiveSourceJobStatus.  # noqa: E501
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this LiveSourceJobStatus.


        :param job_id: The job_id of this LiveSourceJobStatus.  # noqa: E501
        :type: str
        """

        self._job_id = job_id

    @property
    def status(self):
        """Gets the status of this LiveSourceJobStatus.  # noqa: E501


        :return: The status of this LiveSourceJobStatus.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this LiveSourceJobStatus.


        :param status: The status of this LiveSourceJobStatus.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def documents_outstanding(self):
        """Gets the documents_outstanding of this LiveSourceJobStatus.  # noqa: E501


        :return: The documents_outstanding of this LiveSourceJobStatus.  # noqa: E501
        :rtype: float
        """
        return self._documents_outstanding

    @documents_outstanding.setter
    def documents_outstanding(self, documents_outstanding):
        """Sets the documents_outstanding of this LiveSourceJobStatus.


        :param documents_outstanding: The documents_outstanding of this LiveSourceJobStatus.  # noqa: E501
        :type: float
        """

        self._documents_outstanding = documents_outstanding

    @property
    def documents_processed(self):
        """Gets the documents_processed of this LiveSourceJobStatus.  # noqa: E501


        :return: The documents_processed of this LiveSourceJobStatus.  # noqa: E501
        :rtype: float
        """
        return self._documents_processed

    @documents_processed.setter
    def documents_processed(self, documents_processed):
        """Sets the documents_processed of this LiveSourceJobStatus.


        :param documents_processed: The documents_processed of this LiveSourceJobStatus.  # noqa: E501
        :type: float
        """

        self._documents_processed = documents_processed

    @property
    def documents_in_queue(self):
        """Gets the documents_in_queue of this LiveSourceJobStatus.  # noqa: E501


        :return: The documents_in_queue of this LiveSourceJobStatus.  # noqa: E501
        :rtype: float
        """
        return self._documents_in_queue

    @documents_in_queue.setter
    def documents_in_queue(self, documents_in_queue):
        """Sets the documents_in_queue of this LiveSourceJobStatus.


        :param documents_in_queue: The documents_in_queue of this LiveSourceJobStatus.  # noqa: E501
        :type: float
        """

        self._documents_in_queue = documents_in_queue

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
        if issubclass(LiveSourceJobStatus, dict):
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
        if not isinstance(other, LiveSourceJobStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
