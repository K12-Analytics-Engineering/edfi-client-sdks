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


class EdFiLearningStandardEquivalenceAssociation(object):
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
        'namespace': 'str',
        'source_learning_standard_reference': 'EdFiLearningStandardReference',
        'target_learning_standard_reference': 'EdFiLearningStandardReference',
        'effective_date': 'date',
        'learning_standard_equivalence_strength_description': 'str',
        'learning_standard_equivalence_strength_descriptor': 'str',
        'etag': 'str'
    }

    attribute_map = {
        'id': 'id',
        'namespace': 'namespace',
        'source_learning_standard_reference': 'sourceLearningStandardReference',
        'target_learning_standard_reference': 'targetLearningStandardReference',
        'effective_date': 'effectiveDate',
        'learning_standard_equivalence_strength_description': 'learningStandardEquivalenceStrengthDescription',
        'learning_standard_equivalence_strength_descriptor': 'learningStandardEquivalenceStrengthDescriptor',
        'etag': '_etag'
    }

    def __init__(self, id=None, namespace=None, source_learning_standard_reference=None, target_learning_standard_reference=None, effective_date=None, learning_standard_equivalence_strength_description=None, learning_standard_equivalence_strength_descriptor=None, etag=None, _configuration=None):  # noqa: E501
        """EdFiLearningStandardEquivalenceAssociation - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._namespace = None
        self._source_learning_standard_reference = None
        self._target_learning_standard_reference = None
        self._effective_date = None
        self._learning_standard_equivalence_strength_description = None
        self._learning_standard_equivalence_strength_descriptor = None
        self._etag = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.namespace = namespace
        self.source_learning_standard_reference = source_learning_standard_reference
        self.target_learning_standard_reference = target_learning_standard_reference
        if effective_date is not None:
            self.effective_date = effective_date
        if learning_standard_equivalence_strength_description is not None:
            self.learning_standard_equivalence_strength_description = learning_standard_equivalence_strength_description
        if learning_standard_equivalence_strength_descriptor is not None:
            self.learning_standard_equivalence_strength_descriptor = learning_standard_equivalence_strength_descriptor
        if etag is not None:
            self.etag = etag

    @property
    def id(self):
        """Gets the id of this EdFiLearningStandardEquivalenceAssociation.  # noqa: E501

          # noqa: E501

        :return: The id of this EdFiLearningStandardEquivalenceAssociation.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this EdFiLearningStandardEquivalenceAssociation.

          # noqa: E501

        :param id: The id of this EdFiLearningStandardEquivalenceAssociation.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def namespace(self):
        """Gets the namespace of this EdFiLearningStandardEquivalenceAssociation.  # noqa: E501

        The namespace of the organization that has created and owns the association.  # noqa: E501

        :return: The namespace of this EdFiLearningStandardEquivalenceAssociation.  # noqa: E501
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """Sets the namespace of this EdFiLearningStandardEquivalenceAssociation.

        The namespace of the organization that has created and owns the association.  # noqa: E501

        :param namespace: The namespace of this EdFiLearningStandardEquivalenceAssociation.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and namespace is None:
            raise ValueError("Invalid value for `namespace`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                namespace is not None and len(namespace) > 255):
            raise ValueError("Invalid value for `namespace`, length must be less than or equal to `255`")  # noqa: E501

        self._namespace = namespace

    @property
    def source_learning_standard_reference(self):
        """Gets the source_learning_standard_reference of this EdFiLearningStandardEquivalenceAssociation.  # noqa: E501


        :return: The source_learning_standard_reference of this EdFiLearningStandardEquivalenceAssociation.  # noqa: E501
        :rtype: EdFiLearningStandardReference
        """
        return self._source_learning_standard_reference

    @source_learning_standard_reference.setter
    def source_learning_standard_reference(self, source_learning_standard_reference):
        """Sets the source_learning_standard_reference of this EdFiLearningStandardEquivalenceAssociation.


        :param source_learning_standard_reference: The source_learning_standard_reference of this EdFiLearningStandardEquivalenceAssociation.  # noqa: E501
        :type: EdFiLearningStandardReference
        """
        if self._configuration.client_side_validation and source_learning_standard_reference is None:
            raise ValueError("Invalid value for `source_learning_standard_reference`, must not be `None`")  # noqa: E501

        self._source_learning_standard_reference = source_learning_standard_reference

    @property
    def target_learning_standard_reference(self):
        """Gets the target_learning_standard_reference of this EdFiLearningStandardEquivalenceAssociation.  # noqa: E501


        :return: The target_learning_standard_reference of this EdFiLearningStandardEquivalenceAssociation.  # noqa: E501
        :rtype: EdFiLearningStandardReference
        """
        return self._target_learning_standard_reference

    @target_learning_standard_reference.setter
    def target_learning_standard_reference(self, target_learning_standard_reference):
        """Sets the target_learning_standard_reference of this EdFiLearningStandardEquivalenceAssociation.


        :param target_learning_standard_reference: The target_learning_standard_reference of this EdFiLearningStandardEquivalenceAssociation.  # noqa: E501
        :type: EdFiLearningStandardReference
        """
        if self._configuration.client_side_validation and target_learning_standard_reference is None:
            raise ValueError("Invalid value for `target_learning_standard_reference`, must not be `None`")  # noqa: E501

        self._target_learning_standard_reference = target_learning_standard_reference

    @property
    def effective_date(self):
        """Gets the effective_date of this EdFiLearningStandardEquivalenceAssociation.  # noqa: E501

        The date that the association is considered to be applicable or effective.  # noqa: E501

        :return: The effective_date of this EdFiLearningStandardEquivalenceAssociation.  # noqa: E501
        :rtype: date
        """
        return self._effective_date

    @effective_date.setter
    def effective_date(self, effective_date):
        """Sets the effective_date of this EdFiLearningStandardEquivalenceAssociation.

        The date that the association is considered to be applicable or effective.  # noqa: E501

        :param effective_date: The effective_date of this EdFiLearningStandardEquivalenceAssociation.  # noqa: E501
        :type: date
        """

        self._effective_date = effective_date

    @property
    def learning_standard_equivalence_strength_description(self):
        """Gets the learning_standard_equivalence_strength_description of this EdFiLearningStandardEquivalenceAssociation.  # noqa: E501

        Captures supplemental information on the relationship. Recommended for use only when the match is partial.  # noqa: E501

        :return: The learning_standard_equivalence_strength_description of this EdFiLearningStandardEquivalenceAssociation.  # noqa: E501
        :rtype: str
        """
        return self._learning_standard_equivalence_strength_description

    @learning_standard_equivalence_strength_description.setter
    def learning_standard_equivalence_strength_description(self, learning_standard_equivalence_strength_description):
        """Sets the learning_standard_equivalence_strength_description of this EdFiLearningStandardEquivalenceAssociation.

        Captures supplemental information on the relationship. Recommended for use only when the match is partial.  # noqa: E501

        :param learning_standard_equivalence_strength_description: The learning_standard_equivalence_strength_description of this EdFiLearningStandardEquivalenceAssociation.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                learning_standard_equivalence_strength_description is not None and len(learning_standard_equivalence_strength_description) > 255):
            raise ValueError("Invalid value for `learning_standard_equivalence_strength_description`, length must be less than or equal to `255`")  # noqa: E501

        self._learning_standard_equivalence_strength_description = learning_standard_equivalence_strength_description

    @property
    def learning_standard_equivalence_strength_descriptor(self):
        """Gets the learning_standard_equivalence_strength_descriptor of this EdFiLearningStandardEquivalenceAssociation.  # noqa: E501

        A measure that indicates the strength or quality of the equivalence relationship.  # noqa: E501

        :return: The learning_standard_equivalence_strength_descriptor of this EdFiLearningStandardEquivalenceAssociation.  # noqa: E501
        :rtype: str
        """
        return self._learning_standard_equivalence_strength_descriptor

    @learning_standard_equivalence_strength_descriptor.setter
    def learning_standard_equivalence_strength_descriptor(self, learning_standard_equivalence_strength_descriptor):
        """Sets the learning_standard_equivalence_strength_descriptor of this EdFiLearningStandardEquivalenceAssociation.

        A measure that indicates the strength or quality of the equivalence relationship.  # noqa: E501

        :param learning_standard_equivalence_strength_descriptor: The learning_standard_equivalence_strength_descriptor of this EdFiLearningStandardEquivalenceAssociation.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                learning_standard_equivalence_strength_descriptor is not None and len(learning_standard_equivalence_strength_descriptor) > 306):
            raise ValueError("Invalid value for `learning_standard_equivalence_strength_descriptor`, length must be less than or equal to `306`")  # noqa: E501

        self._learning_standard_equivalence_strength_descriptor = learning_standard_equivalence_strength_descriptor

    @property
    def etag(self):
        """Gets the etag of this EdFiLearningStandardEquivalenceAssociation.  # noqa: E501

        A unique system-generated value that identifies the version of the resource.  # noqa: E501

        :return: The etag of this EdFiLearningStandardEquivalenceAssociation.  # noqa: E501
        :rtype: str
        """
        return self._etag

    @etag.setter
    def etag(self, etag):
        """Sets the etag of this EdFiLearningStandardEquivalenceAssociation.

        A unique system-generated value that identifies the version of the resource.  # noqa: E501

        :param etag: The etag of this EdFiLearningStandardEquivalenceAssociation.  # noqa: E501
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
        if issubclass(EdFiLearningStandardEquivalenceAssociation, dict):
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
        if not isinstance(other, EdFiLearningStandardEquivalenceAssociation):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EdFiLearningStandardEquivalenceAssociation):
            return True

        return self.to_dict() != other.to_dict()
