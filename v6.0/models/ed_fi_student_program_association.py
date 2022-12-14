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


class EdFiStudentProgramAssociation(object):
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
        'begin_date': 'date',
        'education_organization_reference': 'EdFiEducationOrganizationReference',
        'program_reference': 'EdFiProgramReference',
        'student_reference': 'EdFiStudentReference',
        'end_date': 'date',
        'participation_status': 'EdFiGeneralStudentProgramAssociationParticipationStatus',
        'program_participation_statuses': 'list[EdFiGeneralStudentProgramAssociationProgramParticipationStatus]',
        'reason_exited_descriptor': 'str',
        'served_outside_of_regular_session': 'bool',
        'services': 'list[EdFiStudentProgramAssociationService]',
        'etag': 'str'
    }

    attribute_map = {
        'id': 'id',
        'begin_date': 'beginDate',
        'education_organization_reference': 'educationOrganizationReference',
        'program_reference': 'programReference',
        'student_reference': 'studentReference',
        'end_date': 'endDate',
        'participation_status': 'participationStatus',
        'program_participation_statuses': 'programParticipationStatuses',
        'reason_exited_descriptor': 'reasonExitedDescriptor',
        'served_outside_of_regular_session': 'servedOutsideOfRegularSession',
        'services': 'services',
        'etag': '_etag'
    }

    def __init__(self, id=None, begin_date=None, education_organization_reference=None, program_reference=None, student_reference=None, end_date=None, participation_status=None, program_participation_statuses=None, reason_exited_descriptor=None, served_outside_of_regular_session=None, services=None, etag=None, _configuration=None):  # noqa: E501
        """EdFiStudentProgramAssociation - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._begin_date = None
        self._education_organization_reference = None
        self._program_reference = None
        self._student_reference = None
        self._end_date = None
        self._participation_status = None
        self._program_participation_statuses = None
        self._reason_exited_descriptor = None
        self._served_outside_of_regular_session = None
        self._services = None
        self._etag = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.begin_date = begin_date
        self.education_organization_reference = education_organization_reference
        self.program_reference = program_reference
        self.student_reference = student_reference
        if end_date is not None:
            self.end_date = end_date
        if participation_status is not None:
            self.participation_status = participation_status
        if program_participation_statuses is not None:
            self.program_participation_statuses = program_participation_statuses
        if reason_exited_descriptor is not None:
            self.reason_exited_descriptor = reason_exited_descriptor
        if served_outside_of_regular_session is not None:
            self.served_outside_of_regular_session = served_outside_of_regular_session
        if services is not None:
            self.services = services
        if etag is not None:
            self.etag = etag

    @property
    def id(self):
        """Gets the id of this EdFiStudentProgramAssociation.  # noqa: E501

          # noqa: E501

        :return: The id of this EdFiStudentProgramAssociation.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this EdFiStudentProgramAssociation.

          # noqa: E501

        :param id: The id of this EdFiStudentProgramAssociation.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def begin_date(self):
        """Gets the begin_date of this EdFiStudentProgramAssociation.  # noqa: E501

        The earliest date the student is involved with the program. Typically, this is the date the student becomes eligible for the program.  # noqa: E501

        :return: The begin_date of this EdFiStudentProgramAssociation.  # noqa: E501
        :rtype: date
        """
        return self._begin_date

    @begin_date.setter
    def begin_date(self, begin_date):
        """Sets the begin_date of this EdFiStudentProgramAssociation.

        The earliest date the student is involved with the program. Typically, this is the date the student becomes eligible for the program.  # noqa: E501

        :param begin_date: The begin_date of this EdFiStudentProgramAssociation.  # noqa: E501
        :type: date
        """
        if self._configuration.client_side_validation and begin_date is None:
            raise ValueError("Invalid value for `begin_date`, must not be `None`")  # noqa: E501

        self._begin_date = begin_date

    @property
    def education_organization_reference(self):
        """Gets the education_organization_reference of this EdFiStudentProgramAssociation.  # noqa: E501


        :return: The education_organization_reference of this EdFiStudentProgramAssociation.  # noqa: E501
        :rtype: EdFiEducationOrganizationReference
        """
        return self._education_organization_reference

    @education_organization_reference.setter
    def education_organization_reference(self, education_organization_reference):
        """Sets the education_organization_reference of this EdFiStudentProgramAssociation.


        :param education_organization_reference: The education_organization_reference of this EdFiStudentProgramAssociation.  # noqa: E501
        :type: EdFiEducationOrganizationReference
        """
        if self._configuration.client_side_validation and education_organization_reference is None:
            raise ValueError("Invalid value for `education_organization_reference`, must not be `None`")  # noqa: E501

        self._education_organization_reference = education_organization_reference

    @property
    def program_reference(self):
        """Gets the program_reference of this EdFiStudentProgramAssociation.  # noqa: E501


        :return: The program_reference of this EdFiStudentProgramAssociation.  # noqa: E501
        :rtype: EdFiProgramReference
        """
        return self._program_reference

    @program_reference.setter
    def program_reference(self, program_reference):
        """Sets the program_reference of this EdFiStudentProgramAssociation.


        :param program_reference: The program_reference of this EdFiStudentProgramAssociation.  # noqa: E501
        :type: EdFiProgramReference
        """
        if self._configuration.client_side_validation and program_reference is None:
            raise ValueError("Invalid value for `program_reference`, must not be `None`")  # noqa: E501

        self._program_reference = program_reference

    @property
    def student_reference(self):
        """Gets the student_reference of this EdFiStudentProgramAssociation.  # noqa: E501


        :return: The student_reference of this EdFiStudentProgramAssociation.  # noqa: E501
        :rtype: EdFiStudentReference
        """
        return self._student_reference

    @student_reference.setter
    def student_reference(self, student_reference):
        """Sets the student_reference of this EdFiStudentProgramAssociation.


        :param student_reference: The student_reference of this EdFiStudentProgramAssociation.  # noqa: E501
        :type: EdFiStudentReference
        """
        if self._configuration.client_side_validation and student_reference is None:
            raise ValueError("Invalid value for `student_reference`, must not be `None`")  # noqa: E501

        self._student_reference = student_reference

    @property
    def end_date(self):
        """Gets the end_date of this EdFiStudentProgramAssociation.  # noqa: E501

        The month, day, and year on which the student exited the program or stopped receiving services.  # noqa: E501

        :return: The end_date of this EdFiStudentProgramAssociation.  # noqa: E501
        :rtype: date
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this EdFiStudentProgramAssociation.

        The month, day, and year on which the student exited the program or stopped receiving services.  # noqa: E501

        :param end_date: The end_date of this EdFiStudentProgramAssociation.  # noqa: E501
        :type: date
        """

        self._end_date = end_date

    @property
    def participation_status(self):
        """Gets the participation_status of this EdFiStudentProgramAssociation.  # noqa: E501


        :return: The participation_status of this EdFiStudentProgramAssociation.  # noqa: E501
        :rtype: EdFiGeneralStudentProgramAssociationParticipationStatus
        """
        return self._participation_status

    @participation_status.setter
    def participation_status(self, participation_status):
        """Sets the participation_status of this EdFiStudentProgramAssociation.


        :param participation_status: The participation_status of this EdFiStudentProgramAssociation.  # noqa: E501
        :type: EdFiGeneralStudentProgramAssociationParticipationStatus
        """

        self._participation_status = participation_status

    @property
    def program_participation_statuses(self):
        """Gets the program_participation_statuses of this EdFiStudentProgramAssociation.  # noqa: E501

        An unordered collection of generalStudentProgramAssociationProgramParticipationStatuses. The status of the student's program participation.  # noqa: E501

        :return: The program_participation_statuses of this EdFiStudentProgramAssociation.  # noqa: E501
        :rtype: list[EdFiGeneralStudentProgramAssociationProgramParticipationStatus]
        """
        return self._program_participation_statuses

    @program_participation_statuses.setter
    def program_participation_statuses(self, program_participation_statuses):
        """Sets the program_participation_statuses of this EdFiStudentProgramAssociation.

        An unordered collection of generalStudentProgramAssociationProgramParticipationStatuses. The status of the student's program participation.  # noqa: E501

        :param program_participation_statuses: The program_participation_statuses of this EdFiStudentProgramAssociation.  # noqa: E501
        :type: list[EdFiGeneralStudentProgramAssociationProgramParticipationStatus]
        """

        self._program_participation_statuses = program_participation_statuses

    @property
    def reason_exited_descriptor(self):
        """Gets the reason_exited_descriptor of this EdFiStudentProgramAssociation.  # noqa: E501

        The reason the student left the program within a school or district.  # noqa: E501

        :return: The reason_exited_descriptor of this EdFiStudentProgramAssociation.  # noqa: E501
        :rtype: str
        """
        return self._reason_exited_descriptor

    @reason_exited_descriptor.setter
    def reason_exited_descriptor(self, reason_exited_descriptor):
        """Sets the reason_exited_descriptor of this EdFiStudentProgramAssociation.

        The reason the student left the program within a school or district.  # noqa: E501

        :param reason_exited_descriptor: The reason_exited_descriptor of this EdFiStudentProgramAssociation.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                reason_exited_descriptor is not None and len(reason_exited_descriptor) > 306):
            raise ValueError("Invalid value for `reason_exited_descriptor`, length must be less than or equal to `306`")  # noqa: E501

        self._reason_exited_descriptor = reason_exited_descriptor

    @property
    def served_outside_of_regular_session(self):
        """Gets the served_outside_of_regular_session of this EdFiStudentProgramAssociation.  # noqa: E501

        Indicates whether the student received services during the summer session or between sessions.  # noqa: E501

        :return: The served_outside_of_regular_session of this EdFiStudentProgramAssociation.  # noqa: E501
        :rtype: bool
        """
        return self._served_outside_of_regular_session

    @served_outside_of_regular_session.setter
    def served_outside_of_regular_session(self, served_outside_of_regular_session):
        """Sets the served_outside_of_regular_session of this EdFiStudentProgramAssociation.

        Indicates whether the student received services during the summer session or between sessions.  # noqa: E501

        :param served_outside_of_regular_session: The served_outside_of_regular_session of this EdFiStudentProgramAssociation.  # noqa: E501
        :type: bool
        """

        self._served_outside_of_regular_session = served_outside_of_regular_session

    @property
    def services(self):
        """Gets the services of this EdFiStudentProgramAssociation.  # noqa: E501

        An unordered collection of studentProgramAssociationServices. Indicates the service(s) being provided to the student by the program.  # noqa: E501

        :return: The services of this EdFiStudentProgramAssociation.  # noqa: E501
        :rtype: list[EdFiStudentProgramAssociationService]
        """
        return self._services

    @services.setter
    def services(self, services):
        """Sets the services of this EdFiStudentProgramAssociation.

        An unordered collection of studentProgramAssociationServices. Indicates the service(s) being provided to the student by the program.  # noqa: E501

        :param services: The services of this EdFiStudentProgramAssociation.  # noqa: E501
        :type: list[EdFiStudentProgramAssociationService]
        """

        self._services = services

    @property
    def etag(self):
        """Gets the etag of this EdFiStudentProgramAssociation.  # noqa: E501

        A unique system-generated value that identifies the version of the resource.  # noqa: E501

        :return: The etag of this EdFiStudentProgramAssociation.  # noqa: E501
        :rtype: str
        """
        return self._etag

    @etag.setter
    def etag(self, etag):
        """Sets the etag of this EdFiStudentProgramAssociation.

        A unique system-generated value that identifies the version of the resource.  # noqa: E501

        :param etag: The etag of this EdFiStudentProgramAssociation.  # noqa: E501
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
        if issubclass(EdFiStudentProgramAssociation, dict):
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
        if not isinstance(other, EdFiStudentProgramAssociation):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EdFiStudentProgramAssociation):
            return True

        return self.to_dict() != other.to_dict()
