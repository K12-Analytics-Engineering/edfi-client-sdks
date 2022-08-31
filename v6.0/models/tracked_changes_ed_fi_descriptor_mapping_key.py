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


class TrackedChangesEdFiDescriptorMappingKey(object):
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
        'mapped_namespace': 'str',
        'mapped_value': 'str',
        'namespace': 'str',
        'value': 'str'
    }

    attribute_map = {
        'mapped_namespace': 'mappedNamespace',
        'mapped_value': 'mappedValue',
        'namespace': 'namespace',
        'value': 'value'
    }

    def __init__(self, mapped_namespace=None, mapped_value=None, namespace=None, value=None, _configuration=None):  # noqa: E501
        """TrackedChangesEdFiDescriptorMappingKey - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._mapped_namespace = None
        self._mapped_value = None
        self._namespace = None
        self._value = None
        self.discriminator = None

        if mapped_namespace is not None:
            self.mapped_namespace = mapped_namespace
        if mapped_value is not None:
            self.mapped_value = mapped_value
        if namespace is not None:
            self.namespace = namespace
        if value is not None:
            self.value = value

    @property
    def mapped_namespace(self):
        """Gets the mapped_namespace of this TrackedChangesEdFiDescriptorMappingKey.  # noqa: E501

        The namespace of the descriptor value to which the from descriptor value is mapped to.  # noqa: E501

        :return: The mapped_namespace of this TrackedChangesEdFiDescriptorMappingKey.  # noqa: E501
        :rtype: str
        """
        return self._mapped_namespace

    @mapped_namespace.setter
    def mapped_namespace(self, mapped_namespace):
        """Sets the mapped_namespace of this TrackedChangesEdFiDescriptorMappingKey.

        The namespace of the descriptor value to which the from descriptor value is mapped to.  # noqa: E501

        :param mapped_namespace: The mapped_namespace of this TrackedChangesEdFiDescriptorMappingKey.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                mapped_namespace is not None and len(mapped_namespace) > 255):
            raise ValueError("Invalid value for `mapped_namespace`, length must be less than or equal to `255`")  # noqa: E501

        self._mapped_namespace = mapped_namespace

    @property
    def mapped_value(self):
        """Gets the mapped_value of this TrackedChangesEdFiDescriptorMappingKey.  # noqa: E501

        The descriptor value to which the from descriptor value is being mapped to.  # noqa: E501

        :return: The mapped_value of this TrackedChangesEdFiDescriptorMappingKey.  # noqa: E501
        :rtype: str
        """
        return self._mapped_value

    @mapped_value.setter
    def mapped_value(self, mapped_value):
        """Sets the mapped_value of this TrackedChangesEdFiDescriptorMappingKey.

        The descriptor value to which the from descriptor value is being mapped to.  # noqa: E501

        :param mapped_value: The mapped_value of this TrackedChangesEdFiDescriptorMappingKey.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                mapped_value is not None and len(mapped_value) > 50):
            raise ValueError("Invalid value for `mapped_value`, length must be less than or equal to `50`")  # noqa: E501

        self._mapped_value = mapped_value

    @property
    def namespace(self):
        """Gets the namespace of this TrackedChangesEdFiDescriptorMappingKey.  # noqa: E501

        The namespace of the descriptor value that is being mapped to another value.  # noqa: E501

        :return: The namespace of this TrackedChangesEdFiDescriptorMappingKey.  # noqa: E501
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """Sets the namespace of this TrackedChangesEdFiDescriptorMappingKey.

        The namespace of the descriptor value that is being mapped to another value.  # noqa: E501

        :param namespace: The namespace of this TrackedChangesEdFiDescriptorMappingKey.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                namespace is not None and len(namespace) > 255):
            raise ValueError("Invalid value for `namespace`, length must be less than or equal to `255`")  # noqa: E501

        self._namespace = namespace

    @property
    def value(self):
        """Gets the value of this TrackedChangesEdFiDescriptorMappingKey.  # noqa: E501

        The descriptor value that is being mapped to another value.  # noqa: E501

        :return: The value of this TrackedChangesEdFiDescriptorMappingKey.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this TrackedChangesEdFiDescriptorMappingKey.

        The descriptor value that is being mapped to another value.  # noqa: E501

        :param value: The value of this TrackedChangesEdFiDescriptorMappingKey.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                value is not None and len(value) > 50):
            raise ValueError("Invalid value for `value`, length must be less than or equal to `50`")  # noqa: E501

        self._value = value

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
        if issubclass(TrackedChangesEdFiDescriptorMappingKey, dict):
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
        if not isinstance(other, TrackedChangesEdFiDescriptorMappingKey):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TrackedChangesEdFiDescriptorMappingKey):
            return True

        return self.to_dict() != other.to_dict()