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


class TpdmCandidateEducatorPreparationProgramAssociation(object):
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
        'candidate_reference': 'TpdmCandidateReference',
        'educator_preparation_program_reference': 'TpdmEducatorPreparationProgramReference',
        'cohort_years': 'list[TpdmCandidateEducatorPreparationProgramAssociationCohortYear]',
        'degree_specializations': 'list[TpdmCandidateEducatorPreparationProgramAssociationDegreeSpecialization]',
        'end_date': 'date',
        'epp_program_pathway_descriptor': 'str',
        'reason_exited_descriptor': 'str',
        'etag': 'str'
    }

    attribute_map = {
        'id': 'id',
        'begin_date': 'beginDate',
        'candidate_reference': 'candidateReference',
        'educator_preparation_program_reference': 'educatorPreparationProgramReference',
        'cohort_years': 'cohortYears',
        'degree_specializations': 'degreeSpecializations',
        'end_date': 'endDate',
        'epp_program_pathway_descriptor': 'eppProgramPathwayDescriptor',
        'reason_exited_descriptor': 'reasonExitedDescriptor',
        'etag': '_etag'
    }

    def __init__(self, id=None, begin_date=None, candidate_reference=None, educator_preparation_program_reference=None, cohort_years=None, degree_specializations=None, end_date=None, epp_program_pathway_descriptor=None, reason_exited_descriptor=None, etag=None, _configuration=None):  # noqa: E501
        """TpdmCandidateEducatorPreparationProgramAssociation - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._begin_date = None
        self._candidate_reference = None
        self._educator_preparation_program_reference = None
        self._cohort_years = None
        self._degree_specializations = None
        self._end_date = None
        self._epp_program_pathway_descriptor = None
        self._reason_exited_descriptor = None
        self._etag = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.begin_date = begin_date
        self.candidate_reference = candidate_reference
        self.educator_preparation_program_reference = educator_preparation_program_reference
        if cohort_years is not None:
            self.cohort_years = cohort_years
        if degree_specializations is not None:
            self.degree_specializations = degree_specializations
        if end_date is not None:
            self.end_date = end_date
        if epp_program_pathway_descriptor is not None:
            self.epp_program_pathway_descriptor = epp_program_pathway_descriptor
        if reason_exited_descriptor is not None:
            self.reason_exited_descriptor = reason_exited_descriptor
        if etag is not None:
            self.etag = etag

    @property
    def id(self):
        """Gets the id of this TpdmCandidateEducatorPreparationProgramAssociation.  # noqa: E501

          # noqa: E501

        :return: The id of this TpdmCandidateEducatorPreparationProgramAssociation.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TpdmCandidateEducatorPreparationProgramAssociation.

          # noqa: E501

        :param id: The id of this TpdmCandidateEducatorPreparationProgramAssociation.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def begin_date(self):
        """Gets the begin_date of this TpdmCandidateEducatorPreparationProgramAssociation.  # noqa: E501

        The begin date for the association.  # noqa: E501

        :return: The begin_date of this TpdmCandidateEducatorPreparationProgramAssociation.  # noqa: E501
        :rtype: date
        """
        return self._begin_date

    @begin_date.setter
    def begin_date(self, begin_date):
        """Sets the begin_date of this TpdmCandidateEducatorPreparationProgramAssociation.

        The begin date for the association.  # noqa: E501

        :param begin_date: The begin_date of this TpdmCandidateEducatorPreparationProgramAssociation.  # noqa: E501
        :type: date
        """
        if self._configuration.client_side_validation and begin_date is None:
            raise ValueError("Invalid value for `begin_date`, must not be `None`")  # noqa: E501

        self._begin_date = begin_date

    @property
    def candidate_reference(self):
        """Gets the candidate_reference of this TpdmCandidateEducatorPreparationProgramAssociation.  # noqa: E501


        :return: The candidate_reference of this TpdmCandidateEducatorPreparationProgramAssociation.  # noqa: E501
        :rtype: TpdmCandidateReference
        """
        return self._candidate_reference

    @candidate_reference.setter
    def candidate_reference(self, candidate_reference):
        """Sets the candidate_reference of this TpdmCandidateEducatorPreparationProgramAssociation.


        :param candidate_reference: The candidate_reference of this TpdmCandidateEducatorPreparationProgramAssociation.  # noqa: E501
        :type: TpdmCandidateReference
        """
        if self._configuration.client_side_validation and candidate_reference is None:
            raise ValueError("Invalid value for `candidate_reference`, must not be `None`")  # noqa: E501

        self._candidate_reference = candidate_reference

    @property
    def educator_preparation_program_reference(self):
        """Gets the educator_preparation_program_reference of this TpdmCandidateEducatorPreparationProgramAssociation.  # noqa: E501


        :return: The educator_preparation_program_reference of this TpdmCandidateEducatorPreparationProgramAssociation.  # noqa: E501
        :rtype: TpdmEducatorPreparationProgramReference
        """
        return self._educator_preparation_program_reference

    @educator_preparation_program_reference.setter
    def educator_preparation_program_reference(self, educator_preparation_program_reference):
        """Sets the educator_preparation_program_reference of this TpdmCandidateEducatorPreparationProgramAssociation.


        :param educator_preparation_program_reference: The educator_preparation_program_reference of this TpdmCandidateEducatorPreparationProgramAssociation.  # noqa: E501
        :type: TpdmEducatorPreparationProgramReference
        """
        if self._configuration.client_side_validation and educator_preparation_program_reference is None:
            raise ValueError("Invalid value for `educator_preparation_program_reference`, must not be `None`")  # noqa: E501

        self._educator_preparation_program_reference = educator_preparation_program_reference

    @property
    def cohort_years(self):
        """Gets the cohort_years of this TpdmCandidateEducatorPreparationProgramAssociation.  # noqa: E501

        An unordered collection of candidateEducatorPreparationProgramAssociationCohortYears. The type and year of a cohort the student belongs to as determined by the year that student entered a specific grade.  # noqa: E501

        :return: The cohort_years of this TpdmCandidateEducatorPreparationProgramAssociation.  # noqa: E501
        :rtype: list[TpdmCandidateEducatorPreparationProgramAssociationCohortYear]
        """
        return self._cohort_years

    @cohort_years.setter
    def cohort_years(self, cohort_years):
        """Sets the cohort_years of this TpdmCandidateEducatorPreparationProgramAssociation.

        An unordered collection of candidateEducatorPreparationProgramAssociationCohortYears. The type and year of a cohort the student belongs to as determined by the year that student entered a specific grade.  # noqa: E501

        :param cohort_years: The cohort_years of this TpdmCandidateEducatorPreparationProgramAssociation.  # noqa: E501
        :type: list[TpdmCandidateEducatorPreparationProgramAssociationCohortYear]
        """

        self._cohort_years = cohort_years

    @property
    def degree_specializations(self):
        """Gets the degree_specializations of this TpdmCandidateEducatorPreparationProgramAssociation.  # noqa: E501

        An unordered collection of candidateEducatorPreparationProgramAssociationDegreeSpecializations. Information around the area(s) of specialization for an individual.  # noqa: E501

        :return: The degree_specializations of this TpdmCandidateEducatorPreparationProgramAssociation.  # noqa: E501
        :rtype: list[TpdmCandidateEducatorPreparationProgramAssociationDegreeSpecialization]
        """
        return self._degree_specializations

    @degree_specializations.setter
    def degree_specializations(self, degree_specializations):
        """Sets the degree_specializations of this TpdmCandidateEducatorPreparationProgramAssociation.

        An unordered collection of candidateEducatorPreparationProgramAssociationDegreeSpecializations. Information around the area(s) of specialization for an individual.  # noqa: E501

        :param degree_specializations: The degree_specializations of this TpdmCandidateEducatorPreparationProgramAssociation.  # noqa: E501
        :type: list[TpdmCandidateEducatorPreparationProgramAssociationDegreeSpecialization]
        """

        self._degree_specializations = degree_specializations

    @property
    def end_date(self):
        """Gets the end_date of this TpdmCandidateEducatorPreparationProgramAssociation.  # noqa: E501

        The end date for the association.  # noqa: E501

        :return: The end_date of this TpdmCandidateEducatorPreparationProgramAssociation.  # noqa: E501
        :rtype: date
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this TpdmCandidateEducatorPreparationProgramAssociation.

        The end date for the association.  # noqa: E501

        :param end_date: The end_date of this TpdmCandidateEducatorPreparationProgramAssociation.  # noqa: E501
        :type: date
        """

        self._end_date = end_date

    @property
    def epp_program_pathway_descriptor(self):
        """Gets the epp_program_pathway_descriptor of this TpdmCandidateEducatorPreparationProgramAssociation.  # noqa: E501

        The program pathway the candidate is following; for example: Residency, Internship, Traditional  # noqa: E501

        :return: The epp_program_pathway_descriptor of this TpdmCandidateEducatorPreparationProgramAssociation.  # noqa: E501
        :rtype: str
        """
        return self._epp_program_pathway_descriptor

    @epp_program_pathway_descriptor.setter
    def epp_program_pathway_descriptor(self, epp_program_pathway_descriptor):
        """Sets the epp_program_pathway_descriptor of this TpdmCandidateEducatorPreparationProgramAssociation.

        The program pathway the candidate is following; for example: Residency, Internship, Traditional  # noqa: E501

        :param epp_program_pathway_descriptor: The epp_program_pathway_descriptor of this TpdmCandidateEducatorPreparationProgramAssociation.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                epp_program_pathway_descriptor is not None and len(epp_program_pathway_descriptor) > 306):
            raise ValueError("Invalid value for `epp_program_pathway_descriptor`, length must be less than or equal to `306`")  # noqa: E501

        self._epp_program_pathway_descriptor = epp_program_pathway_descriptor

    @property
    def reason_exited_descriptor(self):
        """Gets the reason_exited_descriptor of this TpdmCandidateEducatorPreparationProgramAssociation.  # noqa: E501

        Reason exited for the association.  # noqa: E501

        :return: The reason_exited_descriptor of this TpdmCandidateEducatorPreparationProgramAssociation.  # noqa: E501
        :rtype: str
        """
        return self._reason_exited_descriptor

    @reason_exited_descriptor.setter
    def reason_exited_descriptor(self, reason_exited_descriptor):
        """Sets the reason_exited_descriptor of this TpdmCandidateEducatorPreparationProgramAssociation.

        Reason exited for the association.  # noqa: E501

        :param reason_exited_descriptor: The reason_exited_descriptor of this TpdmCandidateEducatorPreparationProgramAssociation.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                reason_exited_descriptor is not None and len(reason_exited_descriptor) > 306):
            raise ValueError("Invalid value for `reason_exited_descriptor`, length must be less than or equal to `306`")  # noqa: E501

        self._reason_exited_descriptor = reason_exited_descriptor

    @property
    def etag(self):
        """Gets the etag of this TpdmCandidateEducatorPreparationProgramAssociation.  # noqa: E501

        A unique system-generated value that identifies the version of the resource.  # noqa: E501

        :return: The etag of this TpdmCandidateEducatorPreparationProgramAssociation.  # noqa: E501
        :rtype: str
        """
        return self._etag

    @etag.setter
    def etag(self, etag):
        """Sets the etag of this TpdmCandidateEducatorPreparationProgramAssociation.

        A unique system-generated value that identifies the version of the resource.  # noqa: E501

        :param etag: The etag of this TpdmCandidateEducatorPreparationProgramAssociation.  # noqa: E501
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
        if issubclass(TpdmCandidateEducatorPreparationProgramAssociation, dict):
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
        if not isinstance(other, TpdmCandidateEducatorPreparationProgramAssociation):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TpdmCandidateEducatorPreparationProgramAssociation):
            return True

        return self.to_dict() != other.to_dict()