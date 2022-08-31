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


class TpdmPerformanceEvaluationRatingReviewer(object):
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
        'first_name': 'str',
        'last_surname': 'str',
        'reviewer_person_reference': 'EdFiPersonReference',
        'received_training': 'TpdmPerformanceEvaluationRatingReviewerReceivedTraining'
    }

    attribute_map = {
        'first_name': 'firstName',
        'last_surname': 'lastSurname',
        'reviewer_person_reference': 'reviewerPersonReference',
        'received_training': 'receivedTraining'
    }

    def __init__(self, first_name=None, last_surname=None, reviewer_person_reference=None, received_training=None, _configuration=None):  # noqa: E501
        """TpdmPerformanceEvaluationRatingReviewer - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._first_name = None
        self._last_surname = None
        self._reviewer_person_reference = None
        self._received_training = None
        self.discriminator = None

        self.first_name = first_name
        self.last_surname = last_surname
        if reviewer_person_reference is not None:
            self.reviewer_person_reference = reviewer_person_reference
        if received_training is not None:
            self.received_training = received_training

    @property
    def first_name(self):
        """Gets the first_name of this TpdmPerformanceEvaluationRatingReviewer.  # noqa: E501

        A name given to an individual at birth, baptism, or during another naming ceremony, or through legal change.  # noqa: E501

        :return: The first_name of this TpdmPerformanceEvaluationRatingReviewer.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this TpdmPerformanceEvaluationRatingReviewer.

        A name given to an individual at birth, baptism, or during another naming ceremony, or through legal change.  # noqa: E501

        :param first_name: The first_name of this TpdmPerformanceEvaluationRatingReviewer.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and first_name is None:
            raise ValueError("Invalid value for `first_name`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                first_name is not None and len(first_name) > 75):
            raise ValueError("Invalid value for `first_name`, length must be less than or equal to `75`")  # noqa: E501

        self._first_name = first_name

    @property
    def last_surname(self):
        """Gets the last_surname of this TpdmPerformanceEvaluationRatingReviewer.  # noqa: E501

        The name borne in common by members of a family.  # noqa: E501

        :return: The last_surname of this TpdmPerformanceEvaluationRatingReviewer.  # noqa: E501
        :rtype: str
        """
        return self._last_surname

    @last_surname.setter
    def last_surname(self, last_surname):
        """Sets the last_surname of this TpdmPerformanceEvaluationRatingReviewer.

        The name borne in common by members of a family.  # noqa: E501

        :param last_surname: The last_surname of this TpdmPerformanceEvaluationRatingReviewer.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and last_surname is None:
            raise ValueError("Invalid value for `last_surname`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                last_surname is not None and len(last_surname) > 75):
            raise ValueError("Invalid value for `last_surname`, length must be less than or equal to `75`")  # noqa: E501

        self._last_surname = last_surname

    @property
    def reviewer_person_reference(self):
        """Gets the reviewer_person_reference of this TpdmPerformanceEvaluationRatingReviewer.  # noqa: E501


        :return: The reviewer_person_reference of this TpdmPerformanceEvaluationRatingReviewer.  # noqa: E501
        :rtype: EdFiPersonReference
        """
        return self._reviewer_person_reference

    @reviewer_person_reference.setter
    def reviewer_person_reference(self, reviewer_person_reference):
        """Sets the reviewer_person_reference of this TpdmPerformanceEvaluationRatingReviewer.


        :param reviewer_person_reference: The reviewer_person_reference of this TpdmPerformanceEvaluationRatingReviewer.  # noqa: E501
        :type: EdFiPersonReference
        """

        self._reviewer_person_reference = reviewer_person_reference

    @property
    def received_training(self):
        """Gets the received_training of this TpdmPerformanceEvaluationRatingReviewer.  # noqa: E501


        :return: The received_training of this TpdmPerformanceEvaluationRatingReviewer.  # noqa: E501
        :rtype: TpdmPerformanceEvaluationRatingReviewerReceivedTraining
        """
        return self._received_training

    @received_training.setter
    def received_training(self, received_training):
        """Sets the received_training of this TpdmPerformanceEvaluationRatingReviewer.


        :param received_training: The received_training of this TpdmPerformanceEvaluationRatingReviewer.  # noqa: E501
        :type: TpdmPerformanceEvaluationRatingReviewerReceivedTraining
        """

        self._received_training = received_training

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
        if issubclass(TpdmPerformanceEvaluationRatingReviewer, dict):
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
        if not isinstance(other, TpdmPerformanceEvaluationRatingReviewer):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TpdmPerformanceEvaluationRatingReviewer):
            return True

        return self.to_dict() != other.to_dict()
