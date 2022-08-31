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


class EdFiSectionAttendanceTakenEvent(object):
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
        'calendar_date_reference': 'EdFiCalendarDateReference',
        'section_reference': 'EdFiSectionReference',
        'staff_reference': 'EdFiStaffReference',
        'event_date': 'date',
        'etag': 'str'
    }

    attribute_map = {
        'id': 'id',
        'calendar_date_reference': 'calendarDateReference',
        'section_reference': 'sectionReference',
        'staff_reference': 'staffReference',
        'event_date': 'eventDate',
        'etag': '_etag'
    }

    def __init__(self, id=None, calendar_date_reference=None, section_reference=None, staff_reference=None, event_date=None, etag=None, _configuration=None):  # noqa: E501
        """EdFiSectionAttendanceTakenEvent - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._calendar_date_reference = None
        self._section_reference = None
        self._staff_reference = None
        self._event_date = None
        self._etag = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.calendar_date_reference = calendar_date_reference
        self.section_reference = section_reference
        if staff_reference is not None:
            self.staff_reference = staff_reference
        self.event_date = event_date
        if etag is not None:
            self.etag = etag

    @property
    def id(self):
        """Gets the id of this EdFiSectionAttendanceTakenEvent.  # noqa: E501

          # noqa: E501

        :return: The id of this EdFiSectionAttendanceTakenEvent.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this EdFiSectionAttendanceTakenEvent.

          # noqa: E501

        :param id: The id of this EdFiSectionAttendanceTakenEvent.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def calendar_date_reference(self):
        """Gets the calendar_date_reference of this EdFiSectionAttendanceTakenEvent.  # noqa: E501


        :return: The calendar_date_reference of this EdFiSectionAttendanceTakenEvent.  # noqa: E501
        :rtype: EdFiCalendarDateReference
        """
        return self._calendar_date_reference

    @calendar_date_reference.setter
    def calendar_date_reference(self, calendar_date_reference):
        """Sets the calendar_date_reference of this EdFiSectionAttendanceTakenEvent.


        :param calendar_date_reference: The calendar_date_reference of this EdFiSectionAttendanceTakenEvent.  # noqa: E501
        :type: EdFiCalendarDateReference
        """
        if self._configuration.client_side_validation and calendar_date_reference is None:
            raise ValueError("Invalid value for `calendar_date_reference`, must not be `None`")  # noqa: E501

        self._calendar_date_reference = calendar_date_reference

    @property
    def section_reference(self):
        """Gets the section_reference of this EdFiSectionAttendanceTakenEvent.  # noqa: E501


        :return: The section_reference of this EdFiSectionAttendanceTakenEvent.  # noqa: E501
        :rtype: EdFiSectionReference
        """
        return self._section_reference

    @section_reference.setter
    def section_reference(self, section_reference):
        """Sets the section_reference of this EdFiSectionAttendanceTakenEvent.


        :param section_reference: The section_reference of this EdFiSectionAttendanceTakenEvent.  # noqa: E501
        :type: EdFiSectionReference
        """
        if self._configuration.client_side_validation and section_reference is None:
            raise ValueError("Invalid value for `section_reference`, must not be `None`")  # noqa: E501

        self._section_reference = section_reference

    @property
    def staff_reference(self):
        """Gets the staff_reference of this EdFiSectionAttendanceTakenEvent.  # noqa: E501


        :return: The staff_reference of this EdFiSectionAttendanceTakenEvent.  # noqa: E501
        :rtype: EdFiStaffReference
        """
        return self._staff_reference

    @staff_reference.setter
    def staff_reference(self, staff_reference):
        """Sets the staff_reference of this EdFiSectionAttendanceTakenEvent.


        :param staff_reference: The staff_reference of this EdFiSectionAttendanceTakenEvent.  # noqa: E501
        :type: EdFiStaffReference
        """

        self._staff_reference = staff_reference

    @property
    def event_date(self):
        """Gets the event_date of this EdFiSectionAttendanceTakenEvent.  # noqa: E501

        The date the section attendance taken event was submitted, which could be a different date than the instructional day.  # noqa: E501

        :return: The event_date of this EdFiSectionAttendanceTakenEvent.  # noqa: E501
        :rtype: date
        """
        return self._event_date

    @event_date.setter
    def event_date(self, event_date):
        """Sets the event_date of this EdFiSectionAttendanceTakenEvent.

        The date the section attendance taken event was submitted, which could be a different date than the instructional day.  # noqa: E501

        :param event_date: The event_date of this EdFiSectionAttendanceTakenEvent.  # noqa: E501
        :type: date
        """
        if self._configuration.client_side_validation and event_date is None:
            raise ValueError("Invalid value for `event_date`, must not be `None`")  # noqa: E501

        self._event_date = event_date

    @property
    def etag(self):
        """Gets the etag of this EdFiSectionAttendanceTakenEvent.  # noqa: E501

        A unique system-generated value that identifies the version of the resource.  # noqa: E501

        :return: The etag of this EdFiSectionAttendanceTakenEvent.  # noqa: E501
        :rtype: str
        """
        return self._etag

    @etag.setter
    def etag(self, etag):
        """Sets the etag of this EdFiSectionAttendanceTakenEvent.

        A unique system-generated value that identifies the version of the resource.  # noqa: E501

        :param etag: The etag of this EdFiSectionAttendanceTakenEvent.  # noqa: E501
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
        if issubclass(EdFiSectionAttendanceTakenEvent, dict):
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
        if not isinstance(other, EdFiSectionAttendanceTakenEvent):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EdFiSectionAttendanceTakenEvent):
            return True

        return self.to_dict() != other.to_dict()
