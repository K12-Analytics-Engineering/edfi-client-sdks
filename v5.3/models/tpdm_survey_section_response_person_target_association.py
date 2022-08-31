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


class TpdmSurveySectionResponsePersonTargetAssociation(object):
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
        'person_reference': 'EdFiPersonReference',
        'survey_section_response_reference': 'EdFiSurveySectionResponseReference',
        'etag': 'str'
    }

    attribute_map = {
        'id': 'id',
        'person_reference': 'personReference',
        'survey_section_response_reference': 'surveySectionResponseReference',
        'etag': '_etag'
    }

    def __init__(self, id=None, person_reference=None, survey_section_response_reference=None, etag=None, _configuration=None):  # noqa: E501
        """TpdmSurveySectionResponsePersonTargetAssociation - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._person_reference = None
        self._survey_section_response_reference = None
        self._etag = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.person_reference = person_reference
        self.survey_section_response_reference = survey_section_response_reference
        if etag is not None:
            self.etag = etag

    @property
    def id(self):
        """Gets the id of this TpdmSurveySectionResponsePersonTargetAssociation.  # noqa: E501

          # noqa: E501

        :return: The id of this TpdmSurveySectionResponsePersonTargetAssociation.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TpdmSurveySectionResponsePersonTargetAssociation.

          # noqa: E501

        :param id: The id of this TpdmSurveySectionResponsePersonTargetAssociation.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def person_reference(self):
        """Gets the person_reference of this TpdmSurveySectionResponsePersonTargetAssociation.  # noqa: E501


        :return: The person_reference of this TpdmSurveySectionResponsePersonTargetAssociation.  # noqa: E501
        :rtype: EdFiPersonReference
        """
        return self._person_reference

    @person_reference.setter
    def person_reference(self, person_reference):
        """Sets the person_reference of this TpdmSurveySectionResponsePersonTargetAssociation.


        :param person_reference: The person_reference of this TpdmSurveySectionResponsePersonTargetAssociation.  # noqa: E501
        :type: EdFiPersonReference
        """
        if self._configuration.client_side_validation and person_reference is None:
            raise ValueError("Invalid value for `person_reference`, must not be `None`")  # noqa: E501

        self._person_reference = person_reference

    @property
    def survey_section_response_reference(self):
        """Gets the survey_section_response_reference of this TpdmSurveySectionResponsePersonTargetAssociation.  # noqa: E501


        :return: The survey_section_response_reference of this TpdmSurveySectionResponsePersonTargetAssociation.  # noqa: E501
        :rtype: EdFiSurveySectionResponseReference
        """
        return self._survey_section_response_reference

    @survey_section_response_reference.setter
    def survey_section_response_reference(self, survey_section_response_reference):
        """Sets the survey_section_response_reference of this TpdmSurveySectionResponsePersonTargetAssociation.


        :param survey_section_response_reference: The survey_section_response_reference of this TpdmSurveySectionResponsePersonTargetAssociation.  # noqa: E501
        :type: EdFiSurveySectionResponseReference
        """
        if self._configuration.client_side_validation and survey_section_response_reference is None:
            raise ValueError("Invalid value for `survey_section_response_reference`, must not be `None`")  # noqa: E501

        self._survey_section_response_reference = survey_section_response_reference

    @property
    def etag(self):
        """Gets the etag of this TpdmSurveySectionResponsePersonTargetAssociation.  # noqa: E501

        A unique system-generated value that identifies the version of the resource.  # noqa: E501

        :return: The etag of this TpdmSurveySectionResponsePersonTargetAssociation.  # noqa: E501
        :rtype: str
        """
        return self._etag

    @etag.setter
    def etag(self, etag):
        """Sets the etag of this TpdmSurveySectionResponsePersonTargetAssociation.

        A unique system-generated value that identifies the version of the resource.  # noqa: E501

        :param etag: The etag of this TpdmSurveySectionResponsePersonTargetAssociation.  # noqa: E501
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
        if issubclass(TpdmSurveySectionResponsePersonTargetAssociation, dict):
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
        if not isinstance(other, TpdmSurveySectionResponsePersonTargetAssociation):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TpdmSurveySectionResponsePersonTargetAssociation):
            return True

        return self.to_dict() != other.to_dict()
