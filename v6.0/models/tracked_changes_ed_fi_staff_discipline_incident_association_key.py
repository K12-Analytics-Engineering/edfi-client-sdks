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


class TrackedChangesEdFiStaffDisciplineIncidentAssociationKey(object):
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
        'incident_identifier': 'str',
        'school_id': 'int',
        'staff_unique_id': 'str'
    }

    attribute_map = {
        'incident_identifier': 'incidentIdentifier',
        'school_id': 'schoolId',
        'staff_unique_id': 'staffUniqueId'
    }

    def __init__(self, incident_identifier=None, school_id=None, staff_unique_id=None, _configuration=None):  # noqa: E501
        """TrackedChangesEdFiStaffDisciplineIncidentAssociationKey - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._incident_identifier = None
        self._school_id = None
        self._staff_unique_id = None
        self.discriminator = None

        if incident_identifier is not None:
            self.incident_identifier = incident_identifier
        if school_id is not None:
            self.school_id = school_id
        if staff_unique_id is not None:
            self.staff_unique_id = staff_unique_id

    @property
    def incident_identifier(self):
        """Gets the incident_identifier of this TrackedChangesEdFiStaffDisciplineIncidentAssociationKey.  # noqa: E501

        A locally assigned unique identifier (within the school or school district) to identify each specific DisciplineIncident or occurrence. The same identifier should be used to document the entire discipline incident even if it included multiple offenses and multiple offenders.  # noqa: E501

        :return: The incident_identifier of this TrackedChangesEdFiStaffDisciplineIncidentAssociationKey.  # noqa: E501
        :rtype: str
        """
        return self._incident_identifier

    @incident_identifier.setter
    def incident_identifier(self, incident_identifier):
        """Sets the incident_identifier of this TrackedChangesEdFiStaffDisciplineIncidentAssociationKey.

        A locally assigned unique identifier (within the school or school district) to identify each specific DisciplineIncident or occurrence. The same identifier should be used to document the entire discipline incident even if it included multiple offenses and multiple offenders.  # noqa: E501

        :param incident_identifier: The incident_identifier of this TrackedChangesEdFiStaffDisciplineIncidentAssociationKey.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                incident_identifier is not None and len(incident_identifier) > 20):
            raise ValueError("Invalid value for `incident_identifier`, length must be less than or equal to `20`")  # noqa: E501

        self._incident_identifier = incident_identifier

    @property
    def school_id(self):
        """Gets the school_id of this TrackedChangesEdFiStaffDisciplineIncidentAssociationKey.  # noqa: E501

        The identifier assigned to a school.  # noqa: E501

        :return: The school_id of this TrackedChangesEdFiStaffDisciplineIncidentAssociationKey.  # noqa: E501
        :rtype: int
        """
        return self._school_id

    @school_id.setter
    def school_id(self, school_id):
        """Sets the school_id of this TrackedChangesEdFiStaffDisciplineIncidentAssociationKey.

        The identifier assigned to a school.  # noqa: E501

        :param school_id: The school_id of this TrackedChangesEdFiStaffDisciplineIncidentAssociationKey.  # noqa: E501
        :type: int
        """

        self._school_id = school_id

    @property
    def staff_unique_id(self):
        """Gets the staff_unique_id of this TrackedChangesEdFiStaffDisciplineIncidentAssociationKey.  # noqa: E501

        A unique alphanumeric code assigned to a staff.  # noqa: E501

        :return: The staff_unique_id of this TrackedChangesEdFiStaffDisciplineIncidentAssociationKey.  # noqa: E501
        :rtype: str
        """
        return self._staff_unique_id

    @staff_unique_id.setter
    def staff_unique_id(self, staff_unique_id):
        """Sets the staff_unique_id of this TrackedChangesEdFiStaffDisciplineIncidentAssociationKey.

        A unique alphanumeric code assigned to a staff.  # noqa: E501

        :param staff_unique_id: The staff_unique_id of this TrackedChangesEdFiStaffDisciplineIncidentAssociationKey.  # noqa: E501
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
        if issubclass(TrackedChangesEdFiStaffDisciplineIncidentAssociationKey, dict):
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
        if not isinstance(other, TrackedChangesEdFiStaffDisciplineIncidentAssociationKey):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TrackedChangesEdFiStaffDisciplineIncidentAssociationKey):
            return True

        return self.to_dict() != other.to_dict()