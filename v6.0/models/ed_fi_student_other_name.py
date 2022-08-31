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


class EdFiStudentOtherName(object):
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
        'other_name_type_descriptor': 'str',
        'first_name': 'str',
        'generation_code_suffix': 'str',
        'last_surname': 'str',
        'middle_name': 'str',
        'personal_title_prefix': 'str'
    }

    attribute_map = {
        'other_name_type_descriptor': 'otherNameTypeDescriptor',
        'first_name': 'firstName',
        'generation_code_suffix': 'generationCodeSuffix',
        'last_surname': 'lastSurname',
        'middle_name': 'middleName',
        'personal_title_prefix': 'personalTitlePrefix'
    }

    def __init__(self, other_name_type_descriptor=None, first_name=None, generation_code_suffix=None, last_surname=None, middle_name=None, personal_title_prefix=None, _configuration=None):  # noqa: E501
        """EdFiStudentOtherName - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._other_name_type_descriptor = None
        self._first_name = None
        self._generation_code_suffix = None
        self._last_surname = None
        self._middle_name = None
        self._personal_title_prefix = None
        self.discriminator = None

        self.other_name_type_descriptor = other_name_type_descriptor
        self.first_name = first_name
        if generation_code_suffix is not None:
            self.generation_code_suffix = generation_code_suffix
        self.last_surname = last_surname
        if middle_name is not None:
            self.middle_name = middle_name
        if personal_title_prefix is not None:
            self.personal_title_prefix = personal_title_prefix

    @property
    def other_name_type_descriptor(self):
        """Gets the other_name_type_descriptor of this EdFiStudentOtherName.  # noqa: E501

        The types of alternate names for an individual.  # noqa: E501

        :return: The other_name_type_descriptor of this EdFiStudentOtherName.  # noqa: E501
        :rtype: str
        """
        return self._other_name_type_descriptor

    @other_name_type_descriptor.setter
    def other_name_type_descriptor(self, other_name_type_descriptor):
        """Sets the other_name_type_descriptor of this EdFiStudentOtherName.

        The types of alternate names for an individual.  # noqa: E501

        :param other_name_type_descriptor: The other_name_type_descriptor of this EdFiStudentOtherName.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and other_name_type_descriptor is None:
            raise ValueError("Invalid value for `other_name_type_descriptor`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                other_name_type_descriptor is not None and len(other_name_type_descriptor) > 306):
            raise ValueError("Invalid value for `other_name_type_descriptor`, length must be less than or equal to `306`")  # noqa: E501

        self._other_name_type_descriptor = other_name_type_descriptor

    @property
    def first_name(self):
        """Gets the first_name of this EdFiStudentOtherName.  # noqa: E501

        A name given to an individual at birth, baptism, or during another naming ceremony, or through legal change.  # noqa: E501

        :return: The first_name of this EdFiStudentOtherName.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this EdFiStudentOtherName.

        A name given to an individual at birth, baptism, or during another naming ceremony, or through legal change.  # noqa: E501

        :param first_name: The first_name of this EdFiStudentOtherName.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and first_name is None:
            raise ValueError("Invalid value for `first_name`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                first_name is not None and len(first_name) > 75):
            raise ValueError("Invalid value for `first_name`, length must be less than or equal to `75`")  # noqa: E501

        self._first_name = first_name

    @property
    def generation_code_suffix(self):
        """Gets the generation_code_suffix of this EdFiStudentOtherName.  # noqa: E501

        An appendage, if any, used to denote an individual's generation in his family (e.g., Jr., Sr., III).  # noqa: E501

        :return: The generation_code_suffix of this EdFiStudentOtherName.  # noqa: E501
        :rtype: str
        """
        return self._generation_code_suffix

    @generation_code_suffix.setter
    def generation_code_suffix(self, generation_code_suffix):
        """Sets the generation_code_suffix of this EdFiStudentOtherName.

        An appendage, if any, used to denote an individual's generation in his family (e.g., Jr., Sr., III).  # noqa: E501

        :param generation_code_suffix: The generation_code_suffix of this EdFiStudentOtherName.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                generation_code_suffix is not None and len(generation_code_suffix) > 10):
            raise ValueError("Invalid value for `generation_code_suffix`, length must be less than or equal to `10`")  # noqa: E501

        self._generation_code_suffix = generation_code_suffix

    @property
    def last_surname(self):
        """Gets the last_surname of this EdFiStudentOtherName.  # noqa: E501

        The name borne in common by members of a family.  # noqa: E501

        :return: The last_surname of this EdFiStudentOtherName.  # noqa: E501
        :rtype: str
        """
        return self._last_surname

    @last_surname.setter
    def last_surname(self, last_surname):
        """Sets the last_surname of this EdFiStudentOtherName.

        The name borne in common by members of a family.  # noqa: E501

        :param last_surname: The last_surname of this EdFiStudentOtherName.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and last_surname is None:
            raise ValueError("Invalid value for `last_surname`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                last_surname is not None and len(last_surname) > 75):
            raise ValueError("Invalid value for `last_surname`, length must be less than or equal to `75`")  # noqa: E501

        self._last_surname = last_surname

    @property
    def middle_name(self):
        """Gets the middle_name of this EdFiStudentOtherName.  # noqa: E501

        A secondary name given to an individual at birth, baptism, or during another naming ceremony.  # noqa: E501

        :return: The middle_name of this EdFiStudentOtherName.  # noqa: E501
        :rtype: str
        """
        return self._middle_name

    @middle_name.setter
    def middle_name(self, middle_name):
        """Sets the middle_name of this EdFiStudentOtherName.

        A secondary name given to an individual at birth, baptism, or during another naming ceremony.  # noqa: E501

        :param middle_name: The middle_name of this EdFiStudentOtherName.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                middle_name is not None and len(middle_name) > 75):
            raise ValueError("Invalid value for `middle_name`, length must be less than or equal to `75`")  # noqa: E501

        self._middle_name = middle_name

    @property
    def personal_title_prefix(self):
        """Gets the personal_title_prefix of this EdFiStudentOtherName.  # noqa: E501

        A prefix used to denote the title, degree, position, or seniority of the individual.  # noqa: E501

        :return: The personal_title_prefix of this EdFiStudentOtherName.  # noqa: E501
        :rtype: str
        """
        return self._personal_title_prefix

    @personal_title_prefix.setter
    def personal_title_prefix(self, personal_title_prefix):
        """Sets the personal_title_prefix of this EdFiStudentOtherName.

        A prefix used to denote the title, degree, position, or seniority of the individual.  # noqa: E501

        :param personal_title_prefix: The personal_title_prefix of this EdFiStudentOtherName.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                personal_title_prefix is not None and len(personal_title_prefix) > 30):
            raise ValueError("Invalid value for `personal_title_prefix`, length must be less than or equal to `30`")  # noqa: E501

        self._personal_title_prefix = personal_title_prefix

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
        if issubclass(EdFiStudentOtherName, dict):
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
        if not isinstance(other, EdFiStudentOtherName):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EdFiStudentOtherName):
            return True

        return self.to_dict() != other.to_dict()
