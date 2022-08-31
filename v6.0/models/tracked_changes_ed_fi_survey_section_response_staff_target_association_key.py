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


class TrackedChangesEdFiSurveySectionResponseStaffTargetAssociationKey(object):
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
        'staff_unique_id': 'str',
        'namespace': 'str',
        'survey_identifier': 'str',
        'survey_response_identifier': 'str',
        'survey_section_title': 'str'
    }

    attribute_map = {
        'staff_unique_id': 'staffUniqueId',
        'namespace': 'namespace',
        'survey_identifier': 'surveyIdentifier',
        'survey_response_identifier': 'surveyResponseIdentifier',
        'survey_section_title': 'surveySectionTitle'
    }

    def __init__(self, staff_unique_id=None, namespace=None, survey_identifier=None, survey_response_identifier=None, survey_section_title=None, _configuration=None):  # noqa: E501
        """TrackedChangesEdFiSurveySectionResponseStaffTargetAssociationKey - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._staff_unique_id = None
        self._namespace = None
        self._survey_identifier = None
        self._survey_response_identifier = None
        self._survey_section_title = None
        self.discriminator = None

        if staff_unique_id is not None:
            self.staff_unique_id = staff_unique_id
        if namespace is not None:
            self.namespace = namespace
        if survey_identifier is not None:
            self.survey_identifier = survey_identifier
        if survey_response_identifier is not None:
            self.survey_response_identifier = survey_response_identifier
        if survey_section_title is not None:
            self.survey_section_title = survey_section_title

    @property
    def staff_unique_id(self):
        """Gets the staff_unique_id of this TrackedChangesEdFiSurveySectionResponseStaffTargetAssociationKey.  # noqa: E501

        A unique alphanumeric code assigned to a staff.  # noqa: E501

        :return: The staff_unique_id of this TrackedChangesEdFiSurveySectionResponseStaffTargetAssociationKey.  # noqa: E501
        :rtype: str
        """
        return self._staff_unique_id

    @staff_unique_id.setter
    def staff_unique_id(self, staff_unique_id):
        """Sets the staff_unique_id of this TrackedChangesEdFiSurveySectionResponseStaffTargetAssociationKey.

        A unique alphanumeric code assigned to a staff.  # noqa: E501

        :param staff_unique_id: The staff_unique_id of this TrackedChangesEdFiSurveySectionResponseStaffTargetAssociationKey.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                staff_unique_id is not None and len(staff_unique_id) > 32):
            raise ValueError("Invalid value for `staff_unique_id`, length must be less than or equal to `32`")  # noqa: E501

        self._staff_unique_id = staff_unique_id

    @property
    def namespace(self):
        """Gets the namespace of this TrackedChangesEdFiSurveySectionResponseStaffTargetAssociationKey.  # noqa: E501

        Namespace for the survey.  # noqa: E501

        :return: The namespace of this TrackedChangesEdFiSurveySectionResponseStaffTargetAssociationKey.  # noqa: E501
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """Sets the namespace of this TrackedChangesEdFiSurveySectionResponseStaffTargetAssociationKey.

        Namespace for the survey.  # noqa: E501

        :param namespace: The namespace of this TrackedChangesEdFiSurveySectionResponseStaffTargetAssociationKey.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                namespace is not None and len(namespace) > 255):
            raise ValueError("Invalid value for `namespace`, length must be less than or equal to `255`")  # noqa: E501

        self._namespace = namespace

    @property
    def survey_identifier(self):
        """Gets the survey_identifier of this TrackedChangesEdFiSurveySectionResponseStaffTargetAssociationKey.  # noqa: E501

        The unique survey identifier from the survey tool.  # noqa: E501

        :return: The survey_identifier of this TrackedChangesEdFiSurveySectionResponseStaffTargetAssociationKey.  # noqa: E501
        :rtype: str
        """
        return self._survey_identifier

    @survey_identifier.setter
    def survey_identifier(self, survey_identifier):
        """Sets the survey_identifier of this TrackedChangesEdFiSurveySectionResponseStaffTargetAssociationKey.

        The unique survey identifier from the survey tool.  # noqa: E501

        :param survey_identifier: The survey_identifier of this TrackedChangesEdFiSurveySectionResponseStaffTargetAssociationKey.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                survey_identifier is not None and len(survey_identifier) > 60):
            raise ValueError("Invalid value for `survey_identifier`, length must be less than or equal to `60`")  # noqa: E501

        self._survey_identifier = survey_identifier

    @property
    def survey_response_identifier(self):
        """Gets the survey_response_identifier of this TrackedChangesEdFiSurveySectionResponseStaffTargetAssociationKey.  # noqa: E501

        The identifier of the survey typically from the survey application.  # noqa: E501

        :return: The survey_response_identifier of this TrackedChangesEdFiSurveySectionResponseStaffTargetAssociationKey.  # noqa: E501
        :rtype: str
        """
        return self._survey_response_identifier

    @survey_response_identifier.setter
    def survey_response_identifier(self, survey_response_identifier):
        """Sets the survey_response_identifier of this TrackedChangesEdFiSurveySectionResponseStaffTargetAssociationKey.

        The identifier of the survey typically from the survey application.  # noqa: E501

        :param survey_response_identifier: The survey_response_identifier of this TrackedChangesEdFiSurveySectionResponseStaffTargetAssociationKey.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                survey_response_identifier is not None and len(survey_response_identifier) > 60):
            raise ValueError("Invalid value for `survey_response_identifier`, length must be less than or equal to `60`")  # noqa: E501

        self._survey_response_identifier = survey_response_identifier

    @property
    def survey_section_title(self):
        """Gets the survey_section_title of this TrackedChangesEdFiSurveySectionResponseStaffTargetAssociationKey.  # noqa: E501

        The title or label for the survey section.  # noqa: E501

        :return: The survey_section_title of this TrackedChangesEdFiSurveySectionResponseStaffTargetAssociationKey.  # noqa: E501
        :rtype: str
        """
        return self._survey_section_title

    @survey_section_title.setter
    def survey_section_title(self, survey_section_title):
        """Sets the survey_section_title of this TrackedChangesEdFiSurveySectionResponseStaffTargetAssociationKey.

        The title or label for the survey section.  # noqa: E501

        :param survey_section_title: The survey_section_title of this TrackedChangesEdFiSurveySectionResponseStaffTargetAssociationKey.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                survey_section_title is not None and len(survey_section_title) > 255):
            raise ValueError("Invalid value for `survey_section_title`, length must be less than or equal to `255`")  # noqa: E501

        self._survey_section_title = survey_section_title

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
        if issubclass(TrackedChangesEdFiSurveySectionResponseStaffTargetAssociationKey, dict):
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
        if not isinstance(other, TrackedChangesEdFiSurveySectionResponseStaffTargetAssociationKey):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TrackedChangesEdFiSurveySectionResponseStaffTargetAssociationKey):
            return True

        return self.to_dict() != other.to_dict()
