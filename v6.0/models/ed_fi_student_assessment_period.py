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


class EdFiStudentAssessmentPeriod(object):
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
        'assessment_period_descriptor': 'str',
        'begin_date': 'date',
        'end_date': 'date'
    }

    attribute_map = {
        'assessment_period_descriptor': 'assessmentPeriodDescriptor',
        'begin_date': 'beginDate',
        'end_date': 'endDate'
    }

    def __init__(self, assessment_period_descriptor=None, begin_date=None, end_date=None, _configuration=None):  # noqa: E501
        """EdFiStudentAssessmentPeriod - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._assessment_period_descriptor = None
        self._begin_date = None
        self._end_date = None
        self.discriminator = None

        self.assessment_period_descriptor = assessment_period_descriptor
        if begin_date is not None:
            self.begin_date = begin_date
        if end_date is not None:
            self.end_date = end_date

    @property
    def assessment_period_descriptor(self):
        """Gets the assessment_period_descriptor of this EdFiStudentAssessmentPeriod.  # noqa: E501

        The period of time in which an assessment is supposed to be administered (e.g., Beginning of Year, Middle of Year, End of Year).  # noqa: E501

        :return: The assessment_period_descriptor of this EdFiStudentAssessmentPeriod.  # noqa: E501
        :rtype: str
        """
        return self._assessment_period_descriptor

    @assessment_period_descriptor.setter
    def assessment_period_descriptor(self, assessment_period_descriptor):
        """Sets the assessment_period_descriptor of this EdFiStudentAssessmentPeriod.

        The period of time in which an assessment is supposed to be administered (e.g., Beginning of Year, Middle of Year, End of Year).  # noqa: E501

        :param assessment_period_descriptor: The assessment_period_descriptor of this EdFiStudentAssessmentPeriod.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and assessment_period_descriptor is None:
            raise ValueError("Invalid value for `assessment_period_descriptor`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                assessment_period_descriptor is not None and len(assessment_period_descriptor) > 306):
            raise ValueError("Invalid value for `assessment_period_descriptor`, length must be less than or equal to `306`")  # noqa: E501

        self._assessment_period_descriptor = assessment_period_descriptor

    @property
    def begin_date(self):
        """Gets the begin_date of this EdFiStudentAssessmentPeriod.  # noqa: E501

        The first date the assessment is to be administered.  # noqa: E501

        :return: The begin_date of this EdFiStudentAssessmentPeriod.  # noqa: E501
        :rtype: date
        """
        return self._begin_date

    @begin_date.setter
    def begin_date(self, begin_date):
        """Sets the begin_date of this EdFiStudentAssessmentPeriod.

        The first date the assessment is to be administered.  # noqa: E501

        :param begin_date: The begin_date of this EdFiStudentAssessmentPeriod.  # noqa: E501
        :type: date
        """

        self._begin_date = begin_date

    @property
    def end_date(self):
        """Gets the end_date of this EdFiStudentAssessmentPeriod.  # noqa: E501

        The last date the assessment is to be administered.  # noqa: E501

        :return: The end_date of this EdFiStudentAssessmentPeriod.  # noqa: E501
        :rtype: date
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this EdFiStudentAssessmentPeriod.

        The last date the assessment is to be administered.  # noqa: E501

        :param end_date: The end_date of this EdFiStudentAssessmentPeriod.  # noqa: E501
        :type: date
        """

        self._end_date = end_date

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
        if issubclass(EdFiStudentAssessmentPeriod, dict):
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
        if not isinstance(other, EdFiStudentAssessmentPeriod):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EdFiStudentAssessmentPeriod):
            return True

        return self.to_dict() != other.to_dict()
