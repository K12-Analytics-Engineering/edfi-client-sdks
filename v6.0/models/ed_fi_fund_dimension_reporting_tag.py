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


class EdFiFundDimensionReportingTag(object):
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
        'reporting_tag_descriptor': 'str'
    }

    attribute_map = {
        'reporting_tag_descriptor': 'reportingTagDescriptor'
    }

    def __init__(self, reporting_tag_descriptor=None, _configuration=None):  # noqa: E501
        """EdFiFundDimensionReportingTag - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._reporting_tag_descriptor = None
        self.discriminator = None

        self.reporting_tag_descriptor = reporting_tag_descriptor

    @property
    def reporting_tag_descriptor(self):
        """Gets the reporting_tag_descriptor of this EdFiFundDimensionReportingTag.  # noqa: E501

        Optional tag for accountability reporting.  # noqa: E501

        :return: The reporting_tag_descriptor of this EdFiFundDimensionReportingTag.  # noqa: E501
        :rtype: str
        """
        return self._reporting_tag_descriptor

    @reporting_tag_descriptor.setter
    def reporting_tag_descriptor(self, reporting_tag_descriptor):
        """Sets the reporting_tag_descriptor of this EdFiFundDimensionReportingTag.

        Optional tag for accountability reporting.  # noqa: E501

        :param reporting_tag_descriptor: The reporting_tag_descriptor of this EdFiFundDimensionReportingTag.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and reporting_tag_descriptor is None:
            raise ValueError("Invalid value for `reporting_tag_descriptor`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                reporting_tag_descriptor is not None and len(reporting_tag_descriptor) > 306):
            raise ValueError("Invalid value for `reporting_tag_descriptor`, length must be less than or equal to `306`")  # noqa: E501

        self._reporting_tag_descriptor = reporting_tag_descriptor

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
        if issubclass(EdFiFundDimensionReportingTag, dict):
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
        if not isinstance(other, EdFiFundDimensionReportingTag):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EdFiFundDimensionReportingTag):
            return True

        return self.to_dict() != other.to_dict()
