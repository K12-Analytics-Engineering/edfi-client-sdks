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


class EdFiStudentEducationOrganizationAssociationAddress(object):
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
        'address_type_descriptor': 'str',
        'state_abbreviation_descriptor': 'str',
        'city': 'str',
        'postal_code': 'str',
        'street_number_name': 'str',
        'locale_descriptor': 'str',
        'apartment_room_suite_number': 'str',
        'building_site_number': 'str',
        'congressional_district': 'str',
        'county_fips_code': 'str',
        'do_not_publish_indicator': 'bool',
        'latitude': 'str',
        'longitude': 'str',
        'name_of_county': 'str',
        'periods': 'list[EdFiStudentEducationOrganizationAssociationAddressPeriod]'
    }

    attribute_map = {
        'address_type_descriptor': 'addressTypeDescriptor',
        'state_abbreviation_descriptor': 'stateAbbreviationDescriptor',
        'city': 'city',
        'postal_code': 'postalCode',
        'street_number_name': 'streetNumberName',
        'locale_descriptor': 'localeDescriptor',
        'apartment_room_suite_number': 'apartmentRoomSuiteNumber',
        'building_site_number': 'buildingSiteNumber',
        'congressional_district': 'congressionalDistrict',
        'county_fips_code': 'countyFIPSCode',
        'do_not_publish_indicator': 'doNotPublishIndicator',
        'latitude': 'latitude',
        'longitude': 'longitude',
        'name_of_county': 'nameOfCounty',
        'periods': 'periods'
    }

    def __init__(self, address_type_descriptor=None, state_abbreviation_descriptor=None, city=None, postal_code=None, street_number_name=None, locale_descriptor=None, apartment_room_suite_number=None, building_site_number=None, congressional_district=None, county_fips_code=None, do_not_publish_indicator=None, latitude=None, longitude=None, name_of_county=None, periods=None, _configuration=None):  # noqa: E501
        """EdFiStudentEducationOrganizationAssociationAddress - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._address_type_descriptor = None
        self._state_abbreviation_descriptor = None
        self._city = None
        self._postal_code = None
        self._street_number_name = None
        self._locale_descriptor = None
        self._apartment_room_suite_number = None
        self._building_site_number = None
        self._congressional_district = None
        self._county_fips_code = None
        self._do_not_publish_indicator = None
        self._latitude = None
        self._longitude = None
        self._name_of_county = None
        self._periods = None
        self.discriminator = None

        self.address_type_descriptor = address_type_descriptor
        self.state_abbreviation_descriptor = state_abbreviation_descriptor
        self.city = city
        self.postal_code = postal_code
        self.street_number_name = street_number_name
        if locale_descriptor is not None:
            self.locale_descriptor = locale_descriptor
        if apartment_room_suite_number is not None:
            self.apartment_room_suite_number = apartment_room_suite_number
        if building_site_number is not None:
            self.building_site_number = building_site_number
        if congressional_district is not None:
            self.congressional_district = congressional_district
        if county_fips_code is not None:
            self.county_fips_code = county_fips_code
        if do_not_publish_indicator is not None:
            self.do_not_publish_indicator = do_not_publish_indicator
        if latitude is not None:
            self.latitude = latitude
        if longitude is not None:
            self.longitude = longitude
        if name_of_county is not None:
            self.name_of_county = name_of_county
        if periods is not None:
            self.periods = periods

    @property
    def address_type_descriptor(self):
        """Gets the address_type_descriptor of this EdFiStudentEducationOrganizationAssociationAddress.  # noqa: E501

        The type of address listed for an individual or organization.    For example:  Physical Address, Mailing Address, Home Address, etc.)  # noqa: E501

        :return: The address_type_descriptor of this EdFiStudentEducationOrganizationAssociationAddress.  # noqa: E501
        :rtype: str
        """
        return self._address_type_descriptor

    @address_type_descriptor.setter
    def address_type_descriptor(self, address_type_descriptor):
        """Sets the address_type_descriptor of this EdFiStudentEducationOrganizationAssociationAddress.

        The type of address listed for an individual or organization.    For example:  Physical Address, Mailing Address, Home Address, etc.)  # noqa: E501

        :param address_type_descriptor: The address_type_descriptor of this EdFiStudentEducationOrganizationAssociationAddress.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and address_type_descriptor is None:
            raise ValueError("Invalid value for `address_type_descriptor`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                address_type_descriptor is not None and len(address_type_descriptor) > 306):
            raise ValueError("Invalid value for `address_type_descriptor`, length must be less than or equal to `306`")  # noqa: E501

        self._address_type_descriptor = address_type_descriptor

    @property
    def state_abbreviation_descriptor(self):
        """Gets the state_abbreviation_descriptor of this EdFiStudentEducationOrganizationAssociationAddress.  # noqa: E501

        The abbreviation for the state (within the United States) or outlying area in which an address is located.  # noqa: E501

        :return: The state_abbreviation_descriptor of this EdFiStudentEducationOrganizationAssociationAddress.  # noqa: E501
        :rtype: str
        """
        return self._state_abbreviation_descriptor

    @state_abbreviation_descriptor.setter
    def state_abbreviation_descriptor(self, state_abbreviation_descriptor):
        """Sets the state_abbreviation_descriptor of this EdFiStudentEducationOrganizationAssociationAddress.

        The abbreviation for the state (within the United States) or outlying area in which an address is located.  # noqa: E501

        :param state_abbreviation_descriptor: The state_abbreviation_descriptor of this EdFiStudentEducationOrganizationAssociationAddress.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and state_abbreviation_descriptor is None:
            raise ValueError("Invalid value for `state_abbreviation_descriptor`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                state_abbreviation_descriptor is not None and len(state_abbreviation_descriptor) > 306):
            raise ValueError("Invalid value for `state_abbreviation_descriptor`, length must be less than or equal to `306`")  # noqa: E501

        self._state_abbreviation_descriptor = state_abbreviation_descriptor

    @property
    def city(self):
        """Gets the city of this EdFiStudentEducationOrganizationAssociationAddress.  # noqa: E501

        The name of the city in which an address is located.  # noqa: E501

        :return: The city of this EdFiStudentEducationOrganizationAssociationAddress.  # noqa: E501
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this EdFiStudentEducationOrganizationAssociationAddress.

        The name of the city in which an address is located.  # noqa: E501

        :param city: The city of this EdFiStudentEducationOrganizationAssociationAddress.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and city is None:
            raise ValueError("Invalid value for `city`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                city is not None and len(city) > 30):
            raise ValueError("Invalid value for `city`, length must be less than or equal to `30`")  # noqa: E501

        self._city = city

    @property
    def postal_code(self):
        """Gets the postal_code of this EdFiStudentEducationOrganizationAssociationAddress.  # noqa: E501

        The five or nine digit zip code or overseas postal code portion of an address.  # noqa: E501

        :return: The postal_code of this EdFiStudentEducationOrganizationAssociationAddress.  # noqa: E501
        :rtype: str
        """
        return self._postal_code

    @postal_code.setter
    def postal_code(self, postal_code):
        """Sets the postal_code of this EdFiStudentEducationOrganizationAssociationAddress.

        The five or nine digit zip code or overseas postal code portion of an address.  # noqa: E501

        :param postal_code: The postal_code of this EdFiStudentEducationOrganizationAssociationAddress.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and postal_code is None:
            raise ValueError("Invalid value for `postal_code`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                postal_code is not None and len(postal_code) > 17):
            raise ValueError("Invalid value for `postal_code`, length must be less than or equal to `17`")  # noqa: E501

        self._postal_code = postal_code

    @property
    def street_number_name(self):
        """Gets the street_number_name of this EdFiStudentEducationOrganizationAssociationAddress.  # noqa: E501

        The street number and street name or post office box number of an address.  # noqa: E501

        :return: The street_number_name of this EdFiStudentEducationOrganizationAssociationAddress.  # noqa: E501
        :rtype: str
        """
        return self._street_number_name

    @street_number_name.setter
    def street_number_name(self, street_number_name):
        """Sets the street_number_name of this EdFiStudentEducationOrganizationAssociationAddress.

        The street number and street name or post office box number of an address.  # noqa: E501

        :param street_number_name: The street_number_name of this EdFiStudentEducationOrganizationAssociationAddress.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and street_number_name is None:
            raise ValueError("Invalid value for `street_number_name`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                street_number_name is not None and len(street_number_name) > 150):
            raise ValueError("Invalid value for `street_number_name`, length must be less than or equal to `150`")  # noqa: E501

        self._street_number_name = street_number_name

    @property
    def locale_descriptor(self):
        """Gets the locale_descriptor of this EdFiStudentEducationOrganizationAssociationAddress.  # noqa: E501

        A general geographic indicator that categorizes U.S. territory (e.g., City, Suburban).  # noqa: E501

        :return: The locale_descriptor of this EdFiStudentEducationOrganizationAssociationAddress.  # noqa: E501
        :rtype: str
        """
        return self._locale_descriptor

    @locale_descriptor.setter
    def locale_descriptor(self, locale_descriptor):
        """Sets the locale_descriptor of this EdFiStudentEducationOrganizationAssociationAddress.

        A general geographic indicator that categorizes U.S. territory (e.g., City, Suburban).  # noqa: E501

        :param locale_descriptor: The locale_descriptor of this EdFiStudentEducationOrganizationAssociationAddress.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                locale_descriptor is not None and len(locale_descriptor) > 306):
            raise ValueError("Invalid value for `locale_descriptor`, length must be less than or equal to `306`")  # noqa: E501

        self._locale_descriptor = locale_descriptor

    @property
    def apartment_room_suite_number(self):
        """Gets the apartment_room_suite_number of this EdFiStudentEducationOrganizationAssociationAddress.  # noqa: E501

        The apartment, room, or suite number of an address.  # noqa: E501

        :return: The apartment_room_suite_number of this EdFiStudentEducationOrganizationAssociationAddress.  # noqa: E501
        :rtype: str
        """
        return self._apartment_room_suite_number

    @apartment_room_suite_number.setter
    def apartment_room_suite_number(self, apartment_room_suite_number):
        """Sets the apartment_room_suite_number of this EdFiStudentEducationOrganizationAssociationAddress.

        The apartment, room, or suite number of an address.  # noqa: E501

        :param apartment_room_suite_number: The apartment_room_suite_number of this EdFiStudentEducationOrganizationAssociationAddress.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                apartment_room_suite_number is not None and len(apartment_room_suite_number) > 50):
            raise ValueError("Invalid value for `apartment_room_suite_number`, length must be less than or equal to `50`")  # noqa: E501

        self._apartment_room_suite_number = apartment_room_suite_number

    @property
    def building_site_number(self):
        """Gets the building_site_number of this EdFiStudentEducationOrganizationAssociationAddress.  # noqa: E501

        The number of the building on the site, if more than one building shares the same address.  # noqa: E501

        :return: The building_site_number of this EdFiStudentEducationOrganizationAssociationAddress.  # noqa: E501
        :rtype: str
        """
        return self._building_site_number

    @building_site_number.setter
    def building_site_number(self, building_site_number):
        """Sets the building_site_number of this EdFiStudentEducationOrganizationAssociationAddress.

        The number of the building on the site, if more than one building shares the same address.  # noqa: E501

        :param building_site_number: The building_site_number of this EdFiStudentEducationOrganizationAssociationAddress.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                building_site_number is not None and len(building_site_number) > 20):
            raise ValueError("Invalid value for `building_site_number`, length must be less than or equal to `20`")  # noqa: E501

        self._building_site_number = building_site_number

    @property
    def congressional_district(self):
        """Gets the congressional_district of this EdFiStudentEducationOrganizationAssociationAddress.  # noqa: E501

        The congressional district in which an address is located.  # noqa: E501

        :return: The congressional_district of this EdFiStudentEducationOrganizationAssociationAddress.  # noqa: E501
        :rtype: str
        """
        return self._congressional_district

    @congressional_district.setter
    def congressional_district(self, congressional_district):
        """Sets the congressional_district of this EdFiStudentEducationOrganizationAssociationAddress.

        The congressional district in which an address is located.  # noqa: E501

        :param congressional_district: The congressional_district of this EdFiStudentEducationOrganizationAssociationAddress.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                congressional_district is not None and len(congressional_district) > 30):
            raise ValueError("Invalid value for `congressional_district`, length must be less than or equal to `30`")  # noqa: E501

        self._congressional_district = congressional_district

    @property
    def county_fips_code(self):
        """Gets the county_fips_code of this EdFiStudentEducationOrganizationAssociationAddress.  # noqa: E501

        The Federal Information Processing Standards (FIPS) numeric code for the county issued by the National Institute of Standards and Technology (NIST). Counties are considered to be the \"first-order subdivisions\" of each State and statistically equivalent entity, regardless of their local designations (county, parish, borough, etc.) Counties in different States will have the same code. A unique county number is created when combined with the 2-digit FIPS State Code.  # noqa: E501

        :return: The county_fips_code of this EdFiStudentEducationOrganizationAssociationAddress.  # noqa: E501
        :rtype: str
        """
        return self._county_fips_code

    @county_fips_code.setter
    def county_fips_code(self, county_fips_code):
        """Sets the county_fips_code of this EdFiStudentEducationOrganizationAssociationAddress.

        The Federal Information Processing Standards (FIPS) numeric code for the county issued by the National Institute of Standards and Technology (NIST). Counties are considered to be the \"first-order subdivisions\" of each State and statistically equivalent entity, regardless of their local designations (county, parish, borough, etc.) Counties in different States will have the same code. A unique county number is created when combined with the 2-digit FIPS State Code.  # noqa: E501

        :param county_fips_code: The county_fips_code of this EdFiStudentEducationOrganizationAssociationAddress.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                county_fips_code is not None and len(county_fips_code) > 5):
            raise ValueError("Invalid value for `county_fips_code`, length must be less than or equal to `5`")  # noqa: E501

        self._county_fips_code = county_fips_code

    @property
    def do_not_publish_indicator(self):
        """Gets the do_not_publish_indicator of this EdFiStudentEducationOrganizationAssociationAddress.  # noqa: E501

        An indication that the address should not be published.  # noqa: E501

        :return: The do_not_publish_indicator of this EdFiStudentEducationOrganizationAssociationAddress.  # noqa: E501
        :rtype: bool
        """
        return self._do_not_publish_indicator

    @do_not_publish_indicator.setter
    def do_not_publish_indicator(self, do_not_publish_indicator):
        """Sets the do_not_publish_indicator of this EdFiStudentEducationOrganizationAssociationAddress.

        An indication that the address should not be published.  # noqa: E501

        :param do_not_publish_indicator: The do_not_publish_indicator of this EdFiStudentEducationOrganizationAssociationAddress.  # noqa: E501
        :type: bool
        """

        self._do_not_publish_indicator = do_not_publish_indicator

    @property
    def latitude(self):
        """Gets the latitude of this EdFiStudentEducationOrganizationAssociationAddress.  # noqa: E501

        The geographic latitude of the physical address.  # noqa: E501

        :return: The latitude of this EdFiStudentEducationOrganizationAssociationAddress.  # noqa: E501
        :rtype: str
        """
        return self._latitude

    @latitude.setter
    def latitude(self, latitude):
        """Sets the latitude of this EdFiStudentEducationOrganizationAssociationAddress.

        The geographic latitude of the physical address.  # noqa: E501

        :param latitude: The latitude of this EdFiStudentEducationOrganizationAssociationAddress.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                latitude is not None and len(latitude) > 20):
            raise ValueError("Invalid value for `latitude`, length must be less than or equal to `20`")  # noqa: E501

        self._latitude = latitude

    @property
    def longitude(self):
        """Gets the longitude of this EdFiStudentEducationOrganizationAssociationAddress.  # noqa: E501

        The geographic longitude of the physical address.  # noqa: E501

        :return: The longitude of this EdFiStudentEducationOrganizationAssociationAddress.  # noqa: E501
        :rtype: str
        """
        return self._longitude

    @longitude.setter
    def longitude(self, longitude):
        """Sets the longitude of this EdFiStudentEducationOrganizationAssociationAddress.

        The geographic longitude of the physical address.  # noqa: E501

        :param longitude: The longitude of this EdFiStudentEducationOrganizationAssociationAddress.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                longitude is not None and len(longitude) > 20):
            raise ValueError("Invalid value for `longitude`, length must be less than or equal to `20`")  # noqa: E501

        self._longitude = longitude

    @property
    def name_of_county(self):
        """Gets the name_of_county of this EdFiStudentEducationOrganizationAssociationAddress.  # noqa: E501

        The name of the county, parish, borough, or comparable unit (within a state) in                       'which an address is located.  # noqa: E501

        :return: The name_of_county of this EdFiStudentEducationOrganizationAssociationAddress.  # noqa: E501
        :rtype: str
        """
        return self._name_of_county

    @name_of_county.setter
    def name_of_county(self, name_of_county):
        """Sets the name_of_county of this EdFiStudentEducationOrganizationAssociationAddress.

        The name of the county, parish, borough, or comparable unit (within a state) in                       'which an address is located.  # noqa: E501

        :param name_of_county: The name_of_county of this EdFiStudentEducationOrganizationAssociationAddress.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                name_of_county is not None and len(name_of_county) > 30):
            raise ValueError("Invalid value for `name_of_county`, length must be less than or equal to `30`")  # noqa: E501

        self._name_of_county = name_of_county

    @property
    def periods(self):
        """Gets the periods of this EdFiStudentEducationOrganizationAssociationAddress.  # noqa: E501

        An unordered collection of studentEducationOrganizationAssociationAddressPeriods. The time periods for which the address is valid. For physical addresses, the periods in which the person lived at that address.  # noqa: E501

        :return: The periods of this EdFiStudentEducationOrganizationAssociationAddress.  # noqa: E501
        :rtype: list[EdFiStudentEducationOrganizationAssociationAddressPeriod]
        """
        return self._periods

    @periods.setter
    def periods(self, periods):
        """Sets the periods of this EdFiStudentEducationOrganizationAssociationAddress.

        An unordered collection of studentEducationOrganizationAssociationAddressPeriods. The time periods for which the address is valid. For physical addresses, the periods in which the person lived at that address.  # noqa: E501

        :param periods: The periods of this EdFiStudentEducationOrganizationAssociationAddress.  # noqa: E501
        :type: list[EdFiStudentEducationOrganizationAssociationAddressPeriod]
        """

        self._periods = periods

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
        if issubclass(EdFiStudentEducationOrganizationAssociationAddress, dict):
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
        if not isinstance(other, EdFiStudentEducationOrganizationAssociationAddress):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EdFiStudentEducationOrganizationAssociationAddress):
            return True

        return self.to_dict() != other.to_dict()
