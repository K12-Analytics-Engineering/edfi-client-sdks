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


class TrackedChangesEdFiStudentEducationOrganizationResponsibilityAssociationKey(object):
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
        'responsibility_descriptor': 'str',
        'begin_date': 'date',
        'education_organization_id': 'int',
        'student_unique_id': 'str'
    }

    attribute_map = {
        'responsibility_descriptor': 'responsibilityDescriptor',
        'begin_date': 'beginDate',
        'education_organization_id': 'educationOrganizationId',
        'student_unique_id': 'studentUniqueId'
    }

    def __init__(self, responsibility_descriptor=None, begin_date=None, education_organization_id=None, student_unique_id=None, _configuration=None):  # noqa: E501
        """TrackedChangesEdFiStudentEducationOrganizationResponsibilityAssociationKey - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._responsibility_descriptor = None
        self._begin_date = None
        self._education_organization_id = None
        self._student_unique_id = None
        self.discriminator = None

        if responsibility_descriptor is not None:
            self.responsibility_descriptor = responsibility_descriptor
        if begin_date is not None:
            self.begin_date = begin_date
        if education_organization_id is not None:
            self.education_organization_id = education_organization_id
        if student_unique_id is not None:
            self.student_unique_id = student_unique_id

    @property
    def responsibility_descriptor(self):
        """Gets the responsibility_descriptor of this TrackedChangesEdFiStudentEducationOrganizationResponsibilityAssociationKey.  # noqa: E501

        Indications of an education organization's responsibility for a student, such as accountability, attendance, funding, etc.  # noqa: E501

        :return: The responsibility_descriptor of this TrackedChangesEdFiStudentEducationOrganizationResponsibilityAssociationKey.  # noqa: E501
        :rtype: str
        """
        return self._responsibility_descriptor

    @responsibility_descriptor.setter
    def responsibility_descriptor(self, responsibility_descriptor):
        """Sets the responsibility_descriptor of this TrackedChangesEdFiStudentEducationOrganizationResponsibilityAssociationKey.

        Indications of an education organization's responsibility for a student, such as accountability, attendance, funding, etc.  # noqa: E501

        :param responsibility_descriptor: The responsibility_descriptor of this TrackedChangesEdFiStudentEducationOrganizationResponsibilityAssociationKey.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                responsibility_descriptor is not None and len(responsibility_descriptor) > 306):
            raise ValueError("Invalid value for `responsibility_descriptor`, length must be less than or equal to `306`")  # noqa: E501

        self._responsibility_descriptor = responsibility_descriptor

    @property
    def begin_date(self):
        """Gets the begin_date of this TrackedChangesEdFiStudentEducationOrganizationResponsibilityAssociationKey.  # noqa: E501

        Month, day, and year of the start date of an education organization's responsibility for a student.  # noqa: E501

        :return: The begin_date of this TrackedChangesEdFiStudentEducationOrganizationResponsibilityAssociationKey.  # noqa: E501
        :rtype: date
        """
        return self._begin_date

    @begin_date.setter
    def begin_date(self, begin_date):
        """Sets the begin_date of this TrackedChangesEdFiStudentEducationOrganizationResponsibilityAssociationKey.

        Month, day, and year of the start date of an education organization's responsibility for a student.  # noqa: E501

        :param begin_date: The begin_date of this TrackedChangesEdFiStudentEducationOrganizationResponsibilityAssociationKey.  # noqa: E501
        :type: date
        """

        self._begin_date = begin_date

    @property
    def education_organization_id(self):
        """Gets the education_organization_id of this TrackedChangesEdFiStudentEducationOrganizationResponsibilityAssociationKey.  # noqa: E501

        The identifier assigned to an education organization.  # noqa: E501

        :return: The education_organization_id of this TrackedChangesEdFiStudentEducationOrganizationResponsibilityAssociationKey.  # noqa: E501
        :rtype: int
        """
        return self._education_organization_id

    @education_organization_id.setter
    def education_organization_id(self, education_organization_id):
        """Sets the education_organization_id of this TrackedChangesEdFiStudentEducationOrganizationResponsibilityAssociationKey.

        The identifier assigned to an education organization.  # noqa: E501

        :param education_organization_id: The education_organization_id of this TrackedChangesEdFiStudentEducationOrganizationResponsibilityAssociationKey.  # noqa: E501
        :type: int
        """

        self._education_organization_id = education_organization_id

    @property
    def student_unique_id(self):
        """Gets the student_unique_id of this TrackedChangesEdFiStudentEducationOrganizationResponsibilityAssociationKey.  # noqa: E501

        A unique alphanumeric code assigned to a student.  # noqa: E501

        :return: The student_unique_id of this TrackedChangesEdFiStudentEducationOrganizationResponsibilityAssociationKey.  # noqa: E501
        :rtype: str
        """
        return self._student_unique_id

    @student_unique_id.setter
    def student_unique_id(self, student_unique_id):
        """Sets the student_unique_id of this TrackedChangesEdFiStudentEducationOrganizationResponsibilityAssociationKey.

        A unique alphanumeric code assigned to a student.  # noqa: E501

        :param student_unique_id: The student_unique_id of this TrackedChangesEdFiStudentEducationOrganizationResponsibilityAssociationKey.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                student_unique_id is not None and len(student_unique_id) > 32):
            raise ValueError("Invalid value for `student_unique_id`, length must be less than or equal to `32`")  # noqa: E501

        self._student_unique_id = student_unique_id

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
        if issubclass(TrackedChangesEdFiStudentEducationOrganizationResponsibilityAssociationKey, dict):
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
        if not isinstance(other, TrackedChangesEdFiStudentEducationOrganizationResponsibilityAssociationKey):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TrackedChangesEdFiStudentEducationOrganizationResponsibilityAssociationKey):
            return True

        return self.to_dict() != other.to_dict()
