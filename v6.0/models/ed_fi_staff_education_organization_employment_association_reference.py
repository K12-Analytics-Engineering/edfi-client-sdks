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


class EdFiStaffEducationOrganizationEmploymentAssociationReference(object):
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
        'education_organization_id': 'int',
        'employment_status_descriptor': 'str',
        'hire_date': 'date',
        'staff_unique_id': 'str',
        'link': 'Link'
    }

    attribute_map = {
        'education_organization_id': 'educationOrganizationId',
        'employment_status_descriptor': 'employmentStatusDescriptor',
        'hire_date': 'hireDate',
        'staff_unique_id': 'staffUniqueId',
        'link': 'link'
    }

    def __init__(self, education_organization_id=None, employment_status_descriptor=None, hire_date=None, staff_unique_id=None, link=None, _configuration=None):  # noqa: E501
        """EdFiStaffEducationOrganizationEmploymentAssociationReference - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._education_organization_id = None
        self._employment_status_descriptor = None
        self._hire_date = None
        self._staff_unique_id = None
        self._link = None
        self.discriminator = None

        self.education_organization_id = education_organization_id
        self.employment_status_descriptor = employment_status_descriptor
        self.hire_date = hire_date
        self.staff_unique_id = staff_unique_id
        if link is not None:
            self.link = link

    @property
    def education_organization_id(self):
        """Gets the education_organization_id of this EdFiStaffEducationOrganizationEmploymentAssociationReference.  # noqa: E501

        The identifier assigned to an education organization.  # noqa: E501

        :return: The education_organization_id of this EdFiStaffEducationOrganizationEmploymentAssociationReference.  # noqa: E501
        :rtype: int
        """
        return self._education_organization_id

    @education_organization_id.setter
    def education_organization_id(self, education_organization_id):
        """Sets the education_organization_id of this EdFiStaffEducationOrganizationEmploymentAssociationReference.

        The identifier assigned to an education organization.  # noqa: E501

        :param education_organization_id: The education_organization_id of this EdFiStaffEducationOrganizationEmploymentAssociationReference.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and education_organization_id is None:
            raise ValueError("Invalid value for `education_organization_id`, must not be `None`")  # noqa: E501

        self._education_organization_id = education_organization_id

    @property
    def employment_status_descriptor(self):
        """Gets the employment_status_descriptor of this EdFiStaffEducationOrganizationEmploymentAssociationReference.  # noqa: E501

        Reflects the type of employment or contract.  # noqa: E501

        :return: The employment_status_descriptor of this EdFiStaffEducationOrganizationEmploymentAssociationReference.  # noqa: E501
        :rtype: str
        """
        return self._employment_status_descriptor

    @employment_status_descriptor.setter
    def employment_status_descriptor(self, employment_status_descriptor):
        """Sets the employment_status_descriptor of this EdFiStaffEducationOrganizationEmploymentAssociationReference.

        Reflects the type of employment or contract.  # noqa: E501

        :param employment_status_descriptor: The employment_status_descriptor of this EdFiStaffEducationOrganizationEmploymentAssociationReference.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and employment_status_descriptor is None:
            raise ValueError("Invalid value for `employment_status_descriptor`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                employment_status_descriptor is not None and len(employment_status_descriptor) > 306):
            raise ValueError("Invalid value for `employment_status_descriptor`, length must be less than or equal to `306`")  # noqa: E501

        self._employment_status_descriptor = employment_status_descriptor

    @property
    def hire_date(self):
        """Gets the hire_date of this EdFiStaffEducationOrganizationEmploymentAssociationReference.  # noqa: E501

        The month, day, and year on which an individual was hired for a position.  # noqa: E501

        :return: The hire_date of this EdFiStaffEducationOrganizationEmploymentAssociationReference.  # noqa: E501
        :rtype: date
        """
        return self._hire_date

    @hire_date.setter
    def hire_date(self, hire_date):
        """Sets the hire_date of this EdFiStaffEducationOrganizationEmploymentAssociationReference.

        The month, day, and year on which an individual was hired for a position.  # noqa: E501

        :param hire_date: The hire_date of this EdFiStaffEducationOrganizationEmploymentAssociationReference.  # noqa: E501
        :type: date
        """
        if self._configuration.client_side_validation and hire_date is None:
            raise ValueError("Invalid value for `hire_date`, must not be `None`")  # noqa: E501

        self._hire_date = hire_date

    @property
    def staff_unique_id(self):
        """Gets the staff_unique_id of this EdFiStaffEducationOrganizationEmploymentAssociationReference.  # noqa: E501

        A unique alphanumeric code assigned to a staff.  # noqa: E501

        :return: The staff_unique_id of this EdFiStaffEducationOrganizationEmploymentAssociationReference.  # noqa: E501
        :rtype: str
        """
        return self._staff_unique_id

    @staff_unique_id.setter
    def staff_unique_id(self, staff_unique_id):
        """Sets the staff_unique_id of this EdFiStaffEducationOrganizationEmploymentAssociationReference.

        A unique alphanumeric code assigned to a staff.  # noqa: E501

        :param staff_unique_id: The staff_unique_id of this EdFiStaffEducationOrganizationEmploymentAssociationReference.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and staff_unique_id is None:
            raise ValueError("Invalid value for `staff_unique_id`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                staff_unique_id is not None and len(staff_unique_id) > 32):
            raise ValueError("Invalid value for `staff_unique_id`, length must be less than or equal to `32`")  # noqa: E501

        self._staff_unique_id = staff_unique_id

    @property
    def link(self):
        """Gets the link of this EdFiStaffEducationOrganizationEmploymentAssociationReference.  # noqa: E501


        :return: The link of this EdFiStaffEducationOrganizationEmploymentAssociationReference.  # noqa: E501
        :rtype: Link
        """
        return self._link

    @link.setter
    def link(self, link):
        """Sets the link of this EdFiStaffEducationOrganizationEmploymentAssociationReference.


        :param link: The link of this EdFiStaffEducationOrganizationEmploymentAssociationReference.  # noqa: E501
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
        if issubclass(EdFiStaffEducationOrganizationEmploymentAssociationReference, dict):
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
        if not isinstance(other, EdFiStaffEducationOrganizationEmploymentAssociationReference):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EdFiStaffEducationOrganizationEmploymentAssociationReference):
            return True

        return self.to_dict() != other.to_dict()
