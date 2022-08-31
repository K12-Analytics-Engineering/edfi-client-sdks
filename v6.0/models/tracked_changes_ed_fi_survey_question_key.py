# coding: utf-8

"""
    Ed-Fi Operational Data Store API

    The Ed-Fi ODS / API enables applications to read and write education data stored in an Ed-Fi ODS through a secure REST interface.  ***  > *Note: Consumers of ODS / API information should sanitize all data for display and storage. The ODS / API provides reasonable safeguards against cross-site scripting attacks and other malicious content, but the platform does not and cannot guarantee that the data it contains is free of all potentially harmful content.*  ***   # noqa: E501

    OpenAPI spec version: 3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from swagger_client.configuration import Configuration


class TrackedChangesEdFiSurveyQuestionKey(object):
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
        'question_code': 'str',
        'namespace': 'str',
        'survey_identifier': 'str'
    }

    attribute_map = {
        'question_code': 'questionCode',
        'namespace': 'namespace',
        'survey_identifier': 'surveyIdentifier'
    }

    def __init__(self, question_code=None, namespace=None, survey_identifier=None, _configuration=None):  # noqa: E501
        """TrackedChangesEdFiSurveyQuestionKey - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._question_code = None
        self._namespace = None
        self._survey_identifier = None
        self.discriminator = None

        if question_code is not None:
            self.question_code = question_code
        if namespace is not None:
            self.namespace = namespace
        if survey_identifier is not None:
            self.survey_identifier = survey_identifier

    @property
    def question_code(self):
        """Gets the question_code of this TrackedChangesEdFiSurveyQuestionKey.  # noqa: E501

        The identifying code for the question, unique for the survey.  # noqa: E501

        :return: The question_code of this TrackedChangesEdFiSurveyQuestionKey.  # noqa: E501
        :rtype: str
        """
        return self._question_code

    @question_code.setter
    def question_code(self, question_code):
        """Sets the question_code of this TrackedChangesEdFiSurveyQuestionKey.

        The identifying code for the question, unique for the survey.  # noqa: E501

        :param question_code: The question_code of this TrackedChangesEdFiSurveyQuestionKey.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                question_code is not None and len(question_code) > 60):
            raise ValueError("Invalid value for `question_code`, length must be less than or equal to `60`")  # noqa: E501

        self._question_code = question_code

    @property
    def namespace(self):
        """Gets the namespace of this TrackedChangesEdFiSurveyQuestionKey.  # noqa: E501

        Namespace for the survey.  # noqa: E501

        :return: The namespace of this TrackedChangesEdFiSurveyQuestionKey.  # noqa: E501
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """Sets the namespace of this TrackedChangesEdFiSurveyQuestionKey.

        Namespace for the survey.  # noqa: E501

        :param namespace: The namespace of this TrackedChangesEdFiSurveyQuestionKey.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                namespace is not None and len(namespace) > 255):
            raise ValueError("Invalid value for `namespace`, length must be less than or equal to `255`")  # noqa: E501

        self._namespace = namespace

    @property
    def survey_identifier(self):
        """Gets the survey_identifier of this TrackedChangesEdFiSurveyQuestionKey.  # noqa: E501

        The unique survey identifier from the survey tool.  # noqa: E501

        :return: The survey_identifier of this TrackedChangesEdFiSurveyQuestionKey.  # noqa: E501
        :rtype: str
        """
        return self._survey_identifier

    @survey_identifier.setter
    def survey_identifier(self, survey_identifier):
        """Sets the survey_identifier of this TrackedChangesEdFiSurveyQuestionKey.

        The unique survey identifier from the survey tool.  # noqa: E501

        :param survey_identifier: The survey_identifier of this TrackedChangesEdFiSurveyQuestionKey.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                survey_identifier is not None and len(survey_identifier) > 60):
            raise ValueError("Invalid value for `survey_identifier`, length must be less than or equal to `60`")  # noqa: E501

        self._survey_identifier = survey_identifier

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
        if issubclass(TrackedChangesEdFiSurveyQuestionKey, dict):
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
        if not isinstance(other, TrackedChangesEdFiSurveyQuestionKey):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TrackedChangesEdFiSurveyQuestionKey):
            return True

        return self.to_dict() != other.to_dict()
