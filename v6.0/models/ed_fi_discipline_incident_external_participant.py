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


class EdFiDisciplineIncidentExternalParticipant(object):
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
        'discipline_incident_participation_code_descriptor': 'str',
        'first_name': 'str',
        'last_surname': 'str'
    }

    attribute_map = {
        'discipline_incident_participation_code_descriptor': 'disciplineIncidentParticipationCodeDescriptor',
        'first_name': 'firstName',
        'last_surname': 'lastSurname'
    }

    def __init__(self, discipline_incident_participation_code_descriptor=None, first_name=None, last_surname=None, _configuration=None):  # noqa: E501
        """EdFiDisciplineIncidentExternalParticipant - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._discipline_incident_participation_code_descriptor = None
        self._first_name = None
        self._last_surname = None
        self.discriminator = None

        self.discipline_incident_participation_code_descriptor = discipline_incident_participation_code_descriptor
        self.first_name = first_name
        self.last_surname = last_surname

    @property
    def discipline_incident_participation_code_descriptor(self):
        """Gets the discipline_incident_participation_code_descriptor of this EdFiDisciplineIncidentExternalParticipant.  # noqa: E501

        The role or type of participation of an individual in the discipline incident.  # noqa: E501

        :return: The discipline_incident_participation_code_descriptor of this EdFiDisciplineIncidentExternalParticipant.  # noqa: E501
        :rtype: str
        """
        return self._discipline_incident_participation_code_descriptor

    @discipline_incident_participation_code_descriptor.setter
    def discipline_incident_participation_code_descriptor(self, discipline_incident_participation_code_descriptor):
        """Sets the discipline_incident_participation_code_descriptor of this EdFiDisciplineIncidentExternalParticipant.

        The role or type of participation of an individual in the discipline incident.  # noqa: E501

        :param discipline_incident_participation_code_descriptor: The discipline_incident_participation_code_descriptor of this EdFiDisciplineIncidentExternalParticipant.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and discipline_incident_participation_code_descriptor is None:
            raise ValueError("Invalid value for `discipline_incident_participation_code_descriptor`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                discipline_incident_participation_code_descriptor is not None and len(discipline_incident_participation_code_descriptor) > 306):
            raise ValueError("Invalid value for `discipline_incident_participation_code_descriptor`, length must be less than or equal to `306`")  # noqa: E501

        self._discipline_incident_participation_code_descriptor = discipline_incident_participation_code_descriptor

    @property
    def first_name(self):
        """Gets the first_name of this EdFiDisciplineIncidentExternalParticipant.  # noqa: E501

        A name given to an individual at birth, baptism, or during another naming ceremony, or through legal change.  # noqa: E501

        :return: The first_name of this EdFiDisciplineIncidentExternalParticipant.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this EdFiDisciplineIncidentExternalParticipant.

        A name given to an individual at birth, baptism, or during another naming ceremony, or through legal change.  # noqa: E501

        :param first_name: The first_name of this EdFiDisciplineIncidentExternalParticipant.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and first_name is None:
            raise ValueError("Invalid value for `first_name`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                first_name is not None and len(first_name) > 75):
            raise ValueError("Invalid value for `first_name`, length must be less than or equal to `75`")  # noqa: E501

        self._first_name = first_name

    @property
    def last_surname(self):
        """Gets the last_surname of this EdFiDisciplineIncidentExternalParticipant.  # noqa: E501

        The name borne in common by members of a family.  # noqa: E501

        :return: The last_surname of this EdFiDisciplineIncidentExternalParticipant.  # noqa: E501
        :rtype: str
        """
        return self._last_surname

    @last_surname.setter
    def last_surname(self, last_surname):
        """Sets the last_surname of this EdFiDisciplineIncidentExternalParticipant.

        The name borne in common by members of a family.  # noqa: E501

        :param last_surname: The last_surname of this EdFiDisciplineIncidentExternalParticipant.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and last_surname is None:
            raise ValueError("Invalid value for `last_surname`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                last_surname is not None and len(last_surname) > 75):
            raise ValueError("Invalid value for `last_surname`, length must be less than or equal to `75`")  # noqa: E501

        self._last_surname = last_surname

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
        if issubclass(EdFiDisciplineIncidentExternalParticipant, dict):
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
        if not isinstance(other, EdFiDisciplineIncidentExternalParticipant):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EdFiDisciplineIncidentExternalParticipant):
            return True

        return self.to_dict() != other.to_dict()
