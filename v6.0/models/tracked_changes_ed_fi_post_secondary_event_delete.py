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


class TrackedChangesEdFiPostSecondaryEventDelete(object):
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
        'change_version': 'float',
        'key_values': 'TrackedChangesEdFiPostSecondaryEventKey'
    }

    attribute_map = {
        'id': 'id',
        'change_version': 'changeVersion',
        'key_values': 'keyValues'
    }

    def __init__(self, id=None, change_version=None, key_values=None, _configuration=None):  # noqa: E501
        """TrackedChangesEdFiPostSecondaryEventDelete - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._change_version = None
        self._key_values = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if change_version is not None:
            self.change_version = change_version
        if key_values is not None:
            self.key_values = key_values

    @property
    def id(self):
        """Gets the id of this TrackedChangesEdFiPostSecondaryEventDelete.  # noqa: E501

        Resource identifier  # noqa: E501

        :return: The id of this TrackedChangesEdFiPostSecondaryEventDelete.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TrackedChangesEdFiPostSecondaryEventDelete.

        Resource identifier  # noqa: E501

        :param id: The id of this TrackedChangesEdFiPostSecondaryEventDelete.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def change_version(self):
        """Gets the change_version of this TrackedChangesEdFiPostSecondaryEventDelete.  # noqa: E501

        Change version  # noqa: E501

        :return: The change_version of this TrackedChangesEdFiPostSecondaryEventDelete.  # noqa: E501
        :rtype: float
        """
        return self._change_version

    @change_version.setter
    def change_version(self, change_version):
        """Sets the change_version of this TrackedChangesEdFiPostSecondaryEventDelete.

        Change version  # noqa: E501

        :param change_version: The change_version of this TrackedChangesEdFiPostSecondaryEventDelete.  # noqa: E501
        :type: float
        """

        self._change_version = change_version

    @property
    def key_values(self):
        """Gets the key_values of this TrackedChangesEdFiPostSecondaryEventDelete.  # noqa: E501


        :return: The key_values of this TrackedChangesEdFiPostSecondaryEventDelete.  # noqa: E501
        :rtype: TrackedChangesEdFiPostSecondaryEventKey
        """
        return self._key_values

    @key_values.setter
    def key_values(self, key_values):
        """Sets the key_values of this TrackedChangesEdFiPostSecondaryEventDelete.


        :param key_values: The key_values of this TrackedChangesEdFiPostSecondaryEventDelete.  # noqa: E501
        :type: TrackedChangesEdFiPostSecondaryEventKey
        """

        self._key_values = key_values

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
        if issubclass(TrackedChangesEdFiPostSecondaryEventDelete, dict):
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
        if not isinstance(other, TrackedChangesEdFiPostSecondaryEventDelete):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TrackedChangesEdFiPostSecondaryEventDelete):
            return True

        return self.to_dict() != other.to_dict()
