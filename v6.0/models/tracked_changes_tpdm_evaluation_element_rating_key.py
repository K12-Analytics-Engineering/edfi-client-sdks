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


class TrackedChangesTpdmEvaluationElementRatingKey(object):
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
        'education_organization_id': 'int',
        'evaluation_element_title': 'str',
        'evaluation_objective_title': 'str',
        'evaluation_period_descriptor': 'str',
        'evaluation_title': 'str',
        'performance_evaluation_title': 'str',
        'performance_evaluation_type_descriptor': 'str',
        'school_year': 'int',
        'term_descriptor': 'str',
        'evaluation_date': 'datetime',
        'person_id': 'str',
        'source_system_descriptor': 'str'
    }

    attribute_map = {
        'education_organization_id': 'educationOrganizationId',
        'evaluation_element_title': 'evaluationElementTitle',
        'evaluation_objective_title': 'evaluationObjectiveTitle',
        'evaluation_period_descriptor': 'evaluationPeriodDescriptor',
        'evaluation_title': 'evaluationTitle',
        'performance_evaluation_title': 'performanceEvaluationTitle',
        'performance_evaluation_type_descriptor': 'performanceEvaluationTypeDescriptor',
        'school_year': 'schoolYear',
        'term_descriptor': 'termDescriptor',
        'evaluation_date': 'evaluationDate',
        'person_id': 'personId',
        'source_system_descriptor': 'sourceSystemDescriptor'
    }

    def __init__(self, education_organization_id=None, evaluation_element_title=None, evaluation_objective_title=None, evaluation_period_descriptor=None, evaluation_title=None, performance_evaluation_title=None, performance_evaluation_type_descriptor=None, school_year=None, term_descriptor=None, evaluation_date=None, person_id=None, source_system_descriptor=None, _configuration=None):  # noqa: E501
        """TrackedChangesTpdmEvaluationElementRatingKey - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._education_organization_id = None
        self._evaluation_element_title = None
        self._evaluation_objective_title = None
        self._evaluation_period_descriptor = None
        self._evaluation_title = None
        self._performance_evaluation_title = None
        self._performance_evaluation_type_descriptor = None
        self._school_year = None
        self._term_descriptor = None
        self._evaluation_date = None
        self._person_id = None
        self._source_system_descriptor = None
        self.discriminator = None

        if education_organization_id is not None:
            self.education_organization_id = education_organization_id
        if evaluation_element_title is not None:
            self.evaluation_element_title = evaluation_element_title
        if evaluation_objective_title is not None:
            self.evaluation_objective_title = evaluation_objective_title
        if evaluation_period_descriptor is not None:
            self.evaluation_period_descriptor = evaluation_period_descriptor
        if evaluation_title is not None:
            self.evaluation_title = evaluation_title
        if performance_evaluation_title is not None:
            self.performance_evaluation_title = performance_evaluation_title
        if performance_evaluation_type_descriptor is not None:
            self.performance_evaluation_type_descriptor = performance_evaluation_type_descriptor
        if school_year is not None:
            self.school_year = school_year
        if term_descriptor is not None:
            self.term_descriptor = term_descriptor
        if evaluation_date is not None:
            self.evaluation_date = evaluation_date
        if person_id is not None:
            self.person_id = person_id
        if source_system_descriptor is not None:
            self.source_system_descriptor = source_system_descriptor

    @property
    def education_organization_id(self):
        """Gets the education_organization_id of this TrackedChangesTpdmEvaluationElementRatingKey.  # noqa: E501

        The identifier assigned to an education organization.  # noqa: E501

        :return: The education_organization_id of this TrackedChangesTpdmEvaluationElementRatingKey.  # noqa: E501
        :rtype: int
        """
        return self._education_organization_id

    @education_organization_id.setter
    def education_organization_id(self, education_organization_id):
        """Sets the education_organization_id of this TrackedChangesTpdmEvaluationElementRatingKey.

        The identifier assigned to an education organization.  # noqa: E501

        :param education_organization_id: The education_organization_id of this TrackedChangesTpdmEvaluationElementRatingKey.  # noqa: E501
        :type: int
        """

        self._education_organization_id = education_organization_id

    @property
    def evaluation_element_title(self):
        """Gets the evaluation_element_title of this TrackedChangesTpdmEvaluationElementRatingKey.  # noqa: E501

        The name or title of the evaluation element.  # noqa: E501

        :return: The evaluation_element_title of this TrackedChangesTpdmEvaluationElementRatingKey.  # noqa: E501
        :rtype: str
        """
        return self._evaluation_element_title

    @evaluation_element_title.setter
    def evaluation_element_title(self, evaluation_element_title):
        """Sets the evaluation_element_title of this TrackedChangesTpdmEvaluationElementRatingKey.

        The name or title of the evaluation element.  # noqa: E501

        :param evaluation_element_title: The evaluation_element_title of this TrackedChangesTpdmEvaluationElementRatingKey.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                evaluation_element_title is not None and len(evaluation_element_title) > 255):
            raise ValueError("Invalid value for `evaluation_element_title`, length must be less than or equal to `255`")  # noqa: E501

        self._evaluation_element_title = evaluation_element_title

    @property
    def evaluation_objective_title(self):
        """Gets the evaluation_objective_title of this TrackedChangesTpdmEvaluationElementRatingKey.  # noqa: E501

        The name or title of the evaluation Objective.  # noqa: E501

        :return: The evaluation_objective_title of this TrackedChangesTpdmEvaluationElementRatingKey.  # noqa: E501
        :rtype: str
        """
        return self._evaluation_objective_title

    @evaluation_objective_title.setter
    def evaluation_objective_title(self, evaluation_objective_title):
        """Sets the evaluation_objective_title of this TrackedChangesTpdmEvaluationElementRatingKey.

        The name or title of the evaluation Objective.  # noqa: E501

        :param evaluation_objective_title: The evaluation_objective_title of this TrackedChangesTpdmEvaluationElementRatingKey.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                evaluation_objective_title is not None and len(evaluation_objective_title) > 50):
            raise ValueError("Invalid value for `evaluation_objective_title`, length must be less than or equal to `50`")  # noqa: E501

        self._evaluation_objective_title = evaluation_objective_title

    @property
    def evaluation_period_descriptor(self):
        """Gets the evaluation_period_descriptor of this TrackedChangesTpdmEvaluationElementRatingKey.  # noqa: E501

        The period for the evaluation.  # noqa: E501

        :return: The evaluation_period_descriptor of this TrackedChangesTpdmEvaluationElementRatingKey.  # noqa: E501
        :rtype: str
        """
        return self._evaluation_period_descriptor

    @evaluation_period_descriptor.setter
    def evaluation_period_descriptor(self, evaluation_period_descriptor):
        """Sets the evaluation_period_descriptor of this TrackedChangesTpdmEvaluationElementRatingKey.

        The period for the evaluation.  # noqa: E501

        :param evaluation_period_descriptor: The evaluation_period_descriptor of this TrackedChangesTpdmEvaluationElementRatingKey.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                evaluation_period_descriptor is not None and len(evaluation_period_descriptor) > 306):
            raise ValueError("Invalid value for `evaluation_period_descriptor`, length must be less than or equal to `306`")  # noqa: E501

        self._evaluation_period_descriptor = evaluation_period_descriptor

    @property
    def evaluation_title(self):
        """Gets the evaluation_title of this TrackedChangesTpdmEvaluationElementRatingKey.  # noqa: E501

        The name or title of the evaluation.  # noqa: E501

        :return: The evaluation_title of this TrackedChangesTpdmEvaluationElementRatingKey.  # noqa: E501
        :rtype: str
        """
        return self._evaluation_title

    @evaluation_title.setter
    def evaluation_title(self, evaluation_title):
        """Sets the evaluation_title of this TrackedChangesTpdmEvaluationElementRatingKey.

        The name or title of the evaluation.  # noqa: E501

        :param evaluation_title: The evaluation_title of this TrackedChangesTpdmEvaluationElementRatingKey.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                evaluation_title is not None and len(evaluation_title) > 50):
            raise ValueError("Invalid value for `evaluation_title`, length must be less than or equal to `50`")  # noqa: E501

        self._evaluation_title = evaluation_title

    @property
    def performance_evaluation_title(self):
        """Gets the performance_evaluation_title of this TrackedChangesTpdmEvaluationElementRatingKey.  # noqa: E501

        An assigned unique identifier for the performance evaluation.  # noqa: E501

        :return: The performance_evaluation_title of this TrackedChangesTpdmEvaluationElementRatingKey.  # noqa: E501
        :rtype: str
        """
        return self._performance_evaluation_title

    @performance_evaluation_title.setter
    def performance_evaluation_title(self, performance_evaluation_title):
        """Sets the performance_evaluation_title of this TrackedChangesTpdmEvaluationElementRatingKey.

        An assigned unique identifier for the performance evaluation.  # noqa: E501

        :param performance_evaluation_title: The performance_evaluation_title of this TrackedChangesTpdmEvaluationElementRatingKey.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                performance_evaluation_title is not None and len(performance_evaluation_title) > 50):
            raise ValueError("Invalid value for `performance_evaluation_title`, length must be less than or equal to `50`")  # noqa: E501

        self._performance_evaluation_title = performance_evaluation_title

    @property
    def performance_evaluation_type_descriptor(self):
        """Gets the performance_evaluation_type_descriptor of this TrackedChangesTpdmEvaluationElementRatingKey.  # noqa: E501

        The type of performance evaluation conducted.  # noqa: E501

        :return: The performance_evaluation_type_descriptor of this TrackedChangesTpdmEvaluationElementRatingKey.  # noqa: E501
        :rtype: str
        """
        return self._performance_evaluation_type_descriptor

    @performance_evaluation_type_descriptor.setter
    def performance_evaluation_type_descriptor(self, performance_evaluation_type_descriptor):
        """Sets the performance_evaluation_type_descriptor of this TrackedChangesTpdmEvaluationElementRatingKey.

        The type of performance evaluation conducted.  # noqa: E501

        :param performance_evaluation_type_descriptor: The performance_evaluation_type_descriptor of this TrackedChangesTpdmEvaluationElementRatingKey.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                performance_evaluation_type_descriptor is not None and len(performance_evaluation_type_descriptor) > 306):
            raise ValueError("Invalid value for `performance_evaluation_type_descriptor`, length must be less than or equal to `306`")  # noqa: E501

        self._performance_evaluation_type_descriptor = performance_evaluation_type_descriptor

    @property
    def school_year(self):
        """Gets the school_year of this TrackedChangesTpdmEvaluationElementRatingKey.  # noqa: E501

        The identifier for the school year.  # noqa: E501

        :return: The school_year of this TrackedChangesTpdmEvaluationElementRatingKey.  # noqa: E501
        :rtype: int
        """
        return self._school_year

    @school_year.setter
    def school_year(self, school_year):
        """Sets the school_year of this TrackedChangesTpdmEvaluationElementRatingKey.

        The identifier for the school year.  # noqa: E501

        :param school_year: The school_year of this TrackedChangesTpdmEvaluationElementRatingKey.  # noqa: E501
        :type: int
        """

        self._school_year = school_year

    @property
    def term_descriptor(self):
        """Gets the term_descriptor of this TrackedChangesTpdmEvaluationElementRatingKey.  # noqa: E501

        The term for the session during the school year.  # noqa: E501

        :return: The term_descriptor of this TrackedChangesTpdmEvaluationElementRatingKey.  # noqa: E501
        :rtype: str
        """
        return self._term_descriptor

    @term_descriptor.setter
    def term_descriptor(self, term_descriptor):
        """Sets the term_descriptor of this TrackedChangesTpdmEvaluationElementRatingKey.

        The term for the session during the school year.  # noqa: E501

        :param term_descriptor: The term_descriptor of this TrackedChangesTpdmEvaluationElementRatingKey.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                term_descriptor is not None and len(term_descriptor) > 306):
            raise ValueError("Invalid value for `term_descriptor`, length must be less than or equal to `306`")  # noqa: E501

        self._term_descriptor = term_descriptor

    @property
    def evaluation_date(self):
        """Gets the evaluation_date of this TrackedChangesTpdmEvaluationElementRatingKey.  # noqa: E501

        The date for the person's evaluation.  # noqa: E501

        :return: The evaluation_date of this TrackedChangesTpdmEvaluationElementRatingKey.  # noqa: E501
        :rtype: datetime
        """
        return self._evaluation_date

    @evaluation_date.setter
    def evaluation_date(self, evaluation_date):
        """Sets the evaluation_date of this TrackedChangesTpdmEvaluationElementRatingKey.

        The date for the person's evaluation.  # noqa: E501

        :param evaluation_date: The evaluation_date of this TrackedChangesTpdmEvaluationElementRatingKey.  # noqa: E501
        :type: datetime
        """

        self._evaluation_date = evaluation_date

    @property
    def person_id(self):
        """Gets the person_id of this TrackedChangesTpdmEvaluationElementRatingKey.  # noqa: E501

        A unique alphanumeric code assigned to a person.  # noqa: E501

        :return: The person_id of this TrackedChangesTpdmEvaluationElementRatingKey.  # noqa: E501
        :rtype: str
        """
        return self._person_id

    @person_id.setter
    def person_id(self, person_id):
        """Sets the person_id of this TrackedChangesTpdmEvaluationElementRatingKey.

        A unique alphanumeric code assigned to a person.  # noqa: E501

        :param person_id: The person_id of this TrackedChangesTpdmEvaluationElementRatingKey.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                person_id is not None and len(person_id) > 32):
            raise ValueError("Invalid value for `person_id`, length must be less than or equal to `32`")  # noqa: E501

        self._person_id = person_id

    @property
    def source_system_descriptor(self):
        """Gets the source_system_descriptor of this TrackedChangesTpdmEvaluationElementRatingKey.  # noqa: E501

        This descriptor defines the originating record source system for the person.  # noqa: E501

        :return: The source_system_descriptor of this TrackedChangesTpdmEvaluationElementRatingKey.  # noqa: E501
        :rtype: str
        """
        return self._source_system_descriptor

    @source_system_descriptor.setter
    def source_system_descriptor(self, source_system_descriptor):
        """Sets the source_system_descriptor of this TrackedChangesTpdmEvaluationElementRatingKey.

        This descriptor defines the originating record source system for the person.  # noqa: E501

        :param source_system_descriptor: The source_system_descriptor of this TrackedChangesTpdmEvaluationElementRatingKey.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                source_system_descriptor is not None and len(source_system_descriptor) > 306):
            raise ValueError("Invalid value for `source_system_descriptor`, length must be less than or equal to `306`")  # noqa: E501

        self._source_system_descriptor = source_system_descriptor

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
        if issubclass(TrackedChangesTpdmEvaluationElementRatingKey, dict):
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
        if not isinstance(other, TrackedChangesTpdmEvaluationElementRatingKey):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TrackedChangesTpdmEvaluationElementRatingKey):
            return True

        return self.to_dict() != other.to_dict()
