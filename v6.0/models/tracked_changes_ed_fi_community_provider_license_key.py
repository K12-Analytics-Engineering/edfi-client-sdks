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


class TrackedChangesEdFiCommunityProviderLicenseKey(object):
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
        'license_identifier': 'str',
        'licensing_organization': 'str',
        'community_provider_id': 'int'
    }

    attribute_map = {
        'license_identifier': 'licenseIdentifier',
        'licensing_organization': 'licensingOrganization',
        'community_provider_id': 'communityProviderId'
    }

    def __init__(self, license_identifier=None, licensing_organization=None, community_provider_id=None, _configuration=None):  # noqa: E501
        """TrackedChangesEdFiCommunityProviderLicenseKey - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._license_identifier = None
        self._licensing_organization = None
        self._community_provider_id = None
        self.discriminator = None

        if license_identifier is not None:
            self.license_identifier = license_identifier
        if licensing_organization is not None:
            self.licensing_organization = licensing_organization
        if community_provider_id is not None:
            self.community_provider_id = community_provider_id

    @property
    def license_identifier(self):
        """Gets the license_identifier of this TrackedChangesEdFiCommunityProviderLicenseKey.  # noqa: E501

        The unique identifier issued by the licensing organization.  # noqa: E501

        :return: The license_identifier of this TrackedChangesEdFiCommunityProviderLicenseKey.  # noqa: E501
        :rtype: str
        """
        return self._license_identifier

    @license_identifier.setter
    def license_identifier(self, license_identifier):
        """Sets the license_identifier of this TrackedChangesEdFiCommunityProviderLicenseKey.

        The unique identifier issued by the licensing organization.  # noqa: E501

        :param license_identifier: The license_identifier of this TrackedChangesEdFiCommunityProviderLicenseKey.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                license_identifier is not None and len(license_identifier) > 20):
            raise ValueError("Invalid value for `license_identifier`, length must be less than or equal to `20`")  # noqa: E501

        self._license_identifier = license_identifier

    @property
    def licensing_organization(self):
        """Gets the licensing_organization of this TrackedChangesEdFiCommunityProviderLicenseKey.  # noqa: E501

        The organization issuing the license.  # noqa: E501

        :return: The licensing_organization of this TrackedChangesEdFiCommunityProviderLicenseKey.  # noqa: E501
        :rtype: str
        """
        return self._licensing_organization

    @licensing_organization.setter
    def licensing_organization(self, licensing_organization):
        """Sets the licensing_organization of this TrackedChangesEdFiCommunityProviderLicenseKey.

        The organization issuing the license.  # noqa: E501

        :param licensing_organization: The licensing_organization of this TrackedChangesEdFiCommunityProviderLicenseKey.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                licensing_organization is not None and len(licensing_organization) > 75):
            raise ValueError("Invalid value for `licensing_organization`, length must be less than or equal to `75`")  # noqa: E501

        self._licensing_organization = licensing_organization

    @property
    def community_provider_id(self):
        """Gets the community_provider_id of this TrackedChangesEdFiCommunityProviderLicenseKey.  # noqa: E501

        The identifier assigned to a community provider.  # noqa: E501

        :return: The community_provider_id of this TrackedChangesEdFiCommunityProviderLicenseKey.  # noqa: E501
        :rtype: int
        """
        return self._community_provider_id

    @community_provider_id.setter
    def community_provider_id(self, community_provider_id):
        """Sets the community_provider_id of this TrackedChangesEdFiCommunityProviderLicenseKey.

        The identifier assigned to a community provider.  # noqa: E501

        :param community_provider_id: The community_provider_id of this TrackedChangesEdFiCommunityProviderLicenseKey.  # noqa: E501
        :type: int
        """

        self._community_provider_id = community_provider_id

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
        if issubclass(TrackedChangesEdFiCommunityProviderLicenseKey, dict):
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
        if not isinstance(other, TrackedChangesEdFiCommunityProviderLicenseKey):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TrackedChangesEdFiCommunityProviderLicenseKey):
            return True

        return self.to_dict() != other.to_dict()
