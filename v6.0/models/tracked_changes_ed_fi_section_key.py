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


class TrackedChangesEdFiSectionKey(object):
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
        'section_identifier': 'str',
        'local_course_code': 'str',
        'school_id': 'int',
        'school_year': 'int',
        'session_name': 'str'
    }

    attribute_map = {
        'section_identifier': 'sectionIdentifier',
        'local_course_code': 'localCourseCode',
        'school_id': 'schoolId',
        'school_year': 'schoolYear',
        'session_name': 'sessionName'
    }

    def __init__(self, section_identifier=None, local_course_code=None, school_id=None, school_year=None, session_name=None, _configuration=None):  # noqa: E501
        """TrackedChangesEdFiSectionKey - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._section_identifier = None
        self._local_course_code = None
        self._school_id = None
        self._school_year = None
        self._session_name = None
        self.discriminator = None

        if section_identifier is not None:
            self.section_identifier = section_identifier
        if local_course_code is not None:
            self.local_course_code = local_course_code
        if school_id is not None:
            self.school_id = school_id
        if school_year is not None:
            self.school_year = school_year
        if session_name is not None:
            self.session_name = session_name

    @property
    def section_identifier(self):
        """Gets the section_identifier of this TrackedChangesEdFiSectionKey.  # noqa: E501

        The local identifier assigned to a section.  # noqa: E501

        :return: The section_identifier of this TrackedChangesEdFiSectionKey.  # noqa: E501
        :rtype: str
        """
        return self._section_identifier

    @section_identifier.setter
    def section_identifier(self, section_identifier):
        """Sets the section_identifier of this TrackedChangesEdFiSectionKey.

        The local identifier assigned to a section.  # noqa: E501

        :param section_identifier: The section_identifier of this TrackedChangesEdFiSectionKey.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                section_identifier is not None and len(section_identifier) > 255):
            raise ValueError("Invalid value for `section_identifier`, length must be less than or equal to `255`")  # noqa: E501

        self._section_identifier = section_identifier

    @property
    def local_course_code(self):
        """Gets the local_course_code of this TrackedChangesEdFiSectionKey.  # noqa: E501

        The local code assigned by the School that identifies the course offering provided for the instruction of students.  # noqa: E501

        :return: The local_course_code of this TrackedChangesEdFiSectionKey.  # noqa: E501
        :rtype: str
        """
        return self._local_course_code

    @local_course_code.setter
    def local_course_code(self, local_course_code):
        """Sets the local_course_code of this TrackedChangesEdFiSectionKey.

        The local code assigned by the School that identifies the course offering provided for the instruction of students.  # noqa: E501

        :param local_course_code: The local_course_code of this TrackedChangesEdFiSectionKey.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                local_course_code is not None and len(local_course_code) > 60):
            raise ValueError("Invalid value for `local_course_code`, length must be less than or equal to `60`")  # noqa: E501

        self._local_course_code = local_course_code

    @property
    def school_id(self):
        """Gets the school_id of this TrackedChangesEdFiSectionKey.  # noqa: E501

        The identifier assigned to a school.  # noqa: E501

        :return: The school_id of this TrackedChangesEdFiSectionKey.  # noqa: E501
        :rtype: int
        """
        return self._school_id

    @school_id.setter
    def school_id(self, school_id):
        """Sets the school_id of this TrackedChangesEdFiSectionKey.

        The identifier assigned to a school.  # noqa: E501

        :param school_id: The school_id of this TrackedChangesEdFiSectionKey.  # noqa: E501
        :type: int
        """

        self._school_id = school_id

    @property
    def school_year(self):
        """Gets the school_year of this TrackedChangesEdFiSectionKey.  # noqa: E501

        The identifier for the school year.  # noqa: E501

        :return: The school_year of this TrackedChangesEdFiSectionKey.  # noqa: E501
        :rtype: int
        """
        return self._school_year

    @school_year.setter
    def school_year(self, school_year):
        """Sets the school_year of this TrackedChangesEdFiSectionKey.

        The identifier for the school year.  # noqa: E501

        :param school_year: The school_year of this TrackedChangesEdFiSectionKey.  # noqa: E501
        :type: int
        """

        self._school_year = school_year

    @property
    def session_name(self):
        """Gets the session_name of this TrackedChangesEdFiSectionKey.  # noqa: E501

        The identifier for the calendar for the academic session.  # noqa: E501

        :return: The session_name of this TrackedChangesEdFiSectionKey.  # noqa: E501
        :rtype: str
        """
        return self._session_name

    @session_name.setter
    def session_name(self, session_name):
        """Sets the session_name of this TrackedChangesEdFiSectionKey.

        The identifier for the calendar for the academic session.  # noqa: E501

        :param session_name: The session_name of this TrackedChangesEdFiSectionKey.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                session_name is not None and len(session_name) > 60):
            raise ValueError("Invalid value for `session_name`, length must be less than or equal to `60`")  # noqa: E501

        self._session_name = session_name

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
        if issubclass(TrackedChangesEdFiSectionKey, dict):
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
        if not isinstance(other, TrackedChangesEdFiSectionKey):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TrackedChangesEdFiSectionKey):
            return True

        return self.to_dict() != other.to_dict()
