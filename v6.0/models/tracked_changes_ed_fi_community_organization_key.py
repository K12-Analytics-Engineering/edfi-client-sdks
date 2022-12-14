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


class TrackedChangesEdFiCommunityOrganizationKey(object):
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
        'community_organization_id': 'int'
    }

    attribute_map = {
        'community_organization_id': 'communityOrganizationId'
    }

    def __init__(self, community_organization_id=None, _configuration=None):  # noqa: E501
        """TrackedChangesEdFiCommunityOrganizationKey - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._community_organization_id = None
        self.discriminator = None

        if community_organization_id is not None:
            self.community_organization_id = community_organization_id

    @property
    def community_organization_id(self):
        """Gets the community_organization_id of this TrackedChangesEdFiCommunityOrganizationKey.  # noqa: E501

        The identifier assigned to a community organization.  # noqa: E501

        :return: The community_organization_id of this TrackedChangesEdFiCommunityOrganizationKey.  # noqa: E501
        :rtype: int
        """
        return self._community_organization_id

    @community_organization_id.setter
    def community_organization_id(self, community_organization_id):
        """Sets the community_organization_id of this TrackedChangesEdFiCommunityOrganizationKey.

        The identifier assigned to a community organization.  # noqa: E501

        :param community_organization_id: The community_organization_id of this TrackedChangesEdFiCommunityOrganizationKey.  # noqa: E501
        :type: int
        """

        self._community_organization_id = community_organization_id

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
        if issubclass(TrackedChangesEdFiCommunityOrganizationKey, dict):
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
        if not isinstance(other, TrackedChangesEdFiCommunityOrganizationKey):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TrackedChangesEdFiCommunityOrganizationKey):
            return True

        return self.to_dict() != other.to_dict()
