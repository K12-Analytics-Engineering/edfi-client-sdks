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


class EdFiAccountabilityRating(object):
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
        'rating_title': 'str',
        'education_organization_reference': 'EdFiEducationOrganizationReference',
        'school_year_type_reference': 'EdFiSchoolYearTypeReference',
        'rating': 'str',
        'rating_date': 'date',
        'rating_organization': 'str',
        'rating_program': 'str',
        'etag': 'str'
    }

    attribute_map = {
        'id': 'id',
        'rating_title': 'ratingTitle',
        'education_organization_reference': 'educationOrganizationReference',
        'school_year_type_reference': 'schoolYearTypeReference',
        'rating': 'rating',
        'rating_date': 'ratingDate',
        'rating_organization': 'ratingOrganization',
        'rating_program': 'ratingProgram',
        'etag': '_etag'
    }

    def __init__(self, id=None, rating_title=None, education_organization_reference=None, school_year_type_reference=None, rating=None, rating_date=None, rating_organization=None, rating_program=None, etag=None, _configuration=None):  # noqa: E501
        """EdFiAccountabilityRating - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._rating_title = None
        self._education_organization_reference = None
        self._school_year_type_reference = None
        self._rating = None
        self._rating_date = None
        self._rating_organization = None
        self._rating_program = None
        self._etag = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.rating_title = rating_title
        self.education_organization_reference = education_organization_reference
        self.school_year_type_reference = school_year_type_reference
        self.rating = rating
        if rating_date is not None:
            self.rating_date = rating_date
        if rating_organization is not None:
            self.rating_organization = rating_organization
        if rating_program is not None:
            self.rating_program = rating_program
        if etag is not None:
            self.etag = etag

    @property
    def id(self):
        """Gets the id of this EdFiAccountabilityRating.  # noqa: E501

          # noqa: E501

        :return: The id of this EdFiAccountabilityRating.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this EdFiAccountabilityRating.

          # noqa: E501

        :param id: The id of this EdFiAccountabilityRating.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def rating_title(self):
        """Gets the rating_title of this EdFiAccountabilityRating.  # noqa: E501

        The title of the rating.  # noqa: E501

        :return: The rating_title of this EdFiAccountabilityRating.  # noqa: E501
        :rtype: str
        """
        return self._rating_title

    @rating_title.setter
    def rating_title(self, rating_title):
        """Sets the rating_title of this EdFiAccountabilityRating.

        The title of the rating.  # noqa: E501

        :param rating_title: The rating_title of this EdFiAccountabilityRating.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and rating_title is None:
            raise ValueError("Invalid value for `rating_title`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                rating_title is not None and len(rating_title) > 60):
            raise ValueError("Invalid value for `rating_title`, length must be less than or equal to `60`")  # noqa: E501

        self._rating_title = rating_title

    @property
    def education_organization_reference(self):
        """Gets the education_organization_reference of this EdFiAccountabilityRating.  # noqa: E501


        :return: The education_organization_reference of this EdFiAccountabilityRating.  # noqa: E501
        :rtype: EdFiEducationOrganizationReference
        """
        return self._education_organization_reference

    @education_organization_reference.setter
    def education_organization_reference(self, education_organization_reference):
        """Sets the education_organization_reference of this EdFiAccountabilityRating.


        :param education_organization_reference: The education_organization_reference of this EdFiAccountabilityRating.  # noqa: E501
        :type: EdFiEducationOrganizationReference
        """
        if self._configuration.client_side_validation and education_organization_reference is None:
            raise ValueError("Invalid value for `education_organization_reference`, must not be `None`")  # noqa: E501

        self._education_organization_reference = education_organization_reference

    @property
    def school_year_type_reference(self):
        """Gets the school_year_type_reference of this EdFiAccountabilityRating.  # noqa: E501


        :return: The school_year_type_reference of this EdFiAccountabilityRating.  # noqa: E501
        :rtype: EdFiSchoolYearTypeReference
        """
        return self._school_year_type_reference

    @school_year_type_reference.setter
    def school_year_type_reference(self, school_year_type_reference):
        """Sets the school_year_type_reference of this EdFiAccountabilityRating.


        :param school_year_type_reference: The school_year_type_reference of this EdFiAccountabilityRating.  # noqa: E501
        :type: EdFiSchoolYearTypeReference
        """
        if self._configuration.client_side_validation and school_year_type_reference is None:
            raise ValueError("Invalid value for `school_year_type_reference`, must not be `None`")  # noqa: E501

        self._school_year_type_reference = school_year_type_reference

    @property
    def rating(self):
        """Gets the rating of this EdFiAccountabilityRating.  # noqa: E501

        An accountability rating level, designation, or assessment.  # noqa: E501

        :return: The rating of this EdFiAccountabilityRating.  # noqa: E501
        :rtype: str
        """
        return self._rating

    @rating.setter
    def rating(self, rating):
        """Sets the rating of this EdFiAccountabilityRating.

        An accountability rating level, designation, or assessment.  # noqa: E501

        :param rating: The rating of this EdFiAccountabilityRating.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and rating is None:
            raise ValueError("Invalid value for `rating`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                rating is not None and len(rating) > 35):
            raise ValueError("Invalid value for `rating`, length must be less than or equal to `35`")  # noqa: E501

        self._rating = rating

    @property
    def rating_date(self):
        """Gets the rating_date of this EdFiAccountabilityRating.  # noqa: E501

        The date the rating was awarded.  # noqa: E501

        :return: The rating_date of this EdFiAccountabilityRating.  # noqa: E501
        :rtype: date
        """
        return self._rating_date

    @rating_date.setter
    def rating_date(self, rating_date):
        """Sets the rating_date of this EdFiAccountabilityRating.

        The date the rating was awarded.  # noqa: E501

        :param rating_date: The rating_date of this EdFiAccountabilityRating.  # noqa: E501
        :type: date
        """

        self._rating_date = rating_date

    @property
    def rating_organization(self):
        """Gets the rating_organization of this EdFiAccountabilityRating.  # noqa: E501

        The organization that assessed the rating.  # noqa: E501

        :return: The rating_organization of this EdFiAccountabilityRating.  # noqa: E501
        :rtype: str
        """
        return self._rating_organization

    @rating_organization.setter
    def rating_organization(self, rating_organization):
        """Sets the rating_organization of this EdFiAccountabilityRating.

        The organization that assessed the rating.  # noqa: E501

        :param rating_organization: The rating_organization of this EdFiAccountabilityRating.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                rating_organization is not None and len(rating_organization) > 35):
            raise ValueError("Invalid value for `rating_organization`, length must be less than or equal to `35`")  # noqa: E501

        self._rating_organization = rating_organization

    @property
    def rating_program(self):
        """Gets the rating_program of this EdFiAccountabilityRating.  # noqa: E501

        The program associated with the accountability rating (e.g., NCLB, AEIS).  # noqa: E501

        :return: The rating_program of this EdFiAccountabilityRating.  # noqa: E501
        :rtype: str
        """
        return self._rating_program

    @rating_program.setter
    def rating_program(self, rating_program):
        """Sets the rating_program of this EdFiAccountabilityRating.

        The program associated with the accountability rating (e.g., NCLB, AEIS).  # noqa: E501

        :param rating_program: The rating_program of this EdFiAccountabilityRating.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                rating_program is not None and len(rating_program) > 30):
            raise ValueError("Invalid value for `rating_program`, length must be less than or equal to `30`")  # noqa: E501

        self._rating_program = rating_program

    @property
    def etag(self):
        """Gets the etag of this EdFiAccountabilityRating.  # noqa: E501

        A unique system-generated value that identifies the version of the resource.  # noqa: E501

        :return: The etag of this EdFiAccountabilityRating.  # noqa: E501
        :rtype: str
        """
        return self._etag

    @etag.setter
    def etag(self, etag):
        """Sets the etag of this EdFiAccountabilityRating.

        A unique system-generated value that identifies the version of the resource.  # noqa: E501

        :param etag: The etag of this EdFiAccountabilityRating.  # noqa: E501
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
        if issubclass(EdFiAccountabilityRating, dict):
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
        if not isinstance(other, EdFiAccountabilityRating):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EdFiAccountabilityRating):
            return True

        return self.to_dict() != other.to_dict()
