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


class EdFiGradingPeriodReference(object):
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
        'grading_period_descriptor': 'str',
        'period_sequence': 'int',
        'school_id': 'int',
        'school_year': 'int',
        'link': 'Link'
    }

    attribute_map = {
        'grading_period_descriptor': 'gradingPeriodDescriptor',
        'period_sequence': 'periodSequence',
        'school_id': 'schoolId',
        'school_year': 'schoolYear',
        'link': 'link'
    }

    def __init__(self, grading_period_descriptor=None, period_sequence=None, school_id=None, school_year=None, link=None, _configuration=None):  # noqa: E501
        """EdFiGradingPeriodReference - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._grading_period_descriptor = None
        self._period_sequence = None
        self._school_id = None
        self._school_year = None
        self._link = None
        self.discriminator = None

        self.grading_period_descriptor = grading_period_descriptor
        self.period_sequence = period_sequence
        self.school_id = school_id
        self.school_year = school_year
        if link is not None:
            self.link = link

    @property
    def grading_period_descriptor(self):
        """Gets the grading_period_descriptor of this EdFiGradingPeriodReference.  # noqa: E501

        The name of the period for which grades are reported.  # noqa: E501

        :return: The grading_period_descriptor of this EdFiGradingPeriodReference.  # noqa: E501
        :rtype: str
        """
        return self._grading_period_descriptor

    @grading_period_descriptor.setter
    def grading_period_descriptor(self, grading_period_descriptor):
        """Sets the grading_period_descriptor of this EdFiGradingPeriodReference.

        The name of the period for which grades are reported.  # noqa: E501

        :param grading_period_descriptor: The grading_period_descriptor of this EdFiGradingPeriodReference.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and grading_period_descriptor is None:
            raise ValueError("Invalid value for `grading_period_descriptor`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                grading_period_descriptor is not None and len(grading_period_descriptor) > 306):
            raise ValueError("Invalid value for `grading_period_descriptor`, length must be less than or equal to `306`")  # noqa: E501

        self._grading_period_descriptor = grading_period_descriptor

    @property
    def period_sequence(self):
        """Gets the period_sequence of this EdFiGradingPeriodReference.  # noqa: E501

        The sequential order of this period relative to other periods.  # noqa: E501

        :return: The period_sequence of this EdFiGradingPeriodReference.  # noqa: E501
        :rtype: int
        """
        return self._period_sequence

    @period_sequence.setter
    def period_sequence(self, period_sequence):
        """Sets the period_sequence of this EdFiGradingPeriodReference.

        The sequential order of this period relative to other periods.  # noqa: E501

        :param period_sequence: The period_sequence of this EdFiGradingPeriodReference.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and period_sequence is None:
            raise ValueError("Invalid value for `period_sequence`, must not be `None`")  # noqa: E501

        self._period_sequence = period_sequence

    @property
    def school_id(self):
        """Gets the school_id of this EdFiGradingPeriodReference.  # noqa: E501

        The identifier assigned to a school.  # noqa: E501

        :return: The school_id of this EdFiGradingPeriodReference.  # noqa: E501
        :rtype: int
        """
        return self._school_id

    @school_id.setter
    def school_id(self, school_id):
        """Sets the school_id of this EdFiGradingPeriodReference.

        The identifier assigned to a school.  # noqa: E501

        :param school_id: The school_id of this EdFiGradingPeriodReference.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and school_id is None:
            raise ValueError("Invalid value for `school_id`, must not be `None`")  # noqa: E501

        self._school_id = school_id

    @property
    def school_year(self):
        """Gets the school_year of this EdFiGradingPeriodReference.  # noqa: E501

        The identifier for the grading period school year.  # noqa: E501

        :return: The school_year of this EdFiGradingPeriodReference.  # noqa: E501
        :rtype: int
        """
        return self._school_year

    @school_year.setter
    def school_year(self, school_year):
        """Sets the school_year of this EdFiGradingPeriodReference.

        The identifier for the grading period school year.  # noqa: E501

        :param school_year: The school_year of this EdFiGradingPeriodReference.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and school_year is None:
            raise ValueError("Invalid value for `school_year`, must not be `None`")  # noqa: E501

        self._school_year = school_year

    @property
    def link(self):
        """Gets the link of this EdFiGradingPeriodReference.  # noqa: E501


        :return: The link of this EdFiGradingPeriodReference.  # noqa: E501
        :rtype: Link
        """
        return self._link

    @link.setter
    def link(self, link):
        """Sets the link of this EdFiGradingPeriodReference.


        :param link: The link of this EdFiGradingPeriodReference.  # noqa: E501
        :type: Link
        """

        self._link = link

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
        if issubclass(EdFiGradingPeriodReference, dict):
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
        if not isinstance(other, EdFiGradingPeriodReference):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EdFiGradingPeriodReference):
            return True

        return self.to_dict() != other.to_dict()