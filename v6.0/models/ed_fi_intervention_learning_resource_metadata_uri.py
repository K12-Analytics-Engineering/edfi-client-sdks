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


class EdFiInterventionLearningResourceMetadataURI(object):
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
        'learning_resource_metadata_uri': 'str'
    }

    attribute_map = {
        'learning_resource_metadata_uri': 'learningResourceMetadataURI'
    }

    def __init__(self, learning_resource_metadata_uri=None, _configuration=None):  # noqa: E501
        """EdFiInterventionLearningResourceMetadataURI - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._learning_resource_metadata_uri = None
        self.discriminator = None

        self.learning_resource_metadata_uri = learning_resource_metadata_uri

    @property
    def learning_resource_metadata_uri(self):
        """Gets the learning_resource_metadata_uri of this EdFiInterventionLearningResourceMetadataURI.  # noqa: E501

        The URI (typical a URL) pointing to the metadata entry in a LRMI metadata repository, which describes this content item.  # noqa: E501

        :return: The learning_resource_metadata_uri of this EdFiInterventionLearningResourceMetadataURI.  # noqa: E501
        :rtype: str
        """
        return self._learning_resource_metadata_uri

    @learning_resource_metadata_uri.setter
    def learning_resource_metadata_uri(self, learning_resource_metadata_uri):
        """Sets the learning_resource_metadata_uri of this EdFiInterventionLearningResourceMetadataURI.

        The URI (typical a URL) pointing to the metadata entry in a LRMI metadata repository, which describes this content item.  # noqa: E501

        :param learning_resource_metadata_uri: The learning_resource_metadata_uri of this EdFiInterventionLearningResourceMetadataURI.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and learning_resource_metadata_uri is None:
            raise ValueError("Invalid value for `learning_resource_metadata_uri`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                learning_resource_metadata_uri is not None and len(learning_resource_metadata_uri) > 255):
            raise ValueError("Invalid value for `learning_resource_metadata_uri`, length must be less than or equal to `255`")  # noqa: E501

        self._learning_resource_metadata_uri = learning_resource_metadata_uri

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
        if issubclass(EdFiInterventionLearningResourceMetadataURI, dict):
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
        if not isinstance(other, EdFiInterventionLearningResourceMetadataURI):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EdFiInterventionLearningResourceMetadataURI):
            return True

        return self.to_dict() != other.to_dict()
