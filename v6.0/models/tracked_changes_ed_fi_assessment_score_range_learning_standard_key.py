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


class TrackedChangesEdFiAssessmentScoreRangeLearningStandardKey(object):
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
        'score_range_id': 'str',
        'assessment_identifier': 'str',
        'namespace': 'str'
    }

    attribute_map = {
        'score_range_id': 'scoreRangeId',
        'assessment_identifier': 'assessmentIdentifier',
        'namespace': 'namespace'
    }

    def __init__(self, score_range_id=None, assessment_identifier=None, namespace=None, _configuration=None):  # noqa: E501
        """TrackedChangesEdFiAssessmentScoreRangeLearningStandardKey - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._score_range_id = None
        self._assessment_identifier = None
        self._namespace = None
        self.discriminator = None

        if score_range_id is not None:
            self.score_range_id = score_range_id
        if assessment_identifier is not None:
            self.assessment_identifier = assessment_identifier
        if namespace is not None:
            self.namespace = namespace

    @property
    def score_range_id(self):
        """Gets the score_range_id of this TrackedChangesEdFiAssessmentScoreRangeLearningStandardKey.  # noqa: E501

        A unique number or alphanumeric code assigned to the score range associated with one or more learning standards.  # noqa: E501

        :return: The score_range_id of this TrackedChangesEdFiAssessmentScoreRangeLearningStandardKey.  # noqa: E501
        :rtype: str
        """
        return self._score_range_id

    @score_range_id.setter
    def score_range_id(self, score_range_id):
        """Sets the score_range_id of this TrackedChangesEdFiAssessmentScoreRangeLearningStandardKey.

        A unique number or alphanumeric code assigned to the score range associated with one or more learning standards.  # noqa: E501

        :param score_range_id: The score_range_id of this TrackedChangesEdFiAssessmentScoreRangeLearningStandardKey.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                score_range_id is not None and len(score_range_id) > 60):
            raise ValueError("Invalid value for `score_range_id`, length must be less than or equal to `60`")  # noqa: E501

        self._score_range_id = score_range_id

    @property
    def assessment_identifier(self):
        """Gets the assessment_identifier of this TrackedChangesEdFiAssessmentScoreRangeLearningStandardKey.  # noqa: E501

        A unique number or alphanumeric code assigned to an assessment.  # noqa: E501

        :return: The assessment_identifier of this TrackedChangesEdFiAssessmentScoreRangeLearningStandardKey.  # noqa: E501
        :rtype: str
        """
        return self._assessment_identifier

    @assessment_identifier.setter
    def assessment_identifier(self, assessment_identifier):
        """Sets the assessment_identifier of this TrackedChangesEdFiAssessmentScoreRangeLearningStandardKey.

        A unique number or alphanumeric code assigned to an assessment.  # noqa: E501

        :param assessment_identifier: The assessment_identifier of this TrackedChangesEdFiAssessmentScoreRangeLearningStandardKey.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                assessment_identifier is not None and len(assessment_identifier) > 60):
            raise ValueError("Invalid value for `assessment_identifier`, length must be less than or equal to `60`")  # noqa: E501

        self._assessment_identifier = assessment_identifier

    @property
    def namespace(self):
        """Gets the namespace of this TrackedChangesEdFiAssessmentScoreRangeLearningStandardKey.  # noqa: E501

        Namespace for the assessment.  # noqa: E501

        :return: The namespace of this TrackedChangesEdFiAssessmentScoreRangeLearningStandardKey.  # noqa: E501
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """Sets the namespace of this TrackedChangesEdFiAssessmentScoreRangeLearningStandardKey.

        Namespace for the assessment.  # noqa: E501

        :param namespace: The namespace of this TrackedChangesEdFiAssessmentScoreRangeLearningStandardKey.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                namespace is not None and len(namespace) > 255):
            raise ValueError("Invalid value for `namespace`, length must be less than or equal to `255`")  # noqa: E501

        self._namespace = namespace

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
        if issubclass(TrackedChangesEdFiAssessmentScoreRangeLearningStandardKey, dict):
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
        if not isinstance(other, TrackedChangesEdFiAssessmentScoreRangeLearningStandardKey):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TrackedChangesEdFiAssessmentScoreRangeLearningStandardKey):
            return True

        return self.to_dict() != other.to_dict()
