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


class EdFiAssessment(object):
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
        'academic_subjects': 'list[EdFiAssessmentAcademicSubject]',
        'assessment_identifier': 'str',
        'namespace': 'str',
        'education_organization_reference': 'EdFiEducationOrganizationReference',
        'adaptive_assessment': 'bool',
        'assessed_grade_levels': 'list[EdFiAssessmentAssessedGradeLevel]',
        'assessment_category_descriptor': 'str',
        'assessment_family': 'str',
        'assessment_form': 'str',
        'assessment_title': 'str',
        'assessment_version': 'int',
        'content_standard': 'EdFiAssessmentContentStandard',
        'identification_codes': 'list[EdFiAssessmentIdentificationCode]',
        'languages': 'list[EdFiAssessmentLanguage]',
        'max_raw_score': 'float',
        'nomenclature': 'str',
        'performance_levels': 'list[EdFiAssessmentPerformanceLevel]',
        'periods': 'list[EdFiAssessmentPeriod]',
        'platform_types': 'list[EdFiAssessmentPlatformType]',
        'programs': 'list[EdFiAssessmentProgram]',
        'revision_date': 'date',
        'scores': 'list[EdFiAssessmentScore]',
        'sections': 'list[EdFiAssessmentSection]',
        'etag': 'str'
    }

    attribute_map = {
        'id': 'id',
        'academic_subjects': 'academicSubjects',
        'assessment_identifier': 'assessmentIdentifier',
        'namespace': 'namespace',
        'education_organization_reference': 'educationOrganizationReference',
        'adaptive_assessment': 'adaptiveAssessment',
        'assessed_grade_levels': 'assessedGradeLevels',
        'assessment_category_descriptor': 'assessmentCategoryDescriptor',
        'assessment_family': 'assessmentFamily',
        'assessment_form': 'assessmentForm',
        'assessment_title': 'assessmentTitle',
        'assessment_version': 'assessmentVersion',
        'content_standard': 'contentStandard',
        'identification_codes': 'identificationCodes',
        'languages': 'languages',
        'max_raw_score': 'maxRawScore',
        'nomenclature': 'nomenclature',
        'performance_levels': 'performanceLevels',
        'periods': 'periods',
        'platform_types': 'platformTypes',
        'programs': 'programs',
        'revision_date': 'revisionDate',
        'scores': 'scores',
        'sections': 'sections',
        'etag': '_etag'
    }

    def __init__(self, id=None, academic_subjects=None, assessment_identifier=None, namespace=None, education_organization_reference=None, adaptive_assessment=None, assessed_grade_levels=None, assessment_category_descriptor=None, assessment_family=None, assessment_form=None, assessment_title=None, assessment_version=None, content_standard=None, identification_codes=None, languages=None, max_raw_score=None, nomenclature=None, performance_levels=None, periods=None, platform_types=None, programs=None, revision_date=None, scores=None, sections=None, etag=None, _configuration=None):  # noqa: E501
        """EdFiAssessment - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._academic_subjects = None
        self._assessment_identifier = None
        self._namespace = None
        self._education_organization_reference = None
        self._adaptive_assessment = None
        self._assessed_grade_levels = None
        self._assessment_category_descriptor = None
        self._assessment_family = None
        self._assessment_form = None
        self._assessment_title = None
        self._assessment_version = None
        self._content_standard = None
        self._identification_codes = None
        self._languages = None
        self._max_raw_score = None
        self._nomenclature = None
        self._performance_levels = None
        self._periods = None
        self._platform_types = None
        self._programs = None
        self._revision_date = None
        self._scores = None
        self._sections = None
        self._etag = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.academic_subjects = academic_subjects
        self.assessment_identifier = assessment_identifier
        self.namespace = namespace
        if education_organization_reference is not None:
            self.education_organization_reference = education_organization_reference
        if adaptive_assessment is not None:
            self.adaptive_assessment = adaptive_assessment
        if assessed_grade_levels is not None:
            self.assessed_grade_levels = assessed_grade_levels
        if assessment_category_descriptor is not None:
            self.assessment_category_descriptor = assessment_category_descriptor
        if assessment_family is not None:
            self.assessment_family = assessment_family
        if assessment_form is not None:
            self.assessment_form = assessment_form
        self.assessment_title = assessment_title
        if assessment_version is not None:
            self.assessment_version = assessment_version
        if content_standard is not None:
            self.content_standard = content_standard
        if identification_codes is not None:
            self.identification_codes = identification_codes
        if languages is not None:
            self.languages = languages
        if max_raw_score is not None:
            self.max_raw_score = max_raw_score
        if nomenclature is not None:
            self.nomenclature = nomenclature
        if performance_levels is not None:
            self.performance_levels = performance_levels
        if periods is not None:
            self.periods = periods
        if platform_types is not None:
            self.platform_types = platform_types
        if programs is not None:
            self.programs = programs
        if revision_date is not None:
            self.revision_date = revision_date
        if scores is not None:
            self.scores = scores
        if sections is not None:
            self.sections = sections
        if etag is not None:
            self.etag = etag

    @property
    def id(self):
        """Gets the id of this EdFiAssessment.  # noqa: E501

          # noqa: E501

        :return: The id of this EdFiAssessment.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this EdFiAssessment.

          # noqa: E501

        :param id: The id of this EdFiAssessment.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def academic_subjects(self):
        """Gets the academic_subjects of this EdFiAssessment.  # noqa: E501

        An unordered collection of assessmentAcademicSubjects. The description of the content or subject area (e.g., arts, mathematics, reading, stenography, or a foreign language) of an assessment.  # noqa: E501

        :return: The academic_subjects of this EdFiAssessment.  # noqa: E501
        :rtype: list[EdFiAssessmentAcademicSubject]
        """
        return self._academic_subjects

    @academic_subjects.setter
    def academic_subjects(self, academic_subjects):
        """Sets the academic_subjects of this EdFiAssessment.

        An unordered collection of assessmentAcademicSubjects. The description of the content or subject area (e.g., arts, mathematics, reading, stenography, or a foreign language) of an assessment.  # noqa: E501

        :param academic_subjects: The academic_subjects of this EdFiAssessment.  # noqa: E501
        :type: list[EdFiAssessmentAcademicSubject]
        """
        if self._configuration.client_side_validation and academic_subjects is None:
            raise ValueError("Invalid value for `academic_subjects`, must not be `None`")  # noqa: E501

        self._academic_subjects = academic_subjects

    @property
    def assessment_identifier(self):
        """Gets the assessment_identifier of this EdFiAssessment.  # noqa: E501

        A unique number or alphanumeric code assigned to an assessment.  # noqa: E501

        :return: The assessment_identifier of this EdFiAssessment.  # noqa: E501
        :rtype: str
        """
        return self._assessment_identifier

    @assessment_identifier.setter
    def assessment_identifier(self, assessment_identifier):
        """Sets the assessment_identifier of this EdFiAssessment.

        A unique number or alphanumeric code assigned to an assessment.  # noqa: E501

        :param assessment_identifier: The assessment_identifier of this EdFiAssessment.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and assessment_identifier is None:
            raise ValueError("Invalid value for `assessment_identifier`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                assessment_identifier is not None and len(assessment_identifier) > 60):
            raise ValueError("Invalid value for `assessment_identifier`, length must be less than or equal to `60`")  # noqa: E501

        self._assessment_identifier = assessment_identifier

    @property
    def namespace(self):
        """Gets the namespace of this EdFiAssessment.  # noqa: E501

        Namespace for the assessment.  # noqa: E501

        :return: The namespace of this EdFiAssessment.  # noqa: E501
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """Sets the namespace of this EdFiAssessment.

        Namespace for the assessment.  # noqa: E501

        :param namespace: The namespace of this EdFiAssessment.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and namespace is None:
            raise ValueError("Invalid value for `namespace`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                namespace is not None and len(namespace) > 255):
            raise ValueError("Invalid value for `namespace`, length must be less than or equal to `255`")  # noqa: E501

        self._namespace = namespace

    @property
    def education_organization_reference(self):
        """Gets the education_organization_reference of this EdFiAssessment.  # noqa: E501


        :return: The education_organization_reference of this EdFiAssessment.  # noqa: E501
        :rtype: EdFiEducationOrganizationReference
        """
        return self._education_organization_reference

    @education_organization_reference.setter
    def education_organization_reference(self, education_organization_reference):
        """Sets the education_organization_reference of this EdFiAssessment.


        :param education_organization_reference: The education_organization_reference of this EdFiAssessment.  # noqa: E501
        :type: EdFiEducationOrganizationReference
        """

        self._education_organization_reference = education_organization_reference

    @property
    def adaptive_assessment(self):
        """Gets the adaptive_assessment of this EdFiAssessment.  # noqa: E501

        Indicates that the assessment is adaptive.  # noqa: E501

        :return: The adaptive_assessment of this EdFiAssessment.  # noqa: E501
        :rtype: bool
        """
        return self._adaptive_assessment

    @adaptive_assessment.setter
    def adaptive_assessment(self, adaptive_assessment):
        """Sets the adaptive_assessment of this EdFiAssessment.

        Indicates that the assessment is adaptive.  # noqa: E501

        :param adaptive_assessment: The adaptive_assessment of this EdFiAssessment.  # noqa: E501
        :type: bool
        """

        self._adaptive_assessment = adaptive_assessment

    @property
    def assessed_grade_levels(self):
        """Gets the assessed_grade_levels of this EdFiAssessment.  # noqa: E501

        An unordered collection of assessmentAssessedGradeLevels. The grade level(s) for which an assessment is designed. The semantics of null is assumed to mean that the assessment is not associated with any grade level.  # noqa: E501

        :return: The assessed_grade_levels of this EdFiAssessment.  # noqa: E501
        :rtype: list[EdFiAssessmentAssessedGradeLevel]
        """
        return self._assessed_grade_levels

    @assessed_grade_levels.setter
    def assessed_grade_levels(self, assessed_grade_levels):
        """Sets the assessed_grade_levels of this EdFiAssessment.

        An unordered collection of assessmentAssessedGradeLevels. The grade level(s) for which an assessment is designed. The semantics of null is assumed to mean that the assessment is not associated with any grade level.  # noqa: E501

        :param assessed_grade_levels: The assessed_grade_levels of this EdFiAssessment.  # noqa: E501
        :type: list[EdFiAssessmentAssessedGradeLevel]
        """

        self._assessed_grade_levels = assessed_grade_levels

    @property
    def assessment_category_descriptor(self):
        """Gets the assessment_category_descriptor of this EdFiAssessment.  # noqa: E501

        The category of an assessment based on format and content.  # noqa: E501

        :return: The assessment_category_descriptor of this EdFiAssessment.  # noqa: E501
        :rtype: str
        """
        return self._assessment_category_descriptor

    @assessment_category_descriptor.setter
    def assessment_category_descriptor(self, assessment_category_descriptor):
        """Sets the assessment_category_descriptor of this EdFiAssessment.

        The category of an assessment based on format and content.  # noqa: E501

        :param assessment_category_descriptor: The assessment_category_descriptor of this EdFiAssessment.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                assessment_category_descriptor is not None and len(assessment_category_descriptor) > 306):
            raise ValueError("Invalid value for `assessment_category_descriptor`, length must be less than or equal to `306`")  # noqa: E501

        self._assessment_category_descriptor = assessment_category_descriptor

    @property
    def assessment_family(self):
        """Gets the assessment_family of this EdFiAssessment.  # noqa: E501

        The assessment family this assessment is a member of.  # noqa: E501

        :return: The assessment_family of this EdFiAssessment.  # noqa: E501
        :rtype: str
        """
        return self._assessment_family

    @assessment_family.setter
    def assessment_family(self, assessment_family):
        """Sets the assessment_family of this EdFiAssessment.

        The assessment family this assessment is a member of.  # noqa: E501

        :param assessment_family: The assessment_family of this EdFiAssessment.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                assessment_family is not None and len(assessment_family) > 60):
            raise ValueError("Invalid value for `assessment_family`, length must be less than or equal to `60`")  # noqa: E501

        self._assessment_family = assessment_family

    @property
    def assessment_form(self):
        """Gets the assessment_form of this EdFiAssessment.  # noqa: E501

        Identifies the form of the assessment, for example a regular versus makeup form, multiple choice versus constructed response, etc.  # noqa: E501

        :return: The assessment_form of this EdFiAssessment.  # noqa: E501
        :rtype: str
        """
        return self._assessment_form

    @assessment_form.setter
    def assessment_form(self, assessment_form):
        """Sets the assessment_form of this EdFiAssessment.

        Identifies the form of the assessment, for example a regular versus makeup form, multiple choice versus constructed response, etc.  # noqa: E501

        :param assessment_form: The assessment_form of this EdFiAssessment.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                assessment_form is not None and len(assessment_form) > 60):
            raise ValueError("Invalid value for `assessment_form`, length must be less than or equal to `60`")  # noqa: E501

        self._assessment_form = assessment_form

    @property
    def assessment_title(self):
        """Gets the assessment_title of this EdFiAssessment.  # noqa: E501

        The title or name of the assessment.  # noqa: E501

        :return: The assessment_title of this EdFiAssessment.  # noqa: E501
        :rtype: str
        """
        return self._assessment_title

    @assessment_title.setter
    def assessment_title(self, assessment_title):
        """Sets the assessment_title of this EdFiAssessment.

        The title or name of the assessment.  # noqa: E501

        :param assessment_title: The assessment_title of this EdFiAssessment.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and assessment_title is None:
            raise ValueError("Invalid value for `assessment_title`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                assessment_title is not None and len(assessment_title) > 255):
            raise ValueError("Invalid value for `assessment_title`, length must be less than or equal to `255`")  # noqa: E501

        self._assessment_title = assessment_title

    @property
    def assessment_version(self):
        """Gets the assessment_version of this EdFiAssessment.  # noqa: E501

        The version identifier for the assessment.  # noqa: E501

        :return: The assessment_version of this EdFiAssessment.  # noqa: E501
        :rtype: int
        """
        return self._assessment_version

    @assessment_version.setter
    def assessment_version(self, assessment_version):
        """Sets the assessment_version of this EdFiAssessment.

        The version identifier for the assessment.  # noqa: E501

        :param assessment_version: The assessment_version of this EdFiAssessment.  # noqa: E501
        :type: int
        """

        self._assessment_version = assessment_version

    @property
    def content_standard(self):
        """Gets the content_standard of this EdFiAssessment.  # noqa: E501


        :return: The content_standard of this EdFiAssessment.  # noqa: E501
        :rtype: EdFiAssessmentContentStandard
        """
        return self._content_standard

    @content_standard.setter
    def content_standard(self, content_standard):
        """Sets the content_standard of this EdFiAssessment.


        :param content_standard: The content_standard of this EdFiAssessment.  # noqa: E501
        :type: EdFiAssessmentContentStandard
        """

        self._content_standard = content_standard

    @property
    def identification_codes(self):
        """Gets the identification_codes of this EdFiAssessment.  # noqa: E501

        An unordered collection of assessmentIdentificationCodes. A unique number or alphanumeric code assigned to an assessment by a school, school system, a state, or other agency or entity.  # noqa: E501

        :return: The identification_codes of this EdFiAssessment.  # noqa: E501
        :rtype: list[EdFiAssessmentIdentificationCode]
        """
        return self._identification_codes

    @identification_codes.setter
    def identification_codes(self, identification_codes):
        """Sets the identification_codes of this EdFiAssessment.

        An unordered collection of assessmentIdentificationCodes. A unique number or alphanumeric code assigned to an assessment by a school, school system, a state, or other agency or entity.  # noqa: E501

        :param identification_codes: The identification_codes of this EdFiAssessment.  # noqa: E501
        :type: list[EdFiAssessmentIdentificationCode]
        """

        self._identification_codes = identification_codes

    @property
    def languages(self):
        """Gets the languages of this EdFiAssessment.  # noqa: E501

        An unordered collection of assessmentLanguages. An indication of the languages in which the assessment is designed.  # noqa: E501

        :return: The languages of this EdFiAssessment.  # noqa: E501
        :rtype: list[EdFiAssessmentLanguage]
        """
        return self._languages

    @languages.setter
    def languages(self, languages):
        """Sets the languages of this EdFiAssessment.

        An unordered collection of assessmentLanguages. An indication of the languages in which the assessment is designed.  # noqa: E501

        :param languages: The languages of this EdFiAssessment.  # noqa: E501
        :type: list[EdFiAssessmentLanguage]
        """

        self._languages = languages

    @property
    def max_raw_score(self):
        """Gets the max_raw_score of this EdFiAssessment.  # noqa: E501

        The maximum raw score achievable across all assessment items that are correct and scored at the maximum.  # noqa: E501

        :return: The max_raw_score of this EdFiAssessment.  # noqa: E501
        :rtype: float
        """
        return self._max_raw_score

    @max_raw_score.setter
    def max_raw_score(self, max_raw_score):
        """Sets the max_raw_score of this EdFiAssessment.

        The maximum raw score achievable across all assessment items that are correct and scored at the maximum.  # noqa: E501

        :param max_raw_score: The max_raw_score of this EdFiAssessment.  # noqa: E501
        :type: float
        """

        self._max_raw_score = max_raw_score

    @property
    def nomenclature(self):
        """Gets the nomenclature of this EdFiAssessment.  # noqa: E501

        Reflects the specific nomenclature used for assessment.  # noqa: E501

        :return: The nomenclature of this EdFiAssessment.  # noqa: E501
        :rtype: str
        """
        return self._nomenclature

    @nomenclature.setter
    def nomenclature(self, nomenclature):
        """Sets the nomenclature of this EdFiAssessment.

        Reflects the specific nomenclature used for assessment.  # noqa: E501

        :param nomenclature: The nomenclature of this EdFiAssessment.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                nomenclature is not None and len(nomenclature) > 100):
            raise ValueError("Invalid value for `nomenclature`, length must be less than or equal to `100`")  # noqa: E501

        self._nomenclature = nomenclature

    @property
    def performance_levels(self):
        """Gets the performance_levels of this EdFiAssessment.  # noqa: E501

        An unordered collection of assessmentPerformanceLevels. Definition of the performance levels and the associated cut scores. Three styles are supported: 1. Specification of performance level by minimum and maximum score, 2. Specification of performance level by cut score, using only minimum score, 3. Specification of performance level without any mapping to scores.  # noqa: E501

        :return: The performance_levels of this EdFiAssessment.  # noqa: E501
        :rtype: list[EdFiAssessmentPerformanceLevel]
        """
        return self._performance_levels

    @performance_levels.setter
    def performance_levels(self, performance_levels):
        """Sets the performance_levels of this EdFiAssessment.

        An unordered collection of assessmentPerformanceLevels. Definition of the performance levels and the associated cut scores. Three styles are supported: 1. Specification of performance level by minimum and maximum score, 2. Specification of performance level by cut score, using only minimum score, 3. Specification of performance level without any mapping to scores.  # noqa: E501

        :param performance_levels: The performance_levels of this EdFiAssessment.  # noqa: E501
        :type: list[EdFiAssessmentPerformanceLevel]
        """

        self._performance_levels = performance_levels

    @property
    def periods(self):
        """Gets the periods of this EdFiAssessment.  # noqa: E501

        An unordered collection of assessmentPeriods. The period or window in which an assessment is supposed to be administered.  # noqa: E501

        :return: The periods of this EdFiAssessment.  # noqa: E501
        :rtype: list[EdFiAssessmentPeriod]
        """
        return self._periods

    @periods.setter
    def periods(self, periods):
        """Sets the periods of this EdFiAssessment.

        An unordered collection of assessmentPeriods. The period or window in which an assessment is supposed to be administered.  # noqa: E501

        :param periods: The periods of this EdFiAssessment.  # noqa: E501
        :type: list[EdFiAssessmentPeriod]
        """

        self._periods = periods

    @property
    def platform_types(self):
        """Gets the platform_types of this EdFiAssessment.  # noqa: E501

        An unordered collection of assessmentPlatformTypes. The platforms with which the assessment may be delivered.  # noqa: E501

        :return: The platform_types of this EdFiAssessment.  # noqa: E501
        :rtype: list[EdFiAssessmentPlatformType]
        """
        return self._platform_types

    @platform_types.setter
    def platform_types(self, platform_types):
        """Sets the platform_types of this EdFiAssessment.

        An unordered collection of assessmentPlatformTypes. The platforms with which the assessment may be delivered.  # noqa: E501

        :param platform_types: The platform_types of this EdFiAssessment.  # noqa: E501
        :type: list[EdFiAssessmentPlatformType]
        """

        self._platform_types = platform_types

    @property
    def programs(self):
        """Gets the programs of this EdFiAssessment.  # noqa: E501

        An unordered collection of assessmentPrograms. The programs associated with the assessment.  # noqa: E501

        :return: The programs of this EdFiAssessment.  # noqa: E501
        :rtype: list[EdFiAssessmentProgram]
        """
        return self._programs

    @programs.setter
    def programs(self, programs):
        """Sets the programs of this EdFiAssessment.

        An unordered collection of assessmentPrograms. The programs associated with the assessment.  # noqa: E501

        :param programs: The programs of this EdFiAssessment.  # noqa: E501
        :type: list[EdFiAssessmentProgram]
        """

        self._programs = programs

    @property
    def revision_date(self):
        """Gets the revision_date of this EdFiAssessment.  # noqa: E501

        The month, day, and year that the conceptual design for the assessment was most recently revised substantially.  # noqa: E501

        :return: The revision_date of this EdFiAssessment.  # noqa: E501
        :rtype: date
        """
        return self._revision_date

    @revision_date.setter
    def revision_date(self, revision_date):
        """Sets the revision_date of this EdFiAssessment.

        The month, day, and year that the conceptual design for the assessment was most recently revised substantially.  # noqa: E501

        :param revision_date: The revision_date of this EdFiAssessment.  # noqa: E501
        :type: date
        """

        self._revision_date = revision_date

    @property
    def scores(self):
        """Gets the scores of this EdFiAssessment.  # noqa: E501

        An unordered collection of assessmentScores. Definition of the scores to be expected from this assessment.  # noqa: E501

        :return: The scores of this EdFiAssessment.  # noqa: E501
        :rtype: list[EdFiAssessmentScore]
        """
        return self._scores

    @scores.setter
    def scores(self, scores):
        """Sets the scores of this EdFiAssessment.

        An unordered collection of assessmentScores. Definition of the scores to be expected from this assessment.  # noqa: E501

        :param scores: The scores of this EdFiAssessment.  # noqa: E501
        :type: list[EdFiAssessmentScore]
        """

        self._scores = scores

    @property
    def sections(self):
        """Gets the sections of this EdFiAssessment.  # noqa: E501

        An unordered collection of assessmentSections. The Section(s) to which the assessment is associated.  # noqa: E501

        :return: The sections of this EdFiAssessment.  # noqa: E501
        :rtype: list[EdFiAssessmentSection]
        """
        return self._sections

    @sections.setter
    def sections(self, sections):
        """Sets the sections of this EdFiAssessment.

        An unordered collection of assessmentSections. The Section(s) to which the assessment is associated.  # noqa: E501

        :param sections: The sections of this EdFiAssessment.  # noqa: E501
        :type: list[EdFiAssessmentSection]
        """

        self._sections = sections

    @property
    def etag(self):
        """Gets the etag of this EdFiAssessment.  # noqa: E501

        A unique system-generated value that identifies the version of the resource.  # noqa: E501

        :return: The etag of this EdFiAssessment.  # noqa: E501
        :rtype: str
        """
        return self._etag

    @etag.setter
    def etag(self, etag):
        """Sets the etag of this EdFiAssessment.

        A unique system-generated value that identifies the version of the resource.  # noqa: E501

        :param etag: The etag of this EdFiAssessment.  # noqa: E501
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
        if issubclass(EdFiAssessment, dict):
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
        if not isinstance(other, EdFiAssessment):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EdFiAssessment):
            return True

        return self.to_dict() != other.to_dict()
