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


class TrackedChangesEdFiGradeKey(object):
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
        'grade_type_descriptor': 'str',
        'grading_period_descriptor': 'str',
        'grading_period_sequence': 'int',
        'school_id': 'int',
        'grading_period_school_year': 'int',
        'begin_date': 'date',
        'local_course_code': 'str',
        'school_year': 'int',
        'section_identifier': 'str',
        'session_name': 'str',
        'student_unique_id': 'str'
    }

    attribute_map = {
        'grade_type_descriptor': 'gradeTypeDescriptor',
        'grading_period_descriptor': 'gradingPeriodDescriptor',
        'grading_period_sequence': 'gradingPeriodSequence',
        'school_id': 'schoolId',
        'grading_period_school_year': 'gradingPeriodSchoolYear',
        'begin_date': 'beginDate',
        'local_course_code': 'localCourseCode',
        'school_year': 'schoolYear',
        'section_identifier': 'sectionIdentifier',
        'session_name': 'sessionName',
        'student_unique_id': 'studentUniqueId'
    }

    def __init__(self, grade_type_descriptor=None, grading_period_descriptor=None, grading_period_sequence=None, school_id=None, grading_period_school_year=None, begin_date=None, local_course_code=None, school_year=None, section_identifier=None, session_name=None, student_unique_id=None, _configuration=None):  # noqa: E501
        """TrackedChangesEdFiGradeKey - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._grade_type_descriptor = None
        self._grading_period_descriptor = None
        self._grading_period_sequence = None
        self._school_id = None
        self._grading_period_school_year = None
        self._begin_date = None
        self._local_course_code = None
        self._school_year = None
        self._section_identifier = None
        self._session_name = None
        self._student_unique_id = None
        self.discriminator = None

        if grade_type_descriptor is not None:
            self.grade_type_descriptor = grade_type_descriptor
        if grading_period_descriptor is not None:
            self.grading_period_descriptor = grading_period_descriptor
        if grading_period_sequence is not None:
            self.grading_period_sequence = grading_period_sequence
        if school_id is not None:
            self.school_id = school_id
        if grading_period_school_year is not None:
            self.grading_period_school_year = grading_period_school_year
        if begin_date is not None:
            self.begin_date = begin_date
        if local_course_code is not None:
            self.local_course_code = local_course_code
        if school_year is not None:
            self.school_year = school_year
        if section_identifier is not None:
            self.section_identifier = section_identifier
        if session_name is not None:
            self.session_name = session_name
        if student_unique_id is not None:
            self.student_unique_id = student_unique_id

    @property
    def grade_type_descriptor(self):
        """Gets the grade_type_descriptor of this TrackedChangesEdFiGradeKey.  # noqa: E501

        The type of grade reported (e.g., exam, final, grading period).  # noqa: E501

        :return: The grade_type_descriptor of this TrackedChangesEdFiGradeKey.  # noqa: E501
        :rtype: str
        """
        return self._grade_type_descriptor

    @grade_type_descriptor.setter
    def grade_type_descriptor(self, grade_type_descriptor):
        """Sets the grade_type_descriptor of this TrackedChangesEdFiGradeKey.

        The type of grade reported (e.g., exam, final, grading period).  # noqa: E501

        :param grade_type_descriptor: The grade_type_descriptor of this TrackedChangesEdFiGradeKey.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                grade_type_descriptor is not None and len(grade_type_descriptor) > 306):
            raise ValueError("Invalid value for `grade_type_descriptor`, length must be less than or equal to `306`")  # noqa: E501

        self._grade_type_descriptor = grade_type_descriptor

    @property
    def grading_period_descriptor(self):
        """Gets the grading_period_descriptor of this TrackedChangesEdFiGradeKey.  # noqa: E501

        The name of the period for which grades are reported.  # noqa: E501

        :return: The grading_period_descriptor of this TrackedChangesEdFiGradeKey.  # noqa: E501
        :rtype: str
        """
        return self._grading_period_descriptor

    @grading_period_descriptor.setter
    def grading_period_descriptor(self, grading_period_descriptor):
        """Sets the grading_period_descriptor of this TrackedChangesEdFiGradeKey.

        The name of the period for which grades are reported.  # noqa: E501

        :param grading_period_descriptor: The grading_period_descriptor of this TrackedChangesEdFiGradeKey.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                grading_period_descriptor is not None and len(grading_period_descriptor) > 306):
            raise ValueError("Invalid value for `grading_period_descriptor`, length must be less than or equal to `306`")  # noqa: E501

        self._grading_period_descriptor = grading_period_descriptor

    @property
    def grading_period_sequence(self):
        """Gets the grading_period_sequence of this TrackedChangesEdFiGradeKey.  # noqa: E501

        The sequential order of this period relative to other periods.  # noqa: E501

        :return: The grading_period_sequence of this TrackedChangesEdFiGradeKey.  # noqa: E501
        :rtype: int
        """
        return self._grading_period_sequence

    @grading_period_sequence.setter
    def grading_period_sequence(self, grading_period_sequence):
        """Sets the grading_period_sequence of this TrackedChangesEdFiGradeKey.

        The sequential order of this period relative to other periods.  # noqa: E501

        :param grading_period_sequence: The grading_period_sequence of this TrackedChangesEdFiGradeKey.  # noqa: E501
        :type: int
        """

        self._grading_period_sequence = grading_period_sequence

    @property
    def school_id(self):
        """Gets the school_id of this TrackedChangesEdFiGradeKey.  # noqa: E501

        The identifier assigned to a school.  # noqa: E501

        :return: The school_id of this TrackedChangesEdFiGradeKey.  # noqa: E501
        :rtype: int
        """
        return self._school_id

    @school_id.setter
    def school_id(self, school_id):
        """Sets the school_id of this TrackedChangesEdFiGradeKey.

        The identifier assigned to a school.  # noqa: E501

        :param school_id: The school_id of this TrackedChangesEdFiGradeKey.  # noqa: E501
        :type: int
        """

        self._school_id = school_id

    @property
    def grading_period_school_year(self):
        """Gets the grading_period_school_year of this TrackedChangesEdFiGradeKey.  # noqa: E501

        The identifier for the grading period school year.  # noqa: E501

        :return: The grading_period_school_year of this TrackedChangesEdFiGradeKey.  # noqa: E501
        :rtype: int
        """
        return self._grading_period_school_year

    @grading_period_school_year.setter
    def grading_period_school_year(self, grading_period_school_year):
        """Sets the grading_period_school_year of this TrackedChangesEdFiGradeKey.

        The identifier for the grading period school year.  # noqa: E501

        :param grading_period_school_year: The grading_period_school_year of this TrackedChangesEdFiGradeKey.  # noqa: E501
        :type: int
        """

        self._grading_period_school_year = grading_period_school_year

    @property
    def begin_date(self):
        """Gets the begin_date of this TrackedChangesEdFiGradeKey.  # noqa: E501

        Month, day, and year of the student's entry or assignment to the section.  # noqa: E501

        :return: The begin_date of this TrackedChangesEdFiGradeKey.  # noqa: E501
        :rtype: date
        """
        return self._begin_date

    @begin_date.setter
    def begin_date(self, begin_date):
        """Sets the begin_date of this TrackedChangesEdFiGradeKey.

        Month, day, and year of the student's entry or assignment to the section.  # noqa: E501

        :param begin_date: The begin_date of this TrackedChangesEdFiGradeKey.  # noqa: E501
        :type: date
        """

        self._begin_date = begin_date

    @property
    def local_course_code(self):
        """Gets the local_course_code of this TrackedChangesEdFiGradeKey.  # noqa: E501

        The local code assigned by the School that identifies the course offering provided for the instruction of students.  # noqa: E501

        :return: The local_course_code of this TrackedChangesEdFiGradeKey.  # noqa: E501
        :rtype: str
        """
        return self._local_course_code

    @local_course_code.setter
    def local_course_code(self, local_course_code):
        """Sets the local_course_code of this TrackedChangesEdFiGradeKey.

        The local code assigned by the School that identifies the course offering provided for the instruction of students.  # noqa: E501

        :param local_course_code: The local_course_code of this TrackedChangesEdFiGradeKey.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                local_course_code is not None and len(local_course_code) > 60):
            raise ValueError("Invalid value for `local_course_code`, length must be less than or equal to `60`")  # noqa: E501

        self._local_course_code = local_course_code

    @property
    def school_year(self):
        """Gets the school_year of this TrackedChangesEdFiGradeKey.  # noqa: E501

        The identifier for the school year.  # noqa: E501

        :return: The school_year of this TrackedChangesEdFiGradeKey.  # noqa: E501
        :rtype: int
        """
        return self._school_year

    @school_year.setter
    def school_year(self, school_year):
        """Sets the school_year of this TrackedChangesEdFiGradeKey.

        The identifier for the school year.  # noqa: E501

        :param school_year: The school_year of this TrackedChangesEdFiGradeKey.  # noqa: E501
        :type: int
        """

        self._school_year = school_year

    @property
    def section_identifier(self):
        """Gets the section_identifier of this TrackedChangesEdFiGradeKey.  # noqa: E501

        The local identifier assigned to a section.  # noqa: E501

        :return: The section_identifier of this TrackedChangesEdFiGradeKey.  # noqa: E501
        :rtype: str
        """
        return self._section_identifier

    @section_identifier.setter
    def section_identifier(self, section_identifier):
        """Sets the section_identifier of this TrackedChangesEdFiGradeKey.

        The local identifier assigned to a section.  # noqa: E501

        :param section_identifier: The section_identifier of this TrackedChangesEdFiGradeKey.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                section_identifier is not None and len(section_identifier) > 255):
            raise ValueError("Invalid value for `section_identifier`, length must be less than or equal to `255`")  # noqa: E501

        self._section_identifier = section_identifier

    @property
    def session_name(self):
        """Gets the session_name of this TrackedChangesEdFiGradeKey.  # noqa: E501

        The identifier for the calendar for the academic session.  # noqa: E501

        :return: The session_name of this TrackedChangesEdFiGradeKey.  # noqa: E501
        :rtype: str
        """
        return self._session_name

    @session_name.setter
    def session_name(self, session_name):
        """Sets the session_name of this TrackedChangesEdFiGradeKey.

        The identifier for the calendar for the academic session.  # noqa: E501

        :param session_name: The session_name of this TrackedChangesEdFiGradeKey.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                session_name is not None and len(session_name) > 60):
            raise ValueError("Invalid value for `session_name`, length must be less than or equal to `60`")  # noqa: E501

        self._session_name = session_name

    @property
    def student_unique_id(self):
        """Gets the student_unique_id of this TrackedChangesEdFiGradeKey.  # noqa: E501

        A unique alphanumeric code assigned to a student.  # noqa: E501

        :return: The student_unique_id of this TrackedChangesEdFiGradeKey.  # noqa: E501
        :rtype: str
        """
        return self._student_unique_id

    @student_unique_id.setter
    def student_unique_id(self, student_unique_id):
        """Sets the student_unique_id of this TrackedChangesEdFiGradeKey.

        A unique alphanumeric code assigned to a student.  # noqa: E501

        :param student_unique_id: The student_unique_id of this TrackedChangesEdFiGradeKey.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                student_unique_id is not None and len(student_unique_id) > 32):
            raise ValueError("Invalid value for `student_unique_id`, length must be less than or equal to `32`")  # noqa: E501

        self._student_unique_id = student_unique_id

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
        if issubclass(TrackedChangesEdFiGradeKey, dict):
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
        if not isinstance(other, TrackedChangesEdFiGradeKey):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TrackedChangesEdFiGradeKey):
            return True

        return self.to_dict() != other.to_dict()