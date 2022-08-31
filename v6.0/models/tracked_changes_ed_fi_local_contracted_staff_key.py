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


class TrackedChangesEdFiLocalContractedStaffKey(object):
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
        'as_of_date': 'date',
        'account_identifier': 'str',
        'education_organization_id': 'int',
        'fiscal_year': 'int',
        'staff_unique_id': 'str'
    }

    attribute_map = {
        'as_of_date': 'asOfDate',
        'account_identifier': 'accountIdentifier',
        'education_organization_id': 'educationOrganizationId',
        'fiscal_year': 'fiscalYear',
        'staff_unique_id': 'staffUniqueId'
    }

    def __init__(self, as_of_date=None, account_identifier=None, education_organization_id=None, fiscal_year=None, staff_unique_id=None, _configuration=None):  # noqa: E501
        """TrackedChangesEdFiLocalContractedStaffKey - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._as_of_date = None
        self._account_identifier = None
        self._education_organization_id = None
        self._fiscal_year = None
        self._staff_unique_id = None
        self.discriminator = None

        if as_of_date is not None:
            self.as_of_date = as_of_date
        if account_identifier is not None:
            self.account_identifier = account_identifier
        if education_organization_id is not None:
            self.education_organization_id = education_organization_id
        if fiscal_year is not None:
            self.fiscal_year = fiscal_year
        if staff_unique_id is not None:
            self.staff_unique_id = staff_unique_id

    @property
    def as_of_date(self):
        """Gets the as_of_date of this TrackedChangesEdFiLocalContractedStaffKey.  # noqa: E501

        The date of the reported amount for the account.  # noqa: E501

        :return: The as_of_date of this TrackedChangesEdFiLocalContractedStaffKey.  # noqa: E501
        :rtype: date
        """
        return self._as_of_date

    @as_of_date.setter
    def as_of_date(self, as_of_date):
        """Sets the as_of_date of this TrackedChangesEdFiLocalContractedStaffKey.

        The date of the reported amount for the account.  # noqa: E501

        :param as_of_date: The as_of_date of this TrackedChangesEdFiLocalContractedStaffKey.  # noqa: E501
        :type: date
        """

        self._as_of_date = as_of_date

    @property
    def account_identifier(self):
        """Gets the account_identifier of this TrackedChangesEdFiLocalContractedStaffKey.  # noqa: E501

        Code value for the valid combination of account dimensions by LEA under which financials are reported.  # noqa: E501

        :return: The account_identifier of this TrackedChangesEdFiLocalContractedStaffKey.  # noqa: E501
        :rtype: str
        """
        return self._account_identifier

    @account_identifier.setter
    def account_identifier(self, account_identifier):
        """Sets the account_identifier of this TrackedChangesEdFiLocalContractedStaffKey.

        Code value for the valid combination of account dimensions by LEA under which financials are reported.  # noqa: E501

        :param account_identifier: The account_identifier of this TrackedChangesEdFiLocalContractedStaffKey.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                account_identifier is not None and len(account_identifier) > 50):
            raise ValueError("Invalid value for `account_identifier`, length must be less than or equal to `50`")  # noqa: E501

        self._account_identifier = account_identifier

    @property
    def education_organization_id(self):
        """Gets the education_organization_id of this TrackedChangesEdFiLocalContractedStaffKey.  # noqa: E501

        The identifier assigned to an education organization.  # noqa: E501

        :return: The education_organization_id of this TrackedChangesEdFiLocalContractedStaffKey.  # noqa: E501
        :rtype: int
        """
        return self._education_organization_id

    @education_organization_id.setter
    def education_organization_id(self, education_organization_id):
        """Sets the education_organization_id of this TrackedChangesEdFiLocalContractedStaffKey.

        The identifier assigned to an education organization.  # noqa: E501

        :param education_organization_id: The education_organization_id of this TrackedChangesEdFiLocalContractedStaffKey.  # noqa: E501
        :type: int
        """

        self._education_organization_id = education_organization_id

    @property
    def fiscal_year(self):
        """Gets the fiscal_year of this TrackedChangesEdFiLocalContractedStaffKey.  # noqa: E501

        The fiscal year for the account.  # noqa: E501

        :return: The fiscal_year of this TrackedChangesEdFiLocalContractedStaffKey.  # noqa: E501
        :rtype: int
        """
        return self._fiscal_year

    @fiscal_year.setter
    def fiscal_year(self, fiscal_year):
        """Sets the fiscal_year of this TrackedChangesEdFiLocalContractedStaffKey.

        The fiscal year for the account.  # noqa: E501

        :param fiscal_year: The fiscal_year of this TrackedChangesEdFiLocalContractedStaffKey.  # noqa: E501
        :type: int
        """

        self._fiscal_year = fiscal_year

    @property
    def staff_unique_id(self):
        """Gets the staff_unique_id of this TrackedChangesEdFiLocalContractedStaffKey.  # noqa: E501

        A unique alphanumeric code assigned to a staff.  # noqa: E501

        :return: The staff_unique_id of this TrackedChangesEdFiLocalContractedStaffKey.  # noqa: E501
        :rtype: str
        """
        return self._staff_unique_id

    @staff_unique_id.setter
    def staff_unique_id(self, staff_unique_id):
        """Sets the staff_unique_id of this TrackedChangesEdFiLocalContractedStaffKey.

        A unique alphanumeric code assigned to a staff.  # noqa: E501

        :param staff_unique_id: The staff_unique_id of this TrackedChangesEdFiLocalContractedStaffKey.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                staff_unique_id is not None and len(staff_unique_id) > 32):
            raise ValueError("Invalid value for `staff_unique_id`, length must be less than or equal to `32`")  # noqa: E501

        self._staff_unique_id = staff_unique_id

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
        if issubclass(TrackedChangesEdFiLocalContractedStaffKey, dict):
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
        if not isinstance(other, TrackedChangesEdFiLocalContractedStaffKey):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TrackedChangesEdFiLocalContractedStaffKey):
            return True

        return self.to_dict() != other.to_dict()