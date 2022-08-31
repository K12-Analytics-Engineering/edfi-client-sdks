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


class EdFiStudentEducationOrganizationAssociationProgramParticipation(object):
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
        'program_type_descriptor': 'str',
        'begin_date': 'date',
        'designated_by': 'str',
        'end_date': 'date',
        'program_characteristics': 'list[EdFiStudentEducationOrganizationAssociationProgramParticipationProgramCharacteristic]'
    }

    attribute_map = {
        'program_type_descriptor': 'programTypeDescriptor',
        'begin_date': 'beginDate',
        'designated_by': 'designatedBy',
        'end_date': 'endDate',
        'program_characteristics': 'programCharacteristics'
    }

    def __init__(self, program_type_descriptor=None, begin_date=None, designated_by=None, end_date=None, program_characteristics=None, _configuration=None):  # noqa: E501
        """EdFiStudentEducationOrganizationAssociationProgramParticipation - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._program_type_descriptor = None
        self._begin_date = None
        self._designated_by = None
        self._end_date = None
        self._program_characteristics = None
        self.discriminator = None

        self.program_type_descriptor = program_type_descriptor
        if begin_date is not None:
            self.begin_date = begin_date
        if designated_by is not None:
            self.designated_by = designated_by
        if end_date is not None:
            self.end_date = end_date
        if program_characteristics is not None:
            self.program_characteristics = program_characteristics

    @property
    def program_type_descriptor(self):
        """Gets the program_type_descriptor of this EdFiStudentEducationOrganizationAssociationProgramParticipation.  # noqa: E501

        The type of program.  # noqa: E501

        :return: The program_type_descriptor of this EdFiStudentEducationOrganizationAssociationProgramParticipation.  # noqa: E501
        :rtype: str
        """
        return self._program_type_descriptor

    @program_type_descriptor.setter
    def program_type_descriptor(self, program_type_descriptor):
        """Sets the program_type_descriptor of this EdFiStudentEducationOrganizationAssociationProgramParticipation.

        The type of program.  # noqa: E501

        :param program_type_descriptor: The program_type_descriptor of this EdFiStudentEducationOrganizationAssociationProgramParticipation.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and program_type_descriptor is None:
            raise ValueError("Invalid value for `program_type_descriptor`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                program_type_descriptor is not None and len(program_type_descriptor) > 306):
            raise ValueError("Invalid value for `program_type_descriptor`, length must be less than or equal to `306`")  # noqa: E501

        self._program_type_descriptor = program_type_descriptor

    @property
    def begin_date(self):
        """Gets the begin_date of this EdFiStudentEducationOrganizationAssociationProgramParticipation.  # noqa: E501

        The date the Student was associated with the Program or service.  # noqa: E501

        :return: The begin_date of this EdFiStudentEducationOrganizationAssociationProgramParticipation.  # noqa: E501
        :rtype: date
        """
        return self._begin_date

    @begin_date.setter
    def begin_date(self, begin_date):
        """Sets the begin_date of this EdFiStudentEducationOrganizationAssociationProgramParticipation.

        The date the Student was associated with the Program or service.  # noqa: E501

        :param begin_date: The begin_date of this EdFiStudentEducationOrganizationAssociationProgramParticipation.  # noqa: E501
        :type: date
        """

        self._begin_date = begin_date

    @property
    def designated_by(self):
        """Gets the designated_by of this EdFiStudentEducationOrganizationAssociationProgramParticipation.  # noqa: E501

        The person, organization, or department that designated the program association.  # noqa: E501

        :return: The designated_by of this EdFiStudentEducationOrganizationAssociationProgramParticipation.  # noqa: E501
        :rtype: str
        """
        return self._designated_by

    @designated_by.setter
    def designated_by(self, designated_by):
        """Sets the designated_by of this EdFiStudentEducationOrganizationAssociationProgramParticipation.

        The person, organization, or department that designated the program association.  # noqa: E501

        :param designated_by: The designated_by of this EdFiStudentEducationOrganizationAssociationProgramParticipation.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                designated_by is not None and len(designated_by) > 60):
            raise ValueError("Invalid value for `designated_by`, length must be less than or equal to `60`")  # noqa: E501

        self._designated_by = designated_by

    @property
    def end_date(self):
        """Gets the end_date of this EdFiStudentEducationOrganizationAssociationProgramParticipation.  # noqa: E501

        The date the Program participation ended.  # noqa: E501

        :return: The end_date of this EdFiStudentEducationOrganizationAssociationProgramParticipation.  # noqa: E501
        :rtype: date
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this EdFiStudentEducationOrganizationAssociationProgramParticipation.

        The date the Program participation ended.  # noqa: E501

        :param end_date: The end_date of this EdFiStudentEducationOrganizationAssociationProgramParticipation.  # noqa: E501
        :type: date
        """

        self._end_date = end_date

    @property
    def program_characteristics(self):
        """Gets the program_characteristics of this EdFiStudentEducationOrganizationAssociationProgramParticipation.  # noqa: E501

        An unordered collection of studentEducationOrganizationAssociationProgramParticipationProgramCharacteristics. Reflects important characteristics of the Program, such as categories or particular indications.  # noqa: E501

        :return: The program_characteristics of this EdFiStudentEducationOrganizationAssociationProgramParticipation.  # noqa: E501
        :rtype: list[EdFiStudentEducationOrganizationAssociationProgramParticipationProgramCharacteristic]
        """
        return self._program_characteristics

    @program_characteristics.setter
    def program_characteristics(self, program_characteristics):
        """Sets the program_characteristics of this EdFiStudentEducationOrganizationAssociationProgramParticipation.

        An unordered collection of studentEducationOrganizationAssociationProgramParticipationProgramCharacteristics. Reflects important characteristics of the Program, such as categories or particular indications.  # noqa: E501

        :param program_characteristics: The program_characteristics of this EdFiStudentEducationOrganizationAssociationProgramParticipation.  # noqa: E501
        :type: list[EdFiStudentEducationOrganizationAssociationProgramParticipationProgramCharacteristic]
        """

        self._program_characteristics = program_characteristics

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
        if issubclass(EdFiStudentEducationOrganizationAssociationProgramParticipation, dict):
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
        if not isinstance(other, EdFiStudentEducationOrganizationAssociationProgramParticipation):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EdFiStudentEducationOrganizationAssociationProgramParticipation):
            return True

        return self.to_dict() != other.to_dict()
