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


class TrackedChangesEdFiAssessmentItemKey(object):
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
        'identification_code': 'str',
        'assessment_identifier': 'str',
        'namespace': 'str'
    }

    attribute_map = {
        'identification_code': 'identificationCode',
        'assessment_identifier': 'assessmentIdentifier',
        'namespace': 'namespace'
    }

    def __init__(self, identification_code=None, assessment_identifier=None, namespace=None, _configuration=None):  # noqa: E501
        """TrackedChangesEdFiAssessmentItemKey - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._identification_code = None
        self._assessment_identifier = None
        self._namespace = None
        self.discriminator = None

        if identification_code is not None:
            self.identification_code = identification_code
        if assessment_identifier is not None:
            self.assessment_identifier = assessment_identifier
        if namespace is not None:
            self.namespace = namespace

    @property
    def identification_code(self):
        """Gets the identification_code of this TrackedChangesEdFiAssessmentItemKey.  # noqa: E501

        A unique number or alphanumeric code assigned to a space, room, site, building, individual, organization, program, or institution by a school, school system, state, or other agency or entity.  # noqa: E501

        :return: The identification_code of this TrackedChangesEdFiAssessmentItemKey.  # noqa: E501
        :rtype: str
        """
        return self._identification_code

    @identification_code.setter
    def identification_code(self, identification_code):
        """Sets the identification_code of this TrackedChangesEdFiAssessmentItemKey.

        A unique number or alphanumeric code assigned to a space, room, site, building, individual, organization, program, or institution by a school, school system, state, or other agency or entity.  # noqa: E501

        :param identification_code: The identification_code of this TrackedChangesEdFiAssessmentItemKey.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                identification_code is not None and len(identification_code) > 60):
            raise ValueError("Invalid value for `identification_code`, length must be less than or equal to `60`")  # noqa: E501

        self._identification_code = identification_code

    @property
    def assessment_identifier(self):
        """Gets the assessment_identifier of this TrackedChangesEdFiAssessmentItemKey.  # noqa: E501

        A unique number or alphanumeric code assigned to an assessment.  # noqa: E501

        :return: The assessment_identifier of this TrackedChangesEdFiAssessmentItemKey.  # noqa: E501
        :rtype: str
        """
        return self._assessment_identifier

    @assessment_identifier.setter
    def assessment_identifier(self, assessment_identifier):
        """Sets the assessment_identifier of this TrackedChangesEdFiAssessmentItemKey.

        A unique number or alphanumeric code assigned to an assessment.  # noqa: E501

        :param assessment_identifier: The assessment_identifier of this TrackedChangesEdFiAssessmentItemKey.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                assessment_identifier is not None and len(assessment_identifier) > 60):
            raise ValueError("Invalid value for `assessment_identifier`, length must be less than or equal to `60`")  # noqa: E501

        self._assessment_identifier = assessment_identifier

    @property
    def namespace(self):
        """Gets the namespace of this TrackedChangesEdFiAssessmentItemKey.  # noqa: E501

        Namespace for the assessment.  # noqa: E501

        :return: The namespace of this TrackedChangesEdFiAssessmentItemKey.  # noqa: E501
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """Sets the namespace of this TrackedChangesEdFiAssessmentItemKey.

        Namespace for the assessment.  # noqa: E501

        :param namespace: The namespace of this TrackedChangesEdFiAssessmentItemKey.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                namespace is not None and len(namespace) > 255):
            raise ValueError("Invalid value for `namespace`, length must be less than or equal to `255`")  # noqa: E501

        self._namespace = namespace

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
        if issubclass(TrackedChangesEdFiAssessmentItemKey, dict):
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
        if not isinstance(other, TrackedChangesEdFiAssessmentItemKey):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TrackedChangesEdFiAssessmentItemKey):
            return True

        return self.to_dict() != other.to_dict()