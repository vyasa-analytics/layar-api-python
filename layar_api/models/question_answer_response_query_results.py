# coding: utf-8

"""
    Layar API Documentation

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class QuestionAnswerResponseQueryResults(object):
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
        'nbest_predictions': 'object',
        'predictions': 'object'
    }

    attribute_map = {
        'nbest_predictions': 'nbest_predictions',
        'predictions': 'predictions'
    }

    def __init__(self, nbest_predictions=None, predictions=None):  # noqa: E501
        """QuestionAnswerResponseQueryResults - a model defined in Swagger"""  # noqa: E501
        self._nbest_predictions = None
        self._predictions = None
        self.discriminator = None
        if nbest_predictions is not None:
            self.nbest_predictions = nbest_predictions
        if predictions is not None:
            self.predictions = predictions

    @property
    def nbest_predictions(self):
        """Gets the nbest_predictions of this QuestionAnswerResponseQueryResults.  # noqa: E501


        :return: The nbest_predictions of this QuestionAnswerResponseQueryResults.  # noqa: E501
        :rtype: object
        """
        return self._nbest_predictions

    @nbest_predictions.setter
    def nbest_predictions(self, nbest_predictions):
        """Sets the nbest_predictions of this QuestionAnswerResponseQueryResults.


        :param nbest_predictions: The nbest_predictions of this QuestionAnswerResponseQueryResults.  # noqa: E501
        :type: object
        """

        self._nbest_predictions = nbest_predictions

    @property
    def predictions(self):
        """Gets the predictions of this QuestionAnswerResponseQueryResults.  # noqa: E501


        :return: The predictions of this QuestionAnswerResponseQueryResults.  # noqa: E501
        :rtype: object
        """
        return self._predictions

    @predictions.setter
    def predictions(self, predictions):
        """Sets the predictions of this QuestionAnswerResponseQueryResults.


        :param predictions: The predictions of this QuestionAnswerResponseQueryResults.  # noqa: E501
        :type: object
        """

        self._predictions = predictions

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
        if issubclass(QuestionAnswerResponseQueryResults, dict):
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
        if not isinstance(other, QuestionAnswerResponseQueryResults):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
