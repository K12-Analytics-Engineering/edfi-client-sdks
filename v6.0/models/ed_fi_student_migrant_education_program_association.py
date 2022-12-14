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


class EdFiStudentMigrantEducationProgramAssociation(object):
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
        'continuation_of_services_reason_descriptor': 'str',
        'eligibility_expiration_date': 'date',
        'end_date': 'date',
        'last_qualifying_move': 'date',
        'migrant_education_program_services': 'list[EdFiStudentMigrantEducationProgramAssociationMigrantEducationProgramService]',
        'participation_status': 'EdFiGeneralStudentProgramAssociationParticipationStatus',
        'priority_for_services': 'bool',
        'program_participation_statuses': 'list[EdFiGeneralStudentProgramAssociationProgramParticipationStatus]',
        'qualifying_arrival_date': 'date',
        'reason_exited_descriptor': 'str',
        'served_outside_of_regular_session': 'bool',
        'state_residency_date': 'date',
        'us_initial_entry': 'date',
        'us_initial_school_entry': 'date',
        'us_most_recent_entry': 'date',
        'etag': 'str'
    }

    attribute_map = {
        'id': 'id',
        'begin_date': 'beginDate',
        'education_organization_reference': 'educationOrganizationReference',
        'program_reference': 'programReference',
        'student_reference': 'studentReference',
        'continuation_of_services_reason_descriptor': 'continuationOfServicesReasonDescriptor',
        'eligibility_expiration_date': 'eligibilityExpirationDate',
        'end_date': 'endDate',
        'last_qualifying_move': 'lastQualifyingMove',
        'migrant_education_program_services': 'migrantEducationProgramServices',
        'participation_status': 'participationStatus',
        'priority_for_services': 'priorityForServices',
        'program_participation_statuses': 'programParticipationStatuses',
        'qualifying_arrival_date': 'qualifyingArrivalDate',
        'reason_exited_descriptor': 'reasonExitedDescriptor',
        'served_outside_of_regular_session': 'servedOutsideOfRegularSession',
        'state_residency_date': 'stateResidencyDate',
        'us_initial_entry': 'usInitialEntry',
        'us_initial_school_entry': 'usInitialSchoolEntry',
        'us_most_recent_entry': 'usMostRecentEntry',
        'etag': '_etag'
    }

    def __init__(self, id=None, begin_date=None, education_organization_reference=None, program_reference=None, student_reference=None, continuation_of_services_reason_descriptor=None, eligibility_expiration_date=None, end_date=None, last_qualifying_move=None, migrant_education_program_services=None, participation_status=None, priority_for_services=None, program_participation_statuses=None, qualifying_arrival_date=None, reason_exited_descriptor=None, served_outside_of_regular_session=None, state_residency_date=None, us_initial_entry=None, us_initial_school_entry=None, us_most_recent_entry=None, etag=None, _configuration=None):  # noqa: E501
        """EdFiStudentMigrantEducationProgramAssociation - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._begin_date = None
        self._education_organization_reference = None
        self._program_reference = None
        self._student_reference = None
        self._continuation_of_services_reason_descriptor = None
        self._eligibility_expiration_date = None
        self._end_date = None
        self._last_qualifying_move = None
        self._migrant_education_program_services = None
        self._participation_status = None
        self._priority_for_services = None
        self._program_participation_statuses = None
        self._qualifying_arrival_date = None
        self._reason_exited_descriptor = None
        self._served_outside_of_regular_session = None
        self._state_residency_date = None
        self._us_initial_entry = None
        self._us_initial_school_entry = None
        self._us_most_recent_entry = None
        self._etag = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.begin_date = begin_date
        self.education_organization_reference = education_organization_reference
        self.program_reference = program_reference
        self.student_reference = student_reference
        if continuation_of_services_reason_descriptor is not None:
            self.continuation_of_services_reason_descriptor = continuation_of_services_reason_descriptor
        if eligibility_expiration_date is not None:
            self.eligibility_expiration_date = eligibility_expiration_date
        if end_date is not None:
            self.end_date = end_date
        self.last_qualifying_move = last_qualifying_move
        if migrant_education_program_services is not None:
            self.migrant_education_program_services = migrant_education_program_services
        if participation_status is not None:
            self.participation_status = participation_status
        self.priority_for_services = priority_for_services
        if program_participation_statuses is not None:
            self.program_participation_statuses = program_participation_statuses
        if qualifying_arrival_date is not None:
            self.qualifying_arrival_date = qualifying_arrival_date
        if reason_exited_descriptor is not None:
            self.reason_exited_descriptor = reason_exited_descriptor
        if served_outside_of_regular_session is not None:
            self.served_outside_of_regular_session = served_outside_of_regular_session
        if state_residency_date is not None:
            self.state_residency_date = state_residency_date
        if us_initial_entry is not None:
            self.us_initial_entry = us_initial_entry
        if us_initial_school_entry is not None:
            self.us_initial_school_entry = us_initial_school_entry
        if us_most_recent_entry is not None:
            self.us_most_recent_entry = us_most_recent_entry
        if etag is not None:
            self.etag = etag

    @property
    def id(self):
        """Gets the id of this EdFiStudentMigrantEducationProgramAssociation.  # noqa: E501

          # noqa: E501

        :return: The id of this EdFiStudentMigrantEducationProgramAssociation.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this EdFiStudentMigrantEducationProgramAssociation.

          # noqa: E501

        :param id: The id of this EdFiStudentMigrantEducationProgramAssociation.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def begin_date(self):
        """Gets the begin_date of this EdFiStudentMigrantEducationProgramAssociation.  # noqa: E501

        The earliest date the student is involved with the program. Typically, this is the date the student becomes eligible for the program.  # noqa: E501

        :return: The begin_date of this EdFiStudentMigrantEducationProgramAssociation.  # noqa: E501
        :rtype: date
        """
        return self._begin_date

    @begin_date.setter
    def begin_date(self, begin_date):
        """Sets the begin_date of this EdFiStudentMigrantEducationProgramAssociation.

        The earliest date the student is involved with the program. Typically, this is the date the student becomes eligible for the program.  # noqa: E501

        :param begin_date: The begin_date of this EdFiStudentMigrantEducationProgramAssociation.  # noqa: E501
        :type: date
        """
        if self._configuration.client_side_validation and begin_date is None:
            raise ValueError("Invalid value for `begin_date`, must not be `None`")  # noqa: E501

        self._begin_date = begin_date

    @property
    def education_organization_reference(self):
        """Gets the education_organization_reference of this EdFiStudentMigrantEducationProgramAssociation.  # noqa: E501


        :return: The education_organization_reference of this EdFiStudentMigrantEducationProgramAssociation.  # noqa: E501
        :rtype: EdFiEducationOrganizationReference
        """
        return self._education_organization_reference

    @education_organization_reference.setter
    def education_organization_reference(self, education_organization_reference):
        """Sets the education_organization_reference of this EdFiStudentMigrantEducationProgramAssociation.


        :param education_organization_reference: The education_organization_reference of this EdFiStudentMigrantEducationProgramAssociation.  # noqa: E501
        :type: EdFiEducationOrganizationReference
        """
        if self._configuration.client_side_validation and education_organization_reference is None:
            raise ValueError("Invalid value for `education_organization_reference`, must not be `None`")  # noqa: E501

        self._education_organization_reference = education_organization_reference

    @property
    def program_reference(self):
        """Gets the program_reference of this EdFiStudentMigrantEducationProgramAssociation.  # noqa: E501


        :return: The program_reference of this EdFiStudentMigrantEducationProgramAssociation.  # noqa: E501
        :rtype: EdFiProgramReference
        """
        return self._program_reference

    @program_reference.setter
    def program_reference(self, program_reference):
        """Sets the program_reference of this EdFiStudentMigrantEducationProgramAssociation.


        :param program_reference: The program_reference of this EdFiStudentMigrantEducationProgramAssociation.  # noqa: E501
        :type: EdFiProgramReference
        """
        if self._configuration.client_side_validation and program_reference is None:
            raise ValueError("Invalid value for `program_reference`, must not be `None`")  # noqa: E501

        self._program_reference = program_reference

    @property
    def student_reference(self):
        """Gets the student_reference of this EdFiStudentMigrantEducationProgramAssociation.  # noqa: E501


        :return: The student_reference of this EdFiStudentMigrantEducationProgramAssociation.  # noqa: E501
        :rtype: EdFiStudentReference
        """
        return self._student_reference

    @student_reference.setter
    def student_reference(self, student_reference):
        """Sets the student_reference of this EdFiStudentMigrantEducationProgramAssociation.


        :param student_reference: The student_reference of this EdFiStudentMigrantEducationProgramAssociation.  # noqa: E501
        :type: EdFiStudentReference
        """
        if self._configuration.client_side_validation and student_reference is None:
            raise ValueError("Invalid value for `student_reference`, must not be `None`")  # noqa: E501

        self._student_reference = student_reference

    @property
    def continuation_of_services_reason_descriptor(self):
        """Gets the continuation_of_services_reason_descriptor of this EdFiStudentMigrantEducationProgramAssociation.  # noqa: E501

        The \"continuation of services\" provision found in Section 1304(e) of the statute provides that (1) a child who ceases to be a migratory child during a school term shall be eligible for services until the end of such term; (2) a child who is no longer a migratory child may continue to receive services for one additional school year, but only if comparable services are not available through other programs; and (3) secondary school students who were eligible for services in secondary school may continue to be served through credit accrual programs until graduation. Only students who received services at any time during their 36 month eligibility period may continue to receive services (not necessarily the same service).  # noqa: E501

        :return: The continuation_of_services_reason_descriptor of this EdFiStudentMigrantEducationProgramAssociation.  # noqa: E501
        :rtype: str
        """
        return self._continuation_of_services_reason_descriptor

    @continuation_of_services_reason_descriptor.setter
    def continuation_of_services_reason_descriptor(self, continuation_of_services_reason_descriptor):
        """Sets the continuation_of_services_reason_descriptor of this EdFiStudentMigrantEducationProgramAssociation.

        The \"continuation of services\" provision found in Section 1304(e) of the statute provides that (1) a child who ceases to be a migratory child during a school term shall be eligible for services until the end of such term; (2) a child who is no longer a migratory child may continue to receive services for one additional school year, but only if comparable services are not available through other programs; and (3) secondary school students who were eligible for services in secondary school may continue to be served through credit accrual programs until graduation. Only students who received services at any time during their 36 month eligibility period may continue to receive services (not necessarily the same service).  # noqa: E501

        :param continuation_of_services_reason_descriptor: The continuation_of_services_reason_descriptor of this EdFiStudentMigrantEducationProgramAssociation.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                continuation_of_services_reason_descriptor is not None and len(continuation_of_services_reason_descriptor) > 306):
            raise ValueError("Invalid value for `continuation_of_services_reason_descriptor`, length must be less than or equal to `306`")  # noqa: E501

        self._continuation_of_services_reason_descriptor = continuation_of_services_reason_descriptor

    @property
    def eligibility_expiration_date(self):
        """Gets the eligibility_expiration_date of this EdFiStudentMigrantEducationProgramAssociation.  # noqa: E501

        The eligibility expiration date is used to determine end of eligibility and to account for a child's eligibility expiring earlier than 36 months from the child's QAD. A child's eligibility would end earlier than 36 months from the child's QAD, if the child is no longer entitled to a free public education (e.g., graduated with a high school diploma, obtained a high school equivalency diploma (HSED), or for other reasons as determined by states' requirements), or if the child passes away.  # noqa: E501

        :return: The eligibility_expiration_date of this EdFiStudentMigrantEducationProgramAssociation.  # noqa: E501
        :rtype: date
        """
        return self._eligibility_expiration_date

    @eligibility_expiration_date.setter
    def eligibility_expiration_date(self, eligibility_expiration_date):
        """Sets the eligibility_expiration_date of this EdFiStudentMigrantEducationProgramAssociation.

        The eligibility expiration date is used to determine end of eligibility and to account for a child's eligibility expiring earlier than 36 months from the child's QAD. A child's eligibility would end earlier than 36 months from the child's QAD, if the child is no longer entitled to a free public education (e.g., graduated with a high school diploma, obtained a high school equivalency diploma (HSED), or for other reasons as determined by states' requirements), or if the child passes away.  # noqa: E501

        :param eligibility_expiration_date: The eligibility_expiration_date of this EdFiStudentMigrantEducationProgramAssociation.  # noqa: E501
        :type: date
        """

        self._eligibility_expiration_date = eligibility_expiration_date

    @property
    def end_date(self):
        """Gets the end_date of this EdFiStudentMigrantEducationProgramAssociation.  # noqa: E501

        The month, day, and year on which the student exited the program or stopped receiving services.  # noqa: E501

        :return: The end_date of this EdFiStudentMigrantEducationProgramAssociation.  # noqa: E501
        :rtype: date
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this EdFiStudentMigrantEducationProgramAssociation.

        The month, day, and year on which the student exited the program or stopped receiving services.  # noqa: E501

        :param end_date: The end_date of this EdFiStudentMigrantEducationProgramAssociation.  # noqa: E501
        :type: date
        """

        self._end_date = end_date

    @property
    def last_qualifying_move(self):
        """Gets the last_qualifying_move of this EdFiStudentMigrantEducationProgramAssociation.  # noqa: E501

        Date the last qualifying move occurred; used to compute MEP status.  # noqa: E501

        :return: The last_qualifying_move of this EdFiStudentMigrantEducationProgramAssociation.  # noqa: E501
        :rtype: date
        """
        return self._last_qualifying_move

    @last_qualifying_move.setter
    def last_qualifying_move(self, last_qualifying_move):
        """Sets the last_qualifying_move of this EdFiStudentMigrantEducationProgramAssociation.

        Date the last qualifying move occurred; used to compute MEP status.  # noqa: E501

        :param last_qualifying_move: The last_qualifying_move of this EdFiStudentMigrantEducationProgramAssociation.  # noqa: E501
        :type: date
        """
        if self._configuration.client_side_validation and last_qualifying_move is None:
            raise ValueError("Invalid value for `last_qualifying_move`, must not be `None`")  # noqa: E501

        self._last_qualifying_move = last_qualifying_move

    @property
    def migrant_education_program_services(self):
        """Gets the migrant_education_program_services of this EdFiStudentMigrantEducationProgramAssociation.  # noqa: E501

        An unordered collection of studentMigrantEducationProgramAssociationMigrantEducationProgramServices. Indicates the service(s) being provided to the student by the migrant education program.  # noqa: E501

        :return: The migrant_education_program_services of this EdFiStudentMigrantEducationProgramAssociation.  # noqa: E501
        :rtype: list[EdFiStudentMigrantEducationProgramAssociationMigrantEducationProgramService]
        """
        return self._migrant_education_program_services

    @migrant_education_program_services.setter
    def migrant_education_program_services(self, migrant_education_program_services):
        """Sets the migrant_education_program_services of this EdFiStudentMigrantEducationProgramAssociation.

        An unordered collection of studentMigrantEducationProgramAssociationMigrantEducationProgramServices. Indicates the service(s) being provided to the student by the migrant education program.  # noqa: E501

        :param migrant_education_program_services: The migrant_education_program_services of this EdFiStudentMigrantEducationProgramAssociation.  # noqa: E501
        :type: list[EdFiStudentMigrantEducationProgramAssociationMigrantEducationProgramService]
        """

        self._migrant_education_program_services = migrant_education_program_services

    @property
    def participation_status(self):
        """Gets the participation_status of this EdFiStudentMigrantEducationProgramAssociation.  # noqa: E501


        :return: The participation_status of this EdFiStudentMigrantEducationProgramAssociation.  # noqa: E501
        :rtype: EdFiGeneralStudentProgramAssociationParticipationStatus
        """
        return self._participation_status

    @participation_status.setter
    def participation_status(self, participation_status):
        """Sets the participation_status of this EdFiStudentMigrantEducationProgramAssociation.


        :param participation_status: The participation_status of this EdFiStudentMigrantEducationProgramAssociation.  # noqa: E501
        :type: EdFiGeneralStudentProgramAssociationParticipationStatus
        """

        self._participation_status = participation_status

    @property
    def priority_for_services(self):
        """Gets the priority_for_services of this EdFiStudentMigrantEducationProgramAssociation.  # noqa: E501

        Report migratory children who are classified as having \"priority for services\" because they are failing, or most at risk of failing to meet the state's challenging state academic content standards and challenging state student academic achievement standards, and their education has been interrupted during the regular school year.  # noqa: E501

        :return: The priority_for_services of this EdFiStudentMigrantEducationProgramAssociation.  # noqa: E501
        :rtype: bool
        """
        return self._priority_for_services

    @priority_for_services.setter
    def priority_for_services(self, priority_for_services):
        """Sets the priority_for_services of this EdFiStudentMigrantEducationProgramAssociation.

        Report migratory children who are classified as having \"priority for services\" because they are failing, or most at risk of failing to meet the state's challenging state academic content standards and challenging state student academic achievement standards, and their education has been interrupted during the regular school year.  # noqa: E501

        :param priority_for_services: The priority_for_services of this EdFiStudentMigrantEducationProgramAssociation.  # noqa: E501
        :type: bool
        """
        if self._configuration.client_side_validation and priority_for_services is None:
            raise ValueError("Invalid value for `priority_for_services`, must not be `None`")  # noqa: E501

        self._priority_for_services = priority_for_services

    @property
    def program_participation_statuses(self):
        """Gets the program_participation_statuses of this EdFiStudentMigrantEducationProgramAssociation.  # noqa: E501

        An unordered collection of generalStudentProgramAssociationProgramParticipationStatuses. The status of the student's program participation.  # noqa: E501

        :return: The program_participation_statuses of this EdFiStudentMigrantEducationProgramAssociation.  # noqa: E501
        :rtype: list[EdFiGeneralStudentProgramAssociationProgramParticipationStatus]
        """
        return self._program_participation_statuses

    @program_participation_statuses.setter
    def program_participation_statuses(self, program_participation_statuses):
        """Sets the program_participation_statuses of this EdFiStudentMigrantEducationProgramAssociation.

        An unordered collection of generalStudentProgramAssociationProgramParticipationStatuses. The status of the student's program participation.  # noqa: E501

        :param program_participation_statuses: The program_participation_statuses of this EdFiStudentMigrantEducationProgramAssociation.  # noqa: E501
        :type: list[EdFiGeneralStudentProgramAssociationProgramParticipationStatus]
        """

        self._program_participation_statuses = program_participation_statuses

    @property
    def qualifying_arrival_date(self):
        """Gets the qualifying_arrival_date of this EdFiStudentMigrantEducationProgramAssociation.  # noqa: E501

        The qualifying arrival date (QAD) is the date the child joins the worker who has already moved, or the date when the worker joins the child who has already moved. The QAD is the date that the child's eligibility for the MEP begins. The QAD is not affected by subsequent non-qualifying moves.  # noqa: E501

        :return: The qualifying_arrival_date of this EdFiStudentMigrantEducationProgramAssociation.  # noqa: E501
        :rtype: date
        """
        return self._qualifying_arrival_date

    @qualifying_arrival_date.setter
    def qualifying_arrival_date(self, qualifying_arrival_date):
        """Sets the qualifying_arrival_date of this EdFiStudentMigrantEducationProgramAssociation.

        The qualifying arrival date (QAD) is the date the child joins the worker who has already moved, or the date when the worker joins the child who has already moved. The QAD is the date that the child's eligibility for the MEP begins. The QAD is not affected by subsequent non-qualifying moves.  # noqa: E501

        :param qualifying_arrival_date: The qualifying_arrival_date of this EdFiStudentMigrantEducationProgramAssociation.  # noqa: E501
        :type: date
        """

        self._qualifying_arrival_date = qualifying_arrival_date

    @property
    def reason_exited_descriptor(self):
        """Gets the reason_exited_descriptor of this EdFiStudentMigrantEducationProgramAssociation.  # noqa: E501

        The reason the student left the program within a school or district.  # noqa: E501

        :return: The reason_exited_descriptor of this EdFiStudentMigrantEducationProgramAssociation.  # noqa: E501
        :rtype: str
        """
        return self._reason_exited_descriptor

    @reason_exited_descriptor.setter
    def reason_exited_descriptor(self, reason_exited_descriptor):
        """Sets the reason_exited_descriptor of this EdFiStudentMigrantEducationProgramAssociation.

        The reason the student left the program within a school or district.  # noqa: E501

        :param reason_exited_descriptor: The reason_exited_descriptor of this EdFiStudentMigrantEducationProgramAssociation.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                reason_exited_descriptor is not None and len(reason_exited_descriptor) > 306):
            raise ValueError("Invalid value for `reason_exited_descriptor`, length must be less than or equal to `306`")  # noqa: E501

        self._reason_exited_descriptor = reason_exited_descriptor

    @property
    def served_outside_of_regular_session(self):
        """Gets the served_outside_of_regular_session of this EdFiStudentMigrantEducationProgramAssociation.  # noqa: E501

        Indicates whether the student received services during the summer session or between sessions.  # noqa: E501

        :return: The served_outside_of_regular_session of this EdFiStudentMigrantEducationProgramAssociation.  # noqa: E501
        :rtype: bool
        """
        return self._served_outside_of_regular_session

    @served_outside_of_regular_session.setter
    def served_outside_of_regular_session(self, served_outside_of_regular_session):
        """Sets the served_outside_of_regular_session of this EdFiStudentMigrantEducationProgramAssociation.

        Indicates whether the student received services during the summer session or between sessions.  # noqa: E501

        :param served_outside_of_regular_session: The served_outside_of_regular_session of this EdFiStudentMigrantEducationProgramAssociation.  # noqa: E501
        :type: bool
        """

        self._served_outside_of_regular_session = served_outside_of_regular_session

    @property
    def state_residency_date(self):
        """Gets the state_residency_date of this EdFiStudentMigrantEducationProgramAssociation.  # noqa: E501

        The verified state residency for the student.  # noqa: E501

        :return: The state_residency_date of this EdFiStudentMigrantEducationProgramAssociation.  # noqa: E501
        :rtype: date
        """
        return self._state_residency_date

    @state_residency_date.setter
    def state_residency_date(self, state_residency_date):
        """Sets the state_residency_date of this EdFiStudentMigrantEducationProgramAssociation.

        The verified state residency for the student.  # noqa: E501

        :param state_residency_date: The state_residency_date of this EdFiStudentMigrantEducationProgramAssociation.  # noqa: E501
        :type: date
        """

        self._state_residency_date = state_residency_date

    @property
    def us_initial_entry(self):
        """Gets the us_initial_entry of this EdFiStudentMigrantEducationProgramAssociation.  # noqa: E501

        The month, day, and year on which the student first entered the U.S.  # noqa: E501

        :return: The us_initial_entry of this EdFiStudentMigrantEducationProgramAssociation.  # noqa: E501
        :rtype: date
        """
        return self._us_initial_entry

    @us_initial_entry.setter
    def us_initial_entry(self, us_initial_entry):
        """Sets the us_initial_entry of this EdFiStudentMigrantEducationProgramAssociation.

        The month, day, and year on which the student first entered the U.S.  # noqa: E501

        :param us_initial_entry: The us_initial_entry of this EdFiStudentMigrantEducationProgramAssociation.  # noqa: E501
        :type: date
        """

        self._us_initial_entry = us_initial_entry

    @property
    def us_initial_school_entry(self):
        """Gets the us_initial_school_entry of this EdFiStudentMigrantEducationProgramAssociation.  # noqa: E501

        The month, day, and year on which the student first entered a U.S. school.  # noqa: E501

        :return: The us_initial_school_entry of this EdFiStudentMigrantEducationProgramAssociation.  # noqa: E501
        :rtype: date
        """
        return self._us_initial_school_entry

    @us_initial_school_entry.setter
    def us_initial_school_entry(self, us_initial_school_entry):
        """Sets the us_initial_school_entry of this EdFiStudentMigrantEducationProgramAssociation.

        The month, day, and year on which the student first entered a U.S. school.  # noqa: E501

        :param us_initial_school_entry: The us_initial_school_entry of this EdFiStudentMigrantEducationProgramAssociation.  # noqa: E501
        :type: date
        """

        self._us_initial_school_entry = us_initial_school_entry

    @property
    def us_most_recent_entry(self):
        """Gets the us_most_recent_entry of this EdFiStudentMigrantEducationProgramAssociation.  # noqa: E501

        The month, day, and year of the student's most recent entry into the U.S.  # noqa: E501

        :return: The us_most_recent_entry of this EdFiStudentMigrantEducationProgramAssociation.  # noqa: E501
        :rtype: date
        """
        return self._us_most_recent_entry

    @us_most_recent_entry.setter
    def us_most_recent_entry(self, us_most_recent_entry):
        """Sets the us_most_recent_entry of this EdFiStudentMigrantEducationProgramAssociation.

        The month, day, and year of the student's most recent entry into the U.S.  # noqa: E501

        :param us_most_recent_entry: The us_most_recent_entry of this EdFiStudentMigrantEducationProgramAssociation.  # noqa: E501
        :type: date
        """

        self._us_most_recent_entry = us_most_recent_entry

    @property
    def etag(self):
        """Gets the etag of this EdFiStudentMigrantEducationProgramAssociation.  # noqa: E501

        A unique system-generated value that identifies the version of the resource.  # noqa: E501

        :return: The etag of this EdFiStudentMigrantEducationProgramAssociation.  # noqa: E501
        :rtype: str
        """
        return self._etag

    @etag.setter
    def etag(self, etag):
        """Sets the etag of this EdFiStudentMigrantEducationProgramAssociation.

        A unique system-generated value that identifies the version of the resource.  # noqa: E501

        :param etag: The etag of this EdFiStudentMigrantEducationProgramAssociation.  # noqa: E501
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
        if issubclass(EdFiStudentMigrantEducationProgramAssociation, dict):
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
        if not isinstance(other, EdFiStudentMigrantEducationProgramAssociation):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EdFiStudentMigrantEducationProgramAssociation):
            return True

        return self.to_dict() != other.to_dict()
