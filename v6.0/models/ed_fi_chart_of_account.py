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


class EdFiChartOfAccount(object):
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
        'balance_sheet_dimension_reference': 'EdFiBalanceSheetDimensionReference',
        'education_organization_reference': 'EdFiEducationOrganizationReference',
        'function_dimension_reference': 'EdFiFunctionDimensionReference',
        'fund_dimension_reference': 'EdFiFundDimensionReference',
        'object_dimension_reference': 'EdFiObjectDimensionReference',
        'operational_unit_dimension_reference': 'EdFiOperationalUnitDimensionReference',
        'program_dimension_reference': 'EdFiProgramDimensionReference',
        'project_dimension_reference': 'EdFiProjectDimensionReference',
        'source_dimension_reference': 'EdFiSourceDimensionReference',
        'account_name': 'str',
        'account_type_descriptor': 'str',
        'reporting_tags': 'list[EdFiChartOfAccountReportingTag]',
        'etag': 'str'
    }

    attribute_map = {
        'id': 'id',
        'account_identifier': 'accountIdentifier',
        'balance_sheet_dimension_reference': 'balanceSheetDimensionReference',
        'education_organization_reference': 'educationOrganizationReference',
        'function_dimension_reference': 'functionDimensionReference',
        'fund_dimension_reference': 'fundDimensionReference',
        'object_dimension_reference': 'objectDimensionReference',
        'operational_unit_dimension_reference': 'operationalUnitDimensionReference',
        'program_dimension_reference': 'programDimensionReference',
        'project_dimension_reference': 'projectDimensionReference',
        'source_dimension_reference': 'sourceDimensionReference',
        'account_name': 'accountName',
        'account_type_descriptor': 'accountTypeDescriptor',
        'reporting_tags': 'reportingTags',
        'etag': '_etag'
    }

    def __init__(self, id=None, account_identifier=None, balance_sheet_dimension_reference=None, education_organization_reference=None, function_dimension_reference=None, fund_dimension_reference=None, object_dimension_reference=None, operational_unit_dimension_reference=None, program_dimension_reference=None, project_dimension_reference=None, source_dimension_reference=None, account_name=None, account_type_descriptor=None, reporting_tags=None, etag=None, _configuration=None):  # noqa: E501
        """EdFiChartOfAccount - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._account_identifier = None
        self._balance_sheet_dimension_reference = None
        self._education_organization_reference = None
        self._function_dimension_reference = None
        self._fund_dimension_reference = None
        self._object_dimension_reference = None
        self._operational_unit_dimension_reference = None
        self._program_dimension_reference = None
        self._project_dimension_reference = None
        self._source_dimension_reference = None
        self._account_name = None
        self._account_type_descriptor = None
        self._reporting_tags = None
        self._etag = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.account_identifier = account_identifier
        if balance_sheet_dimension_reference is not None:
            self.balance_sheet_dimension_reference = balance_sheet_dimension_reference
        self.education_organization_reference = education_organization_reference
        if function_dimension_reference is not None:
            self.function_dimension_reference = function_dimension_reference
        if fund_dimension_reference is not None:
            self.fund_dimension_reference = fund_dimension_reference
        if object_dimension_reference is not None:
            self.object_dimension_reference = object_dimension_reference
        if operational_unit_dimension_reference is not None:
            self.operational_unit_dimension_reference = operational_unit_dimension_reference
        if program_dimension_reference is not None:
            self.program_dimension_reference = program_dimension_reference
        if project_dimension_reference is not None:
            self.project_dimension_reference = project_dimension_reference
        if source_dimension_reference is not None:
            self.source_dimension_reference = source_dimension_reference
        if account_name is not None:
            self.account_name = account_name
        self.account_type_descriptor = account_type_descriptor
        if reporting_tags is not None:
            self.reporting_tags = reporting_tags
        if etag is not None:
            self.etag = etag

    @property
    def id(self):
        """Gets the id of this EdFiChartOfAccount.  # noqa: E501

          # noqa: E501

        :return: The id of this EdFiChartOfAccount.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this EdFiChartOfAccount.

          # noqa: E501

        :param id: The id of this EdFiChartOfAccount.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def account_identifier(self):
        """Gets the account_identifier of this EdFiChartOfAccount.  # noqa: E501

        SEA populated code value for the valid combination of account dimensions under which financials are reported.  # noqa: E501

        :return: The account_identifier of this EdFiChartOfAccount.  # noqa: E501
        :rtype: str
        """
        return self._account_identifier

    @account_identifier.setter
    def account_identifier(self, account_identifier):
        """Sets the account_identifier of this EdFiChartOfAccount.

        SEA populated code value for the valid combination of account dimensions under which financials are reported.  # noqa: E501

        :param account_identifier: The account_identifier of this EdFiChartOfAccount.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and account_identifier is None:
            raise ValueError("Invalid value for `account_identifier`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                account_identifier is not None and len(account_identifier) > 50):
            raise ValueError("Invalid value for `account_identifier`, length must be less than or equal to `50`")  # noqa: E501

        self._account_identifier = account_identifier

    @property
    def balance_sheet_dimension_reference(self):
        """Gets the balance_sheet_dimension_reference of this EdFiChartOfAccount.  # noqa: E501


        :return: The balance_sheet_dimension_reference of this EdFiChartOfAccount.  # noqa: E501
        :rtype: EdFiBalanceSheetDimensionReference
        """
        return self._balance_sheet_dimension_reference

    @balance_sheet_dimension_reference.setter
    def balance_sheet_dimension_reference(self, balance_sheet_dimension_reference):
        """Sets the balance_sheet_dimension_reference of this EdFiChartOfAccount.


        :param balance_sheet_dimension_reference: The balance_sheet_dimension_reference of this EdFiChartOfAccount.  # noqa: E501
        :type: EdFiBalanceSheetDimensionReference
        """

        self._balance_sheet_dimension_reference = balance_sheet_dimension_reference

    @property
    def education_organization_reference(self):
        """Gets the education_organization_reference of this EdFiChartOfAccount.  # noqa: E501


        :return: The education_organization_reference of this EdFiChartOfAccount.  # noqa: E501
        :rtype: EdFiEducationOrganizationReference
        """
        return self._education_organization_reference

    @education_organization_reference.setter
    def education_organization_reference(self, education_organization_reference):
        """Sets the education_organization_reference of this EdFiChartOfAccount.


        :param education_organization_reference: The education_organization_reference of this EdFiChartOfAccount.  # noqa: E501
        :type: EdFiEducationOrganizationReference
        """
        if self._configuration.client_side_validation and education_organization_reference is None:
            raise ValueError("Invalid value for `education_organization_reference`, must not be `None`")  # noqa: E501

        self._education_organization_reference = education_organization_reference

    @property
    def function_dimension_reference(self):
        """Gets the function_dimension_reference of this EdFiChartOfAccount.  # noqa: E501


        :return: The function_dimension_reference of this EdFiChartOfAccount.  # noqa: E501
        :rtype: EdFiFunctionDimensionReference
        """
        return self._function_dimension_reference

    @function_dimension_reference.setter
    def function_dimension_reference(self, function_dimension_reference):
        """Sets the function_dimension_reference of this EdFiChartOfAccount.


        :param function_dimension_reference: The function_dimension_reference of this EdFiChartOfAccount.  # noqa: E501
        :type: EdFiFunctionDimensionReference
        """

        self._function_dimension_reference = function_dimension_reference

    @property
    def fund_dimension_reference(self):
        """Gets the fund_dimension_reference of this EdFiChartOfAccount.  # noqa: E501


        :return: The fund_dimension_reference of this EdFiChartOfAccount.  # noqa: E501
        :rtype: EdFiFundDimensionReference
        """
        return self._fund_dimension_reference

    @fund_dimension_reference.setter
    def fund_dimension_reference(self, fund_dimension_reference):
        """Sets the fund_dimension_reference of this EdFiChartOfAccount.


        :param fund_dimension_reference: The fund_dimension_reference of this EdFiChartOfAccount.  # noqa: E501
        :type: EdFiFundDimensionReference
        """

        self._fund_dimension_reference = fund_dimension_reference

    @property
    def object_dimension_reference(self):
        """Gets the object_dimension_reference of this EdFiChartOfAccount.  # noqa: E501


        :return: The object_dimension_reference of this EdFiChartOfAccount.  # noqa: E501
        :rtype: EdFiObjectDimensionReference
        """
        return self._object_dimension_reference

    @object_dimension_reference.setter
    def object_dimension_reference(self, object_dimension_reference):
        """Sets the object_dimension_reference of this EdFiChartOfAccount.


        :param object_dimension_reference: The object_dimension_reference of this EdFiChartOfAccount.  # noqa: E501
        :type: EdFiObjectDimensionReference
        """

        self._object_dimension_reference = object_dimension_reference

    @property
    def operational_unit_dimension_reference(self):
        """Gets the operational_unit_dimension_reference of this EdFiChartOfAccount.  # noqa: E501


        :return: The operational_unit_dimension_reference of this EdFiChartOfAccount.  # noqa: E501
        :rtype: EdFiOperationalUnitDimensionReference
        """
        return self._operational_unit_dimension_reference

    @operational_unit_dimension_reference.setter
    def operational_unit_dimension_reference(self, operational_unit_dimension_reference):
        """Sets the operational_unit_dimension_reference of this EdFiChartOfAccount.


        :param operational_unit_dimension_reference: The operational_unit_dimension_reference of this EdFiChartOfAccount.  # noqa: E501
        :type: EdFiOperationalUnitDimensionReference
        """

        self._operational_unit_dimension_reference = operational_unit_dimension_reference

    @property
    def program_dimension_reference(self):
        """Gets the program_dimension_reference of this EdFiChartOfAccount.  # noqa: E501


        :return: The program_dimension_reference of this EdFiChartOfAccount.  # noqa: E501
        :rtype: EdFiProgramDimensionReference
        """
        return self._program_dimension_reference

    @program_dimension_reference.setter
    def program_dimension_reference(self, program_dimension_reference):
        """Sets the program_dimension_reference of this EdFiChartOfAccount.


        :param program_dimension_reference: The program_dimension_reference of this EdFiChartOfAccount.  # noqa: E501
        :type: EdFiProgramDimensionReference
        """

        self._program_dimension_reference = program_dimension_reference

    @property
    def project_dimension_reference(self):
        """Gets the project_dimension_reference of this EdFiChartOfAccount.  # noqa: E501


        :return: The project_dimension_reference of this EdFiChartOfAccount.  # noqa: E501
        :rtype: EdFiProjectDimensionReference
        """
        return self._project_dimension_reference

    @project_dimension_reference.setter
    def project_dimension_reference(self, project_dimension_reference):
        """Sets the project_dimension_reference of this EdFiChartOfAccount.


        :param project_dimension_reference: The project_dimension_reference of this EdFiChartOfAccount.  # noqa: E501
        :type: EdFiProjectDimensionReference
        """

        self._project_dimension_reference = project_dimension_reference

    @property
    def source_dimension_reference(self):
        """Gets the source_dimension_reference of this EdFiChartOfAccount.  # noqa: E501


        :return: The source_dimension_reference of this EdFiChartOfAccount.  # noqa: E501
        :rtype: EdFiSourceDimensionReference
        """
        return self._source_dimension_reference

    @source_dimension_reference.setter
    def source_dimension_reference(self, source_dimension_reference):
        """Sets the source_dimension_reference of this EdFiChartOfAccount.


        :param source_dimension_reference: The source_dimension_reference of this EdFiChartOfAccount.  # noqa: E501
        :type: EdFiSourceDimensionReference
        """

        self._source_dimension_reference = source_dimension_reference

    @property
    def account_name(self):
        """Gets the account_name of this EdFiChartOfAccount.  # noqa: E501

        A descriptive name for the account.  # noqa: E501

        :return: The account_name of this EdFiChartOfAccount.  # noqa: E501
        :rtype: str
        """
        return self._account_name

    @account_name.setter
    def account_name(self, account_name):
        """Sets the account_name of this EdFiChartOfAccount.

        A descriptive name for the account.  # noqa: E501

        :param account_name: The account_name of this EdFiChartOfAccount.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                account_name is not None and len(account_name) > 100):
            raise ValueError("Invalid value for `account_name`, length must be less than or equal to `100`")  # noqa: E501

        self._account_name = account_name

    @property
    def account_type_descriptor(self):
        """Gets the account_type_descriptor of this EdFiChartOfAccount.  # noqa: E501

        The type of account used in accounting such as revenue, expenditure, or balance sheet.  # noqa: E501

        :return: The account_type_descriptor of this EdFiChartOfAccount.  # noqa: E501
        :rtype: str
        """
        return self._account_type_descriptor

    @account_type_descriptor.setter
    def account_type_descriptor(self, account_type_descriptor):
        """Sets the account_type_descriptor of this EdFiChartOfAccount.

        The type of account used in accounting such as revenue, expenditure, or balance sheet.  # noqa: E501

        :param account_type_descriptor: The account_type_descriptor of this EdFiChartOfAccount.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and account_type_descriptor is None:
            raise ValueError("Invalid value for `account_type_descriptor`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                account_type_descriptor is not None and len(account_type_descriptor) > 306):
            raise ValueError("Invalid value for `account_type_descriptor`, length must be less than or equal to `306`")  # noqa: E501

        self._account_type_descriptor = account_type_descriptor

    @property
    def reporting_tags(self):
        """Gets the reporting_tags of this EdFiChartOfAccount.  # noqa: E501

        An unordered collection of chartOfAccountReportingTags. Optional tag for accountability reporting.  # noqa: E501

        :return: The reporting_tags of this EdFiChartOfAccount.  # noqa: E501
        :rtype: list[EdFiChartOfAccountReportingTag]
        """
        return self._reporting_tags

    @reporting_tags.setter
    def reporting_tags(self, reporting_tags):
        """Sets the reporting_tags of this EdFiChartOfAccount.

        An unordered collection of chartOfAccountReportingTags. Optional tag for accountability reporting.  # noqa: E501

        :param reporting_tags: The reporting_tags of this EdFiChartOfAccount.  # noqa: E501
        :type: list[EdFiChartOfAccountReportingTag]
        """

        self._reporting_tags = reporting_tags

    @property
    def etag(self):
        """Gets the etag of this EdFiChartOfAccount.  # noqa: E501

        A unique system-generated value that identifies the version of the resource.  # noqa: E501

        :return: The etag of this EdFiChartOfAccount.  # noqa: E501
        :rtype: str
        """
        return self._etag

    @etag.setter
    def etag(self, etag):
        """Sets the etag of this EdFiChartOfAccount.

        A unique system-generated value that identifies the version of the resource.  # noqa: E501

        :param etag: The etag of this EdFiChartOfAccount.  # noqa: E501
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
        if issubclass(EdFiChartOfAccount, dict):
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
        if not isinstance(other, EdFiChartOfAccount):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EdFiChartOfAccount):
            return True

        return self.to_dict() != other.to_dict()
