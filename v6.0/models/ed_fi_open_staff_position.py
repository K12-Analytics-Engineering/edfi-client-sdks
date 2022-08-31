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


class EdFiOpenStaffPosition(object):
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
        'requisition_number': 'str',
        'education_organization_reference': 'EdFiEducationOrganizationReference',
        'academic_subjects': 'list[EdFiOpenStaffPositionAcademicSubject]',
        'date_posted': 'date',
        'date_posting_removed': 'date',
        'employment_status_descriptor': 'str',
        'instructional_grade_levels': 'list[EdFiOpenStaffPositionInstructionalGradeLevel]',
        'position_title': 'str',
        'posting_result_descriptor': 'str',
        'program_assignment_descriptor': 'str',
        'staff_classification_descriptor': 'str',
        'etag': 'str'
    }

    attribute_map = {
        'id': 'id',
        'requisition_number': 'requisitionNumber',
        'education_organization_reference': 'educationOrganizationReference',
        'academic_subjects': 'academicSubjects',
        'date_posted': 'datePosted',
        'date_posting_removed': 'datePostingRemoved',
        'employment_status_descriptor': 'employmentStatusDescriptor',
        'instructional_grade_levels': 'instructionalGradeLevels',
        'position_title': 'positionTitle',
        'posting_result_descriptor': 'postingResultDescriptor',
        'program_assignment_descriptor': 'programAssignmentDescriptor',
        'staff_classification_descriptor': 'staffClassificationDescriptor',
        'etag': '_etag'
    }

    def __init__(self, id=None, requisition_number=None, education_organization_reference=None, academic_subjects=None, date_posted=None, date_posting_removed=None, employment_status_descriptor=None, instructional_grade_levels=None, position_title=None, posting_result_descriptor=None, program_assignment_descriptor=None, staff_classification_descriptor=None, etag=None, _configuration=None):  # noqa: E501
        """EdFiOpenStaffPosition - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._requisition_number = None
        self._education_organization_reference = None
        self._academic_subjects = None
        self._date_posted = None
        self._date_posting_removed = None
        self._employment_status_descriptor = None
        self._instructional_grade_levels = None
        self._position_title = None
        self._posting_result_descriptor = None
        self._program_assignment_descriptor = None
        self._staff_classification_descriptor = None
        self._etag = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.requisition_number = requisition_number
        self.education_organization_reference = education_organization_reference
        if academic_subjects is not None:
            self.academic_subjects = academic_subjects
        self.date_posted = date_posted
        if date_posting_removed is not None:
            self.date_posting_removed = date_posting_removed
        self.employment_status_descriptor = employment_status_descriptor
        if instructional_grade_levels is not None:
            self.instructional_grade_levels = instructional_grade_levels
        if position_title is not None:
            self.position_title = position_title
        if posting_result_descriptor is not None:
            self.posting_result_descriptor = posting_result_descriptor
        if program_assignment_descriptor is not None:
            self.program_assignment_descriptor = program_assignment_descriptor
        self.staff_classification_descriptor = staff_classification_descriptor
        if etag is not None:
            self.etag = etag

    @property
    def id(self):
        """Gets the id of this EdFiOpenStaffPosition.  # noqa: E501

          # noqa: E501

        :return: The id of this EdFiOpenStaffPosition.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this EdFiOpenStaffPosition.

          # noqa: E501

        :param id: The id of this EdFiOpenStaffPosition.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def requisition_number(self):
        """Gets the requisition_number of this EdFiOpenStaffPosition.  # noqa: E501

        The number or identifier assigned to an open staff position, typically a requisition number assigned by Human Resources.  # noqa: E501

        :return: The requisition_number of this EdFiOpenStaffPosition.  # noqa: E501
        :rtype: str
        """
        return self._requisition_number

    @requisition_number.setter
    def requisition_number(self, requisition_number):
        """Sets the requisition_number of this EdFiOpenStaffPosition.

        The number or identifier assigned to an open staff position, typically a requisition number assigned by Human Resources.  # noqa: E501

        :param requisition_number: The requisition_number of this EdFiOpenStaffPosition.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and requisition_number is None:
            raise ValueError("Invalid value for `requisition_number`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                requisition_number is not None and len(requisition_number) > 20):
            raise ValueError("Invalid value for `requisition_number`, length must be less than or equal to `20`")  # noqa: E501

        self._requisition_number = requisition_number

    @property
    def education_organization_reference(self):
        """Gets the education_organization_reference of this EdFiOpenStaffPosition.  # noqa: E501


        :return: The education_organization_reference of this EdFiOpenStaffPosition.  # noqa: E501
        :rtype: EdFiEducationOrganizationReference
        """
        return self._education_organization_reference

    @education_organization_reference.setter
    def education_organization_reference(self, education_organization_reference):
        """Sets the education_organization_reference of this EdFiOpenStaffPosition.


        :param education_organization_reference: The education_organization_reference of this EdFiOpenStaffPosition.  # noqa: E501
        :type: EdFiEducationOrganizationReference
        """
        if self._configuration.client_side_validation and education_organization_reference is None:
            raise ValueError("Invalid value for `education_organization_reference`, must not be `None`")  # noqa: E501

        self._education_organization_reference = education_organization_reference

    @property
    def academic_subjects(self):
        """Gets the academic_subjects of this EdFiOpenStaffPosition.  # noqa: E501

        An unordered collection of openStaffPositionAcademicSubjects. The teaching field required for the open staff position.  # noqa: E501

        :return: The academic_subjects of this EdFiOpenStaffPosition.  # noqa: E501
        :rtype: list[EdFiOpenStaffPositionAcademicSubject]
        """
        return self._academic_subjects

    @academic_subjects.setter
    def academic_subjects(self, academic_subjects):
        """Sets the academic_subjects of this EdFiOpenStaffPosition.

        An unordered collection of openStaffPositionAcademicSubjects. The teaching field required for the open staff position.  # noqa: E501

        :param academic_subjects: The academic_subjects of this EdFiOpenStaffPosition.  # noqa: E501
        :type: list[EdFiOpenStaffPositionAcademicSubject]
        """

        self._academic_subjects = academic_subjects

    @property
    def date_posted(self):
        """Gets the date_posted of this EdFiOpenStaffPosition.  # noqa: E501

        Date the open staff position was posted.  # noqa: E501

        :return: The date_posted of this EdFiOpenStaffPosition.  # noqa: E501
        :rtype: date
        """
        return self._date_posted

    @date_posted.setter
    def date_posted(self, date_posted):
        """Sets the date_posted of this EdFiOpenStaffPosition.

        Date the open staff position was posted.  # noqa: E501

        :param date_posted: The date_posted of this EdFiOpenStaffPosition.  # noqa: E501
        :type: date
        """
        if self._configuration.client_side_validation and date_posted is None:
            raise ValueError("Invalid value for `date_posted`, must not be `None`")  # noqa: E501

        self._date_posted = date_posted

    @property
    def date_posting_removed(self):
        """Gets the date_posting_removed of this EdFiOpenStaffPosition.  # noqa: E501

        The date the posting was removed or filled.  # noqa: E501

        :return: The date_posting_removed of this EdFiOpenStaffPosition.  # noqa: E501
        :rtype: date
        """
        return self._date_posting_removed

    @date_posting_removed.setter
    def date_posting_removed(self, date_posting_removed):
        """Sets the date_posting_removed of this EdFiOpenStaffPosition.

        The date the posting was removed or filled.  # noqa: E501

        :param date_posting_removed: The date_posting_removed of this EdFiOpenStaffPosition.  # noqa: E501
        :type: date
        """

        self._date_posting_removed = date_posting_removed

    @property
    def employment_status_descriptor(self):
        """Gets the employment_status_descriptor of this EdFiOpenStaffPosition.  # noqa: E501

        Reflects the type of employment or contract desired for the position.  # noqa: E501

        :return: The employment_status_descriptor of this EdFiOpenStaffPosition.  # noqa: E501
        :rtype: str
        """
        return self._employment_status_descriptor

    @employment_status_descriptor.setter
    def employment_status_descriptor(self, employment_status_descriptor):
        """Sets the employment_status_descriptor of this EdFiOpenStaffPosition.

        Reflects the type of employment or contract desired for the position.  # noqa: E501

        :param employment_status_descriptor: The employment_status_descriptor of this EdFiOpenStaffPosition.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and employment_status_descriptor is None:
            raise ValueError("Invalid value for `employment_status_descriptor`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                employment_status_descriptor is not None and len(employment_status_descriptor) > 306):
            raise ValueError("Invalid value for `employment_status_descriptor`, length must be less than or equal to `306`")  # noqa: E501

        self._employment_status_descriptor = employment_status_descriptor

    @property
    def instructional_grade_levels(self):
        """Gets the instructional_grade_levels of this EdFiOpenStaffPosition.  # noqa: E501

        An unordered collection of openStaffPositionInstructionalGradeLevels. The set of grade levels for which the position's assignment is responsible.  # noqa: E501

        :return: The instructional_grade_levels of this EdFiOpenStaffPosition.  # noqa: E501
        :rtype: list[EdFiOpenStaffPositionInstructionalGradeLevel]
        """
        return self._instructional_grade_levels

    @instructional_grade_levels.setter
    def instructional_grade_levels(self, instructional_grade_levels):
        """Sets the instructional_grade_levels of this EdFiOpenStaffPosition.

        An unordered collection of openStaffPositionInstructionalGradeLevels. The set of grade levels for which the position's assignment is responsible.  # noqa: E501

        :param instructional_grade_levels: The instructional_grade_levels of this EdFiOpenStaffPosition.  # noqa: E501
        :type: list[EdFiOpenStaffPositionInstructionalGradeLevel]
        """

        self._instructional_grade_levels = instructional_grade_levels

    @property
    def position_title(self):
        """Gets the position_title of this EdFiOpenStaffPosition.  # noqa: E501

        The descriptive name of an individual's position.  # noqa: E501

        :return: The position_title of this EdFiOpenStaffPosition.  # noqa: E501
        :rtype: str
        """
        return self._position_title

    @position_title.setter
    def position_title(self, position_title):
        """Sets the position_title of this EdFiOpenStaffPosition.

        The descriptive name of an individual's position.  # noqa: E501

        :param position_title: The position_title of this EdFiOpenStaffPosition.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                position_title is not None and len(position_title) > 100):
            raise ValueError("Invalid value for `position_title`, length must be less than or equal to `100`")  # noqa: E501

        self._position_title = position_title

    @property
    def posting_result_descriptor(self):
        """Gets the posting_result_descriptor of this EdFiOpenStaffPosition.  # noqa: E501

        Indication of whether the OpenStaffPosition was filled or retired without filling.  # noqa: E501

        :return: The posting_result_descriptor of this EdFiOpenStaffPosition.  # noqa: E501
        :rtype: str
        """
        return self._posting_result_descriptor

    @posting_result_descriptor.setter
    def posting_result_descriptor(self, posting_result_descriptor):
        """Sets the posting_result_descriptor of this EdFiOpenStaffPosition.

        Indication of whether the OpenStaffPosition was filled or retired without filling.  # noqa: E501

        :param posting_result_descriptor: The posting_result_descriptor of this EdFiOpenStaffPosition.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                posting_result_descriptor is not None and len(posting_result_descriptor) > 306):
            raise ValueError("Invalid value for `posting_result_descriptor`, length must be less than or equal to `306`")  # noqa: E501

        self._posting_result_descriptor = posting_result_descriptor

    @property
    def program_assignment_descriptor(self):
        """Gets the program_assignment_descriptor of this EdFiOpenStaffPosition.  # noqa: E501

        The name of the program for which the open staff position will be assigned.  # noqa: E501

        :return: The program_assignment_descriptor of this EdFiOpenStaffPosition.  # noqa: E501
        :rtype: str
        """
        return self._program_assignment_descriptor

    @program_assignment_descriptor.setter
    def program_assignment_descriptor(self, program_assignment_descriptor):
        """Sets the program_assignment_descriptor of this EdFiOpenStaffPosition.

        The name of the program for which the open staff position will be assigned.  # noqa: E501

        :param program_assignment_descriptor: The program_assignment_descriptor of this EdFiOpenStaffPosition.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                program_assignment_descriptor is not None and len(program_assignment_descriptor) > 306):
            raise ValueError("Invalid value for `program_assignment_descriptor`, length must be less than or equal to `306`")  # noqa: E501

        self._program_assignment_descriptor = program_assignment_descriptor

    @property
    def staff_classification_descriptor(self):
        """Gets the staff_classification_descriptor of this EdFiOpenStaffPosition.  # noqa: E501

        The titles of employment, official status, or rank of education staff.  # noqa: E501

        :return: The staff_classification_descriptor of this EdFiOpenStaffPosition.  # noqa: E501
        :rtype: str
        """
        return self._staff_classification_descriptor

    @staff_classification_descriptor.setter
    def staff_classification_descriptor(self, staff_classification_descriptor):
        """Sets the staff_classification_descriptor of this EdFiOpenStaffPosition.

        The titles of employment, official status, or rank of education staff.  # noqa: E501

        :param staff_classification_descriptor: The staff_classification_descriptor of this EdFiOpenStaffPosition.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and staff_classification_descriptor is None:
            raise ValueError("Invalid value for `staff_classification_descriptor`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                staff_classification_descriptor is not None and len(staff_classification_descriptor) > 306):
            raise ValueError("Invalid value for `staff_classification_descriptor`, length must be less than or equal to `306`")  # noqa: E501

        self._staff_classification_descriptor = staff_classification_descriptor

    @property
    def etag(self):
        """Gets the etag of this EdFiOpenStaffPosition.  # noqa: E501

        A unique system-generated value that identifies the version of the resource.  # noqa: E501

        :return: The etag of this EdFiOpenStaffPosition.  # noqa: E501
        :rtype: str
        """
        return self._etag

    @etag.setter
    def etag(self, etag):
        """Sets the etag of this EdFiOpenStaffPosition.

        A unique system-generated value that identifies the version of the resource.  # noqa: E501

        :param etag: The etag of this EdFiOpenStaffPosition.  # noqa: E501
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
        if issubclass(EdFiOpenStaffPosition, dict):
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
        if not isinstance(other, EdFiOpenStaffPosition):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EdFiOpenStaffPosition):
            return True

        return self.to_dict() != other.to_dict()