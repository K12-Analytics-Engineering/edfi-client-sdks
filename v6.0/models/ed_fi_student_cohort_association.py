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


class EdFiStudentCohortAssociation(object):
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
        'begin_date': 'date',
        'cohort_reference': 'EdFiCohortReference',
        'student_reference': 'EdFiStudentReference',
        'end_date': 'date',
        'sections': 'list[EdFiStudentCohortAssociationSection]',
        'etag': 'str'
    }

    attribute_map = {
        'id': 'id',
        'begin_date': 'beginDate',
        'cohort_reference': 'cohortReference',
        'student_reference': 'studentReference',
        'end_date': 'endDate',
        'sections': 'sections',
        'etag': '_etag'
    }

    def __init__(self, id=None, begin_date=None, cohort_reference=None, student_reference=None, end_date=None, sections=None, etag=None, _configuration=None):  # noqa: E501
        """EdFiStudentCohortAssociation - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._begin_date = None
        self._cohort_reference = None
        self._student_reference = None
        self._end_date = None
        self._sections = None
        self._etag = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.begin_date = begin_date
        self.cohort_reference = cohort_reference
        self.student_reference = student_reference
        if end_date is not None:
            self.end_date = end_date
        if sections is not None:
            self.sections = sections
        if etag is not None:
            self.etag = etag

    @property
    def id(self):
        """Gets the id of this EdFiStudentCohortAssociation.  # noqa: E501

          # noqa: E501

        :return: The id of this EdFiStudentCohortAssociation.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this EdFiStudentCohortAssociation.

          # noqa: E501

        :param id: The id of this EdFiStudentCohortAssociation.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def begin_date(self):
        """Gets the begin_date of this EdFiStudentCohortAssociation.  # noqa: E501

        The month, day, and year on which the student was first identified as part of the cohort.  # noqa: E501

        :return: The begin_date of this EdFiStudentCohortAssociation.  # noqa: E501
        :rtype: date
        """
        return self._begin_date

    @begin_date.setter
    def begin_date(self, begin_date):
        """Sets the begin_date of this EdFiStudentCohortAssociation.

        The month, day, and year on which the student was first identified as part of the cohort.  # noqa: E501

        :param begin_date: The begin_date of this EdFiStudentCohortAssociation.  # noqa: E501
        :type: date
        """
        if self._configuration.client_side_validation and begin_date is None:
            raise ValueError("Invalid value for `begin_date`, must not be `None`")  # noqa: E501

        self._begin_date = begin_date

    @property
    def cohort_reference(self):
        """Gets the cohort_reference of this EdFiStudentCohortAssociation.  # noqa: E501


        :return: The cohort_reference of this EdFiStudentCohortAssociation.  # noqa: E501
        :rtype: EdFiCohortReference
        """
        return self._cohort_reference

    @cohort_reference.setter
    def cohort_reference(self, cohort_reference):
        """Sets the cohort_reference of this EdFiStudentCohortAssociation.


        :param cohort_reference: The cohort_reference of this EdFiStudentCohortAssociation.  # noqa: E501
        :type: EdFiCohortReference
        """
        if self._configuration.client_side_validation and cohort_reference is None:
            raise ValueError("Invalid value for `cohort_reference`, must not be `None`")  # noqa: E501

        self._cohort_reference = cohort_reference

    @property
    def student_reference(self):
        """Gets the student_reference of this EdFiStudentCohortAssociation.  # noqa: E501


        :return: The student_reference of this EdFiStudentCohortAssociation.  # noqa: E501
        :rtype: EdFiStudentReference
        """
        return self._student_reference

    @student_reference.setter
    def student_reference(self, student_reference):
        """Sets the student_reference of this EdFiStudentCohortAssociation.


        :param student_reference: The student_reference of this EdFiStudentCohortAssociation.  # noqa: E501
        :type: EdFiStudentReference
        """
        if self._configuration.client_side_validation and student_reference is None:
            raise ValueError("Invalid value for `student_reference`, must not be `None`")  # noqa: E501

        self._student_reference = student_reference

    @property
    def end_date(self):
        """Gets the end_date of this EdFiStudentCohortAssociation.  # noqa: E501

        The month, day, and year on which the student was removed as part of the cohort.  # noqa: E501

        :return: The end_date of this EdFiStudentCohortAssociation.  # noqa: E501
        :rtype: date
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this EdFiStudentCohortAssociation.

        The month, day, and year on which the student was removed as part of the cohort.  # noqa: E501

        :param end_date: The end_date of this EdFiStudentCohortAssociation.  # noqa: E501
        :type: date
        """

        self._end_date = end_date

    @property
    def sections(self):
        """Gets the sections of this EdFiStudentCohortAssociation.  # noqa: E501

        An unordered collection of studentCohortAssociationSections. The cohort representing the subdivision of students within one or more sections. For example, a group of students may be given additional instruction and tracked as a cohort.  # noqa: E501

        :return: The sections of this EdFiStudentCohortAssociation.  # noqa: E501
        :rtype: list[EdFiStudentCohortAssociationSection]
        """
        return self._sections

    @sections.setter
    def sections(self, sections):
        """Sets the sections of this EdFiStudentCohortAssociation.

        An unordered collection of studentCohortAssociationSections. The cohort representing the subdivision of students within one or more sections. For example, a group of students may be given additional instruction and tracked as a cohort.  # noqa: E501

        :param sections: The sections of this EdFiStudentCohortAssociation.  # noqa: E501
        :type: list[EdFiStudentCohortAssociationSection]
        """

        self._sections = sections

    @property
    def etag(self):
        """Gets the etag of this EdFiStudentCohortAssociation.  # noqa: E501

        A unique system-generated value that identifies the version of the resource.  # noqa: E501

        :return: The etag of this EdFiStudentCohortAssociation.  # noqa: E501
        :rtype: str
        """
        return self._etag

    @etag.setter
    def etag(self, etag):
        """Sets the etag of this EdFiStudentCohortAssociation.

        A unique system-generated value that identifies the version of the resource.  # noqa: E501

        :param etag: The etag of this EdFiStudentCohortAssociation.  # noqa: E501
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
        if issubclass(EdFiStudentCohortAssociation, dict):
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
        if not isinstance(other, EdFiStudentCohortAssociation):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EdFiStudentCohortAssociation):
            return True

        return self.to_dict() != other.to_dict()