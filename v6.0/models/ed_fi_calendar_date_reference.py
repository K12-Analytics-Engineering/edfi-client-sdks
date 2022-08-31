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


class EdFiCalendarDateReference(object):
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
        'calendar_code': 'str',
        '_date': 'date',
        'school_id': 'int',
        'school_year': 'int',
        'link': 'Link'
    }

    attribute_map = {
        'calendar_code': 'calendarCode',
        '_date': 'date',
        'school_id': 'schoolId',
        'school_year': 'schoolYear',
        'link': 'link'
    }

    def __init__(self, calendar_code=None, _date=None, school_id=None, school_year=None, link=None, _configuration=None):  # noqa: E501
        """EdFiCalendarDateReference - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._calendar_code = None
        self.__date = None
        self._school_id = None
        self._school_year = None
        self._link = None
        self.discriminator = None

        self.calendar_code = calendar_code
        self._date = _date
        self.school_id = school_id
        self.school_year = school_year
        if link is not None:
            self.link = link

    @property
    def calendar_code(self):
        """Gets the calendar_code of this EdFiCalendarDateReference.  # noqa: E501

        The identifier for the calendar.  # noqa: E501

        :return: The calendar_code of this EdFiCalendarDateReference.  # noqa: E501
        :rtype: str
        """
        return self._calendar_code

    @calendar_code.setter
    def calendar_code(self, calendar_code):
        """Sets the calendar_code of this EdFiCalendarDateReference.

        The identifier for the calendar.  # noqa: E501

        :param calendar_code: The calendar_code of this EdFiCalendarDateReference.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and calendar_code is None:
            raise ValueError("Invalid value for `calendar_code`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                calendar_code is not None and len(calendar_code) > 60):
            raise ValueError("Invalid value for `calendar_code`, length must be less than or equal to `60`")  # noqa: E501

        self._calendar_code = calendar_code

    @property
    def _date(self):
        """Gets the _date of this EdFiCalendarDateReference.  # noqa: E501

        The month, day, and year of the calendar event.  # noqa: E501

        :return: The _date of this EdFiCalendarDateReference.  # noqa: E501
        :rtype: date
        """
        return self.__date

    @_date.setter
    def _date(self, _date):
        """Sets the _date of this EdFiCalendarDateReference.

        The month, day, and year of the calendar event.  # noqa: E501

        :param _date: The _date of this EdFiCalendarDateReference.  # noqa: E501
        :type: date
        """
        if self._configuration.client_side_validation and _date is None:
            raise ValueError("Invalid value for `_date`, must not be `None`")  # noqa: E501

        self.__date = _date

    @property
    def school_id(self):
        """Gets the school_id of this EdFiCalendarDateReference.  # noqa: E501

        The identifier assigned to a school.  # noqa: E501

        :return: The school_id of this EdFiCalendarDateReference.  # noqa: E501
        :rtype: int
        """
        return self._school_id

    @school_id.setter
    def school_id(self, school_id):
        """Sets the school_id of this EdFiCalendarDateReference.

        The identifier assigned to a school.  # noqa: E501

        :param school_id: The school_id of this EdFiCalendarDateReference.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and school_id is None:
            raise ValueError("Invalid value for `school_id`, must not be `None`")  # noqa: E501

        self._school_id = school_id

    @property
    def school_year(self):
        """Gets the school_year of this EdFiCalendarDateReference.  # noqa: E501

        The identifier for the school year associated with the calendar.  # noqa: E501

        :return: The school_year of this EdFiCalendarDateReference.  # noqa: E501
        :rtype: int
        """
        return self._school_year

    @school_year.setter
    def school_year(self, school_year):
        """Sets the school_year of this EdFiCalendarDateReference.

        The identifier for the school year associated with the calendar.  # noqa: E501

        :param school_year: The school_year of this EdFiCalendarDateReference.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and school_year is None:
            raise ValueError("Invalid value for `school_year`, must not be `None`")  # noqa: E501

        self._school_year = school_year

    @property
    def link(self):
        """Gets the link of this EdFiCalendarDateReference.  # noqa: E501


        :return: The link of this EdFiCalendarDateReference.  # noqa: E501
        :rtype: Link
        """
        return self._link

    @link.setter
    def link(self, link):
        """Sets the link of this EdFiCalendarDateReference.


        :param link: The link of this EdFiCalendarDateReference.  # noqa: E501
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
        if issubclass(EdFiCalendarDateReference, dict):
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
        if not isinstance(other, EdFiCalendarDateReference):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EdFiCalendarDateReference):
            return True

        return self.to_dict() != other.to_dict()
