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


class EdFiAssessmentScoreRangeLearningStandard(object):
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
        'learning_standards': 'list[EdFiAssessmentScoreRangeLearningStandardLearningStandard]',
        'score_range_id': 'str',
        'assessment_reference': 'EdFiAssessmentReference',
        'objective_assessment_reference': 'EdFiObjectiveAssessmentReference',
        'assessment_reporting_method_descriptor': 'str',
        'maximum_score': 'str',
        'minimum_score': 'str',
        'etag': 'str'
    }

    attribute_map = {
        'id': 'id',
        'learning_standards': 'learningStandards',
        'score_range_id': 'scoreRangeId',
        'assessment_reference': 'assessmentReference',
        'objective_assessment_reference': 'objectiveAssessmentReference',
        'assessment_reporting_method_descriptor': 'assessmentReportingMethodDescriptor',
        'maximum_score': 'maximumScore',
        'minimum_score': 'minimumScore',
        'etag': '_etag'
    }

    def __init__(self, id=None, learning_standards=None, score_range_id=None, assessment_reference=None, objective_assessment_reference=None, assessment_reporting_method_descriptor=None, maximum_score=None, minimum_score=None, etag=None, _configuration=None):  # noqa: E501
        """EdFiAssessmentScoreRangeLearningStandard - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._learning_standards = None
        self._score_range_id = None
        self._assessment_reference = None
        self._objective_assessment_reference = None
        self._assessment_reporting_method_descriptor = None
        self._maximum_score = None
        self._minimum_score = None
        self._etag = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.learning_standards = learning_standards
        self.score_range_id = score_range_id
        self.assessment_reference = assessment_reference
        if objective_assessment_reference is not None:
            self.objective_assessment_reference = objective_assessment_reference
        if assessment_reporting_method_descriptor is not None:
            self.assessment_reporting_method_descriptor = assessment_reporting_method_descriptor
        self.maximum_score = maximum_score
        self.minimum_score = minimum_score
        if etag is not None:
            self.etag = etag

    @property
    def id(self):
        """Gets the id of this EdFiAssessmentScoreRangeLearningStandard.  # noqa: E501

          # noqa: E501

        :return: The id of this EdFiAssessmentScoreRangeLearningStandard.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this EdFiAssessmentScoreRangeLearningStandard.

          # noqa: E501

        :param id: The id of this EdFiAssessmentScoreRangeLearningStandard.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def learning_standards(self):
        """Gets the learning_standards of this EdFiAssessmentScoreRangeLearningStandard.  # noqa: E501

        An unordered collection of assessmentScoreRangeLearningStandardLearningStandards. Learning standard associated with the score range.  # noqa: E501

        :return: The learning_standards of this EdFiAssessmentScoreRangeLearningStandard.  # noqa: E501
        :rtype: list[EdFiAssessmentScoreRangeLearningStandardLearningStandard]
        """
        return self._learning_standards

    @learning_standards.setter
    def learning_standards(self, learning_standards):
        """Sets the learning_standards of this EdFiAssessmentScoreRangeLearningStandard.

        An unordered collection of assessmentScoreRangeLearningStandardLearningStandards. Learning standard associated with the score range.  # noqa: E501

        :param learning_standards: The learning_standards of this EdFiAssessmentScoreRangeLearningStandard.  # noqa: E501
        :type: list[EdFiAssessmentScoreRangeLearningStandardLearningStandard]
        """
        if self._configuration.client_side_validation and learning_standards is None:
            raise ValueError("Invalid value for `learning_standards`, must not be `None`")  # noqa: E501

        self._learning_standards = learning_standards

    @property
    def score_range_id(self):
        """Gets the score_range_id of this EdFiAssessmentScoreRangeLearningStandard.  # noqa: E501

        A unique number or alphanumeric code assigned to the score range associated with one or more learning standards.  # noqa: E501

        :return: The score_range_id of this EdFiAssessmentScoreRangeLearningStandard.  # noqa: E501
        :rtype: str
        """
        return self._score_range_id

    @score_range_id.setter
    def score_range_id(self, score_range_id):
        """Sets the score_range_id of this EdFiAssessmentScoreRangeLearningStandard.

        A unique number or alphanumeric code assigned to the score range associated with one or more learning standards.  # noqa: E501

        :param score_range_id: The score_range_id of this EdFiAssessmentScoreRangeLearningStandard.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and score_range_id is None:
            raise ValueError("Invalid value for `score_range_id`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                score_range_id is not None and len(score_range_id) > 60):
            raise ValueError("Invalid value for `score_range_id`, length must be less than or equal to `60`")  # noqa: E501

        self._score_range_id = score_range_id

    @property
    def assessment_reference(self):
        """Gets the assessment_reference of this EdFiAssessmentScoreRangeLearningStandard.  # noqa: E501


        :return: The assessment_reference of this EdFiAssessmentScoreRangeLearningStandard.  # noqa: E501
        :rtype: EdFiAssessmentReference
        """
        return self._assessment_reference

    @assessment_reference.setter
    def assessment_reference(self, assessment_reference):
        """Sets the assessment_reference of this EdFiAssessmentScoreRangeLearningStandard.


        :param assessment_reference: The assessment_reference of this EdFiAssessmentScoreRangeLearningStandard.  # noqa: E501
        :type: EdFiAssessmentReference
        """
        if self._configuration.client_side_validation and assessment_reference is None:
            raise ValueError("Invalid value for `assessment_reference`, must not be `None`")  # noqa: E501

        self._assessment_reference = assessment_reference

    @property
    def objective_assessment_reference(self):
        """Gets the objective_assessment_reference of this EdFiAssessmentScoreRangeLearningStandard.  # noqa: E501


        :return: The objective_assessment_reference of this EdFiAssessmentScoreRangeLearningStandard.  # noqa: E501
        :rtype: EdFiObjectiveAssessmentReference
        """
        return self._objective_assessment_reference

    @objective_assessment_reference.setter
    def objective_assessment_reference(self, objective_assessment_reference):
        """Sets the objective_assessment_reference of this EdFiAssessmentScoreRangeLearningStandard.


        :param objective_assessment_reference: The objective_assessment_reference of this EdFiAssessmentScoreRangeLearningStandard.  # noqa: E501
        :type: EdFiObjectiveAssessmentReference
        """

        self._objective_assessment_reference = objective_assessment_reference

    @property
    def assessment_reporting_method_descriptor(self):
        """Gets the assessment_reporting_method_descriptor of this EdFiAssessmentScoreRangeLearningStandard.  # noqa: E501

        The assessment reporting method defined (e.g., scale score, RIT scale score) associated with the referenced learning standard(s).  # noqa: E501

        :return: The assessment_reporting_method_descriptor of this EdFiAssessmentScoreRangeLearningStandard.  # noqa: E501
        :rtype: str
        """
        return self._assessment_reporting_method_descriptor

    @assessment_reporting_method_descriptor.setter
    def assessment_reporting_method_descriptor(self, assessment_reporting_method_descriptor):
        """Sets the assessment_reporting_method_descriptor of this EdFiAssessmentScoreRangeLearningStandard.

        The assessment reporting method defined (e.g., scale score, RIT scale score) associated with the referenced learning standard(s).  # noqa: E501

        :param assessment_reporting_method_descriptor: The assessment_reporting_method_descriptor of this EdFiAssessmentScoreRangeLearningStandard.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                assessment_reporting_method_descriptor is not None and len(assessment_reporting_method_descriptor) > 306):
            raise ValueError("Invalid value for `assessment_reporting_method_descriptor`, length must be less than or equal to `306`")  # noqa: E501

        self._assessment_reporting_method_descriptor = assessment_reporting_method_descriptor

    @property
    def maximum_score(self):
        """Gets the maximum_score of this EdFiAssessmentScoreRangeLearningStandard.  # noqa: E501

        The maximum score in the score range.  # noqa: E501

        :return: The maximum_score of this EdFiAssessmentScoreRangeLearningStandard.  # noqa: E501
        :rtype: str
        """
        return self._maximum_score

    @maximum_score.setter
    def maximum_score(self, maximum_score):
        """Sets the maximum_score of this EdFiAssessmentScoreRangeLearningStandard.

        The maximum score in the score range.  # noqa: E501

        :param maximum_score: The maximum_score of this EdFiAssessmentScoreRangeLearningStandard.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and maximum_score is None:
            raise ValueError("Invalid value for `maximum_score`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                maximum_score is not None and len(maximum_score) > 35):
            raise ValueError("Invalid value for `maximum_score`, length must be less than or equal to `35`")  # noqa: E501

        self._maximum_score = maximum_score

    @property
    def minimum_score(self):
        """Gets the minimum_score of this EdFiAssessmentScoreRangeLearningStandard.  # noqa: E501

        The minimum score in the score range.  # noqa: E501

        :return: The minimum_score of this EdFiAssessmentScoreRangeLearningStandard.  # noqa: E501
        :rtype: str
        """
        return self._minimum_score

    @minimum_score.setter
    def minimum_score(self, minimum_score):
        """Sets the minimum_score of this EdFiAssessmentScoreRangeLearningStandard.

        The minimum score in the score range.  # noqa: E501

        :param minimum_score: The minimum_score of this EdFiAssessmentScoreRangeLearningStandard.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and minimum_score is None:
            raise ValueError("Invalid value for `minimum_score`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                minimum_score is not None and len(minimum_score) > 35):
            raise ValueError("Invalid value for `minimum_score`, length must be less than or equal to `35`")  # noqa: E501

        self._minimum_score = minimum_score

    @property
    def etag(self):
        """Gets the etag of this EdFiAssessmentScoreRangeLearningStandard.  # noqa: E501

        A unique system-generated value that identifies the version of the resource.  # noqa: E501

        :return: The etag of this EdFiAssessmentScoreRangeLearningStandard.  # noqa: E501
        :rtype: str
        """
        return self._etag

    @etag.setter
    def etag(self, etag):
        """Sets the etag of this EdFiAssessmentScoreRangeLearningStandard.

        A unique system-generated value that identifies the version of the resource.  # noqa: E501

        :param etag: The etag of this EdFiAssessmentScoreRangeLearningStandard.  # noqa: E501
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
        if issubclass(EdFiAssessmentScoreRangeLearningStandard, dict):
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
        if not isinstance(other, EdFiAssessmentScoreRangeLearningStandard):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EdFiAssessmentScoreRangeLearningStandard):
            return True

        return self.to_dict() != other.to_dict()
