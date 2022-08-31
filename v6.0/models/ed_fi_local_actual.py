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


class EdFiLocalActual(object):
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
        'as_of_date': 'date',
        'local_account_reference': 'EdFiLocalAccountReference',
        'amount': 'float',
        'financial_collection_descriptor': 'str',
        'etag': 'str'
    }

    attribute_map = {
        'id': 'id',
        'as_of_date': 'asOfDate',
        'local_account_reference': 'localAccountReference',
        'amount': 'amount',
        'financial_collection_descriptor': 'financialCollectionDescriptor',
        'etag': '_etag'
    }

    def __init__(self, id=None, as_of_date=None, local_account_reference=None, amount=None, financial_collection_descriptor=None, etag=None, _configuration=None):  # noqa: E501
        """EdFiLocalActual - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._as_of_date = None
        self._local_account_reference = None
        self._amount = None
        self._financial_collection_descriptor = None
        self._etag = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.as_of_date = as_of_date
        self.local_account_reference = local_account_reference
        self.amount = amount
        if financial_collection_descriptor is not None:
            self.financial_collection_descriptor = financial_collection_descriptor
        if etag is not None:
            self.etag = etag

    @property
    def id(self):
        """Gets the id of this EdFiLocalActual.  # noqa: E501

          # noqa: E501

        :return: The id of this EdFiLocalActual.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this EdFiLocalActual.

          # noqa: E501

        :param id: The id of this EdFiLocalActual.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def as_of_date(self):
        """Gets the as_of_date of this EdFiLocalActual.  # noqa: E501

        The date of the reported amount for the account.  # noqa: E501

        :return: The as_of_date of this EdFiLocalActual.  # noqa: E501
        :rtype: date
        """
        return self._as_of_date

    @as_of_date.setter
    def as_of_date(self, as_of_date):
        """Sets the as_of_date of this EdFiLocalActual.

        The date of the reported amount for the account.  # noqa: E501

        :param as_of_date: The as_of_date of this EdFiLocalActual.  # noqa: E501
        :type: date
        """
        if self._configuration.client_side_validation and as_of_date is None:
            raise ValueError("Invalid value for `as_of_date`, must not be `None`")  # noqa: E501

        self._as_of_date = as_of_date

    @property
    def local_account_reference(self):
        """Gets the local_account_reference of this EdFiLocalActual.  # noqa: E501


        :return: The local_account_reference of this EdFiLocalActual.  # noqa: E501
        :rtype: EdFiLocalAccountReference
        """
        return self._local_account_reference

    @local_account_reference.setter
    def local_account_reference(self, local_account_reference):
        """Sets the local_account_reference of this EdFiLocalActual.


        :param local_account_reference: The local_account_reference of this EdFiLocalActual.  # noqa: E501
        :type: EdFiLocalAccountReference
        """
        if self._configuration.client_side_validation and local_account_reference is None:
            raise ValueError("Invalid value for `local_account_reference`, must not be `None`")  # noqa: E501

        self._local_account_reference = local_account_reference

    @property
    def amount(self):
        """Gets the amount of this EdFiLocalActual.  # noqa: E501

        Current balance for the account.  # noqa: E501

        :return: The amount of this EdFiLocalActual.  # noqa: E501
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this EdFiLocalActual.

        Current balance for the account.  # noqa: E501

        :param amount: The amount of this EdFiLocalActual.  # noqa: E501
        :type: float
        """
        if self._configuration.client_side_validation and amount is None:
            raise ValueError("Invalid value for `amount`, must not be `None`")  # noqa: E501

        self._amount = amount

    @property
    def financial_collection_descriptor(self):
        """Gets the financial_collection_descriptor of this EdFiLocalActual.  # noqa: E501

        The accounting period or grouping for which the amount is collected.  # noqa: E501

        :return: The financial_collection_descriptor of this EdFiLocalActual.  # noqa: E501
        :rtype: str
        """
        return self._financial_collection_descriptor

    @financial_collection_descriptor.setter
    def financial_collection_descriptor(self, financial_collection_descriptor):
        """Sets the financial_collection_descriptor of this EdFiLocalActual.

        The accounting period or grouping for which the amount is collected.  # noqa: E501

        :param financial_collection_descriptor: The financial_collection_descriptor of this EdFiLocalActual.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                financial_collection_descriptor is not None and len(financial_collection_descriptor) > 306):
            raise ValueError("Invalid value for `financial_collection_descriptor`, length must be less than or equal to `306`")  # noqa: E501

        self._financial_collection_descriptor = financial_collection_descriptor

    @property
    def etag(self):
        """Gets the etag of this EdFiLocalActual.  # noqa: E501

        A unique system-generated value that identifies the version of the resource.  # noqa: E501

        :return: The etag of this EdFiLocalActual.  # noqa: E501
        :rtype: str
        """
        return self._etag

    @etag.setter
    def etag(self, etag):
        """Sets the etag of this EdFiLocalActual.

        A unique system-generated value that identifies the version of the resource.  # noqa: E501

        :param etag: The etag of this EdFiLocalActual.  # noqa: E501
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
        if issubclass(EdFiLocalActual, dict):
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
        if not isinstance(other, EdFiLocalActual):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EdFiLocalActual):
            return True

        return self.to_dict() != other.to_dict()