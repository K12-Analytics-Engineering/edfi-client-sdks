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


class EdFiLearningStandard(object):
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
        'academic_subjects': 'list[EdFiLearningStandardAcademicSubject]',
        'grade_levels': 'list[EdFiLearningStandardGradeLevel]',
        'learning_standard_id': 'str',
        'parent_learning_standard_reference': 'EdFiLearningStandardReference',
        'content_standard': 'EdFiLearningStandardContentStandard',
        'course_title': 'str',
        'description': 'str',
        'identification_codes': 'list[EdFiLearningStandardIdentificationCode]',
        'learning_standard_category_descriptor': 'str',
        'learning_standard_item_code': 'str',
        'learning_standard_scope_descriptor': 'str',
        'namespace': 'str',
        'prerequisite_learning_standards': 'list[EdFiLearningStandardPrerequisiteLearningStandard]',
        'success_criteria': 'str',
        'uri': 'str',
        'etag': 'str'
    }

    attribute_map = {
        'id': 'id',
        'academic_subjects': 'academicSubjects',
        'grade_levels': 'gradeLevels',
        'learning_standard_id': 'learningStandardId',
        'parent_learning_standard_reference': 'parentLearningStandardReference',
        'content_standard': 'contentStandard',
        'course_title': 'courseTitle',
        'description': 'description',
        'identification_codes': 'identificationCodes',
        'learning_standard_category_descriptor': 'learningStandardCategoryDescriptor',
        'learning_standard_item_code': 'learningStandardItemCode',
        'learning_standard_scope_descriptor': 'learningStandardScopeDescriptor',
        'namespace': 'namespace',
        'prerequisite_learning_standards': 'prerequisiteLearningStandards',
        'success_criteria': 'successCriteria',
        'uri': 'uri',
        'etag': '_etag'
    }

    def __init__(self, id=None, academic_subjects=None, grade_levels=None, learning_standard_id=None, parent_learning_standard_reference=None, content_standard=None, course_title=None, description=None, identification_codes=None, learning_standard_category_descriptor=None, learning_standard_item_code=None, learning_standard_scope_descriptor=None, namespace=None, prerequisite_learning_standards=None, success_criteria=None, uri=None, etag=None, _configuration=None):  # noqa: E501
        """EdFiLearningStandard - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._academic_subjects = None
        self._grade_levels = None
        self._learning_standard_id = None
        self._parent_learning_standard_reference = None
        self._content_standard = None
        self._course_title = None
        self._description = None
        self._identification_codes = None
        self._learning_standard_category_descriptor = None
        self._learning_standard_item_code = None
        self._learning_standard_scope_descriptor = None
        self._namespace = None
        self._prerequisite_learning_standards = None
        self._success_criteria = None
        self._uri = None
        self._etag = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.academic_subjects = academic_subjects
        self.grade_levels = grade_levels
        self.learning_standard_id = learning_standard_id
        if parent_learning_standard_reference is not None:
            self.parent_learning_standard_reference = parent_learning_standard_reference
        if content_standard is not None:
            self.content_standard = content_standard
        if course_title is not None:
            self.course_title = course_title
        self.description = description
        if identification_codes is not None:
            self.identification_codes = identification_codes
        if learning_standard_category_descriptor is not None:
            self.learning_standard_category_descriptor = learning_standard_category_descriptor
        if learning_standard_item_code is not None:
            self.learning_standard_item_code = learning_standard_item_code
        if learning_standard_scope_descriptor is not None:
            self.learning_standard_scope_descriptor = learning_standard_scope_descriptor
        self.namespace = namespace
        if prerequisite_learning_standards is not None:
            self.prerequisite_learning_standards = prerequisite_learning_standards
        if success_criteria is not None:
            self.success_criteria = success_criteria
        if uri is not None:
            self.uri = uri
        if etag is not None:
            self.etag = etag

    @property
    def id(self):
        """Gets the id of this EdFiLearningStandard.  # noqa: E501

          # noqa: E501

        :return: The id of this EdFiLearningStandard.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this EdFiLearningStandard.

          # noqa: E501

        :param id: The id of this EdFiLearningStandard.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def academic_subjects(self):
        """Gets the academic_subjects of this EdFiLearningStandard.  # noqa: E501

        An unordered collection of learningStandardAcademicSubjects. Subject area for the LearningStandard.  # noqa: E501

        :return: The academic_subjects of this EdFiLearningStandard.  # noqa: E501
        :rtype: list[EdFiLearningStandardAcademicSubject]
        """
        return self._academic_subjects

    @academic_subjects.setter
    def academic_subjects(self, academic_subjects):
        """Sets the academic_subjects of this EdFiLearningStandard.

        An unordered collection of learningStandardAcademicSubjects. Subject area for the LearningStandard.  # noqa: E501

        :param academic_subjects: The academic_subjects of this EdFiLearningStandard.  # noqa: E501
        :type: list[EdFiLearningStandardAcademicSubject]
        """
        if self._configuration.client_side_validation and academic_subjects is None:
            raise ValueError("Invalid value for `academic_subjects`, must not be `None`")  # noqa: E501

        self._academic_subjects = academic_subjects

    @property
    def grade_levels(self):
        """Gets the grade_levels of this EdFiLearningStandard.  # noqa: E501

        An unordered collection of learningStandardGradeLevels. The grade levels for the specific learning standard.  # noqa: E501

        :return: The grade_levels of this EdFiLearningStandard.  # noqa: E501
        :rtype: list[EdFiLearningStandardGradeLevel]
        """
        return self._grade_levels

    @grade_levels.setter
    def grade_levels(self, grade_levels):
        """Sets the grade_levels of this EdFiLearningStandard.

        An unordered collection of learningStandardGradeLevels. The grade levels for the specific learning standard.  # noqa: E501

        :param grade_levels: The grade_levels of this EdFiLearningStandard.  # noqa: E501
        :type: list[EdFiLearningStandardGradeLevel]
        """
        if self._configuration.client_side_validation and grade_levels is None:
            raise ValueError("Invalid value for `grade_levels`, must not be `None`")  # noqa: E501

        self._grade_levels = grade_levels

    @property
    def learning_standard_id(self):
        """Gets the learning_standard_id of this EdFiLearningStandard.  # noqa: E501

        The identifier for the specific learning standard (e.g., 111.15.3.1.A).  # noqa: E501

        :return: The learning_standard_id of this EdFiLearningStandard.  # noqa: E501
        :rtype: str
        """
        return self._learning_standard_id

    @learning_standard_id.setter
    def learning_standard_id(self, learning_standard_id):
        """Sets the learning_standard_id of this EdFiLearningStandard.

        The identifier for the specific learning standard (e.g., 111.15.3.1.A).  # noqa: E501

        :param learning_standard_id: The learning_standard_id of this EdFiLearningStandard.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and learning_standard_id is None:
            raise ValueError("Invalid value for `learning_standard_id`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                learning_standard_id is not None and len(learning_standard_id) > 60):
            raise ValueError("Invalid value for `learning_standard_id`, length must be less than or equal to `60`")  # noqa: E501

        self._learning_standard_id = learning_standard_id

    @property
    def parent_learning_standard_reference(self):
        """Gets the parent_learning_standard_reference of this EdFiLearningStandard.  # noqa: E501


        :return: The parent_learning_standard_reference of this EdFiLearningStandard.  # noqa: E501
        :rtype: EdFiLearningStandardReference
        """
        return self._parent_learning_standard_reference

    @parent_learning_standard_reference.setter
    def parent_learning_standard_reference(self, parent_learning_standard_reference):
        """Sets the parent_learning_standard_reference of this EdFiLearningStandard.


        :param parent_learning_standard_reference: The parent_learning_standard_reference of this EdFiLearningStandard.  # noqa: E501
        :type: EdFiLearningStandardReference
        """

        self._parent_learning_standard_reference = parent_learning_standard_reference

    @property
    def content_standard(self):
        """Gets the content_standard of this EdFiLearningStandard.  # noqa: E501


        :return: The content_standard of this EdFiLearningStandard.  # noqa: E501
        :rtype: EdFiLearningStandardContentStandard
        """
        return self._content_standard

    @content_standard.setter
    def content_standard(self, content_standard):
        """Sets the content_standard of this EdFiLearningStandard.


        :param content_standard: The content_standard of this EdFiLearningStandard.  # noqa: E501
        :type: EdFiLearningStandardContentStandard
        """

        self._content_standard = content_standard

    @property
    def course_title(self):
        """Gets the course_title of this EdFiLearningStandard.  # noqa: E501

        The official Course Title with which this learning standard is associated.  # noqa: E501

        :return: The course_title of this EdFiLearningStandard.  # noqa: E501
        :rtype: str
        """
        return self._course_title

    @course_title.setter
    def course_title(self, course_title):
        """Sets the course_title of this EdFiLearningStandard.

        The official Course Title with which this learning standard is associated.  # noqa: E501

        :param course_title: The course_title of this EdFiLearningStandard.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                course_title is not None and len(course_title) > 60):
            raise ValueError("Invalid value for `course_title`, length must be less than or equal to `60`")  # noqa: E501

        self._course_title = course_title

    @property
    def description(self):
        """Gets the description of this EdFiLearningStandard.  # noqa: E501

        The text of the statement. The textual content that either describes a specific competency such as \"Apply the Pythagorean Theorem to determine unknown side lengths in right triangles in real-world and mathematical problems in two and three dimensions.\" or describes a less granular group of competencies within the taxonomy of the standards document, e.g. \"Understand and apply the Pythagorean Theorem,\" or \"Geometry\".  # noqa: E501

        :return: The description of this EdFiLearningStandard.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this EdFiLearningStandard.

        The text of the statement. The textual content that either describes a specific competency such as \"Apply the Pythagorean Theorem to determine unknown side lengths in right triangles in real-world and mathematical problems in two and three dimensions.\" or describes a less granular group of competencies within the taxonomy of the standards document, e.g. \"Understand and apply the Pythagorean Theorem,\" or \"Geometry\".  # noqa: E501

        :param description: The description of this EdFiLearningStandard.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                description is not None and len(description) > 1024):
            raise ValueError("Invalid value for `description`, length must be less than or equal to `1024`")  # noqa: E501

        self._description = description

    @property
    def identification_codes(self):
        """Gets the identification_codes of this EdFiLearningStandard.  # noqa: E501

        An unordered collection of learningStandardIdentificationCodes. A coding scheme that is used for identification and record-keeping purposes by schools, social services, or other agencies to refer to a learning standard.  # noqa: E501

        :return: The identification_codes of this EdFiLearningStandard.  # noqa: E501
        :rtype: list[EdFiLearningStandardIdentificationCode]
        """
        return self._identification_codes

    @identification_codes.setter
    def identification_codes(self, identification_codes):
        """Sets the identification_codes of this EdFiLearningStandard.

        An unordered collection of learningStandardIdentificationCodes. A coding scheme that is used for identification and record-keeping purposes by schools, social services, or other agencies to refer to a learning standard.  # noqa: E501

        :param identification_codes: The identification_codes of this EdFiLearningStandard.  # noqa: E501
        :type: list[EdFiLearningStandardIdentificationCode]
        """

        self._identification_codes = identification_codes

    @property
    def learning_standard_category_descriptor(self):
        """Gets the learning_standard_category_descriptor of this EdFiLearningStandard.  # noqa: E501

        An additional classification of the type of a specific learning standard.  # noqa: E501

        :return: The learning_standard_category_descriptor of this EdFiLearningStandard.  # noqa: E501
        :rtype: str
        """
        return self._learning_standard_category_descriptor

    @learning_standard_category_descriptor.setter
    def learning_standard_category_descriptor(self, learning_standard_category_descriptor):
        """Sets the learning_standard_category_descriptor of this EdFiLearningStandard.

        An additional classification of the type of a specific learning standard.  # noqa: E501

        :param learning_standard_category_descriptor: The learning_standard_category_descriptor of this EdFiLearningStandard.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                learning_standard_category_descriptor is not None and len(learning_standard_category_descriptor) > 306):
            raise ValueError("Invalid value for `learning_standard_category_descriptor`, length must be less than or equal to `306`")  # noqa: E501

        self._learning_standard_category_descriptor = learning_standard_category_descriptor

    @property
    def learning_standard_item_code(self):
        """Gets the learning_standard_item_code of this EdFiLearningStandard.  # noqa: E501

        A code designated by the promulgating body to identify the statement, e.g. 1.N.3 (usually not globally unique).  # noqa: E501

        :return: The learning_standard_item_code of this EdFiLearningStandard.  # noqa: E501
        :rtype: str
        """
        return self._learning_standard_item_code

    @learning_standard_item_code.setter
    def learning_standard_item_code(self, learning_standard_item_code):
        """Sets the learning_standard_item_code of this EdFiLearningStandard.

        A code designated by the promulgating body to identify the statement, e.g. 1.N.3 (usually not globally unique).  # noqa: E501

        :param learning_standard_item_code: The learning_standard_item_code of this EdFiLearningStandard.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                learning_standard_item_code is not None and len(learning_standard_item_code) > 60):
            raise ValueError("Invalid value for `learning_standard_item_code`, length must be less than or equal to `60`")  # noqa: E501

        self._learning_standard_item_code = learning_standard_item_code

    @property
    def learning_standard_scope_descriptor(self):
        """Gets the learning_standard_scope_descriptor of this EdFiLearningStandard.  # noqa: E501

        Signals the scope of usage the standard. Does not necessarily relate the standard to the governing body.  # noqa: E501

        :return: The learning_standard_scope_descriptor of this EdFiLearningStandard.  # noqa: E501
        :rtype: str
        """
        return self._learning_standard_scope_descriptor

    @learning_standard_scope_descriptor.setter
    def learning_standard_scope_descriptor(self, learning_standard_scope_descriptor):
        """Sets the learning_standard_scope_descriptor of this EdFiLearningStandard.

        Signals the scope of usage the standard. Does not necessarily relate the standard to the governing body.  # noqa: E501

        :param learning_standard_scope_descriptor: The learning_standard_scope_descriptor of this EdFiLearningStandard.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                learning_standard_scope_descriptor is not None and len(learning_standard_scope_descriptor) > 306):
            raise ValueError("Invalid value for `learning_standard_scope_descriptor`, length must be less than or equal to `306`")  # noqa: E501

        self._learning_standard_scope_descriptor = learning_standard_scope_descriptor

    @property
    def namespace(self):
        """Gets the namespace of this EdFiLearningStandard.  # noqa: E501

        The namespace of the organization or entity who governs the standard. It is recommended the namespaces observe a URI format and begin with a domain name under the governing organization or entity control.  # noqa: E501

        :return: The namespace of this EdFiLearningStandard.  # noqa: E501
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """Sets the namespace of this EdFiLearningStandard.

        The namespace of the organization or entity who governs the standard. It is recommended the namespaces observe a URI format and begin with a domain name under the governing organization or entity control.  # noqa: E501

        :param namespace: The namespace of this EdFiLearningStandard.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and namespace is None:
            raise ValueError("Invalid value for `namespace`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                namespace is not None and len(namespace) > 255):
            raise ValueError("Invalid value for `namespace`, length must be less than or equal to `255`")  # noqa: E501

        self._namespace = namespace

    @property
    def prerequisite_learning_standards(self):
        """Gets the prerequisite_learning_standards of this EdFiLearningStandard.  # noqa: E501

        An unordered collection of learningStandardPrerequisiteLearningStandards. The unique identifier of a prerequisite learning standard item, a competency needed prior to learning this one. (Some items may have no prerequisites others may have one or more prerequisites. This should only be used to represent the immediate predecessors in a competency-based pathway, i.e. not prerequisites of prerequisites).  # noqa: E501

        :return: The prerequisite_learning_standards of this EdFiLearningStandard.  # noqa: E501
        :rtype: list[EdFiLearningStandardPrerequisiteLearningStandard]
        """
        return self._prerequisite_learning_standards

    @prerequisite_learning_standards.setter
    def prerequisite_learning_standards(self, prerequisite_learning_standards):
        """Sets the prerequisite_learning_standards of this EdFiLearningStandard.

        An unordered collection of learningStandardPrerequisiteLearningStandards. The unique identifier of a prerequisite learning standard item, a competency needed prior to learning this one. (Some items may have no prerequisites others may have one or more prerequisites. This should only be used to represent the immediate predecessors in a competency-based pathway, i.e. not prerequisites of prerequisites).  # noqa: E501

        :param prerequisite_learning_standards: The prerequisite_learning_standards of this EdFiLearningStandard.  # noqa: E501
        :type: list[EdFiLearningStandardPrerequisiteLearningStandard]
        """

        self._prerequisite_learning_standards = prerequisite_learning_standards

    @property
    def success_criteria(self):
        """Gets the success_criteria of this EdFiLearningStandard.  # noqa: E501

        One or more statements that describes the criteria used by teachers and students to check for attainment of a learning standard. This criteria gives clear indications as to the degree to which learning is moving through the Zone or Proximal Development toward independent achievement of the LearningStandard.  # noqa: E501

        :return: The success_criteria of this EdFiLearningStandard.  # noqa: E501
        :rtype: str
        """
        return self._success_criteria

    @success_criteria.setter
    def success_criteria(self, success_criteria):
        """Sets the success_criteria of this EdFiLearningStandard.

        One or more statements that describes the criteria used by teachers and students to check for attainment of a learning standard. This criteria gives clear indications as to the degree to which learning is moving through the Zone or Proximal Development toward independent achievement of the LearningStandard.  # noqa: E501

        :param success_criteria: The success_criteria of this EdFiLearningStandard.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                success_criteria is not None and len(success_criteria) > 150):
            raise ValueError("Invalid value for `success_criteria`, length must be less than or equal to `150`")  # noqa: E501

        self._success_criteria = success_criteria

    @property
    def uri(self):
        """Gets the uri of this EdFiLearningStandard.  # noqa: E501

        An unambiguous reference to the statement using a network-resolvable URI.  # noqa: E501

        :return: The uri of this EdFiLearningStandard.  # noqa: E501
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """Sets the uri of this EdFiLearningStandard.

        An unambiguous reference to the statement using a network-resolvable URI.  # noqa: E501

        :param uri: The uri of this EdFiLearningStandard.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                uri is not None and len(uri) > 255):
            raise ValueError("Invalid value for `uri`, length must be less than or equal to `255`")  # noqa: E501

        self._uri = uri

    @property
    def etag(self):
        """Gets the etag of this EdFiLearningStandard.  # noqa: E501

        A unique system-generated value that identifies the version of the resource.  # noqa: E501

        :return: The etag of this EdFiLearningStandard.  # noqa: E501
        :rtype: str
        """
        return self._etag

    @etag.setter
    def etag(self, etag):
        """Sets the etag of this EdFiLearningStandard.

        A unique system-generated value that identifies the version of the resource.  # noqa: E501

        :param etag: The etag of this EdFiLearningStandard.  # noqa: E501
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
        if issubclass(EdFiLearningStandard, dict):
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
        if not isinstance(other, EdFiLearningStandard):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EdFiLearningStandard):
            return True

        return self.to_dict() != other.to_dict()
