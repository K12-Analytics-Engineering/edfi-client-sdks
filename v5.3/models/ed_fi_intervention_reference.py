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


class EdFiInterventionReference(object):
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
        'intervention_identification_code': 'str',
        'link': 'Link'
    }

    attribute_map = {
        'education_organization_id': 'educationOrganizationId',
        'intervention_identification_code': 'interventionIdentificationCode',
        'link': 'link'
    }

    def __init__(self, education_organization_id=None, intervention_identification_code=None, link=None, _configuration=None):  # noqa: E501
        """EdFiInterventionReference - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._education_organization_id = None
        self._intervention_identification_code = None
        self._link = None
        self.discriminator = None

        self.education_organization_id = education_organization_id
        self.intervention_identification_code = intervention_identification_code
        if link is not None:
            self.link = link

    @property
    def education_organization_id(self):
        """Gets the education_organization_id of this EdFiInterventionReference.  # noqa: E501

        The identifier assigned to an education organization.  # noqa: E501

        :return: The education_organization_id of this EdFiInterventionReference.  # noqa: E501
        :rtype: int
        """
        return self._education_organization_id

    @education_organization_id.setter
    def education_organization_id(self, education_organization_id):
        """Sets the education_organization_id of this EdFiInterventionReference.

        The identifier assigned to an education organization.  # noqa: E501

        :param education_organization_id: The education_organization_id of this EdFiInterventionReference.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and education_organization_id is None:
            raise ValueError("Invalid value for `education_organization_id`, must not be `None`")  # noqa: E501

        self._education_organization_id = education_organization_id

    @property
    def intervention_identification_code(self):
        """Gets the intervention_identification_code of this EdFiInterventionReference.  # noqa: E501

        A unique number or alphanumeric code assigned to an intervention.  # noqa: E501

        :return: The intervention_identification_code of this EdFiInterventionReference.  # noqa: E501
        :rtype: str
        """
        return self._intervention_identification_code

    @intervention_identification_code.setter
    def intervention_identification_code(self, intervention_identification_code):
        """Sets the intervention_identification_code of this EdFiInterventionReference.

        A unique number or alphanumeric code assigned to an intervention.  # noqa: E501

        :param intervention_identification_code: The intervention_identification_code of this EdFiInterventionReference.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and intervention_identification_code is None:
            raise ValueError("Invalid value for `intervention_identification_code`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                intervention_identification_code is not None and len(intervention_identification_code) > 60):
            raise ValueError("Invalid value for `intervention_identification_code`, length must be less than or equal to `60`")  # noqa: E501

        self._intervention_identification_code = intervention_identification_code

    @property
    def link(self):
        """Gets the link of this EdFiInterventionReference.  # noqa: E501


        :return: The link of this EdFiInterventionReference.  # noqa: E501
        :rtype: Link
        """
        return self._link

    @link.setter
    def link(self, link):
        """Sets the link of this EdFiInterventionReference.


        :param link: The link of this EdFiInterventionReference.  # noqa: E501
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
        if issubclass(EdFiInterventionReference, dict):
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
        if not isinstance(other, EdFiInterventionReference):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EdFiInterventionReference):
            return True

        return self.to_dict() != other.to_dict()
