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

class AskQuestionResponseAnswers(object):
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
        'best_prediction': 'str',
        'evidence_text': 'str',
        'passage_ranking_score': 'list[float]',
        'question_text': 'str',
        'nbest_predictions': 'list[AskQuestionResponseNbestPredictions]'
    }

    attribute_map = {
        'id': 'id',
        'best_prediction': 'best_prediction',
        'evidence_text': 'evidence_text',
        'passage_ranking_score': 'passage_ranking_score',
        'question_text': 'question_text',
        'nbest_predictions': 'nbest_predictions'
    }

    def __init__(self, id=None, best_prediction=None, evidence_text=None, passage_ranking_score=None, question_text=None, nbest_predictions=None):  # noqa: E501
        """AskQuestionResponseAnswers - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._best_prediction = None
        self._evidence_text = None
        self._passage_ranking_score = None
        self._question_text = None
        self._nbest_predictions = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if best_prediction is not None:
            self.best_prediction = best_prediction
        if evidence_text is not None:
            self.evidence_text = evidence_text
        if passage_ranking_score is not None:
            self.passage_ranking_score = passage_ranking_score
        if question_text is not None:
            self.question_text = question_text
        if nbest_predictions is not None:
            self.nbest_predictions = nbest_predictions

    @property
    def id(self):
        """Gets the id of this AskQuestionResponseAnswers.  # noqa: E501


        :return: The id of this AskQuestionResponseAnswers.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AskQuestionResponseAnswers.


        :param id: The id of this AskQuestionResponseAnswers.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def best_prediction(self):
        """Gets the best_prediction of this AskQuestionResponseAnswers.  # noqa: E501


        :return: The best_prediction of this AskQuestionResponseAnswers.  # noqa: E501
        :rtype: str
        """
        return self._best_prediction

    @best_prediction.setter
    def best_prediction(self, best_prediction):
        """Sets the best_prediction of this AskQuestionResponseAnswers.


        :param best_prediction: The best_prediction of this AskQuestionResponseAnswers.  # noqa: E501
        :type: str
        """

        self._best_prediction = best_prediction

    @property
    def evidence_text(self):
        """Gets the evidence_text of this AskQuestionResponseAnswers.  # noqa: E501


        :return: The evidence_text of this AskQuestionResponseAnswers.  # noqa: E501
        :rtype: str
        """
        return self._evidence_text

    @evidence_text.setter
    def evidence_text(self, evidence_text):
        """Sets the evidence_text of this AskQuestionResponseAnswers.


        :param evidence_text: The evidence_text of this AskQuestionResponseAnswers.  # noqa: E501
        :type: str
        """

        self._evidence_text = evidence_text

    @property
    def passage_ranking_score(self):
        """Gets the passage_ranking_score of this AskQuestionResponseAnswers.  # noqa: E501


        :return: The passage_ranking_score of this AskQuestionResponseAnswers.  # noqa: E501
        :rtype: list[float]
        """
        return self._passage_ranking_score

    @passage_ranking_score.setter
    def passage_ranking_score(self, passage_ranking_score):
        """Sets the passage_ranking_score of this AskQuestionResponseAnswers.


        :param passage_ranking_score: The passage_ranking_score of this AskQuestionResponseAnswers.  # noqa: E501
        :type: list[float]
        """

        self._passage_ranking_score = passage_ranking_score

    @property
    def question_text(self):
        """Gets the question_text of this AskQuestionResponseAnswers.  # noqa: E501


        :return: The question_text of this AskQuestionResponseAnswers.  # noqa: E501
        :rtype: str
        """
        return self._question_text

    @question_text.setter
    def question_text(self, question_text):
        """Sets the question_text of this AskQuestionResponseAnswers.


        :param question_text: The question_text of this AskQuestionResponseAnswers.  # noqa: E501
        :type: str
        """

        self._question_text = question_text

    @property
    def nbest_predictions(self):
        """Gets the nbest_predictions of this AskQuestionResponseAnswers.  # noqa: E501


        :return: The nbest_predictions of this AskQuestionResponseAnswers.  # noqa: E501
        :rtype: list[AskQuestionResponseNbestPredictions]
        """
        return self._nbest_predictions

    @nbest_predictions.setter
    def nbest_predictions(self, nbest_predictions):
        """Sets the nbest_predictions of this AskQuestionResponseAnswers.


        :param nbest_predictions: The nbest_predictions of this AskQuestionResponseAnswers.  # noqa: E501
        :type: list[AskQuestionResponseNbestPredictions]
        """

        self._nbest_predictions = nbest_predictions

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
        if issubclass(AskQuestionResponseAnswers, dict):
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
        if not isinstance(other, AskQuestionResponseAnswers):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
