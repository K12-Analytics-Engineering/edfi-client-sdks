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


class TrackedChangesTpdmCandidateEducatorPreparationProgramAssociationKey(object):
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
        'begin_date': 'date',
        'candidate_identifier': 'str',
        'education_organization_id': 'int',
        'program_name': 'str',
        'program_type_descriptor': 'str'
    }

    attribute_map = {
        'begin_date': 'beginDate',
        'candidate_identifier': 'candidateIdentifier',
        'education_organization_id': 'educationOrganizationId',
        'program_name': 'programName',
        'program_type_descriptor': 'programTypeDescriptor'
    }

    def __init__(self, begin_date=None, candidate_identifier=None, education_organization_id=None, program_name=None, program_type_descriptor=None, _configuration=None):  # noqa: E501
        """TrackedChangesTpdmCandidateEducatorPreparationProgramAssociationKey - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._begin_date = None
        self._candidate_identifier = None
        self._education_organization_id = None
        self._program_name = None
        self._program_type_descriptor = None
        self.discriminator = None

        if begin_date is not None:
            self.begin_date = begin_date
        if candidate_identifier is not None:
            self.candidate_identifier = candidate_identifier
        if education_organization_id is not None:
            self.education_organization_id = education_organization_id
        if program_name is not None:
            self.program_name = program_name
        if program_type_descriptor is not None:
            self.program_type_descriptor = program_type_descriptor

    @property
    def begin_date(self):
        """Gets the begin_date of this TrackedChangesTpdmCandidateEducatorPreparationProgramAssociationKey.  # noqa: E501

        The begin date for the association.  # noqa: E501

        :return: The begin_date of this TrackedChangesTpdmCandidateEducatorPreparationProgramAssociationKey.  # noqa: E501
        :rtype: date
        """
        return self._begin_date

    @begin_date.setter
    def begin_date(self, begin_date):
        """Sets the begin_date of this TrackedChangesTpdmCandidateEducatorPreparationProgramAssociationKey.

        The begin date for the association.  # noqa: E501

        :param begin_date: The begin_date of this TrackedChangesTpdmCandidateEducatorPreparationProgramAssociationKey.  # noqa: E501
        :type: date
        """

        self._begin_date = begin_date

    @property
    def candidate_identifier(self):
        """Gets the candidate_identifier of this TrackedChangesTpdmCandidateEducatorPreparationProgramAssociationKey.  # noqa: E501

        A unique alphanumeric code assigned to a candidate.  # noqa: E501

        :return: The candidate_identifier of this TrackedChangesTpdmCandidateEducatorPreparationProgramAssociationKey.  # noqa: E501
        :rtype: str
        """
        return self._candidate_identifier

    @candidate_identifier.setter
    def candidate_identifier(self, candidate_identifier):
        """Sets the candidate_identifier of this TrackedChangesTpdmCandidateEducatorPreparationProgramAssociationKey.

        A unique alphanumeric code assigned to a candidate.  # noqa: E501

        :param candidate_identifier: The candidate_identifier of this TrackedChangesTpdmCandidateEducatorPreparationProgramAssociationKey.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                candidate_identifier is not None and len(candidate_identifier) > 32):
            raise ValueError("Invalid value for `candidate_identifier`, length must be less than or equal to `32`")  # noqa: E501

        self._candidate_identifier = candidate_identifier

    @property
    def education_organization_id(self):
        """Gets the education_organization_id of this TrackedChangesTpdmCandidateEducatorPreparationProgramAssociationKey.  # noqa: E501

        The identifier assigned to an education organization.  # noqa: E501

        :return: The education_organization_id of this TrackedChangesTpdmCandidateEducatorPreparationProgramAssociationKey.  # noqa: E501
        :rtype: int
        """
        return self._education_organization_id

    @education_organization_id.setter
    def education_organization_id(self, education_organization_id):
        """Sets the education_organization_id of this TrackedChangesTpdmCandidateEducatorPreparationProgramAssociationKey.

        The identifier assigned to an education organization.  # noqa: E501

        :param education_organization_id: The education_organization_id of this TrackedChangesTpdmCandidateEducatorPreparationProgramAssociationKey.  # noqa: E501
        :type: int
        """

        self._education_organization_id = education_organization_id

    @property
    def program_name(self):
        """Gets the program_name of this TrackedChangesTpdmCandidateEducatorPreparationProgramAssociationKey.  # noqa: E501

        The name of the Educator Preparation Program.  # noqa: E501

        :return: The program_name of this TrackedChangesTpdmCandidateEducatorPreparationProgramAssociationKey.  # noqa: E501
        :rtype: str
        """
        return self._program_name

    @program_name.setter
    def program_name(self, program_name):
        """Sets the program_name of this TrackedChangesTpdmCandidateEducatorPreparationProgramAssociationKey.

        The name of the Educator Preparation Program.  # noqa: E501

        :param program_name: The program_name of this TrackedChangesTpdmCandidateEducatorPreparationProgramAssociationKey.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                program_name is not None and len(program_name) > 255):
            raise ValueError("Invalid value for `program_name`, length must be less than or equal to `255`")  # noqa: E501

        self._program_name = program_name

    @property
    def program_type_descriptor(self):
        """Gets the program_type_descriptor of this TrackedChangesTpdmCandidateEducatorPreparationProgramAssociationKey.  # noqa: E501

        The type of program.  # noqa: E501

        :return: The program_type_descriptor of this TrackedChangesTpdmCandidateEducatorPreparationProgramAssociationKey.  # noqa: E501
        :rtype: str
        """
        return self._program_type_descriptor

    @program_type_descriptor.setter
    def program_type_descriptor(self, program_type_descriptor):
        """Sets the program_type_descriptor of this TrackedChangesTpdmCandidateEducatorPreparationProgramAssociationKey.

        The type of program.  # noqa: E501

        :param program_type_descriptor: The program_type_descriptor of this TrackedChangesTpdmCandidateEducatorPreparationProgramAssociationKey.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                program_type_descriptor is not None and len(program_type_descriptor) > 306):
            raise ValueError("Invalid value for `program_type_descriptor`, length must be less than or equal to `306`")  # noqa: E501

        self._program_type_descriptor = program_type_descriptor

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
        if issubclass(TrackedChangesTpdmCandidateEducatorPreparationProgramAssociationKey, dict):
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
        if not isinstance(other, TrackedChangesTpdmCandidateEducatorPreparationProgramAssociationKey):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TrackedChangesTpdmCandidateEducatorPreparationProgramAssociationKey):
            return True

        return self.to_dict() != other.to_dict()