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


class TrackedChangesEdFiDisciplineActionKey(object):
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
        'discipline_action_identifier': 'str',
        'discipline_date': 'date',
        'student_unique_id': 'str'
    }

    attribute_map = {
        'discipline_action_identifier': 'disciplineActionIdentifier',
        'discipline_date': 'disciplineDate',
        'student_unique_id': 'studentUniqueId'
    }

    def __init__(self, discipline_action_identifier=None, discipline_date=None, student_unique_id=None, _configuration=None):  # noqa: E501
        """TrackedChangesEdFiDisciplineActionKey - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._discipline_action_identifier = None
        self._discipline_date = None
        self._student_unique_id = None
        self.discriminator = None

        if discipline_action_identifier is not None:
            self.discipline_action_identifier = discipline_action_identifier
        if discipline_date is not None:
            self.discipline_date = discipline_date
        if student_unique_id is not None:
            self.student_unique_id = student_unique_id

    @property
    def discipline_action_identifier(self):
        """Gets the discipline_action_identifier of this TrackedChangesEdFiDisciplineActionKey.  # noqa: E501

        Identifier assigned by the education organization to the discipline action.  # noqa: E501

        :return: The discipline_action_identifier of this TrackedChangesEdFiDisciplineActionKey.  # noqa: E501
        :rtype: str
        """
        return self._discipline_action_identifier

    @discipline_action_identifier.setter
    def discipline_action_identifier(self, discipline_action_identifier):
        """Sets the discipline_action_identifier of this TrackedChangesEdFiDisciplineActionKey.

        Identifier assigned by the education organization to the discipline action.  # noqa: E501

        :param discipline_action_identifier: The discipline_action_identifier of this TrackedChangesEdFiDisciplineActionKey.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                discipline_action_identifier is not None and len(discipline_action_identifier) > 32):
            raise ValueError("Invalid value for `discipline_action_identifier`, length must be less than or equal to `32`")  # noqa: E501

        self._discipline_action_identifier = discipline_action_identifier

    @property
    def discipline_date(self):
        """Gets the discipline_date of this TrackedChangesEdFiDisciplineActionKey.  # noqa: E501

        The date of the discipline action.  # noqa: E501

        :return: The discipline_date of this TrackedChangesEdFiDisciplineActionKey.  # noqa: E501
        :rtype: date
        """
        return self._discipline_date

    @discipline_date.setter
    def discipline_date(self, discipline_date):
        """Sets the discipline_date of this TrackedChangesEdFiDisciplineActionKey.

        The date of the discipline action.  # noqa: E501

        :param discipline_date: The discipline_date of this TrackedChangesEdFiDisciplineActionKey.  # noqa: E501
        :type: date
        """

        self._discipline_date = discipline_date

    @property
    def student_unique_id(self):
        """Gets the student_unique_id of this TrackedChangesEdFiDisciplineActionKey.  # noqa: E501

        A unique alphanumeric code assigned to a student.  # noqa: E501

        :return: The student_unique_id of this TrackedChangesEdFiDisciplineActionKey.  # noqa: E501
        :rtype: str
        """
        return self._student_unique_id

    @student_unique_id.setter
    def student_unique_id(self, student_unique_id):
        """Sets the student_unique_id of this TrackedChangesEdFiDisciplineActionKey.

        A unique alphanumeric code assigned to a student.  # noqa: E501

        :param student_unique_id: The student_unique_id of this TrackedChangesEdFiDisciplineActionKey.  # noqa: E501
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
        if issubclass(TrackedChangesEdFiDisciplineActionKey, dict):
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
        if not isinstance(other, TrackedChangesEdFiDisciplineActionKey):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TrackedChangesEdFiDisciplineActionKey):
            return True

        return self.to_dict() != other.to_dict()
