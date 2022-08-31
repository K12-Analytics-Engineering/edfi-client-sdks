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


class EdFiLocalAccount(object):
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
        'account_identifier': 'str',
        'chart_of_account_reference': 'EdFiChartOfAccountReference',
        'education_organization_reference': 'EdFiEducationOrganizationReference',
        'account_name': 'str',
        'reporting_tags': 'list[EdFiLocalAccountReportingTag]',
        'etag': 'str'
    }

    attribute_map = {
        'id': 'id',
        'account_identifier': 'accountIdentifier',
        'chart_of_account_reference': 'chartOfAccountReference',
        'education_organization_reference': 'educationOrganizationReference',
        'account_name': 'accountName',
        'reporting_tags': 'reportingTags',
        'etag': '_etag'
    }

    def __init__(self, id=None, account_identifier=None, chart_of_account_reference=None, education_organization_reference=None, account_name=None, reporting_tags=None, etag=None, _configuration=None):  # noqa: E501
        """EdFiLocalAccount - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._account_identifier = None
        self._chart_of_account_reference = None
        self._education_organization_reference = None
        self._account_name = None
        self._reporting_tags = None
        self._etag = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.account_identifier = account_identifier
        self.chart_of_account_reference = chart_of_account_reference
        self.education_organization_reference = education_organization_reference
        if account_name is not None:
            self.account_name = account_name
        if reporting_tags is not None:
            self.reporting_tags = reporting_tags
        if etag is not None:
            self.etag = etag

    @property
    def id(self):
        """Gets the id of this EdFiLocalAccount.  # noqa: E501

          # noqa: E501

        :return: The id of this EdFiLocalAccount.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this EdFiLocalAccount.

          # noqa: E501

        :param id: The id of this EdFiLocalAccount.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def account_identifier(self):
        """Gets the account_identifier of this EdFiLocalAccount.  # noqa: E501

        Code value for the valid combination of account dimensions by LEA under which financials are reported.  # noqa: E501

        :return: The account_identifier of this EdFiLocalAccount.  # noqa: E501
        :rtype: str
        """
        return self._account_identifier

    @account_identifier.setter
    def account_identifier(self, account_identifier):
        """Sets the account_identifier of this EdFiLocalAccount.

        Code value for the valid combination of account dimensions by LEA under which financials are reported.  # noqa: E501

        :param account_identifier: The account_identifier of this EdFiLocalAccount.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and account_identifier is None:
            raise ValueError("Invalid value for `account_identifier`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                account_identifier is not None and len(account_identifier) > 50):
            raise ValueError("Invalid value for `account_identifier`, length must be less than or equal to `50`")  # noqa: E501

        self._account_identifier = account_identifier

    @property
    def chart_of_account_reference(self):
        """Gets the chart_of_account_reference of this EdFiLocalAccount.  # noqa: E501


        :return: The chart_of_account_reference of this EdFiLocalAccount.  # noqa: E501
        :rtype: EdFiChartOfAccountReference
        """
        return self._chart_of_account_reference

    @chart_of_account_reference.setter
    def chart_of_account_reference(self, chart_of_account_reference):
        """Sets the chart_of_account_reference of this EdFiLocalAccount.


        :param chart_of_account_reference: The chart_of_account_reference of this EdFiLocalAccount.  # noqa: E501
        :type: EdFiChartOfAccountReference
        """
        if self._configuration.client_side_validation and chart_of_account_reference is None:
            raise ValueError("Invalid value for `chart_of_account_reference`, must not be `None`")  # noqa: E501

        self._chart_of_account_reference = chart_of_account_reference

    @property
    def education_organization_reference(self):
        """Gets the education_organization_reference of this EdFiLocalAccount.  # noqa: E501


        :return: The education_organization_reference of this EdFiLocalAccount.  # noqa: E501
        :rtype: EdFiEducationOrganizationReference
        """
        return self._education_organization_reference

    @education_organization_reference.setter
    def education_organization_reference(self, education_organization_reference):
        """Sets the education_organization_reference of this EdFiLocalAccount.


        :param education_organization_reference: The education_organization_reference of this EdFiLocalAccount.  # noqa: E501
        :type: EdFiEducationOrganizationReference
        """
        if self._configuration.client_side_validation and education_organization_reference is None:
            raise ValueError("Invalid value for `education_organization_reference`, must not be `None`")  # noqa: E501

        self._education_organization_reference = education_organization_reference

    @property
    def account_name(self):
        """Gets the account_name of this EdFiLocalAccount.  # noqa: E501

        A descriptive name for the account.  # noqa: E501

        :return: The account_name of this EdFiLocalAccount.  # noqa: E501
        :rtype: str
        """
        return self._account_name

    @account_name.setter
    def account_name(self, account_name):
        """Sets the account_name of this EdFiLocalAccount.

        A descriptive name for the account.  # noqa: E501

        :param account_name: The account_name of this EdFiLocalAccount.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                account_name is not None and len(account_name) > 100):
            raise ValueError("Invalid value for `account_name`, length must be less than or equal to `100`")  # noqa: E501

        self._account_name = account_name

    @property
    def reporting_tags(self):
        """Gets the reporting_tags of this EdFiLocalAccount.  # noqa: E501

        An unordered collection of localAccountReportingTags. Optional tag for accountability reporting.  # noqa: E501

        :return: The reporting_tags of this EdFiLocalAccount.  # noqa: E501
        :rtype: list[EdFiLocalAccountReportingTag]
        """
        return self._reporting_tags

    @reporting_tags.setter
    def reporting_tags(self, reporting_tags):
        """Sets the reporting_tags of this EdFiLocalAccount.

        An unordered collection of localAccountReportingTags. Optional tag for accountability reporting.  # noqa: E501

        :param reporting_tags: The reporting_tags of this EdFiLocalAccount.  # noqa: E501
        :type: list[EdFiLocalAccountReportingTag]
        """

        self._reporting_tags = reporting_tags

    @property
    def etag(self):
        """Gets the etag of this EdFiLocalAccount.  # noqa: E501

        A unique system-generated value that identifies the version of the resource.  # noqa: E501

        :return: The etag of this EdFiLocalAccount.  # noqa: E501
        :rtype: str
        """
        return self._etag

    @etag.setter
    def etag(self, etag):
        """Sets the etag of this EdFiLocalAccount.

        A unique system-generated value that identifies the version of the resource.  # noqa: E501

        :param etag: The etag of this EdFiLocalAccount.  # noqa: E501
        :type: str
        """

        self._etag = etag

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
        if issubclass(EdFiLocalAccount, dict):
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
        if not isinstance(other, EdFiLocalAccount):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EdFiLocalAccount):
            return True

        return self.to_dict() != other.to_dict()
