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


class EdFiCalendar(object):
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
        'calendar_code': 'str',
        'school_reference': 'EdFiSchoolReference',
        'school_year_type_reference': 'EdFiSchoolYearTypeReference',
        'calendar_type_descriptor': 'str',
        'grade_levels': 'list[EdFiCalendarGradeLevel]',
        'etag': 'str'
    }

    attribute_map = {
        'id': 'id',
        'calendar_code': 'calendarCode',
        'school_reference': 'schoolReference',
        'school_year_type_reference': 'schoolYearTypeReference',
        'calendar_type_descriptor': 'calendarTypeDescriptor',
        'grade_levels': 'gradeLevels',
        'etag': '_etag'
    }

    def __init__(self, id=None, calendar_code=None, school_reference=None, school_year_type_reference=None, calendar_type_descriptor=None, grade_levels=None, etag=None, _configuration=None):  # noqa: E501
        """EdFiCalendar - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._calendar_code = None
        self._school_reference = None
        self._school_year_type_reference = None
        self._calendar_type_descriptor = None
        self._grade_levels = None
        self._etag = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.calendar_code = calendar_code
        self.school_reference = school_reference
        self.school_year_type_reference = school_year_type_reference
        self.calendar_type_descriptor = calendar_type_descriptor
        if grade_levels is not None:
            self.grade_levels = grade_levels
        if etag is not None:
            self.etag = etag

    @property
    def id(self):
        """Gets the id of this EdFiCalendar.  # noqa: E501

          # noqa: E501

        :return: The id of this EdFiCalendar.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this EdFiCalendar.

          # noqa: E501

        :param id: The id of this EdFiCalendar.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def calendar_code(self):
        """Gets the calendar_code of this EdFiCalendar.  # noqa: E501

        The identifier for the calendar.  # noqa: E501

        :return: The calendar_code of this EdFiCalendar.  # noqa: E501
        :rtype: str
        """
        return self._calendar_code

    @calendar_code.setter
    def calendar_code(self, calendar_code):
        """Sets the calendar_code of this EdFiCalendar.

        The identifier for the calendar.  # noqa: E501

        :param calendar_code: The calendar_code of this EdFiCalendar.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and calendar_code is None:
            raise ValueError("Invalid value for `calendar_code`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                calendar_code is not None and len(calendar_code) > 60):
            raise ValueError("Invalid value for `calendar_code`, length must be less than or equal to `60`")  # noqa: E501

        self._calendar_code = calendar_code

    @property
    def school_reference(self):
        """Gets the school_reference of this EdFiCalendar.  # noqa: E501


        :return: The school_reference of this EdFiCalendar.  # noqa: E501
        :rtype: EdFiSchoolReference
        """
        return self._school_reference

    @school_reference.setter
    def school_reference(self, school_reference):
        """Sets the school_reference of this EdFiCalendar.


        :param school_reference: The school_reference of this EdFiCalendar.  # noqa: E501
        :type: EdFiSchoolReference
        """
        if self._configuration.client_side_validation and school_reference is None:
            raise ValueError("Invalid value for `school_reference`, must not be `None`")  # noqa: E501

        self._school_reference = school_reference

    @property
    def school_year_type_reference(self):
        """Gets the school_year_type_reference of this EdFiCalendar.  # noqa: E501


        :return: The school_year_type_reference of this EdFiCalendar.  # noqa: E501
        :rtype: EdFiSchoolYearTypeReference
        """
        return self._school_year_type_reference

    @school_year_type_reference.setter
    def school_year_type_reference(self, school_year_type_reference):
        """Sets the school_year_type_reference of this EdFiCalendar.


        :param school_year_type_reference: The school_year_type_reference of this EdFiCalendar.  # noqa: E501
        :type: EdFiSchoolYearTypeReference
        """
        if self._configuration.client_side_validation and school_year_type_reference is None:
            raise ValueError("Invalid value for `school_year_type_reference`, must not be `None`")  # noqa: E501

        self._school_year_type_reference = school_year_type_reference

    @property
    def calendar_type_descriptor(self):
        """Gets the calendar_type_descriptor of this EdFiCalendar.  # noqa: E501

        Indicates the type of calendar.  # noqa: E501

        :return: The calendar_type_descriptor of this EdFiCalendar.  # noqa: E501
        :rtype: str
        """
        return self._calendar_type_descriptor

    @calendar_type_descriptor.setter
    def calendar_type_descriptor(self, calendar_type_descriptor):
        """Sets the calendar_type_descriptor of this EdFiCalendar.

        Indicates the type of calendar.  # noqa: E501

        :param calendar_type_descriptor: The calendar_type_descriptor of this EdFiCalendar.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and calendar_type_descriptor is None:
            raise ValueError("Invalid value for `calendar_type_descriptor`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                calendar_type_descriptor is not None and len(calendar_type_descriptor) > 306):
            raise ValueError("Invalid value for `calendar_type_descriptor`, length must be less than or equal to `306`")  # noqa: E501

        self._calendar_type_descriptor = calendar_type_descriptor

    @property
    def grade_levels(self):
        """Gets the grade_levels of this EdFiCalendar.  # noqa: E501

        An unordered collection of calendarGradeLevels. Indicates the grade level associated with the calendar.  # noqa: E501

        :return: The grade_levels of this EdFiCalendar.  # noqa: E501
        :rtype: list[EdFiCalendarGradeLevel]
        """
        return self._grade_levels

    @grade_levels.setter
    def grade_levels(self, grade_levels):
        """Sets the grade_levels of this EdFiCalendar.

        An unordered collection of calendarGradeLevels. Indicates the grade level associated with the calendar.  # noqa: E501

        :param grade_levels: The grade_levels of this EdFiCalendar.  # noqa: E501
        :type: list[EdFiCalendarGradeLevel]
        """

        self._grade_levels = grade_levels

    @property
    def etag(self):
        """Gets the etag of this EdFiCalendar.  # noqa: E501

        A unique system-generated value that identifies the version of the resource.  # noqa: E501

        :return: The etag of this EdFiCalendar.  # noqa: E501
        :rtype: str
        """
        return self._etag

    @etag.setter
    def etag(self, etag):
        """Sets the etag of this EdFiCalendar.

        A unique system-generated value that identifies the version of the resource.  # noqa: E501

        :param etag: The etag of this EdFiCalendar.  # noqa: E501
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
        if issubclass(EdFiCalendar, dict):
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
        if not isinstance(other, EdFiCalendar):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EdFiCalendar):
            return True

        return self.to_dict() != other.to_dict()
