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


class TrackedChangesEdFiCredentialKey(object):
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
        'state_of_issue_state_abbreviation_descriptor': 'str',
        'credential_identifier': 'str'
    }

    attribute_map = {
        'state_of_issue_state_abbreviation_descriptor': 'stateOfIssueStateAbbreviationDescriptor',
        'credential_identifier': 'credentialIdentifier'
    }

    def __init__(self, state_of_issue_state_abbreviation_descriptor=None, credential_identifier=None, _configuration=None):  # noqa: E501
        """TrackedChangesEdFiCredentialKey - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._state_of_issue_state_abbreviation_descriptor = None
        self._credential_identifier = None
        self.discriminator = None

        if state_of_issue_state_abbreviation_descriptor is not None:
            self.state_of_issue_state_abbreviation_descriptor = state_of_issue_state_abbreviation_descriptor
        if credential_identifier is not None:
            self.credential_identifier = credential_identifier

    @property
    def state_of_issue_state_abbreviation_descriptor(self):
        """Gets the state_of_issue_state_abbreviation_descriptor of this TrackedChangesEdFiCredentialKey.  # noqa: E501

        The abbreviation for the name of the state (within the United States) or extra-state jurisdiction in which a license/credential was issued.  # noqa: E501

        :return: The state_of_issue_state_abbreviation_descriptor of this TrackedChangesEdFiCredentialKey.  # noqa: E501
        :rtype: str
        """
        return self._state_of_issue_state_abbreviation_descriptor

    @state_of_issue_state_abbreviation_descriptor.setter
    def state_of_issue_state_abbreviation_descriptor(self, state_of_issue_state_abbreviation_descriptor):
        """Sets the state_of_issue_state_abbreviation_descriptor of this TrackedChangesEdFiCredentialKey.

        The abbreviation for the name of the state (within the United States) or extra-state jurisdiction in which a license/credential was issued.  # noqa: E501

        :param state_of_issue_state_abbreviation_descriptor: The state_of_issue_state_abbreviation_descriptor of this TrackedChangesEdFiCredentialKey.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                state_of_issue_state_abbreviation_descriptor is not None and len(state_of_issue_state_abbreviation_descriptor) > 306):
            raise ValueError("Invalid value for `state_of_issue_state_abbreviation_descriptor`, length must be less than or equal to `306`")  # noqa: E501

        self._state_of_issue_state_abbreviation_descriptor = state_of_issue_state_abbreviation_descriptor

    @property
    def credential_identifier(self):
        """Gets the credential_identifier of this TrackedChangesEdFiCredentialKey.  # noqa: E501

        Identifier or serial number assigned to the credential.  # noqa: E501

        :return: The credential_identifier of this TrackedChangesEdFiCredentialKey.  # noqa: E501
        :rtype: str
        """
        return self._credential_identifier

    @credential_identifier.setter
    def credential_identifier(self, credential_identifier):
        """Sets the credential_identifier of this TrackedChangesEdFiCredentialKey.

        Identifier or serial number assigned to the credential.  # noqa: E501

        :param credential_identifier: The credential_identifier of this TrackedChangesEdFiCredentialKey.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                credential_identifier is not None and len(credential_identifier) > 60):
            raise ValueError("Invalid value for `credential_identifier`, length must be less than or equal to `60`")  # noqa: E501

        self._credential_identifier = credential_identifier

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
        if issubclass(TrackedChangesEdFiCredentialKey, dict):
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
        if not isinstance(other, TrackedChangesEdFiCredentialKey):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TrackedChangesEdFiCredentialKey):
            return True

        return self.to_dict() != other.to_dict()
