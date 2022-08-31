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


class EdFiStudentAssessmentStudentObjectiveAssessmentPerformanceLevel(object):
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
        'assessment_reporting_method_descriptor': 'str',
        'performance_level_descriptor': 'str',
        'performance_level_indicator_name': 'str'
    }

    attribute_map = {
        'assessment_reporting_method_descriptor': 'assessmentReportingMethodDescriptor',
        'performance_level_descriptor': 'performanceLevelDescriptor',
        'performance_level_indicator_name': 'performanceLevelIndicatorName'
    }

    def __init__(self, assessment_reporting_method_descriptor=None, performance_level_descriptor=None, performance_level_indicator_name=None, _configuration=None):  # noqa: E501
        """EdFiStudentAssessmentStudentObjectiveAssessmentPerformanceLevel - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._assessment_reporting_method_descriptor = None
        self._performance_level_descriptor = None
        self._performance_level_indicator_name = None
        self.discriminator = None

        self.assessment_reporting_method_descriptor = assessment_reporting_method_descriptor
        self.performance_level_descriptor = performance_level_descriptor
        if performance_level_indicator_name is not None:
            self.performance_level_indicator_name = performance_level_indicator_name

    @property
    def assessment_reporting_method_descriptor(self):
        """Gets the assessment_reporting_method_descriptor of this EdFiStudentAssessmentStudentObjectiveAssessmentPerformanceLevel.  # noqa: E501

        The method that the instructor of the class uses to report the performance and achievement. It may be a qualitative method such as individualized teacher comments or a quantitative method such as a letter or numerical grade. In some cases, more than one type of reporting method may be used.  # noqa: E501

        :return: The assessment_reporting_method_descriptor of this EdFiStudentAssessmentStudentObjectiveAssessmentPerformanceLevel.  # noqa: E501
        :rtype: str
        """
        return self._assessment_reporting_method_descriptor

    @assessment_reporting_method_descriptor.setter
    def assessment_reporting_method_descriptor(self, assessment_reporting_method_descriptor):
        """Sets the assessment_reporting_method_descriptor of this EdFiStudentAssessmentStudentObjectiveAssessmentPerformanceLevel.

        The method that the instructor of the class uses to report the performance and achievement. It may be a qualitative method such as individualized teacher comments or a quantitative method such as a letter or numerical grade. In some cases, more than one type of reporting method may be used.  # noqa: E501

        :param assessment_reporting_method_descriptor: The assessment_reporting_method_descriptor of this EdFiStudentAssessmentStudentObjectiveAssessmentPerformanceLevel.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and assessment_reporting_method_descriptor is None:
            raise ValueError("Invalid value for `assessment_reporting_method_descriptor`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                assessment_reporting_method_descriptor is not None and len(assessment_reporting_method_descriptor) > 306):
            raise ValueError("Invalid value for `assessment_reporting_method_descriptor`, length must be less than or equal to `306`")  # noqa: E501

        self._assessment_reporting_method_descriptor = assessment_reporting_method_descriptor

    @property
    def performance_level_descriptor(self):
        """Gets the performance_level_descriptor of this EdFiStudentAssessmentStudentObjectiveAssessmentPerformanceLevel.  # noqa: E501

        A specification of which performance level value describes the student proficiency.  # noqa: E501

        :return: The performance_level_descriptor of this EdFiStudentAssessmentStudentObjectiveAssessmentPerformanceLevel.  # noqa: E501
        :rtype: str
        """
        return self._performance_level_descriptor

    @performance_level_descriptor.setter
    def performance_level_descriptor(self, performance_level_descriptor):
        """Sets the performance_level_descriptor of this EdFiStudentAssessmentStudentObjectiveAssessmentPerformanceLevel.

        A specification of which performance level value describes the student proficiency.  # noqa: E501

        :param performance_level_descriptor: The performance_level_descriptor of this EdFiStudentAssessmentStudentObjectiveAssessmentPerformanceLevel.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and performance_level_descriptor is None:
            raise ValueError("Invalid value for `performance_level_descriptor`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                performance_level_descriptor is not None and len(performance_level_descriptor) > 306):
            raise ValueError("Invalid value for `performance_level_descriptor`, length must be less than or equal to `306`")  # noqa: E501

        self._performance_level_descriptor = performance_level_descriptor

    @property
    def performance_level_indicator_name(self):
        """Gets the performance_level_indicator_name of this EdFiStudentAssessmentStudentObjectiveAssessmentPerformanceLevel.  # noqa: E501

        The name of the indicator being measured for a collection of performance level values.  # noqa: E501

        :return: The performance_level_indicator_name of this EdFiStudentAssessmentStudentObjectiveAssessmentPerformanceLevel.  # noqa: E501
        :rtype: str
        """
        return self._performance_level_indicator_name

    @performance_level_indicator_name.setter
    def performance_level_indicator_name(self, performance_level_indicator_name):
        """Sets the performance_level_indicator_name of this EdFiStudentAssessmentStudentObjectiveAssessmentPerformanceLevel.

        The name of the indicator being measured for a collection of performance level values.  # noqa: E501

        :param performance_level_indicator_name: The performance_level_indicator_name of this EdFiStudentAssessmentStudentObjectiveAssessmentPerformanceLevel.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                performance_level_indicator_name is not None and len(performance_level_indicator_name) > 60):
            raise ValueError("Invalid value for `performance_level_indicator_name`, length must be less than or equal to `60`")  # noqa: E501

        self._performance_level_indicator_name = performance_level_indicator_name

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
        if issubclass(EdFiStudentAssessmentStudentObjectiveAssessmentPerformanceLevel, dict):
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
        if not isinstance(other, EdFiStudentAssessmentStudentObjectiveAssessmentPerformanceLevel):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EdFiStudentAssessmentStudentObjectiveAssessmentPerformanceLevel):
            return True

        return self.to_dict() != other.to_dict()
