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


class EdFiStudentParentAssociation(object):
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
        'parent_reference': 'EdFiParentReference',
        'student_reference': 'EdFiStudentReference',
        'contact_priority': 'int',
        'contact_restrictions': 'str',
        'emergency_contact_status': 'bool',
        'legal_guardian': 'bool',
        'lives_with': 'bool',
        'primary_contact_status': 'bool',
        'relation_descriptor': 'str',
        'etag': 'str'
    }

    attribute_map = {
        'id': 'id',
        'parent_reference': 'parentReference',
        'student_reference': 'studentReference',
        'contact_priority': 'contactPriority',
        'contact_restrictions': 'contactRestrictions',
        'emergency_contact_status': 'emergencyContactStatus',
        'legal_guardian': 'legalGuardian',
        'lives_with': 'livesWith',
        'primary_contact_status': 'primaryContactStatus',
        'relation_descriptor': 'relationDescriptor',
        'etag': '_etag'
    }

    def __init__(self, id=None, parent_reference=None, student_reference=None, contact_priority=None, contact_restrictions=None, emergency_contact_status=None, legal_guardian=None, lives_with=None, primary_contact_status=None, relation_descriptor=None, etag=None, _configuration=None):  # noqa: E501
        """EdFiStudentParentAssociation - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._parent_reference = None
        self._student_reference = None
        self._contact_priority = None
        self._contact_restrictions = None
        self._emergency_contact_status = None
        self._legal_guardian = None
        self._lives_with = None
        self._primary_contact_status = None
        self._relation_descriptor = None
        self._etag = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.parent_reference = parent_reference
        self.student_reference = student_reference
        if contact_priority is not None:
            self.contact_priority = contact_priority
        if contact_restrictions is not None:
            self.contact_restrictions = contact_restrictions
        if emergency_contact_status is not None:
            self.emergency_contact_status = emergency_contact_status
        if legal_guardian is not None:
            self.legal_guardian = legal_guardian
        if lives_with is not None:
            self.lives_with = lives_with
        if primary_contact_status is not None:
            self.primary_contact_status = primary_contact_status
        if relation_descriptor is not None:
            self.relation_descriptor = relation_descriptor
        if etag is not None:
            self.etag = etag

    @property
    def id(self):
        """Gets the id of this EdFiStudentParentAssociation.  # noqa: E501

          # noqa: E501

        :return: The id of this EdFiStudentParentAssociation.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this EdFiStudentParentAssociation.

          # noqa: E501

        :param id: The id of this EdFiStudentParentAssociation.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def parent_reference(self):
        """Gets the parent_reference of this EdFiStudentParentAssociation.  # noqa: E501


        :return: The parent_reference of this EdFiStudentParentAssociation.  # noqa: E501
        :rtype: EdFiParentReference
        """
        return self._parent_reference

    @parent_reference.setter
    def parent_reference(self, parent_reference):
        """Sets the parent_reference of this EdFiStudentParentAssociation.


        :param parent_reference: The parent_reference of this EdFiStudentParentAssociation.  # noqa: E501
        :type: EdFiParentReference
        """
        if self._configuration.client_side_validation and parent_reference is None:
            raise ValueError("Invalid value for `parent_reference`, must not be `None`")  # noqa: E501

        self._parent_reference = parent_reference

    @property
    def student_reference(self):
        """Gets the student_reference of this EdFiStudentParentAssociation.  # noqa: E501


        :return: The student_reference of this EdFiStudentParentAssociation.  # noqa: E501
        :rtype: EdFiStudentReference
        """
        return self._student_reference

    @student_reference.setter
    def student_reference(self, student_reference):
        """Sets the student_reference of this EdFiStudentParentAssociation.


        :param student_reference: The student_reference of this EdFiStudentParentAssociation.  # noqa: E501
        :type: EdFiStudentReference
        """
        if self._configuration.client_side_validation and student_reference is None:
            raise ValueError("Invalid value for `student_reference`, must not be `None`")  # noqa: E501

        self._student_reference = student_reference

    @property
    def contact_priority(self):
        """Gets the contact_priority of this EdFiStudentParentAssociation.  # noqa: E501

        The numeric order of the preferred sequence or priority of contact.  # noqa: E501

        :return: The contact_priority of this EdFiStudentParentAssociation.  # noqa: E501
        :rtype: int
        """
        return self._contact_priority

    @contact_priority.setter
    def contact_priority(self, contact_priority):
        """Sets the contact_priority of this EdFiStudentParentAssociation.

        The numeric order of the preferred sequence or priority of contact.  # noqa: E501

        :param contact_priority: The contact_priority of this EdFiStudentParentAssociation.  # noqa: E501
        :type: int
        """

        self._contact_priority = contact_priority

    @property
    def contact_restrictions(self):
        """Gets the contact_restrictions of this EdFiStudentParentAssociation.  # noqa: E501

        Restrictions for student and/or teacher contact with the individual (e.g., the student may not be picked up by the individual).  # noqa: E501

        :return: The contact_restrictions of this EdFiStudentParentAssociation.  # noqa: E501
        :rtype: str
        """
        return self._contact_restrictions

    @contact_restrictions.setter
    def contact_restrictions(self, contact_restrictions):
        """Sets the contact_restrictions of this EdFiStudentParentAssociation.

        Restrictions for student and/or teacher contact with the individual (e.g., the student may not be picked up by the individual).  # noqa: E501

        :param contact_restrictions: The contact_restrictions of this EdFiStudentParentAssociation.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                contact_restrictions is not None and len(contact_restrictions) > 250):
            raise ValueError("Invalid value for `contact_restrictions`, length must be less than or equal to `250`")  # noqa: E501

        self._contact_restrictions = contact_restrictions

    @property
    def emergency_contact_status(self):
        """Gets the emergency_contact_status of this EdFiStudentParentAssociation.  # noqa: E501

        Indicator of whether the person is a designated emergency contact for the student.  # noqa: E501

        :return: The emergency_contact_status of this EdFiStudentParentAssociation.  # noqa: E501
        :rtype: bool
        """
        return self._emergency_contact_status

    @emergency_contact_status.setter
    def emergency_contact_status(self, emergency_contact_status):
        """Sets the emergency_contact_status of this EdFiStudentParentAssociation.

        Indicator of whether the person is a designated emergency contact for the student.  # noqa: E501

        :param emergency_contact_status: The emergency_contact_status of this EdFiStudentParentAssociation.  # noqa: E501
        :type: bool
        """

        self._emergency_contact_status = emergency_contact_status

    @property
    def legal_guardian(self):
        """Gets the legal_guardian of this EdFiStudentParentAssociation.  # noqa: E501

        Indicator of whether the person is a legal guardian for the student.  # noqa: E501

        :return: The legal_guardian of this EdFiStudentParentAssociation.  # noqa: E501
        :rtype: bool
        """
        return self._legal_guardian

    @legal_guardian.setter
    def legal_guardian(self, legal_guardian):
        """Sets the legal_guardian of this EdFiStudentParentAssociation.

        Indicator of whether the person is a legal guardian for the student.  # noqa: E501

        :param legal_guardian: The legal_guardian of this EdFiStudentParentAssociation.  # noqa: E501
        :type: bool
        """

        self._legal_guardian = legal_guardian

    @property
    def lives_with(self):
        """Gets the lives_with of this EdFiStudentParentAssociation.  # noqa: E501

        Indicator of whether the student lives with the associated parent.  # noqa: E501

        :return: The lives_with of this EdFiStudentParentAssociation.  # noqa: E501
        :rtype: bool
        """
        return self._lives_with

    @lives_with.setter
    def lives_with(self, lives_with):
        """Sets the lives_with of this EdFiStudentParentAssociation.

        Indicator of whether the student lives with the associated parent.  # noqa: E501

        :param lives_with: The lives_with of this EdFiStudentParentAssociation.  # noqa: E501
        :type: bool
        """

        self._lives_with = lives_with

    @property
    def primary_contact_status(self):
        """Gets the primary_contact_status of this EdFiStudentParentAssociation.  # noqa: E501

        Indicator of whether the person is a primary parental contact for the student.  # noqa: E501

        :return: The primary_contact_status of this EdFiStudentParentAssociation.  # noqa: E501
        :rtype: bool
        """
        return self._primary_contact_status

    @primary_contact_status.setter
    def primary_contact_status(self, primary_contact_status):
        """Sets the primary_contact_status of this EdFiStudentParentAssociation.

        Indicator of whether the person is a primary parental contact for the student.  # noqa: E501

        :param primary_contact_status: The primary_contact_status of this EdFiStudentParentAssociation.  # noqa: E501
        :type: bool
        """

        self._primary_contact_status = primary_contact_status

    @property
    def relation_descriptor(self):
        """Gets the relation_descriptor of this EdFiStudentParentAssociation.  # noqa: E501

        The nature of an individual's relationship to a student, primarily used to capture family relationships.  # noqa: E501

        :return: The relation_descriptor of this EdFiStudentParentAssociation.  # noqa: E501
        :rtype: str
        """
        return self._relation_descriptor

    @relation_descriptor.setter
    def relation_descriptor(self, relation_descriptor):
        """Sets the relation_descriptor of this EdFiStudentParentAssociation.

        The nature of an individual's relationship to a student, primarily used to capture family relationships.  # noqa: E501

        :param relation_descriptor: The relation_descriptor of this EdFiStudentParentAssociation.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                relation_descriptor is not None and len(relation_descriptor) > 306):
            raise ValueError("Invalid value for `relation_descriptor`, length must be less than or equal to `306`")  # noqa: E501

        self._relation_descriptor = relation_descriptor

    @property
    def etag(self):
        """Gets the etag of this EdFiStudentParentAssociation.  # noqa: E501

        A unique system-generated value that identifies the version of the resource.  # noqa: E501

        :return: The etag of this EdFiStudentParentAssociation.  # noqa: E501
        :rtype: str
        """
        return self._etag

    @etag.setter
    def etag(self, etag):
        """Sets the etag of this EdFiStudentParentAssociation.

        A unique system-generated value that identifies the version of the resource.  # noqa: E501

        :param etag: The etag of this EdFiStudentParentAssociation.  # noqa: E501
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
        if issubclass(EdFiStudentParentAssociation, dict):
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
        if not isinstance(other, EdFiStudentParentAssociation):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EdFiStudentParentAssociation):
            return True

        return self.to_dict() != other.to_dict()
