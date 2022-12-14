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


class EdFiSchool(object):
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
        'education_organization_categories': 'list[EdFiEducationOrganizationCategory]',
        'grade_levels': 'list[EdFiSchoolGradeLevel]',
        'school_id': 'int',
        'charter_approval_school_year_type_reference': 'EdFiSchoolYearTypeReference',
        'local_education_agency_reference': 'EdFiLocalEducationAgencyReference',
        'addresses': 'list[EdFiEducationOrganizationAddress]',
        'administrative_funding_control_descriptor': 'str',
        'charter_approval_agency_type_descriptor': 'str',
        'charter_status_descriptor': 'str',
        'identification_codes': 'list[EdFiEducationOrganizationIdentificationCode]',
        'indicators': 'list[EdFiEducationOrganizationIndicator]',
        'institution_telephones': 'list[EdFiEducationOrganizationInstitutionTelephone]',
        'international_addresses': 'list[EdFiEducationOrganizationInternationalAddress]',
        'internet_access_descriptor': 'str',
        'magnet_special_program_emphasis_school_descriptor': 'str',
        'name_of_institution': 'str',
        'operational_status_descriptor': 'str',
        'school_categories': 'list[EdFiSchoolCategory]',
        'school_type_descriptor': 'str',
        'short_name_of_institution': 'str',
        'title_i_part_a_school_designation_descriptor': 'str',
        'web_site': 'str',
        'etag': 'str',
        'ext': 'SchoolExtensions'
    }

    attribute_map = {
        'id': 'id',
        'education_organization_categories': 'educationOrganizationCategories',
        'grade_levels': 'gradeLevels',
        'school_id': 'schoolId',
        'charter_approval_school_year_type_reference': 'charterApprovalSchoolYearTypeReference',
        'local_education_agency_reference': 'localEducationAgencyReference',
        'addresses': 'addresses',
        'administrative_funding_control_descriptor': 'administrativeFundingControlDescriptor',
        'charter_approval_agency_type_descriptor': 'charterApprovalAgencyTypeDescriptor',
        'charter_status_descriptor': 'charterStatusDescriptor',
        'identification_codes': 'identificationCodes',
        'indicators': 'indicators',
        'institution_telephones': 'institutionTelephones',
        'international_addresses': 'internationalAddresses',
        'internet_access_descriptor': 'internetAccessDescriptor',
        'magnet_special_program_emphasis_school_descriptor': 'magnetSpecialProgramEmphasisSchoolDescriptor',
        'name_of_institution': 'nameOfInstitution',
        'operational_status_descriptor': 'operationalStatusDescriptor',
        'school_categories': 'schoolCategories',
        'school_type_descriptor': 'schoolTypeDescriptor',
        'short_name_of_institution': 'shortNameOfInstitution',
        'title_i_part_a_school_designation_descriptor': 'titleIPartASchoolDesignationDescriptor',
        'web_site': 'webSite',
        'etag': '_etag',
        'ext': '_ext'
    }

    def __init__(self, id=None, education_organization_categories=None, grade_levels=None, school_id=None, charter_approval_school_year_type_reference=None, local_education_agency_reference=None, addresses=None, administrative_funding_control_descriptor=None, charter_approval_agency_type_descriptor=None, charter_status_descriptor=None, identification_codes=None, indicators=None, institution_telephones=None, international_addresses=None, internet_access_descriptor=None, magnet_special_program_emphasis_school_descriptor=None, name_of_institution=None, operational_status_descriptor=None, school_categories=None, school_type_descriptor=None, short_name_of_institution=None, title_i_part_a_school_designation_descriptor=None, web_site=None, etag=None, ext=None, _configuration=None):  # noqa: E501
        """EdFiSchool - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._education_organization_categories = None
        self._grade_levels = None
        self._school_id = None
        self._charter_approval_school_year_type_reference = None
        self._local_education_agency_reference = None
        self._addresses = None
        self._administrative_funding_control_descriptor = None
        self._charter_approval_agency_type_descriptor = None
        self._charter_status_descriptor = None
        self._identification_codes = None
        self._indicators = None
        self._institution_telephones = None
        self._international_addresses = None
        self._internet_access_descriptor = None
        self._magnet_special_program_emphasis_school_descriptor = None
        self._name_of_institution = None
        self._operational_status_descriptor = None
        self._school_categories = None
        self._school_type_descriptor = None
        self._short_name_of_institution = None
        self._title_i_part_a_school_designation_descriptor = None
        self._web_site = None
        self._etag = None
        self._ext = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.education_organization_categories = education_organization_categories
        self.grade_levels = grade_levels
        self.school_id = school_id
        if charter_approval_school_year_type_reference is not None:
            self.charter_approval_school_year_type_reference = charter_approval_school_year_type_reference
        if local_education_agency_reference is not None:
            self.local_education_agency_reference = local_education_agency_reference
        if addresses is not None:
            self.addresses = addresses
        if administrative_funding_control_descriptor is not None:
            self.administrative_funding_control_descriptor = administrative_funding_control_descriptor
        if charter_approval_agency_type_descriptor is not None:
            self.charter_approval_agency_type_descriptor = charter_approval_agency_type_descriptor
        if charter_status_descriptor is not None:
            self.charter_status_descriptor = charter_status_descriptor
        if identification_codes is not None:
            self.identification_codes = identification_codes
        if indicators is not None:
            self.indicators = indicators
        if institution_telephones is not None:
            self.institution_telephones = institution_telephones
        if international_addresses is not None:
            self.international_addresses = international_addresses
        if internet_access_descriptor is not None:
            self.internet_access_descriptor = internet_access_descriptor
        if magnet_special_program_emphasis_school_descriptor is not None:
            self.magnet_special_program_emphasis_school_descriptor = magnet_special_program_emphasis_school_descriptor
        self.name_of_institution = name_of_institution
        if operational_status_descriptor is not None:
            self.operational_status_descriptor = operational_status_descriptor
        if school_categories is not None:
            self.school_categories = school_categories
        if school_type_descriptor is not None:
            self.school_type_descriptor = school_type_descriptor
        if short_name_of_institution is not None:
            self.short_name_of_institution = short_name_of_institution
        if title_i_part_a_school_designation_descriptor is not None:
            self.title_i_part_a_school_designation_descriptor = title_i_part_a_school_designation_descriptor
        if web_site is not None:
            self.web_site = web_site
        if etag is not None:
            self.etag = etag
        if ext is not None:
            self.ext = ext

    @property
    def id(self):
        """Gets the id of this EdFiSchool.  # noqa: E501

          # noqa: E501

        :return: The id of this EdFiSchool.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this EdFiSchool.

          # noqa: E501

        :param id: The id of this EdFiSchool.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def education_organization_categories(self):
        """Gets the education_organization_categories of this EdFiSchool.  # noqa: E501

        An unordered collection of educationOrganizationCategories. The classification of the education agency within the geographic boundaries of a state according to the level of administrative and operational control granted by the state.  # noqa: E501

        :return: The education_organization_categories of this EdFiSchool.  # noqa: E501
        :rtype: list[EdFiEducationOrganizationCategory]
        """
        return self._education_organization_categories

    @education_organization_categories.setter
    def education_organization_categories(self, education_organization_categories):
        """Sets the education_organization_categories of this EdFiSchool.

        An unordered collection of educationOrganizationCategories. The classification of the education agency within the geographic boundaries of a state according to the level of administrative and operational control granted by the state.  # noqa: E501

        :param education_organization_categories: The education_organization_categories of this EdFiSchool.  # noqa: E501
        :type: list[EdFiEducationOrganizationCategory]
        """
        if self._configuration.client_side_validation and education_organization_categories is None:
            raise ValueError("Invalid value for `education_organization_categories`, must not be `None`")  # noqa: E501

        self._education_organization_categories = education_organization_categories

    @property
    def grade_levels(self):
        """Gets the grade_levels of this EdFiSchool.  # noqa: E501

        An unordered collection of schoolGradeLevels. The grade levels served at the school.  # noqa: E501

        :return: The grade_levels of this EdFiSchool.  # noqa: E501
        :rtype: list[EdFiSchoolGradeLevel]
        """
        return self._grade_levels

    @grade_levels.setter
    def grade_levels(self, grade_levels):
        """Sets the grade_levels of this EdFiSchool.

        An unordered collection of schoolGradeLevels. The grade levels served at the school.  # noqa: E501

        :param grade_levels: The grade_levels of this EdFiSchool.  # noqa: E501
        :type: list[EdFiSchoolGradeLevel]
        """
        if self._configuration.client_side_validation and grade_levels is None:
            raise ValueError("Invalid value for `grade_levels`, must not be `None`")  # noqa: E501

        self._grade_levels = grade_levels

    @property
    def school_id(self):
        """Gets the school_id of this EdFiSchool.  # noqa: E501

        The identifier assigned to a school.  # noqa: E501

        :return: The school_id of this EdFiSchool.  # noqa: E501
        :rtype: int
        """
        return self._school_id

    @school_id.setter
    def school_id(self, school_id):
        """Sets the school_id of this EdFiSchool.

        The identifier assigned to a school.  # noqa: E501

        :param school_id: The school_id of this EdFiSchool.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and school_id is None:
            raise ValueError("Invalid value for `school_id`, must not be `None`")  # noqa: E501

        self._school_id = school_id

    @property
    def charter_approval_school_year_type_reference(self):
        """Gets the charter_approval_school_year_type_reference of this EdFiSchool.  # noqa: E501


        :return: The charter_approval_school_year_type_reference of this EdFiSchool.  # noqa: E501
        :rtype: EdFiSchoolYearTypeReference
        """
        return self._charter_approval_school_year_type_reference

    @charter_approval_school_year_type_reference.setter
    def charter_approval_school_year_type_reference(self, charter_approval_school_year_type_reference):
        """Sets the charter_approval_school_year_type_reference of this EdFiSchool.


        :param charter_approval_school_year_type_reference: The charter_approval_school_year_type_reference of this EdFiSchool.  # noqa: E501
        :type: EdFiSchoolYearTypeReference
        """

        self._charter_approval_school_year_type_reference = charter_approval_school_year_type_reference

    @property
    def local_education_agency_reference(self):
        """Gets the local_education_agency_reference of this EdFiSchool.  # noqa: E501


        :return: The local_education_agency_reference of this EdFiSchool.  # noqa: E501
        :rtype: EdFiLocalEducationAgencyReference
        """
        return self._local_education_agency_reference

    @local_education_agency_reference.setter
    def local_education_agency_reference(self, local_education_agency_reference):
        """Sets the local_education_agency_reference of this EdFiSchool.


        :param local_education_agency_reference: The local_education_agency_reference of this EdFiSchool.  # noqa: E501
        :type: EdFiLocalEducationAgencyReference
        """

        self._local_education_agency_reference = local_education_agency_reference

    @property
    def addresses(self):
        """Gets the addresses of this EdFiSchool.  # noqa: E501

        An unordered collection of educationOrganizationAddresses. The set of elements that describes an address for the education entity, including the street address, city, state, ZIP code, and ZIP code + 4.  # noqa: E501

        :return: The addresses of this EdFiSchool.  # noqa: E501
        :rtype: list[EdFiEducationOrganizationAddress]
        """
        return self._addresses

    @addresses.setter
    def addresses(self, addresses):
        """Sets the addresses of this EdFiSchool.

        An unordered collection of educationOrganizationAddresses. The set of elements that describes an address for the education entity, including the street address, city, state, ZIP code, and ZIP code + 4.  # noqa: E501

        :param addresses: The addresses of this EdFiSchool.  # noqa: E501
        :type: list[EdFiEducationOrganizationAddress]
        """

        self._addresses = addresses

    @property
    def administrative_funding_control_descriptor(self):
        """Gets the administrative_funding_control_descriptor of this EdFiSchool.  # noqa: E501

        The type of education institution as classified by its funding source, for example public or private.  # noqa: E501

        :return: The administrative_funding_control_descriptor of this EdFiSchool.  # noqa: E501
        :rtype: str
        """
        return self._administrative_funding_control_descriptor

    @administrative_funding_control_descriptor.setter
    def administrative_funding_control_descriptor(self, administrative_funding_control_descriptor):
        """Sets the administrative_funding_control_descriptor of this EdFiSchool.

        The type of education institution as classified by its funding source, for example public or private.  # noqa: E501

        :param administrative_funding_control_descriptor: The administrative_funding_control_descriptor of this EdFiSchool.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                administrative_funding_control_descriptor is not None and len(administrative_funding_control_descriptor) > 306):
            raise ValueError("Invalid value for `administrative_funding_control_descriptor`, length must be less than or equal to `306`")  # noqa: E501

        self._administrative_funding_control_descriptor = administrative_funding_control_descriptor

    @property
    def charter_approval_agency_type_descriptor(self):
        """Gets the charter_approval_agency_type_descriptor of this EdFiSchool.  # noqa: E501

        The type of agency that approved the establishment or continuation of a charter school.  # noqa: E501

        :return: The charter_approval_agency_type_descriptor of this EdFiSchool.  # noqa: E501
        :rtype: str
        """
        return self._charter_approval_agency_type_descriptor

    @charter_approval_agency_type_descriptor.setter
    def charter_approval_agency_type_descriptor(self, charter_approval_agency_type_descriptor):
        """Sets the charter_approval_agency_type_descriptor of this EdFiSchool.

        The type of agency that approved the establishment or continuation of a charter school.  # noqa: E501

        :param charter_approval_agency_type_descriptor: The charter_approval_agency_type_descriptor of this EdFiSchool.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                charter_approval_agency_type_descriptor is not None and len(charter_approval_agency_type_descriptor) > 306):
            raise ValueError("Invalid value for `charter_approval_agency_type_descriptor`, length must be less than or equal to `306`")  # noqa: E501

        self._charter_approval_agency_type_descriptor = charter_approval_agency_type_descriptor

    @property
    def charter_status_descriptor(self):
        """Gets the charter_status_descriptor of this EdFiSchool.  # noqa: E501

        A school or agency providing free public elementary or secondary education to eligible students under a specific charter granted by the state legislature or other appropriate authority and designated by such authority to be a charter school.  # noqa: E501

        :return: The charter_status_descriptor of this EdFiSchool.  # noqa: E501
        :rtype: str
        """
        return self._charter_status_descriptor

    @charter_status_descriptor.setter
    def charter_status_descriptor(self, charter_status_descriptor):
        """Sets the charter_status_descriptor of this EdFiSchool.

        A school or agency providing free public elementary or secondary education to eligible students under a specific charter granted by the state legislature or other appropriate authority and designated by such authority to be a charter school.  # noqa: E501

        :param charter_status_descriptor: The charter_status_descriptor of this EdFiSchool.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                charter_status_descriptor is not None and len(charter_status_descriptor) > 306):
            raise ValueError("Invalid value for `charter_status_descriptor`, length must be less than or equal to `306`")  # noqa: E501

        self._charter_status_descriptor = charter_status_descriptor

    @property
    def identification_codes(self):
        """Gets the identification_codes of this EdFiSchool.  # noqa: E501

        An unordered collection of educationOrganizationIdentificationCodes. A unique number or alphanumeric code assigned to an education organization by a school, school system, a state, or other agency or entity.  # noqa: E501

        :return: The identification_codes of this EdFiSchool.  # noqa: E501
        :rtype: list[EdFiEducationOrganizationIdentificationCode]
        """
        return self._identification_codes

    @identification_codes.setter
    def identification_codes(self, identification_codes):
        """Sets the identification_codes of this EdFiSchool.

        An unordered collection of educationOrganizationIdentificationCodes. A unique number or alphanumeric code assigned to an education organization by a school, school system, a state, or other agency or entity.  # noqa: E501

        :param identification_codes: The identification_codes of this EdFiSchool.  # noqa: E501
        :type: list[EdFiEducationOrganizationIdentificationCode]
        """

        self._identification_codes = identification_codes

    @property
    def indicators(self):
        """Gets the indicators of this EdFiSchool.  # noqa: E501

        An unordered collection of educationOrganizationIndicators. An indicator or metric of an education organization.  # noqa: E501

        :return: The indicators of this EdFiSchool.  # noqa: E501
        :rtype: list[EdFiEducationOrganizationIndicator]
        """
        return self._indicators

    @indicators.setter
    def indicators(self, indicators):
        """Sets the indicators of this EdFiSchool.

        An unordered collection of educationOrganizationIndicators. An indicator or metric of an education organization.  # noqa: E501

        :param indicators: The indicators of this EdFiSchool.  # noqa: E501
        :type: list[EdFiEducationOrganizationIndicator]
        """

        self._indicators = indicators

    @property
    def institution_telephones(self):
        """Gets the institution_telephones of this EdFiSchool.  # noqa: E501

        An unordered collection of educationOrganizationInstitutionTelephones. The 10-digit telephone number, including the area code, for the education entity.  # noqa: E501

        :return: The institution_telephones of this EdFiSchool.  # noqa: E501
        :rtype: list[EdFiEducationOrganizationInstitutionTelephone]
        """
        return self._institution_telephones

    @institution_telephones.setter
    def institution_telephones(self, institution_telephones):
        """Sets the institution_telephones of this EdFiSchool.

        An unordered collection of educationOrganizationInstitutionTelephones. The 10-digit telephone number, including the area code, for the education entity.  # noqa: E501

        :param institution_telephones: The institution_telephones of this EdFiSchool.  # noqa: E501
        :type: list[EdFiEducationOrganizationInstitutionTelephone]
        """

        self._institution_telephones = institution_telephones

    @property
    def international_addresses(self):
        """Gets the international_addresses of this EdFiSchool.  # noqa: E501

        An unordered collection of educationOrganizationInternationalAddresses. The set of elements that describes the international physical location of the education entity.  # noqa: E501

        :return: The international_addresses of this EdFiSchool.  # noqa: E501
        :rtype: list[EdFiEducationOrganizationInternationalAddress]
        """
        return self._international_addresses

    @international_addresses.setter
    def international_addresses(self, international_addresses):
        """Sets the international_addresses of this EdFiSchool.

        An unordered collection of educationOrganizationInternationalAddresses. The set of elements that describes the international physical location of the education entity.  # noqa: E501

        :param international_addresses: The international_addresses of this EdFiSchool.  # noqa: E501
        :type: list[EdFiEducationOrganizationInternationalAddress]
        """

        self._international_addresses = international_addresses

    @property
    def internet_access_descriptor(self):
        """Gets the internet_access_descriptor of this EdFiSchool.  # noqa: E501

        The type of Internet access available.  # noqa: E501

        :return: The internet_access_descriptor of this EdFiSchool.  # noqa: E501
        :rtype: str
        """
        return self._internet_access_descriptor

    @internet_access_descriptor.setter
    def internet_access_descriptor(self, internet_access_descriptor):
        """Sets the internet_access_descriptor of this EdFiSchool.

        The type of Internet access available.  # noqa: E501

        :param internet_access_descriptor: The internet_access_descriptor of this EdFiSchool.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                internet_access_descriptor is not None and len(internet_access_descriptor) > 306):
            raise ValueError("Invalid value for `internet_access_descriptor`, length must be less than or equal to `306`")  # noqa: E501

        self._internet_access_descriptor = internet_access_descriptor

    @property
    def magnet_special_program_emphasis_school_descriptor(self):
        """Gets the magnet_special_program_emphasis_school_descriptor of this EdFiSchool.  # noqa: E501

        A school that has been designed: 1) to attract students of different racial/ethnic backgrounds for the purpose of reducing, preventing, or eliminating racial isolation; and/or 2) to provide an academic or social focus on a particular theme (e.g., science/math, performing arts, gifted/talented, or foreign language).  # noqa: E501

        :return: The magnet_special_program_emphasis_school_descriptor of this EdFiSchool.  # noqa: E501
        :rtype: str
        """
        return self._magnet_special_program_emphasis_school_descriptor

    @magnet_special_program_emphasis_school_descriptor.setter
    def magnet_special_program_emphasis_school_descriptor(self, magnet_special_program_emphasis_school_descriptor):
        """Sets the magnet_special_program_emphasis_school_descriptor of this EdFiSchool.

        A school that has been designed: 1) to attract students of different racial/ethnic backgrounds for the purpose of reducing, preventing, or eliminating racial isolation; and/or 2) to provide an academic or social focus on a particular theme (e.g., science/math, performing arts, gifted/talented, or foreign language).  # noqa: E501

        :param magnet_special_program_emphasis_school_descriptor: The magnet_special_program_emphasis_school_descriptor of this EdFiSchool.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                magnet_special_program_emphasis_school_descriptor is not None and len(magnet_special_program_emphasis_school_descriptor) > 306):
            raise ValueError("Invalid value for `magnet_special_program_emphasis_school_descriptor`, length must be less than or equal to `306`")  # noqa: E501

        self._magnet_special_program_emphasis_school_descriptor = magnet_special_program_emphasis_school_descriptor

    @property
    def name_of_institution(self):
        """Gets the name_of_institution of this EdFiSchool.  # noqa: E501

        The full, legally accepted name of the institution.  # noqa: E501

        :return: The name_of_institution of this EdFiSchool.  # noqa: E501
        :rtype: str
        """
        return self._name_of_institution

    @name_of_institution.setter
    def name_of_institution(self, name_of_institution):
        """Sets the name_of_institution of this EdFiSchool.

        The full, legally accepted name of the institution.  # noqa: E501

        :param name_of_institution: The name_of_institution of this EdFiSchool.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and name_of_institution is None:
            raise ValueError("Invalid value for `name_of_institution`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                name_of_institution is not None and len(name_of_institution) > 75):
            raise ValueError("Invalid value for `name_of_institution`, length must be less than or equal to `75`")  # noqa: E501

        self._name_of_institution = name_of_institution

    @property
    def operational_status_descriptor(self):
        """Gets the operational_status_descriptor of this EdFiSchool.  # noqa: E501

        The current operational status of the education organization (e.g., active, inactive).  # noqa: E501

        :return: The operational_status_descriptor of this EdFiSchool.  # noqa: E501
        :rtype: str
        """
        return self._operational_status_descriptor

    @operational_status_descriptor.setter
    def operational_status_descriptor(self, operational_status_descriptor):
        """Sets the operational_status_descriptor of this EdFiSchool.

        The current operational status of the education organization (e.g., active, inactive).  # noqa: E501

        :param operational_status_descriptor: The operational_status_descriptor of this EdFiSchool.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                operational_status_descriptor is not None and len(operational_status_descriptor) > 306):
            raise ValueError("Invalid value for `operational_status_descriptor`, length must be less than or equal to `306`")  # noqa: E501

        self._operational_status_descriptor = operational_status_descriptor

    @property
    def school_categories(self):
        """Gets the school_categories of this EdFiSchool.  # noqa: E501

        An unordered collection of schoolCategories. The one or more categories of school.  # noqa: E501

        :return: The school_categories of this EdFiSchool.  # noqa: E501
        :rtype: list[EdFiSchoolCategory]
        """
        return self._school_categories

    @school_categories.setter
    def school_categories(self, school_categories):
        """Sets the school_categories of this EdFiSchool.

        An unordered collection of schoolCategories. The one or more categories of school.  # noqa: E501

        :param school_categories: The school_categories of this EdFiSchool.  # noqa: E501
        :type: list[EdFiSchoolCategory]
        """

        self._school_categories = school_categories

    @property
    def school_type_descriptor(self):
        """Gets the school_type_descriptor of this EdFiSchool.  # noqa: E501

        The type of education institution as classified by its primary focus.  # noqa: E501

        :return: The school_type_descriptor of this EdFiSchool.  # noqa: E501
        :rtype: str
        """
        return self._school_type_descriptor

    @school_type_descriptor.setter
    def school_type_descriptor(self, school_type_descriptor):
        """Sets the school_type_descriptor of this EdFiSchool.

        The type of education institution as classified by its primary focus.  # noqa: E501

        :param school_type_descriptor: The school_type_descriptor of this EdFiSchool.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                school_type_descriptor is not None and len(school_type_descriptor) > 306):
            raise ValueError("Invalid value for `school_type_descriptor`, length must be less than or equal to `306`")  # noqa: E501

        self._school_type_descriptor = school_type_descriptor

    @property
    def short_name_of_institution(self):
        """Gets the short_name_of_institution of this EdFiSchool.  # noqa: E501

        A short name for the institution.  # noqa: E501

        :return: The short_name_of_institution of this EdFiSchool.  # noqa: E501
        :rtype: str
        """
        return self._short_name_of_institution

    @short_name_of_institution.setter
    def short_name_of_institution(self, short_name_of_institution):
        """Sets the short_name_of_institution of this EdFiSchool.

        A short name for the institution.  # noqa: E501

        :param short_name_of_institution: The short_name_of_institution of this EdFiSchool.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                short_name_of_institution is not None and len(short_name_of_institution) > 75):
            raise ValueError("Invalid value for `short_name_of_institution`, length must be less than or equal to `75`")  # noqa: E501

        self._short_name_of_institution = short_name_of_institution

    @property
    def title_i_part_a_school_designation_descriptor(self):
        """Gets the title_i_part_a_school_designation_descriptor of this EdFiSchool.  # noqa: E501

        Denotes the Title I Part A designation for the school.  # noqa: E501

        :return: The title_i_part_a_school_designation_descriptor of this EdFiSchool.  # noqa: E501
        :rtype: str
        """
        return self._title_i_part_a_school_designation_descriptor

    @title_i_part_a_school_designation_descriptor.setter
    def title_i_part_a_school_designation_descriptor(self, title_i_part_a_school_designation_descriptor):
        """Sets the title_i_part_a_school_designation_descriptor of this EdFiSchool.

        Denotes the Title I Part A designation for the school.  # noqa: E501

        :param title_i_part_a_school_designation_descriptor: The title_i_part_a_school_designation_descriptor of this EdFiSchool.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                title_i_part_a_school_designation_descriptor is not None and len(title_i_part_a_school_designation_descriptor) > 306):
            raise ValueError("Invalid value for `title_i_part_a_school_designation_descriptor`, length must be less than or equal to `306`")  # noqa: E501

        self._title_i_part_a_school_designation_descriptor = title_i_part_a_school_designation_descriptor

    @property
    def web_site(self):
        """Gets the web_site of this EdFiSchool.  # noqa: E501

        The public web site address (URL) for the education organization.  # noqa: E501

        :return: The web_site of this EdFiSchool.  # noqa: E501
        :rtype: str
        """
        return self._web_site

    @web_site.setter
    def web_site(self, web_site):
        """Sets the web_site of this EdFiSchool.

        The public web site address (URL) for the education organization.  # noqa: E501

        :param web_site: The web_site of this EdFiSchool.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                web_site is not None and len(web_site) > 255):
            raise ValueError("Invalid value for `web_site`, length must be less than or equal to `255`")  # noqa: E501

        self._web_site = web_site

    @property
    def etag(self):
        """Gets the etag of this EdFiSchool.  # noqa: E501

        A unique system-generated value that identifies the version of the resource.  # noqa: E501

        :return: The etag of this EdFiSchool.  # noqa: E501
        :rtype: str
        """
        return self._etag

    @etag.setter
    def etag(self, etag):
        """Sets the etag of this EdFiSchool.

        A unique system-generated value that identifies the version of the resource.  # noqa: E501

        :param etag: The etag of this EdFiSchool.  # noqa: E501
        :type: str
        """

        self._etag = etag

    @property
    def ext(self):
        """Gets the ext of this EdFiSchool.  # noqa: E501


        :return: The ext of this EdFiSchool.  # noqa: E501
        :rtype: SchoolExtensions
        """
        return self._ext

    @ext.setter
    def ext(self, ext):
        """Sets the ext of this EdFiSchool.


        :param ext: The ext of this EdFiSchool.  # noqa: E501
        :type: SchoolExtensions
        """

        self._ext = ext

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
        if issubclass(EdFiSchool, dict):
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
        if not isinstance(other, EdFiSchool):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EdFiSchool):
            return True

        return self.to_dict() != other.to_dict()
