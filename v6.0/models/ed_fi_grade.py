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


class EdFiGrade(object):
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
        'grade_type_descriptor': 'str',
        'grading_period_reference': 'EdFiGradingPeriodReference',
        'student_section_association_reference': 'EdFiStudentSectionAssociationReference',
        'current_grade_as_of_date': 'date',
        'current_grade_indicator': 'bool',
        'diagnostic_statement': 'str',
        'learning_standard_grades': 'list[EdFiGradeLearningStandardGrade]',
        'letter_grade_earned': 'str',
        'numeric_grade_earned': 'float',
        'performance_base_conversion_descriptor': 'str',
        'etag': 'str'
    }

    attribute_map = {
        'id': 'id',
        'grade_type_descriptor': 'gradeTypeDescriptor',
        'grading_period_reference': 'gradingPeriodReference',
        'student_section_association_reference': 'studentSectionAssociationReference',
        'current_grade_as_of_date': 'currentGradeAsOfDate',
        'current_grade_indicator': 'currentGradeIndicator',
        'diagnostic_statement': 'diagnosticStatement',
        'learning_standard_grades': 'learningStandardGrades',
        'letter_grade_earned': 'letterGradeEarned',
        'numeric_grade_earned': 'numericGradeEarned',
        'performance_base_conversion_descriptor': 'performanceBaseConversionDescriptor',
        'etag': '_etag'
    }

    def __init__(self, id=None, grade_type_descriptor=None, grading_period_reference=None, student_section_association_reference=None, current_grade_as_of_date=None, current_grade_indicator=None, diagnostic_statement=None, learning_standard_grades=None, letter_grade_earned=None, numeric_grade_earned=None, performance_base_conversion_descriptor=None, etag=None, _configuration=None):  # noqa: E501
        """EdFiGrade - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._grade_type_descriptor = None
        self._grading_period_reference = None
        self._student_section_association_reference = None
        self._current_grade_as_of_date = None
        self._current_grade_indicator = None
        self._diagnostic_statement = None
        self._learning_standard_grades = None
        self._letter_grade_earned = None
        self._numeric_grade_earned = None
        self._performance_base_conversion_descriptor = None
        self._etag = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.grade_type_descriptor = grade_type_descriptor
        self.grading_period_reference = grading_period_reference
        self.student_section_association_reference = student_section_association_reference
        if current_grade_as_of_date is not None:
            self.current_grade_as_of_date = current_grade_as_of_date
        if current_grade_indicator is not None:
            self.current_grade_indicator = current_grade_indicator
        if diagnostic_statement is not None:
            self.diagnostic_statement = diagnostic_statement
        if learning_standard_grades is not None:
            self.learning_standard_grades = learning_standard_grades
        if letter_grade_earned is not None:
            self.letter_grade_earned = letter_grade_earned
        if numeric_grade_earned is not None:
            self.numeric_grade_earned = numeric_grade_earned
        if performance_base_conversion_descriptor is not None:
            self.performance_base_conversion_descriptor = performance_base_conversion_descriptor
        if etag is not None:
            self.etag = etag

    @property
    def id(self):
        """Gets the id of this EdFiGrade.  # noqa: E501

          # noqa: E501

        :return: The id of this EdFiGrade.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this EdFiGrade.

          # noqa: E501

        :param id: The id of this EdFiGrade.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def grade_type_descriptor(self):
        """Gets the grade_type_descriptor of this EdFiGrade.  # noqa: E501

        The type of grade reported (e.g., exam, final, grading period).  # noqa: E501

        :return: The grade_type_descriptor of this EdFiGrade.  # noqa: E501
        :rtype: str
        """
        return self._grade_type_descriptor

    @grade_type_descriptor.setter
    def grade_type_descriptor(self, grade_type_descriptor):
        """Sets the grade_type_descriptor of this EdFiGrade.

        The type of grade reported (e.g., exam, final, grading period).  # noqa: E501

        :param grade_type_descriptor: The grade_type_descriptor of this EdFiGrade.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and grade_type_descriptor is None:
            raise ValueError("Invalid value for `grade_type_descriptor`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                grade_type_descriptor is not None and len(grade_type_descriptor) > 306):
            raise ValueError("Invalid value for `grade_type_descriptor`, length must be less than or equal to `306`")  # noqa: E501

        self._grade_type_descriptor = grade_type_descriptor

    @property
    def grading_period_reference(self):
        """Gets the grading_period_reference of this EdFiGrade.  # noqa: E501


        :return: The grading_period_reference of this EdFiGrade.  # noqa: E501
        :rtype: EdFiGradingPeriodReference
        """
        return self._grading_period_reference

    @grading_period_reference.setter
    def grading_period_reference(self, grading_period_reference):
        """Sets the grading_period_reference of this EdFiGrade.


        :param grading_period_reference: The grading_period_reference of this EdFiGrade.  # noqa: E501
        :type: EdFiGradingPeriodReference
        """
        if self._configuration.client_side_validation and grading_period_reference is None:
            raise ValueError("Invalid value for `grading_period_reference`, must not be `None`")  # noqa: E501

        self._grading_period_reference = grading_period_reference

    @property
    def student_section_association_reference(self):
        """Gets the student_section_association_reference of this EdFiGrade.  # noqa: E501


        :return: The student_section_association_reference of this EdFiGrade.  # noqa: E501
        :rtype: EdFiStudentSectionAssociationReference
        """
        return self._student_section_association_reference

    @student_section_association_reference.setter
    def student_section_association_reference(self, student_section_association_reference):
        """Sets the student_section_association_reference of this EdFiGrade.


        :param student_section_association_reference: The student_section_association_reference of this EdFiGrade.  # noqa: E501
        :type: EdFiStudentSectionAssociationReference
        """
        if self._configuration.client_side_validation and student_section_association_reference is None:
            raise ValueError("Invalid value for `student_section_association_reference`, must not be `None`")  # noqa: E501

        self._student_section_association_reference = student_section_association_reference

    @property
    def current_grade_as_of_date(self):
        """Gets the current_grade_as_of_date of this EdFiGrade.  # noqa: E501

        As-Of date for a grade posted as the current grade.  # noqa: E501

        :return: The current_grade_as_of_date of this EdFiGrade.  # noqa: E501
        :rtype: date
        """
        return self._current_grade_as_of_date

    @current_grade_as_of_date.setter
    def current_grade_as_of_date(self, current_grade_as_of_date):
        """Sets the current_grade_as_of_date of this EdFiGrade.

        As-Of date for a grade posted as the current grade.  # noqa: E501

        :param current_grade_as_of_date: The current_grade_as_of_date of this EdFiGrade.  # noqa: E501
        :type: date
        """

        self._current_grade_as_of_date = current_grade_as_of_date

    @property
    def current_grade_indicator(self):
        """Gets the current_grade_indicator of this EdFiGrade.  # noqa: E501

        An indicator that the posted grade is an interim grade for the grading period and not the final grade.  # noqa: E501

        :return: The current_grade_indicator of this EdFiGrade.  # noqa: E501
        :rtype: bool
        """
        return self._current_grade_indicator

    @current_grade_indicator.setter
    def current_grade_indicator(self, current_grade_indicator):
        """Sets the current_grade_indicator of this EdFiGrade.

        An indicator that the posted grade is an interim grade for the grading period and not the final grade.  # noqa: E501

        :param current_grade_indicator: The current_grade_indicator of this EdFiGrade.  # noqa: E501
        :type: bool
        """

        self._current_grade_indicator = current_grade_indicator

    @property
    def diagnostic_statement(self):
        """Gets the diagnostic_statement of this EdFiGrade.  # noqa: E501

        A statement provided by the teacher that provides information in addition to the grade or assessment score.  # noqa: E501

        :return: The diagnostic_statement of this EdFiGrade.  # noqa: E501
        :rtype: str
        """
        return self._diagnostic_statement

    @diagnostic_statement.setter
    def diagnostic_statement(self, diagnostic_statement):
        """Sets the diagnostic_statement of this EdFiGrade.

        A statement provided by the teacher that provides information in addition to the grade or assessment score.  # noqa: E501

        :param diagnostic_statement: The diagnostic_statement of this EdFiGrade.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                diagnostic_statement is not None and len(diagnostic_statement) > 1024):
            raise ValueError("Invalid value for `diagnostic_statement`, length must be less than or equal to `1024`")  # noqa: E501

        self._diagnostic_statement = diagnostic_statement

    @property
    def learning_standard_grades(self):
        """Gets the learning_standard_grades of this EdFiGrade.  # noqa: E501

        An unordered collection of gradeLearningStandardGrades. A collection of learning standards associated with the grade.  # noqa: E501

        :return: The learning_standard_grades of this EdFiGrade.  # noqa: E501
        :rtype: list[EdFiGradeLearningStandardGrade]
        """
        return self._learning_standard_grades

    @learning_standard_grades.setter
    def learning_standard_grades(self, learning_standard_grades):
        """Sets the learning_standard_grades of this EdFiGrade.

        An unordered collection of gradeLearningStandardGrades. A collection of learning standards associated with the grade.  # noqa: E501

        :param learning_standard_grades: The learning_standard_grades of this EdFiGrade.  # noqa: E501
        :type: list[EdFiGradeLearningStandardGrade]
        """

        self._learning_standard_grades = learning_standard_grades

    @property
    def letter_grade_earned(self):
        """Gets the letter_grade_earned of this EdFiGrade.  # noqa: E501

        A final or interim (grading period) indicator of student performance in a class as submitted by the instructor.  # noqa: E501

        :return: The letter_grade_earned of this EdFiGrade.  # noqa: E501
        :rtype: str
        """
        return self._letter_grade_earned

    @letter_grade_earned.setter
    def letter_grade_earned(self, letter_grade_earned):
        """Sets the letter_grade_earned of this EdFiGrade.

        A final or interim (grading period) indicator of student performance in a class as submitted by the instructor.  # noqa: E501

        :param letter_grade_earned: The letter_grade_earned of this EdFiGrade.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                letter_grade_earned is not None and len(letter_grade_earned) > 20):
            raise ValueError("Invalid value for `letter_grade_earned`, length must be less than or equal to `20`")  # noqa: E501

        self._letter_grade_earned = letter_grade_earned

    @property
    def numeric_grade_earned(self):
        """Gets the numeric_grade_earned of this EdFiGrade.  # noqa: E501

        A final or interim (grading period) indicator of student performance in a class as submitted by the instructor.  # noqa: E501

        :return: The numeric_grade_earned of this EdFiGrade.  # noqa: E501
        :rtype: float
        """
        return self._numeric_grade_earned

    @numeric_grade_earned.setter
    def numeric_grade_earned(self, numeric_grade_earned):
        """Sets the numeric_grade_earned of this EdFiGrade.

        A final or interim (grading period) indicator of student performance in a class as submitted by the instructor.  # noqa: E501

        :param numeric_grade_earned: The numeric_grade_earned of this EdFiGrade.  # noqa: E501
        :type: float
        """

        self._numeric_grade_earned = numeric_grade_earned

    @property
    def performance_base_conversion_descriptor(self):
        """Gets the performance_base_conversion_descriptor of this EdFiGrade.  # noqa: E501

        A conversion of the level to a standard set of performance levels.  # noqa: E501

        :return: The performance_base_conversion_descriptor of this EdFiGrade.  # noqa: E501
        :rtype: str
        """
        return self._performance_base_conversion_descriptor

    @performance_base_conversion_descriptor.setter
    def performance_base_conversion_descriptor(self, performance_base_conversion_descriptor):
        """Sets the performance_base_conversion_descriptor of this EdFiGrade.

        A conversion of the level to a standard set of performance levels.  # noqa: E501

        :param performance_base_conversion_descriptor: The performance_base_conversion_descriptor of this EdFiGrade.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                performance_base_conversion_descriptor is not None and len(performance_base_conversion_descriptor) > 306):
            raise ValueError("Invalid value for `performance_base_conversion_descriptor`, length must be less than or equal to `306`")  # noqa: E501

        self._performance_base_conversion_descriptor = performance_base_conversion_descriptor

    @property
    def etag(self):
        """Gets the etag of this EdFiGrade.  # noqa: E501

        A unique system-generated value that identifies the version of the resource.  # noqa: E501

        :return: The etag of this EdFiGrade.  # noqa: E501
        :rtype: str
        """
        return self._etag

    @etag.setter
    def etag(self, etag):
        """Sets the etag of this EdFiGrade.

        A unique system-generated value that identifies the version of the resource.  # noqa: E501

        :param etag: The etag of this EdFiGrade.  # noqa: E501
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
        if issubclass(EdFiGrade, dict):
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
        if not isinstance(other, EdFiGrade):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EdFiGrade):
            return True

        return self.to_dict() != other.to_dict()
