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


class EdFiProgramDimensionReference(object):
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
        'code': 'str',
        'fiscal_year': 'int',
        'link': 'Link'
    }

    attribute_map = {
        'code': 'code',
        'fiscal_year': 'fiscalYear',
        'link': 'link'
    }

    def __init__(self, code=None, fiscal_year=None, link=None, _configuration=None):  # noqa: E501
        """EdFiProgramDimensionReference - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._code = None
        self._fiscal_year = None
        self._link = None
        self.discriminator = None

        self.code = code
        self.fiscal_year = fiscal_year
        if link is not None:
            self.link = link

    @property
    def code(self):
        """Gets the code of this EdFiProgramDimensionReference.  # noqa: E501

        The code representation of the account program dimension.  # noqa: E501

        :return: The code of this EdFiProgramDimensionReference.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this EdFiProgramDimensionReference.

        The code representation of the account program dimension.  # noqa: E501

        :param code: The code of this EdFiProgramDimensionReference.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and code is None:
            raise ValueError("Invalid value for `code`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                code is not None and len(code) > 16):
            raise ValueError("Invalid value for `code`, length must be less than or equal to `16`")  # noqa: E501

        self._code = code

    @property
    def fiscal_year(self):
        """Gets the fiscal_year of this EdFiProgramDimensionReference.  # noqa: E501

        The fiscal year for which the account program dimension is valid.  # noqa: E501

        :return: The fiscal_year of this EdFiProgramDimensionReference.  # noqa: E501
        :rtype: int
        """
        return self._fiscal_year

    @fiscal_year.setter
    def fiscal_year(self, fiscal_year):
        """Sets the fiscal_year of this EdFiProgramDimensionReference.

        The fiscal year for which the account program dimension is valid.  # noqa: E501

        :param fiscal_year: The fiscal_year of this EdFiProgramDimensionReference.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and fiscal_year is None:
            raise ValueError("Invalid value for `fiscal_year`, must not be `None`")  # noqa: E501

        self._fiscal_year = fiscal_year

    @property
    def link(self):
        """Gets the link of this EdFiProgramDimensionReference.  # noqa: E501


        :return: The link of this EdFiProgramDimensionReference.  # noqa: E501
        :rtype: Link
        """
        return self._link

    @link.setter
    def link(self, link):
        """Sets the link of this EdFiProgramDimensionReference.


        :param link: The link of this EdFiProgramDimensionReference.  # noqa: E501
        :type: Link
        """

        self._link = link

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
        if issubclass(EdFiProgramDimensionReference, dict):
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
        if not isinstance(other, EdFiProgramDimensionReference):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EdFiProgramDimensionReference):
            return True

        return self.to_dict() != other.to_dict()
