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


class TrackedChangesEdFiGraduationPlanKey(object):
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
        'graduation_plan_type_descriptor': 'str',
        'education_organization_id': 'int',
        'graduation_school_year': 'int'
    }

    attribute_map = {
        'graduation_plan_type_descriptor': 'graduationPlanTypeDescriptor',
        'education_organization_id': 'educationOrganizationId',
        'graduation_school_year': 'graduationSchoolYear'
    }

    def __init__(self, graduation_plan_type_descriptor=None, education_organization_id=None, graduation_school_year=None, _configuration=None):  # noqa: E501
        """TrackedChangesEdFiGraduationPlanKey - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._graduation_plan_type_descriptor = None
        self._education_organization_id = None
        self._graduation_school_year = None
        self.discriminator = None

        if graduation_plan_type_descriptor is not None:
            self.graduation_plan_type_descriptor = graduation_plan_type_descriptor
        if education_organization_id is not None:
            self.education_organization_id = education_organization_id
        if graduation_school_year is not None:
            self.graduation_school_year = graduation_school_year

    @property
    def graduation_plan_type_descriptor(self):
        """Gets the graduation_plan_type_descriptor of this TrackedChangesEdFiGraduationPlanKey.  # noqa: E501

        The type of academic plan the student is following for graduation.  # noqa: E501

        :return: The graduation_plan_type_descriptor of this TrackedChangesEdFiGraduationPlanKey.  # noqa: E501
        :rtype: str
        """
        return self._graduation_plan_type_descriptor

    @graduation_plan_type_descriptor.setter
    def graduation_plan_type_descriptor(self, graduation_plan_type_descriptor):
        """Sets the graduation_plan_type_descriptor of this TrackedChangesEdFiGraduationPlanKey.

        The type of academic plan the student is following for graduation.  # noqa: E501

        :param graduation_plan_type_descriptor: The graduation_plan_type_descriptor of this TrackedChangesEdFiGraduationPlanKey.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                graduation_plan_type_descriptor is not None and len(graduation_plan_type_descriptor) > 306):
            raise ValueError("Invalid value for `graduation_plan_type_descriptor`, length must be less than or equal to `306`")  # noqa: E501

        self._graduation_plan_type_descriptor = graduation_plan_type_descriptor

    @property
    def education_organization_id(self):
        """Gets the education_organization_id of this TrackedChangesEdFiGraduationPlanKey.  # noqa: E501

        The identifier assigned to an education organization.  # noqa: E501

        :return: The education_organization_id of this TrackedChangesEdFiGraduationPlanKey.  # noqa: E501
        :rtype: int
        """
        return self._education_organization_id

    @education_organization_id.setter
    def education_organization_id(self, education_organization_id):
        """Sets the education_organization_id of this TrackedChangesEdFiGraduationPlanKey.

        The identifier assigned to an education organization.  # noqa: E501

        :param education_organization_id: The education_organization_id of this TrackedChangesEdFiGraduationPlanKey.  # noqa: E501
        :type: int
        """

        self._education_organization_id = education_organization_id

    @property
    def graduation_school_year(self):
        """Gets the graduation_school_year of this TrackedChangesEdFiGraduationPlanKey.  # noqa: E501

        The school year the student is expected to graduate.  # noqa: E501

        :return: The graduation_school_year of this TrackedChangesEdFiGraduationPlanKey.  # noqa: E501
        :rtype: int
        """
        return self._graduation_school_year

    @graduation_school_year.setter
    def graduation_school_year(self, graduation_school_year):
        """Sets the graduation_school_year of this TrackedChangesEdFiGraduationPlanKey.

        The school year the student is expected to graduate.  # noqa: E501

        :param graduation_school_year: The graduation_school_year of this TrackedChangesEdFiGraduationPlanKey.  # noqa: E501
        :type: int
        """

        self._graduation_school_year = graduation_school_year

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
        if issubclass(TrackedChangesEdFiGraduationPlanKey, dict):
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
        if not isinstance(other, TrackedChangesEdFiGraduationPlanKey):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TrackedChangesEdFiGraduationPlanKey):
            return True

        return self.to_dict() != other.to_dict()
