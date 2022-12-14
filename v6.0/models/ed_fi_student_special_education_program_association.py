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


class EdFiStudentSpecialEducationProgramAssociation(object):
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
        'disabilities': 'list[EdFiStudentSpecialEducationProgramAssociationDisability]',
        'end_date': 'date',
        'idea_eligibility': 'bool',
        'iep_begin_date': 'date',
        'iep_end_date': 'date',
        'iep_review_date': 'date',
        'last_evaluation_date': 'date',
        'medically_fragile': 'bool',
        'multiply_disabled': 'bool',
        'participation_status': 'EdFiGeneralStudentProgramAssociationParticipationStatus',
        'program_participation_statuses': 'list[EdFiGeneralStudentProgramAssociationProgramParticipationStatus]',
        'reason_exited_descriptor': 'str',
        'school_hours_per_week': 'float',
        'served_outside_of_regular_session': 'bool',
        'service_providers': 'list[EdFiStudentSpecialEducationProgramAssociationServiceProvider]',
        'special_education_hours_per_week': 'float',
        'special_education_program_services': 'list[EdFiStudentSpecialEducationProgramAssociationSpecialEducationProgramService]',
        'special_education_setting_descriptor': 'str',
        'etag': 'str'
    }

    attribute_map = {
        'id': 'id',
        'begin_date': 'beginDate',
        'education_organization_reference': 'educationOrganizationReference',
        'program_reference': 'programReference',
        'student_reference': 'studentReference',
        'disabilities': 'disabilities',
        'end_date': 'endDate',
        'idea_eligibility': 'ideaEligibility',
        'iep_begin_date': 'iepBeginDate',
        'iep_end_date': 'iepEndDate',
        'iep_review_date': 'iepReviewDate',
        'last_evaluation_date': 'lastEvaluationDate',
        'medically_fragile': 'medicallyFragile',
        'multiply_disabled': 'multiplyDisabled',
        'participation_status': 'participationStatus',
        'program_participation_statuses': 'programParticipationStatuses',
        'reason_exited_descriptor': 'reasonExitedDescriptor',
        'school_hours_per_week': 'schoolHoursPerWeek',
        'served_outside_of_regular_session': 'servedOutsideOfRegularSession',
        'service_providers': 'serviceProviders',
        'special_education_hours_per_week': 'specialEducationHoursPerWeek',
        'special_education_program_services': 'specialEducationProgramServices',
        'special_education_setting_descriptor': 'specialEducationSettingDescriptor',
        'etag': '_etag'
    }

    def __init__(self, id=None, begin_date=None, education_organization_reference=None, program_reference=None, student_reference=None, disabilities=None, end_date=None, idea_eligibility=None, iep_begin_date=None, iep_end_date=None, iep_review_date=None, last_evaluation_date=None, medically_fragile=None, multiply_disabled=None, participation_status=None, program_participation_statuses=None, reason_exited_descriptor=None, school_hours_per_week=None, served_outside_of_regular_session=None, service_providers=None, special_education_hours_per_week=None, special_education_program_services=None, special_education_setting_descriptor=None, etag=None, _configuration=None):  # noqa: E501
        """EdFiStudentSpecialEducationProgramAssociation - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._begin_date = None
        self._education_organization_reference = None
        self._program_reference = None
        self._student_reference = None
        self._disabilities = None
        self._end_date = None
        self._idea_eligibility = None
        self._iep_begin_date = None
        self._iep_end_date = None
        self._iep_review_date = None
        self._last_evaluation_date = None
        self._medically_fragile = None
        self._multiply_disabled = None
        self._participation_status = None
        self._program_participation_statuses = None
        self._reason_exited_descriptor = None
        self._school_hours_per_week = None
        self._served_outside_of_regular_session = None
        self._service_providers = None
        self._special_education_hours_per_week = None
        self._special_education_program_services = None
        self._special_education_setting_descriptor = None
        self._etag = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.begin_date = begin_date
        self.education_organization_reference = education_organization_reference
        self.program_reference = program_reference
        self.student_reference = student_reference
        if disabilities is not None:
            self.disabilities = disabilities
        if end_date is not None:
            self.end_date = end_date
        if idea_eligibility is not None:
            self.idea_eligibility = idea_eligibility
        if iep_begin_date is not None:
            self.iep_begin_date = iep_begin_date
        if iep_end_date is not None:
            self.iep_end_date = iep_end_date
        if iep_review_date is not None:
            self.iep_review_date = iep_review_date
        if last_evaluation_date is not None:
            self.last_evaluation_date = last_evaluation_date
        if medically_fragile is not None:
            self.medically_fragile = medically_fragile
        if multiply_disabled is not None:
            self.multiply_disabled = multiply_disabled
        if participation_status is not None:
            self.participation_status = participation_status
        if program_participation_statuses is not None:
            self.program_participation_statuses = program_participation_statuses
        if reason_exited_descriptor is not None:
            self.reason_exited_descriptor = reason_exited_descriptor
        if school_hours_per_week is not None:
            self.school_hours_per_week = school_hours_per_week
        if served_outside_of_regular_session is not None:
            self.served_outside_of_regular_session = served_outside_of_regular_session
        if service_providers is not None:
            self.service_providers = service_providers
        if special_education_hours_per_week is not None:
            self.special_education_hours_per_week = special_education_hours_per_week
        if special_education_program_services is not None:
            self.special_education_program_services = special_education_program_services
        if special_education_setting_descriptor is not None:
            self.special_education_setting_descriptor = special_education_setting_descriptor
        if etag is not None:
            self.etag = etag

    @property
    def id(self):
        """Gets the id of this EdFiStudentSpecialEducationProgramAssociation.  # noqa: E501

          # noqa: E501

        :return: The id of this EdFiStudentSpecialEducationProgramAssociation.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this EdFiStudentSpecialEducationProgramAssociation.

          # noqa: E501

        :param id: The id of this EdFiStudentSpecialEducationProgramAssociation.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def begin_date(self):
        """Gets the begin_date of this EdFiStudentSpecialEducationProgramAssociation.  # noqa: E501

        The earliest date the student is involved with the program. Typically, this is the date the student becomes eligible for the program.  # noqa: E501

        :return: The begin_date of this EdFiStudentSpecialEducationProgramAssociation.  # noqa: E501
        :rtype: date
        """
        return self._begin_date

    @begin_date.setter
    def begin_date(self, begin_date):
        """Sets the begin_date of this EdFiStudentSpecialEducationProgramAssociation.

        The earliest date the student is involved with the program. Typically, this is the date the student becomes eligible for the program.  # noqa: E501

        :param begin_date: The begin_date of this EdFiStudentSpecialEducationProgramAssociation.  # noqa: E501
        :type: date
        """
        if self._configuration.client_side_validation and begin_date is None:
            raise ValueError("Invalid value for `begin_date`, must not be `None`")  # noqa: E501

        self._begin_date = begin_date

    @property
    def education_organization_reference(self):
        """Gets the education_organization_reference of this EdFiStudentSpecialEducationProgramAssociation.  # noqa: E501


        :return: The education_organization_reference of this EdFiStudentSpecialEducationProgramAssociation.  # noqa: E501
        :rtype: EdFiEducationOrganizationReference
        """
        return self._education_organization_reference

    @education_organization_reference.setter
    def education_organization_reference(self, education_organization_reference):
        """Sets the education_organization_reference of this EdFiStudentSpecialEducationProgramAssociation.


        :param education_organization_reference: The education_organization_reference of this EdFiStudentSpecialEducationProgramAssociation.  # noqa: E501
        :type: EdFiEducationOrganizationReference
        """
        if self._configuration.client_side_validation and education_organization_reference is None:
            raise ValueError("Invalid value for `education_organization_reference`, must not be `None`")  # noqa: E501

        self._education_organization_reference = education_organization_reference

    @property
    def program_reference(self):
        """Gets the program_reference of this EdFiStudentSpecialEducationProgramAssociation.  # noqa: E501


        :return: The program_reference of this EdFiStudentSpecialEducationProgramAssociation.  # noqa: E501
        :rtype: EdFiProgramReference
        """
        return self._program_reference

    @program_reference.setter
    def program_reference(self, program_reference):
        """Sets the program_reference of this EdFiStudentSpecialEducationProgramAssociation.


        :param program_reference: The program_reference of this EdFiStudentSpecialEducationProgramAssociation.  # noqa: E501
        :type: EdFiProgramReference
        """
        if self._configuration.client_side_validation and program_reference is None:
            raise ValueError("Invalid value for `program_reference`, must not be `None`")  # noqa: E501

        self._program_reference = program_reference

    @property
    def student_reference(self):
        """Gets the student_reference of this EdFiStudentSpecialEducationProgramAssociation.  # noqa: E501


        :return: The student_reference of this EdFiStudentSpecialEducationProgramAssociation.  # noqa: E501
        :rtype: EdFiStudentReference
        """
        return self._student_reference

    @student_reference.setter
    def student_reference(self, student_reference):
        """Sets the student_reference of this EdFiStudentSpecialEducationProgramAssociation.


        :param student_reference: The student_reference of this EdFiStudentSpecialEducationProgramAssociation.  # noqa: E501
        :type: EdFiStudentReference
        """
        if self._configuration.client_side_validation and student_reference is None:
            raise ValueError("Invalid value for `student_reference`, must not be `None`")  # noqa: E501

        self._student_reference = student_reference

    @property
    def disabilities(self):
        """Gets the disabilities of this EdFiStudentSpecialEducationProgramAssociation.  # noqa: E501

        An unordered collection of studentSpecialEducationProgramAssociationDisabilities. The disability condition(s) that best describes an individual's impairment, as related to special education services received.  # noqa: E501

        :return: The disabilities of this EdFiStudentSpecialEducationProgramAssociation.  # noqa: E501
        :rtype: list[EdFiStudentSpecialEducationProgramAssociationDisability]
        """
        return self._disabilities

    @disabilities.setter
    def disabilities(self, disabilities):
        """Sets the disabilities of this EdFiStudentSpecialEducationProgramAssociation.

        An unordered collection of studentSpecialEducationProgramAssociationDisabilities. The disability condition(s) that best describes an individual's impairment, as related to special education services received.  # noqa: E501

        :param disabilities: The disabilities of this EdFiStudentSpecialEducationProgramAssociation.  # noqa: E501
        :type: list[EdFiStudentSpecialEducationProgramAssociationDisability]
        """

        self._disabilities = disabilities

    @property
    def end_date(self):
        """Gets the end_date of this EdFiStudentSpecialEducationProgramAssociation.  # noqa: E501

        The month, day, and year on which the student exited the program or stopped receiving services.  # noqa: E501

        :return: The end_date of this EdFiStudentSpecialEducationProgramAssociation.  # noqa: E501
        :rtype: date
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this EdFiStudentSpecialEducationProgramAssociation.

        The month, day, and year on which the student exited the program or stopped receiving services.  # noqa: E501

        :param end_date: The end_date of this EdFiStudentSpecialEducationProgramAssociation.  # noqa: E501
        :type: date
        """

        self._end_date = end_date

    @property
    def idea_eligibility(self):
        """Gets the idea_eligibility of this EdFiStudentSpecialEducationProgramAssociation.  # noqa: E501

        Indicator of the eligibility of the student to receive special education services according to the Individuals with Disabilities Education Act (IDEA).  # noqa: E501

        :return: The idea_eligibility of this EdFiStudentSpecialEducationProgramAssociation.  # noqa: E501
        :rtype: bool
        """
        return self._idea_eligibility

    @idea_eligibility.setter
    def idea_eligibility(self, idea_eligibility):
        """Sets the idea_eligibility of this EdFiStudentSpecialEducationProgramAssociation.

        Indicator of the eligibility of the student to receive special education services according to the Individuals with Disabilities Education Act (IDEA).  # noqa: E501

        :param idea_eligibility: The idea_eligibility of this EdFiStudentSpecialEducationProgramAssociation.  # noqa: E501
        :type: bool
        """

        self._idea_eligibility = idea_eligibility

    @property
    def iep_begin_date(self):
        """Gets the iep_begin_date of this EdFiStudentSpecialEducationProgramAssociation.  # noqa: E501

        The effective date of the most recent IEP.  # noqa: E501

        :return: The iep_begin_date of this EdFiStudentSpecialEducationProgramAssociation.  # noqa: E501
        :rtype: date
        """
        return self._iep_begin_date

    @iep_begin_date.setter
    def iep_begin_date(self, iep_begin_date):
        """Sets the iep_begin_date of this EdFiStudentSpecialEducationProgramAssociation.

        The effective date of the most recent IEP.  # noqa: E501

        :param iep_begin_date: The iep_begin_date of this EdFiStudentSpecialEducationProgramAssociation.  # noqa: E501
        :type: date
        """

        self._iep_begin_date = iep_begin_date

    @property
    def iep_end_date(self):
        """Gets the iep_end_date of this EdFiStudentSpecialEducationProgramAssociation.  # noqa: E501

        The end date of the most recent IEP.  # noqa: E501

        :return: The iep_end_date of this EdFiStudentSpecialEducationProgramAssociation.  # noqa: E501
        :rtype: date
        """
        return self._iep_end_date

    @iep_end_date.setter
    def iep_end_date(self, iep_end_date):
        """Sets the iep_end_date of this EdFiStudentSpecialEducationProgramAssociation.

        The end date of the most recent IEP.  # noqa: E501

        :param iep_end_date: The iep_end_date of this EdFiStudentSpecialEducationProgramAssociation.  # noqa: E501
        :type: date
        """

        self._iep_end_date = iep_end_date

    @property
    def iep_review_date(self):
        """Gets the iep_review_date of this EdFiStudentSpecialEducationProgramAssociation.  # noqa: E501

        The date of the last IEP review.  # noqa: E501

        :return: The iep_review_date of this EdFiStudentSpecialEducationProgramAssociation.  # noqa: E501
        :rtype: date
        """
        return self._iep_review_date

    @iep_review_date.setter
    def iep_review_date(self, iep_review_date):
        """Sets the iep_review_date of this EdFiStudentSpecialEducationProgramAssociation.

        The date of the last IEP review.  # noqa: E501

        :param iep_review_date: The iep_review_date of this EdFiStudentSpecialEducationProgramAssociation.  # noqa: E501
        :type: date
        """

        self._iep_review_date = iep_review_date

    @property
    def last_evaluation_date(self):
        """Gets the last_evaluation_date of this EdFiStudentSpecialEducationProgramAssociation.  # noqa: E501

        The date of the last special education evaluation.  # noqa: E501

        :return: The last_evaluation_date of this EdFiStudentSpecialEducationProgramAssociation.  # noqa: E501
        :rtype: date
        """
        return self._last_evaluation_date

    @last_evaluation_date.setter
    def last_evaluation_date(self, last_evaluation_date):
        """Sets the last_evaluation_date of this EdFiStudentSpecialEducationProgramAssociation.

        The date of the last special education evaluation.  # noqa: E501

        :param last_evaluation_date: The last_evaluation_date of this EdFiStudentSpecialEducationProgramAssociation.  # noqa: E501
        :type: date
        """

        self._last_evaluation_date = last_evaluation_date

    @property
    def medically_fragile(self):
        """Gets the medically_fragile of this EdFiStudentSpecialEducationProgramAssociation.  # noqa: E501

        Indicates whether the student receiving special education and related services is: 1) in the age range of birth to 22 years, and 2) has a serious, ongoing illness or a chronic condition that has lasted or is anticipated to last at least 12 or more months or has required at least one month of hospitalization, and that requires daily, ongoing medical treatments and monitoring by appropriately trained personnel which may include parents or other family members, and 3) requires the routine use of medical device or of assistive technology to compensate for the loss of usefulness of a body function needed to participate in activities of daily living, and 4) lives with ongoing threat to his or her continued well-being. Aligns with federal requirements.  # noqa: E501

        :return: The medically_fragile of this EdFiStudentSpecialEducationProgramAssociation.  # noqa: E501
        :rtype: bool
        """
        return self._medically_fragile

    @medically_fragile.setter
    def medically_fragile(self, medically_fragile):
        """Sets the medically_fragile of this EdFiStudentSpecialEducationProgramAssociation.

        Indicates whether the student receiving special education and related services is: 1) in the age range of birth to 22 years, and 2) has a serious, ongoing illness or a chronic condition that has lasted or is anticipated to last at least 12 or more months or has required at least one month of hospitalization, and that requires daily, ongoing medical treatments and monitoring by appropriately trained personnel which may include parents or other family members, and 3) requires the routine use of medical device or of assistive technology to compensate for the loss of usefulness of a body function needed to participate in activities of daily living, and 4) lives with ongoing threat to his or her continued well-being. Aligns with federal requirements.  # noqa: E501

        :param medically_fragile: The medically_fragile of this EdFiStudentSpecialEducationProgramAssociation.  # noqa: E501
        :type: bool
        """

        self._medically_fragile = medically_fragile

    @property
    def multiply_disabled(self):
        """Gets the multiply_disabled of this EdFiStudentSpecialEducationProgramAssociation.  # noqa: E501

        Indicates whether the student receiving special education and related services has been designated as multiply disabled by the admission, review, and dismissal committee as aligned with federal requirements.  # noqa: E501

        :return: The multiply_disabled of this EdFiStudentSpecialEducationProgramAssociation.  # noqa: E501
        :rtype: bool
        """
        return self._multiply_disabled

    @multiply_disabled.setter
    def multiply_disabled(self, multiply_disabled):
        """Sets the multiply_disabled of this EdFiStudentSpecialEducationProgramAssociation.

        Indicates whether the student receiving special education and related services has been designated as multiply disabled by the admission, review, and dismissal committee as aligned with federal requirements.  # noqa: E501

        :param multiply_disabled: The multiply_disabled of this EdFiStudentSpecialEducationProgramAssociation.  # noqa: E501
        :type: bool
        """

        self._multiply_disabled = multiply_disabled

    @property
    def participation_status(self):
        """Gets the participation_status of this EdFiStudentSpecialEducationProgramAssociation.  # noqa: E501


        :return: The participation_status of this EdFiStudentSpecialEducationProgramAssociation.  # noqa: E501
        :rtype: EdFiGeneralStudentProgramAssociationParticipationStatus
        """
        return self._participation_status

    @participation_status.setter
    def participation_status(self, participation_status):
        """Sets the participation_status of this EdFiStudentSpecialEducationProgramAssociation.


        :param participation_status: The participation_status of this EdFiStudentSpecialEducationProgramAssociation.  # noqa: E501
        :type: EdFiGeneralStudentProgramAssociationParticipationStatus
        """

        self._participation_status = participation_status

    @property
    def program_participation_statuses(self):
        """Gets the program_participation_statuses of this EdFiStudentSpecialEducationProgramAssociation.  # noqa: E501

        An unordered collection of generalStudentProgramAssociationProgramParticipationStatuses. The status of the student's program participation.  # noqa: E501

        :return: The program_participation_statuses of this EdFiStudentSpecialEducationProgramAssociation.  # noqa: E501
        :rtype: list[EdFiGeneralStudentProgramAssociationProgramParticipationStatus]
        """
        return self._program_participation_statuses

    @program_participation_statuses.setter
    def program_participation_statuses(self, program_participation_statuses):
        """Sets the program_participation_statuses of this EdFiStudentSpecialEducationProgramAssociation.

        An unordered collection of generalStudentProgramAssociationProgramParticipationStatuses. The status of the student's program participation.  # noqa: E501

        :param program_participation_statuses: The program_participation_statuses of this EdFiStudentSpecialEducationProgramAssociation.  # noqa: E501
        :type: list[EdFiGeneralStudentProgramAssociationProgramParticipationStatus]
        """

        self._program_participation_statuses = program_participation_statuses

    @property
    def reason_exited_descriptor(self):
        """Gets the reason_exited_descriptor of this EdFiStudentSpecialEducationProgramAssociation.  # noqa: E501

        The reason the student left the program within a school or district.  # noqa: E501

        :return: The reason_exited_descriptor of this EdFiStudentSpecialEducationProgramAssociation.  # noqa: E501
        :rtype: str
        """
        return self._reason_exited_descriptor

    @reason_exited_descriptor.setter
    def reason_exited_descriptor(self, reason_exited_descriptor):
        """Sets the reason_exited_descriptor of this EdFiStudentSpecialEducationProgramAssociation.

        The reason the student left the program within a school or district.  # noqa: E501

        :param reason_exited_descriptor: The reason_exited_descriptor of this EdFiStudentSpecialEducationProgramAssociation.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                reason_exited_descriptor is not None and len(reason_exited_descriptor) > 306):
            raise ValueError("Invalid value for `reason_exited_descriptor`, length must be less than or equal to `306`")  # noqa: E501

        self._reason_exited_descriptor = reason_exited_descriptor

    @property
    def school_hours_per_week(self):
        """Gets the school_hours_per_week of this EdFiStudentSpecialEducationProgramAssociation.  # noqa: E501

        Indicate the total number of hours of instructional time per week for the school that the student attends.  # noqa: E501

        :return: The school_hours_per_week of this EdFiStudentSpecialEducationProgramAssociation.  # noqa: E501
        :rtype: float
        """
        return self._school_hours_per_week

    @school_hours_per_week.setter
    def school_hours_per_week(self, school_hours_per_week):
        """Sets the school_hours_per_week of this EdFiStudentSpecialEducationProgramAssociation.

        Indicate the total number of hours of instructional time per week for the school that the student attends.  # noqa: E501

        :param school_hours_per_week: The school_hours_per_week of this EdFiStudentSpecialEducationProgramAssociation.  # noqa: E501
        :type: float
        """

        self._school_hours_per_week = school_hours_per_week

    @property
    def served_outside_of_regular_session(self):
        """Gets the served_outside_of_regular_session of this EdFiStudentSpecialEducationProgramAssociation.  # noqa: E501

        Indicates whether the student received services during the summer session or between sessions.  # noqa: E501

        :return: The served_outside_of_regular_session of this EdFiStudentSpecialEducationProgramAssociation.  # noqa: E501
        :rtype: bool
        """
        return self._served_outside_of_regular_session

    @served_outside_of_regular_session.setter
    def served_outside_of_regular_session(self, served_outside_of_regular_session):
        """Sets the served_outside_of_regular_session of this EdFiStudentSpecialEducationProgramAssociation.

        Indicates whether the student received services during the summer session or between sessions.  # noqa: E501

        :param served_outside_of_regular_session: The served_outside_of_regular_session of this EdFiStudentSpecialEducationProgramAssociation.  # noqa: E501
        :type: bool
        """

        self._served_outside_of_regular_session = served_outside_of_regular_session

    @property
    def service_providers(self):
        """Gets the service_providers of this EdFiStudentSpecialEducationProgramAssociation.  # noqa: E501

        An unordered collection of studentSpecialEducationProgramAssociationServiceProviders. The staff providing special education services to the student.  # noqa: E501

        :return: The service_providers of this EdFiStudentSpecialEducationProgramAssociation.  # noqa: E501
        :rtype: list[EdFiStudentSpecialEducationProgramAssociationServiceProvider]
        """
        return self._service_providers

    @service_providers.setter
    def service_providers(self, service_providers):
        """Sets the service_providers of this EdFiStudentSpecialEducationProgramAssociation.

        An unordered collection of studentSpecialEducationProgramAssociationServiceProviders. The staff providing special education services to the student.  # noqa: E501

        :param service_providers: The service_providers of this EdFiStudentSpecialEducationProgramAssociation.  # noqa: E501
        :type: list[EdFiStudentSpecialEducationProgramAssociationServiceProvider]
        """

        self._service_providers = service_providers

    @property
    def special_education_hours_per_week(self):
        """Gets the special_education_hours_per_week of this EdFiStudentSpecialEducationProgramAssociation.  # noqa: E501

        The number of hours per week for special education instruction and therapy.  # noqa: E501

        :return: The special_education_hours_per_week of this EdFiStudentSpecialEducationProgramAssociation.  # noqa: E501
        :rtype: float
        """
        return self._special_education_hours_per_week

    @special_education_hours_per_week.setter
    def special_education_hours_per_week(self, special_education_hours_per_week):
        """Sets the special_education_hours_per_week of this EdFiStudentSpecialEducationProgramAssociation.

        The number of hours per week for special education instruction and therapy.  # noqa: E501

        :param special_education_hours_per_week: The special_education_hours_per_week of this EdFiStudentSpecialEducationProgramAssociation.  # noqa: E501
        :type: float
        """

        self._special_education_hours_per_week = special_education_hours_per_week

    @property
    def special_education_program_services(self):
        """Gets the special_education_program_services of this EdFiStudentSpecialEducationProgramAssociation.  # noqa: E501

        An unordered collection of studentSpecialEducationProgramAssociationSpecialEducationProgramServices. Indicates the service(s) being provided to the student by the special education program.  # noqa: E501

        :return: The special_education_program_services of this EdFiStudentSpecialEducationProgramAssociation.  # noqa: E501
        :rtype: list[EdFiStudentSpecialEducationProgramAssociationSpecialEducationProgramService]
        """
        return self._special_education_program_services

    @special_education_program_services.setter
    def special_education_program_services(self, special_education_program_services):
        """Sets the special_education_program_services of this EdFiStudentSpecialEducationProgramAssociation.

        An unordered collection of studentSpecialEducationProgramAssociationSpecialEducationProgramServices. Indicates the service(s) being provided to the student by the special education program.  # noqa: E501

        :param special_education_program_services: The special_education_program_services of this EdFiStudentSpecialEducationProgramAssociation.  # noqa: E501
        :type: list[EdFiStudentSpecialEducationProgramAssociationSpecialEducationProgramService]
        """

        self._special_education_program_services = special_education_program_services

    @property
    def special_education_setting_descriptor(self):
        """Gets the special_education_setting_descriptor of this EdFiStudentSpecialEducationProgramAssociation.  # noqa: E501

        The major instructional setting (more than 50 percent of a student's special education program).  # noqa: E501

        :return: The special_education_setting_descriptor of this EdFiStudentSpecialEducationProgramAssociation.  # noqa: E501
        :rtype: str
        """
        return self._special_education_setting_descriptor

    @special_education_setting_descriptor.setter
    def special_education_setting_descriptor(self, special_education_setting_descriptor):
        """Sets the special_education_setting_descriptor of this EdFiStudentSpecialEducationProgramAssociation.

        The major instructional setting (more than 50 percent of a student's special education program).  # noqa: E501

        :param special_education_setting_descriptor: The special_education_setting_descriptor of this EdFiStudentSpecialEducationProgramAssociation.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                special_education_setting_descriptor is not None and len(special_education_setting_descriptor) > 306):
            raise ValueError("Invalid value for `special_education_setting_descriptor`, length must be less than or equal to `306`")  # noqa: E501

        self._special_education_setting_descriptor = special_education_setting_descriptor

    @property
    def etag(self):
        """Gets the etag of this EdFiStudentSpecialEducationProgramAssociation.  # noqa: E501

        A unique system-generated value that identifies the version of the resource.  # noqa: E501

        :return: The etag of this EdFiStudentSpecialEducationProgramAssociation.  # noqa: E501
        :rtype: str
        """
        return self._etag

    @etag.setter
    def etag(self, etag):
        """Sets the etag of this EdFiStudentSpecialEducationProgramAssociation.

        A unique system-generated value that identifies the version of the resource.  # noqa: E501

        :param etag: The etag of this EdFiStudentSpecialEducationProgramAssociation.  # noqa: E501
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
        if issubclass(EdFiStudentSpecialEducationProgramAssociation, dict):
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
        if not isinstance(other, EdFiStudentSpecialEducationProgramAssociation):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EdFiStudentSpecialEducationProgramAssociation):
            return True

        return self.to_dict() != other.to_dict()
