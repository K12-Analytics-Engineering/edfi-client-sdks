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


class EdFiSection(object):
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
        'section_identifier': 'str',
        'course_offering_reference': 'EdFiCourseOfferingReference',
        'location_reference': 'EdFiLocationReference',
        'location_school_reference': 'EdFiSchoolReference',
        'available_credit_conversion': 'float',
        'available_credits': 'float',
        'available_credit_type_descriptor': 'str',
        'characteristics': 'list[EdFiSectionCharacteristic]',
        'class_periods': 'list[EdFiSectionClassPeriod]',
        'course_level_characteristics': 'list[EdFiSectionCourseLevelCharacteristic]',
        'educational_environment_descriptor': 'str',
        'instruction_language_descriptor': 'str',
        'medium_of_instruction_descriptor': 'str',
        'offered_grade_levels': 'list[EdFiSectionOfferedGradeLevel]',
        'official_attendance_period': 'bool',
        'population_served_descriptor': 'str',
        'programs': 'list[EdFiSectionProgram]',
        'section_name': 'str',
        'sequence_of_course': 'int',
        'etag': 'str'
    }

    attribute_map = {
        'id': 'id',
        'section_identifier': 'sectionIdentifier',
        'course_offering_reference': 'courseOfferingReference',
        'location_reference': 'locationReference',
        'location_school_reference': 'locationSchoolReference',
        'available_credit_conversion': 'availableCreditConversion',
        'available_credits': 'availableCredits',
        'available_credit_type_descriptor': 'availableCreditTypeDescriptor',
        'characteristics': 'characteristics',
        'class_periods': 'classPeriods',
        'course_level_characteristics': 'courseLevelCharacteristics',
        'educational_environment_descriptor': 'educationalEnvironmentDescriptor',
        'instruction_language_descriptor': 'instructionLanguageDescriptor',
        'medium_of_instruction_descriptor': 'mediumOfInstructionDescriptor',
        'offered_grade_levels': 'offeredGradeLevels',
        'official_attendance_period': 'officialAttendancePeriod',
        'population_served_descriptor': 'populationServedDescriptor',
        'programs': 'programs',
        'section_name': 'sectionName',
        'sequence_of_course': 'sequenceOfCourse',
        'etag': '_etag'
    }

    def __init__(self, id=None, section_identifier=None, course_offering_reference=None, location_reference=None, location_school_reference=None, available_credit_conversion=None, available_credits=None, available_credit_type_descriptor=None, characteristics=None, class_periods=None, course_level_characteristics=None, educational_environment_descriptor=None, instruction_language_descriptor=None, medium_of_instruction_descriptor=None, offered_grade_levels=None, official_attendance_period=None, population_served_descriptor=None, programs=None, section_name=None, sequence_of_course=None, etag=None, _configuration=None):  # noqa: E501
        """EdFiSection - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._section_identifier = None
        self._course_offering_reference = None
        self._location_reference = None
        self._location_school_reference = None
        self._available_credit_conversion = None
        self._available_credits = None
        self._available_credit_type_descriptor = None
        self._characteristics = None
        self._class_periods = None
        self._course_level_characteristics = None
        self._educational_environment_descriptor = None
        self._instruction_language_descriptor = None
        self._medium_of_instruction_descriptor = None
        self._offered_grade_levels = None
        self._official_attendance_period = None
        self._population_served_descriptor = None
        self._programs = None
        self._section_name = None
        self._sequence_of_course = None
        self._etag = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.section_identifier = section_identifier
        self.course_offering_reference = course_offering_reference
        if location_reference is not None:
            self.location_reference = location_reference
        if location_school_reference is not None:
            self.location_school_reference = location_school_reference
        if available_credit_conversion is not None:
            self.available_credit_conversion = available_credit_conversion
        if available_credits is not None:
            self.available_credits = available_credits
        if available_credit_type_descriptor is not None:
            self.available_credit_type_descriptor = available_credit_type_descriptor
        if characteristics is not None:
            self.characteristics = characteristics
        if class_periods is not None:
            self.class_periods = class_periods
        if course_level_characteristics is not None:
            self.course_level_characteristics = course_level_characteristics
        if educational_environment_descriptor is not None:
            self.educational_environment_descriptor = educational_environment_descriptor
        if instruction_language_descriptor is not None:
            self.instruction_language_descriptor = instruction_language_descriptor
        if medium_of_instruction_descriptor is not None:
            self.medium_of_instruction_descriptor = medium_of_instruction_descriptor
        if offered_grade_levels is not None:
            self.offered_grade_levels = offered_grade_levels
        if official_attendance_period is not None:
            self.official_attendance_period = official_attendance_period
        if population_served_descriptor is not None:
            self.population_served_descriptor = population_served_descriptor
        if programs is not None:
            self.programs = programs
        if section_name is not None:
            self.section_name = section_name
        if sequence_of_course is not None:
            self.sequence_of_course = sequence_of_course
        if etag is not None:
            self.etag = etag

    @property
    def id(self):
        """Gets the id of this EdFiSection.  # noqa: E501

          # noqa: E501

        :return: The id of this EdFiSection.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this EdFiSection.

          # noqa: E501

        :param id: The id of this EdFiSection.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def section_identifier(self):
        """Gets the section_identifier of this EdFiSection.  # noqa: E501

        The local identifier assigned to a section.  # noqa: E501

        :return: The section_identifier of this EdFiSection.  # noqa: E501
        :rtype: str
        """
        return self._section_identifier

    @section_identifier.setter
    def section_identifier(self, section_identifier):
        """Sets the section_identifier of this EdFiSection.

        The local identifier assigned to a section.  # noqa: E501

        :param section_identifier: The section_identifier of this EdFiSection.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and section_identifier is None:
            raise ValueError("Invalid value for `section_identifier`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                section_identifier is not None and len(section_identifier) > 255):
            raise ValueError("Invalid value for `section_identifier`, length must be less than or equal to `255`")  # noqa: E501

        self._section_identifier = section_identifier

    @property
    def course_offering_reference(self):
        """Gets the course_offering_reference of this EdFiSection.  # noqa: E501


        :return: The course_offering_reference of this EdFiSection.  # noqa: E501
        :rtype: EdFiCourseOfferingReference
        """
        return self._course_offering_reference

    @course_offering_reference.setter
    def course_offering_reference(self, course_offering_reference):
        """Sets the course_offering_reference of this EdFiSection.


        :param course_offering_reference: The course_offering_reference of this EdFiSection.  # noqa: E501
        :type: EdFiCourseOfferingReference
        """
        if self._configuration.client_side_validation and course_offering_reference is None:
            raise ValueError("Invalid value for `course_offering_reference`, must not be `None`")  # noqa: E501

        self._course_offering_reference = course_offering_reference

    @property
    def location_reference(self):
        """Gets the location_reference of this EdFiSection.  # noqa: E501


        :return: The location_reference of this EdFiSection.  # noqa: E501
        :rtype: EdFiLocationReference
        """
        return self._location_reference

    @location_reference.setter
    def location_reference(self, location_reference):
        """Sets the location_reference of this EdFiSection.


        :param location_reference: The location_reference of this EdFiSection.  # noqa: E501
        :type: EdFiLocationReference
        """

        self._location_reference = location_reference

    @property
    def location_school_reference(self):
        """Gets the location_school_reference of this EdFiSection.  # noqa: E501


        :return: The location_school_reference of this EdFiSection.  # noqa: E501
        :rtype: EdFiSchoolReference
        """
        return self._location_school_reference

    @location_school_reference.setter
    def location_school_reference(self, location_school_reference):
        """Sets the location_school_reference of this EdFiSection.


        :param location_school_reference: The location_school_reference of this EdFiSection.  # noqa: E501
        :type: EdFiSchoolReference
        """

        self._location_school_reference = location_school_reference

    @property
    def available_credit_conversion(self):
        """Gets the available_credit_conversion of this EdFiSection.  # noqa: E501

        Conversion factor that when multiplied by the number of credits is equivalent to Carnegie units.  # noqa: E501

        :return: The available_credit_conversion of this EdFiSection.  # noqa: E501
        :rtype: float
        """
        return self._available_credit_conversion

    @available_credit_conversion.setter
    def available_credit_conversion(self, available_credit_conversion):
        """Sets the available_credit_conversion of this EdFiSection.

        Conversion factor that when multiplied by the number of credits is equivalent to Carnegie units.  # noqa: E501

        :param available_credit_conversion: The available_credit_conversion of this EdFiSection.  # noqa: E501
        :type: float
        """

        self._available_credit_conversion = available_credit_conversion

    @property
    def available_credits(self):
        """Gets the available_credits of this EdFiSection.  # noqa: E501

        The value of credits or units of value awarded for the completion of a course.  # noqa: E501

        :return: The available_credits of this EdFiSection.  # noqa: E501
        :rtype: float
        """
        return self._available_credits

    @available_credits.setter
    def available_credits(self, available_credits):
        """Sets the available_credits of this EdFiSection.

        The value of credits or units of value awarded for the completion of a course.  # noqa: E501

        :param available_credits: The available_credits of this EdFiSection.  # noqa: E501
        :type: float
        """

        self._available_credits = available_credits

    @property
    def available_credit_type_descriptor(self):
        """Gets the available_credit_type_descriptor of this EdFiSection.  # noqa: E501

        The type of credits or units of value awarded for the completion of a course.  # noqa: E501

        :return: The available_credit_type_descriptor of this EdFiSection.  # noqa: E501
        :rtype: str
        """
        return self._available_credit_type_descriptor

    @available_credit_type_descriptor.setter
    def available_credit_type_descriptor(self, available_credit_type_descriptor):
        """Sets the available_credit_type_descriptor of this EdFiSection.

        The type of credits or units of value awarded for the completion of a course.  # noqa: E501

        :param available_credit_type_descriptor: The available_credit_type_descriptor of this EdFiSection.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                available_credit_type_descriptor is not None and len(available_credit_type_descriptor) > 306):
            raise ValueError("Invalid value for `available_credit_type_descriptor`, length must be less than or equal to `306`")  # noqa: E501

        self._available_credit_type_descriptor = available_credit_type_descriptor

    @property
    def characteristics(self):
        """Gets the characteristics of this EdFiSection.  # noqa: E501

        An unordered collection of sectionCharacteristics. Reflects important characteristics of the Section, such as whether or not attendance is taken and the Section is graded.  # noqa: E501

        :return: The characteristics of this EdFiSection.  # noqa: E501
        :rtype: list[EdFiSectionCharacteristic]
        """
        return self._characteristics

    @characteristics.setter
    def characteristics(self, characteristics):
        """Sets the characteristics of this EdFiSection.

        An unordered collection of sectionCharacteristics. Reflects important characteristics of the Section, such as whether or not attendance is taken and the Section is graded.  # noqa: E501

        :param characteristics: The characteristics of this EdFiSection.  # noqa: E501
        :type: list[EdFiSectionCharacteristic]
        """

        self._characteristics = characteristics

    @property
    def class_periods(self):
        """Gets the class_periods of this EdFiSection.  # noqa: E501

        An unordered collection of sectionClassPeriods. The class period during which the Section meets.  # noqa: E501

        :return: The class_periods of this EdFiSection.  # noqa: E501
        :rtype: list[EdFiSectionClassPeriod]
        """
        return self._class_periods

    @class_periods.setter
    def class_periods(self, class_periods):
        """Sets the class_periods of this EdFiSection.

        An unordered collection of sectionClassPeriods. The class period during which the Section meets.  # noqa: E501

        :param class_periods: The class_periods of this EdFiSection.  # noqa: E501
        :type: list[EdFiSectionClassPeriod]
        """

        self._class_periods = class_periods

    @property
    def course_level_characteristics(self):
        """Gets the course_level_characteristics of this EdFiSection.  # noqa: E501

        An unordered collection of sectionCourseLevelCharacteristics. The type of specific program or designation with which the section is associated (e.g., AP, IB, Dual Credit, CTE). This collection should only be populated if it differs from the Course Level Characteristics identified at the Course Offering level.  # noqa: E501

        :return: The course_level_characteristics of this EdFiSection.  # noqa: E501
        :rtype: list[EdFiSectionCourseLevelCharacteristic]
        """
        return self._course_level_characteristics

    @course_level_characteristics.setter
    def course_level_characteristics(self, course_level_characteristics):
        """Sets the course_level_characteristics of this EdFiSection.

        An unordered collection of sectionCourseLevelCharacteristics. The type of specific program or designation with which the section is associated (e.g., AP, IB, Dual Credit, CTE). This collection should only be populated if it differs from the Course Level Characteristics identified at the Course Offering level.  # noqa: E501

        :param course_level_characteristics: The course_level_characteristics of this EdFiSection.  # noqa: E501
        :type: list[EdFiSectionCourseLevelCharacteristic]
        """

        self._course_level_characteristics = course_level_characteristics

    @property
    def educational_environment_descriptor(self):
        """Gets the educational_environment_descriptor of this EdFiSection.  # noqa: E501

        The setting in which a child receives education and related services; for example:        Center-based instruction        Home-based instruction        Hospital class        Mainstream        Residential care and treatment facility        ...  # noqa: E501

        :return: The educational_environment_descriptor of this EdFiSection.  # noqa: E501
        :rtype: str
        """
        return self._educational_environment_descriptor

    @educational_environment_descriptor.setter
    def educational_environment_descriptor(self, educational_environment_descriptor):
        """Sets the educational_environment_descriptor of this EdFiSection.

        The setting in which a child receives education and related services; for example:        Center-based instruction        Home-based instruction        Hospital class        Mainstream        Residential care and treatment facility        ...  # noqa: E501

        :param educational_environment_descriptor: The educational_environment_descriptor of this EdFiSection.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                educational_environment_descriptor is not None and len(educational_environment_descriptor) > 306):
            raise ValueError("Invalid value for `educational_environment_descriptor`, length must be less than or equal to `306`")  # noqa: E501

        self._educational_environment_descriptor = educational_environment_descriptor

    @property
    def instruction_language_descriptor(self):
        """Gets the instruction_language_descriptor of this EdFiSection.  # noqa: E501

        The primary language of instruction, if omitted English is assumed.  # noqa: E501

        :return: The instruction_language_descriptor of this EdFiSection.  # noqa: E501
        :rtype: str
        """
        return self._instruction_language_descriptor

    @instruction_language_descriptor.setter
    def instruction_language_descriptor(self, instruction_language_descriptor):
        """Sets the instruction_language_descriptor of this EdFiSection.

        The primary language of instruction, if omitted English is assumed.  # noqa: E501

        :param instruction_language_descriptor: The instruction_language_descriptor of this EdFiSection.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                instruction_language_descriptor is not None and len(instruction_language_descriptor) > 306):
            raise ValueError("Invalid value for `instruction_language_descriptor`, length must be less than or equal to `306`")  # noqa: E501

        self._instruction_language_descriptor = instruction_language_descriptor

    @property
    def medium_of_instruction_descriptor(self):
        """Gets the medium_of_instruction_descriptor of this EdFiSection.  # noqa: E501

        The media through which teachers provide instruction to students and students and teachers communicate about instructional matters; for example:        Technology-based instruction in classroom        Correspondence instruction        Face-to-face instruction        Virtual/On-line Distance learning        Center-based instruction        ...  # noqa: E501

        :return: The medium_of_instruction_descriptor of this EdFiSection.  # noqa: E501
        :rtype: str
        """
        return self._medium_of_instruction_descriptor

    @medium_of_instruction_descriptor.setter
    def medium_of_instruction_descriptor(self, medium_of_instruction_descriptor):
        """Sets the medium_of_instruction_descriptor of this EdFiSection.

        The media through which teachers provide instruction to students and students and teachers communicate about instructional matters; for example:        Technology-based instruction in classroom        Correspondence instruction        Face-to-face instruction        Virtual/On-line Distance learning        Center-based instruction        ...  # noqa: E501

        :param medium_of_instruction_descriptor: The medium_of_instruction_descriptor of this EdFiSection.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                medium_of_instruction_descriptor is not None and len(medium_of_instruction_descriptor) > 306):
            raise ValueError("Invalid value for `medium_of_instruction_descriptor`, length must be less than or equal to `306`")  # noqa: E501

        self._medium_of_instruction_descriptor = medium_of_instruction_descriptor

    @property
    def offered_grade_levels(self):
        """Gets the offered_grade_levels of this EdFiSection.  # noqa: E501

        An unordered collection of sectionOfferedGradeLevels. The grade levels in which the section is offered. This collection should only be populated if it differs from the Offered Grade Levels identified at the Course Offering level.  # noqa: E501

        :return: The offered_grade_levels of this EdFiSection.  # noqa: E501
        :rtype: list[EdFiSectionOfferedGradeLevel]
        """
        return self._offered_grade_levels

    @offered_grade_levels.setter
    def offered_grade_levels(self, offered_grade_levels):
        """Sets the offered_grade_levels of this EdFiSection.

        An unordered collection of sectionOfferedGradeLevels. The grade levels in which the section is offered. This collection should only be populated if it differs from the Offered Grade Levels identified at the Course Offering level.  # noqa: E501

        :param offered_grade_levels: The offered_grade_levels of this EdFiSection.  # noqa: E501
        :type: list[EdFiSectionOfferedGradeLevel]
        """

        self._offered_grade_levels = offered_grade_levels

    @property
    def official_attendance_period(self):
        """Gets the official_attendance_period of this EdFiSection.  # noqa: E501

        Indicator of whether this section is used for official daily attendance. Alternatively, official daily attendance may be tied to a Class Period.  # noqa: E501

        :return: The official_attendance_period of this EdFiSection.  # noqa: E501
        :rtype: bool
        """
        return self._official_attendance_period

    @official_attendance_period.setter
    def official_attendance_period(self, official_attendance_period):
        """Sets the official_attendance_period of this EdFiSection.

        Indicator of whether this section is used for official daily attendance. Alternatively, official daily attendance may be tied to a Class Period.  # noqa: E501

        :param official_attendance_period: The official_attendance_period of this EdFiSection.  # noqa: E501
        :type: bool
        """

        self._official_attendance_period = official_attendance_period

    @property
    def population_served_descriptor(self):
        """Gets the population_served_descriptor of this EdFiSection.  # noqa: E501

        The type of students the Section is offered and tailored to; for example:        Bilingual students        Remedial education students        Gifted and talented students        Career and Technical Education students        Special education students        ...  # noqa: E501

        :return: The population_served_descriptor of this EdFiSection.  # noqa: E501
        :rtype: str
        """
        return self._population_served_descriptor

    @population_served_descriptor.setter
    def population_served_descriptor(self, population_served_descriptor):
        """Sets the population_served_descriptor of this EdFiSection.

        The type of students the Section is offered and tailored to; for example:        Bilingual students        Remedial education students        Gifted and talented students        Career and Technical Education students        Special education students        ...  # noqa: E501

        :param population_served_descriptor: The population_served_descriptor of this EdFiSection.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                population_served_descriptor is not None and len(population_served_descriptor) > 306):
            raise ValueError("Invalid value for `population_served_descriptor`, length must be less than or equal to `306`")  # noqa: E501

        self._population_served_descriptor = population_served_descriptor

    @property
    def programs(self):
        """Gets the programs of this EdFiSection.  # noqa: E501

        An unordered collection of sectionPrograms. Optional reference to program (e.g., CTE) to which the Section is associated.  # noqa: E501

        :return: The programs of this EdFiSection.  # noqa: E501
        :rtype: list[EdFiSectionProgram]
        """
        return self._programs

    @programs.setter
    def programs(self, programs):
        """Sets the programs of this EdFiSection.

        An unordered collection of sectionPrograms. Optional reference to program (e.g., CTE) to which the Section is associated.  # noqa: E501

        :param programs: The programs of this EdFiSection.  # noqa: E501
        :type: list[EdFiSectionProgram]
        """

        self._programs = programs

    @property
    def section_name(self):
        """Gets the section_name of this EdFiSection.  # noqa: E501

        A locally-defined name for the section, generally created to make the section more recognizable in informal contexts and generally distinct from the SectionIdentifier.  # noqa: E501

        :return: The section_name of this EdFiSection.  # noqa: E501
        :rtype: str
        """
        return self._section_name

    @section_name.setter
    def section_name(self, section_name):
        """Sets the section_name of this EdFiSection.

        A locally-defined name for the section, generally created to make the section more recognizable in informal contexts and generally distinct from the SectionIdentifier.  # noqa: E501

        :param section_name: The section_name of this EdFiSection.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                section_name is not None and len(section_name) > 100):
            raise ValueError("Invalid value for `section_name`, length must be less than or equal to `100`")  # noqa: E501

        self._section_name = section_name

    @property
    def sequence_of_course(self):
        """Gets the sequence_of_course of this EdFiSection.  # noqa: E501

        When a section is part of a sequence of parts for a course, the number of the sequence. If the course has only one part, the value of this section attribute should be 1.  # noqa: E501

        :return: The sequence_of_course of this EdFiSection.  # noqa: E501
        :rtype: int
        """
        return self._sequence_of_course

    @sequence_of_course.setter
    def sequence_of_course(self, sequence_of_course):
        """Sets the sequence_of_course of this EdFiSection.

        When a section is part of a sequence of parts for a course, the number of the sequence. If the course has only one part, the value of this section attribute should be 1.  # noqa: E501

        :param sequence_of_course: The sequence_of_course of this EdFiSection.  # noqa: E501
        :type: int
        """

        self._sequence_of_course = sequence_of_course

    @property
    def etag(self):
        """Gets the etag of this EdFiSection.  # noqa: E501

        A unique system-generated value that identifies the version of the resource.  # noqa: E501

        :return: The etag of this EdFiSection.  # noqa: E501
        :rtype: str
        """
        return self._etag

    @etag.setter
    def etag(self, etag):
        """Sets the etag of this EdFiSection.

        A unique system-generated value that identifies the version of the resource.  # noqa: E501

        :param etag: The etag of this EdFiSection.  # noqa: E501
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
        if issubclass(EdFiSection, dict):
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
        if not isinstance(other, EdFiSection):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EdFiSection):
            return True

        return self.to_dict() != other.to_dict()
