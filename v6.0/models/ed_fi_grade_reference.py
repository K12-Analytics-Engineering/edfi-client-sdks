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


class EdFiGradeReference(object):
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
        'grade_type_descriptor': 'str',
        'grading_period_descriptor': 'str',
        'grading_period_school_year': 'int',
        'grading_period_sequence': 'int',
        'local_course_code': 'str',
        'school_id': 'int',
        'school_year': 'int',
        'section_identifier': 'str',
        'session_name': 'str',
        'student_unique_id': 'str',
        'link': 'Link'
    }

    attribute_map = {
        'begin_date': 'beginDate',
        'grade_type_descriptor': 'gradeTypeDescriptor',
        'grading_period_descriptor': 'gradingPeriodDescriptor',
        'grading_period_school_year': 'gradingPeriodSchoolYear',
        'grading_period_sequence': 'gradingPeriodSequence',
        'local_course_code': 'localCourseCode',
        'school_id': 'schoolId',
        'school_year': 'schoolYear',
        'section_identifier': 'sectionIdentifier',
        'session_name': 'sessionName',
        'student_unique_id': 'studentUniqueId',
        'link': 'link'
    }

    def __init__(self, begin_date=None, grade_type_descriptor=None, grading_period_descriptor=None, grading_period_school_year=None, grading_period_sequence=None, local_course_code=None, school_id=None, school_year=None, section_identifier=None, session_name=None, student_unique_id=None, link=None, _configuration=None):  # noqa: E501
        """EdFiGradeReference - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._begin_date = None
        self._grade_type_descriptor = None
        self._grading_period_descriptor = None
        self._grading_period_school_year = None
        self._grading_period_sequence = None
        self._local_course_code = None
        self._school_id = None
        self._school_year = None
        self._section_identifier = None
        self._session_name = None
        self._student_unique_id = None
        self._link = None
        self.discriminator = None

        self.begin_date = begin_date
        self.grade_type_descriptor = grade_type_descriptor
        self.grading_period_descriptor = grading_period_descriptor
        self.grading_period_school_year = grading_period_school_year
        self.grading_period_sequence = grading_period_sequence
        self.local_course_code = local_course_code
        self.school_id = school_id
        self.school_year = school_year
        self.section_identifier = section_identifier
        self.session_name = session_name
        self.student_unique_id = student_unique_id
        if link is not None:
            self.link = link

    @property
    def begin_date(self):
        """Gets the begin_date of this EdFiGradeReference.  # noqa: E501

        Month, day, and year of the student's entry or assignment to the section.  # noqa: E501

        :return: The begin_date of this EdFiGradeReference.  # noqa: E501
        :rtype: date
        """
        return self._begin_date

    @begin_date.setter
    def begin_date(self, begin_date):
        """Sets the begin_date of this EdFiGradeReference.

        Month, day, and year of the student's entry or assignment to the section.  # noqa: E501

        :param begin_date: The begin_date of this EdFiGradeReference.  # noqa: E501
        :type: date
        """
        if self._configuration.client_side_validation and begin_date is None:
            raise ValueError("Invalid value for `begin_date`, must not be `None`")  # noqa: E501

        self._begin_date = begin_date

    @property
    def grade_type_descriptor(self):
        """Gets the grade_type_descriptor of this EdFiGradeReference.  # noqa: E501

        The type of grade reported (e.g., exam, final, grading period).  # noqa: E501

        :return: The grade_type_descriptor of this EdFiGradeReference.  # noqa: E501
        :rtype: str
        """
        return self._grade_type_descriptor

    @grade_type_descriptor.setter
    def grade_type_descriptor(self, grade_type_descriptor):
        """Sets the grade_type_descriptor of this EdFiGradeReference.

        The type of grade reported (e.g., exam, final, grading period).  # noqa: E501

        :param grade_type_descriptor: The grade_type_descriptor of this EdFiGradeReference.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and grade_type_descriptor is None:
            raise ValueError("Invalid value for `grade_type_descriptor`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                grade_type_descriptor is not None and len(grade_type_descriptor) > 306):
            raise ValueError("Invalid value for `grade_type_descriptor`, length must be less than or equal to `306`")  # noqa: E501

        self._grade_type_descriptor = grade_type_descriptor

    @property
    def grading_period_descriptor(self):
        """Gets the grading_period_descriptor of this EdFiGradeReference.  # noqa: E501

        The name of the period for which grades are reported.  # noqa: E501

        :return: The grading_period_descriptor of this EdFiGradeReference.  # noqa: E501
        :rtype: str
        """
        return self._grading_period_descriptor

    @grading_period_descriptor.setter
    def grading_period_descriptor(self, grading_period_descriptor):
        """Sets the grading_period_descriptor of this EdFiGradeReference.

        The name of the period for which grades are reported.  # noqa: E501

        :param grading_period_descriptor: The grading_period_descriptor of this EdFiGradeReference.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and grading_period_descriptor is None:
            raise ValueError("Invalid value for `grading_period_descriptor`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                grading_period_descriptor is not None and len(grading_period_descriptor) > 306):
            raise ValueError("Invalid value for `grading_period_descriptor`, length must be less than or equal to `306`")  # noqa: E501

        self._grading_period_descriptor = grading_period_descriptor

    @property
    def grading_period_school_year(self):
        """Gets the grading_period_school_year of this EdFiGradeReference.  # noqa: E501

        The identifier for the grading period school year.  # noqa: E501

        :return: The grading_period_school_year of this EdFiGradeReference.  # noqa: E501
        :rtype: int
        """
        return self._grading_period_school_year

    @grading_period_school_year.setter
    def grading_period_school_year(self, grading_period_school_year):
        """Sets the grading_period_school_year of this EdFiGradeReference.

        The identifier for the grading period school year.  # noqa: E501

        :param grading_period_school_year: The grading_period_school_year of this EdFiGradeReference.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and grading_period_school_year is None:
            raise ValueError("Invalid value for `grading_period_school_year`, must not be `None`")  # noqa: E501

        self._grading_period_school_year = grading_period_school_year

    @property
    def grading_period_sequence(self):
        """Gets the grading_period_sequence of this EdFiGradeReference.  # noqa: E501

        The sequential order of this period relative to other periods.  # noqa: E501

        :return: The grading_period_sequence of this EdFiGradeReference.  # noqa: E501
        :rtype: int
        """
        return self._grading_period_sequence

    @grading_period_sequence.setter
    def grading_period_sequence(self, grading_period_sequence):
        """Sets the grading_period_sequence of this EdFiGradeReference.

        The sequential order of this period relative to other periods.  # noqa: E501

        :param grading_period_sequence: The grading_period_sequence of this EdFiGradeReference.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and grading_period_sequence is None:
            raise ValueError("Invalid value for `grading_period_sequence`, must not be `None`")  # noqa: E501

        self._grading_period_sequence = grading_period_sequence

    @property
    def local_course_code(self):
        """Gets the local_course_code of this EdFiGradeReference.  # noqa: E501

        The local code assigned by the School that identifies the course offering provided for the instruction of students.  # noqa: E501

        :return: The local_course_code of this EdFiGradeReference.  # noqa: E501
        :rtype: str
        """
        return self._local_course_code

    @local_course_code.setter
    def local_course_code(self, local_course_code):
        """Sets the local_course_code of this EdFiGradeReference.

        The local code assigned by the School that identifies the course offering provided for the instruction of students.  # noqa: E501

        :param local_course_code: The local_course_code of this EdFiGradeReference.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and local_course_code is None:
            raise ValueError("Invalid value for `local_course_code`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                local_course_code is not None and len(local_course_code) > 60):
            raise ValueError("Invalid value for `local_course_code`, length must be less than or equal to `60`")  # noqa: E501

        self._local_course_code = local_course_code

    @property
    def school_id(self):
        """Gets the school_id of this EdFiGradeReference.  # noqa: E501

        The identifier assigned to a school.  # noqa: E501

        :return: The school_id of this EdFiGradeReference.  # noqa: E501
        :rtype: int
        """
        return self._school_id

    @school_id.setter
    def school_id(self, school_id):
        """Sets the school_id of this EdFiGradeReference.

        The identifier assigned to a school.  # noqa: E501

        :param school_id: The school_id of this EdFiGradeReference.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and school_id is None:
            raise ValueError("Invalid value for `school_id`, must not be `None`")  # noqa: E501

        self._school_id = school_id

    @property
    def school_year(self):
        """Gets the school_year of this EdFiGradeReference.  # noqa: E501

        The identifier for the school year.  # noqa: E501

        :return: The school_year of this EdFiGradeReference.  # noqa: E501
        :rtype: int
        """
        return self._school_year

    @school_year.setter
    def school_year(self, school_year):
        """Sets the school_year of this EdFiGradeReference.

        The identifier for the school year.  # noqa: E501

        :param school_year: The school_year of this EdFiGradeReference.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and school_year is None:
            raise ValueError("Invalid value for `school_year`, must not be `None`")  # noqa: E501

        self._school_year = school_year

    @property
    def section_identifier(self):
        """Gets the section_identifier of this EdFiGradeReference.  # noqa: E501

        The local identifier assigned to a section.  # noqa: E501

        :return: The section_identifier of this EdFiGradeReference.  # noqa: E501
        :rtype: str
        """
        return self._section_identifier

    @section_identifier.setter
    def section_identifier(self, section_identifier):
        """Sets the section_identifier of this EdFiGradeReference.

        The local identifier assigned to a section.  # noqa: E501

        :param section_identifier: The section_identifier of this EdFiGradeReference.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and section_identifier is None:
            raise ValueError("Invalid value for `section_identifier`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                section_identifier is not None and len(section_identifier) > 255):
            raise ValueError("Invalid value for `section_identifier`, length must be less than or equal to `255`")  # noqa: E501

        self._section_identifier = section_identifier

    @property
    def session_name(self):
        """Gets the session_name of this EdFiGradeReference.  # noqa: E501

        The identifier for the calendar for the academic session.  # noqa: E501

        :return: The session_name of this EdFiGradeReference.  # noqa: E501
        :rtype: str
        """
        return self._session_name

    @session_name.setter
    def session_name(self, session_name):
        """Sets the session_name of this EdFiGradeReference.

        The identifier for the calendar for the academic session.  # noqa: E501

        :param session_name: The session_name of this EdFiGradeReference.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and session_name is None:
            raise ValueError("Invalid value for `session_name`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                session_name is not None and len(session_name) > 60):
            raise ValueError("Invalid value for `session_name`, length must be less than or equal to `60`")  # noqa: E501

        self._session_name = session_name

    @property
    def student_unique_id(self):
        """Gets the student_unique_id of this EdFiGradeReference.  # noqa: E501

        A unique alphanumeric code assigned to a student.  # noqa: E501

        :return: The student_unique_id of this EdFiGradeReference.  # noqa: E501
        :rtype: str
        """
        return self._student_unique_id

    @student_unique_id.setter
    def student_unique_id(self, student_unique_id):
        """Sets the student_unique_id of this EdFiGradeReference.

        A unique alphanumeric code assigned to a student.  # noqa: E501

        :param student_unique_id: The student_unique_id of this EdFiGradeReference.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and student_unique_id is None:
            raise ValueError("Invalid value for `student_unique_id`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                student_unique_id is not None and len(student_unique_id) > 32):
            raise ValueError("Invalid value for `student_unique_id`, length must be less than or equal to `32`")  # noqa: E501

        self._student_unique_id = student_unique_id

    @property
    def link(self):
        """Gets the link of this EdFiGradeReference.  # noqa: E501


        :return: The link of this EdFiGradeReference.  # noqa: E501
        :rtype: Link
        """
        return self._link

    @link.setter
    def link(self, link):
        """Sets the link of this EdFiGradeReference.


        :param link: The link of this EdFiGradeReference.  # noqa: E501
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
        if issubclass(EdFiGradeReference, dict):
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
        if not isinstance(other, EdFiGradeReference):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EdFiGradeReference):
            return True

        return self.to_dict() != other.to_dict()