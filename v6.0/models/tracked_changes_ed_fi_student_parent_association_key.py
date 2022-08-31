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


class TrackedChangesEdFiStudentParentAssociationKey(object):
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
        'parent_unique_id': 'str',
        'student_unique_id': 'str'
    }

    attribute_map = {
        'parent_unique_id': 'parentUniqueId',
        'student_unique_id': 'studentUniqueId'
    }

    def __init__(self, parent_unique_id=None, student_unique_id=None, _configuration=None):  # noqa: E501
        """TrackedChangesEdFiStudentParentAssociationKey - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._parent_unique_id = None
        self._student_unique_id = None
        self.discriminator = None

        if parent_unique_id is not None:
            self.parent_unique_id = parent_unique_id
        if student_unique_id is not None:
            self.student_unique_id = student_unique_id

    @property
    def parent_unique_id(self):
        """Gets the parent_unique_id of this TrackedChangesEdFiStudentParentAssociationKey.  # noqa: E501

        A unique alphanumeric code assigned to a parent.  # noqa: E501

        :return: The parent_unique_id of this TrackedChangesEdFiStudentParentAssociationKey.  # noqa: E501
        :rtype: str
        """
        return self._parent_unique_id

    @parent_unique_id.setter
    def parent_unique_id(self, parent_unique_id):
        """Sets the parent_unique_id of this TrackedChangesEdFiStudentParentAssociationKey.

        A unique alphanumeric code assigned to a parent.  # noqa: E501

        :param parent_unique_id: The parent_unique_id of this TrackedChangesEdFiStudentParentAssociationKey.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                parent_unique_id is not None and len(parent_unique_id) > 32):
            raise ValueError("Invalid value for `parent_unique_id`, length must be less than or equal to `32`")  # noqa: E501

        self._parent_unique_id = parent_unique_id

    @property
    def student_unique_id(self):
        """Gets the student_unique_id of this TrackedChangesEdFiStudentParentAssociationKey.  # noqa: E501

        A unique alphanumeric code assigned to a student.  # noqa: E501

        :return: The student_unique_id of this TrackedChangesEdFiStudentParentAssociationKey.  # noqa: E501
        :rtype: str
        """
        return self._student_unique_id

    @student_unique_id.setter
    def student_unique_id(self, student_unique_id):
        """Sets the student_unique_id of this TrackedChangesEdFiStudentParentAssociationKey.

        A unique alphanumeric code assigned to a student.  # noqa: E501

        :param student_unique_id: The student_unique_id of this TrackedChangesEdFiStudentParentAssociationKey.  # noqa: E501
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
        if issubclass(TrackedChangesEdFiStudentParentAssociationKey, dict):
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
        if not isinstance(other, TrackedChangesEdFiStudentParentAssociationKey):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TrackedChangesEdFiStudentParentAssociationKey):
            return True

        return self.to_dict() != other.to_dict()
