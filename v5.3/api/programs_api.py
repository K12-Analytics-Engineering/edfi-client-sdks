# coding: utf-8

"""
    Ed-Fi Operational Data Store API

    The Ed-Fi ODS / API enables applications to read and write education data stored in an Ed-Fi ODS through a secure REST interface.  ***  > *Note: Consumers of ODS / API information should sanitize all data for display and storage. The ODS / API provides reasonable safeguards against cross-site scripting attacks and other malicious content, but the platform does not and cannot guarantee that the data it contains is free of all potentially harmful content.*  ***   # noqa: E501

    OpenAPI spec version: 3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class ProgramsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def delete_program_by_id(self, id, **kwargs):  # noqa: E501
        """Deletes an existing resource using the resource identifier.  # noqa: E501

        The DELETE operation is used to delete an existing resource by identifier. If the resource doesn't exist, an error will result (the resource will not be found).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_program_by_id(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: A resource identifier that uniquely identifies the resource. (required)
        :param str if_match: The ETag header value used to prevent the DELETE from removing a resource modified by another consumer.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_program_by_id_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_program_by_id_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def delete_program_by_id_with_http_info(self, id, **kwargs):  # noqa: E501
        """Deletes an existing resource using the resource identifier.  # noqa: E501

        The DELETE operation is used to delete an existing resource by identifier. If the resource doesn't exist, an error will result (the resource will not be found).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_program_by_id_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: A resource identifier that uniquely identifies the resource. (required)
        :param str if_match: The ETag header value used to prevent the DELETE from removing a resource modified by another consumer.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'if_match']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_program_by_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and ('id' not in params or
                                                       params['id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `id` when calling `delete_program_by_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'if_match' in params:
            header_params['If-Match'] = params['if_match']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth2_client_credentials']  # noqa: E501

        return self.api_client.call_api(
            '/ed-fi/programs/{id}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def deletes_programs(self, **kwargs):  # noqa: E501
        """Retrieves deleted resources based on change version.  # noqa: E501

        The DELETES operation is used to retrieve deleted resources.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.deletes_programs(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int offset: Indicates how many items should be skipped before returning results.
        :param int limit: Indicates the maximum number of items that should be returned in the results.
        :param int min_change_version: Used in synchronization to set sequence minimum ChangeVersion
        :param int max_change_version: Used in synchronization to set sequence maximum ChangeVersion
        :param str snapshot_identifier: Indicates the Snapshot-Identifier that should be used.
        :return: list[DeletedResource]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.deletes_programs_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.deletes_programs_with_http_info(**kwargs)  # noqa: E501
            return data

    def deletes_programs_with_http_info(self, **kwargs):  # noqa: E501
        """Retrieves deleted resources based on change version.  # noqa: E501

        The DELETES operation is used to retrieve deleted resources.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.deletes_programs_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int offset: Indicates how many items should be skipped before returning results.
        :param int limit: Indicates the maximum number of items that should be returned in the results.
        :param int min_change_version: Used in synchronization to set sequence minimum ChangeVersion
        :param int max_change_version: Used in synchronization to set sequence maximum ChangeVersion
        :param str snapshot_identifier: Indicates the Snapshot-Identifier that should be used.
        :return: list[DeletedResource]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['offset', 'limit', 'min_change_version', 'max_change_version', 'snapshot_identifier']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method deletes_programs" % key
                )
            params[key] = val
        del params['kwargs']

        if self.api_client.client_side_validation and ('limit' in params and params['limit'] > 5000):  # noqa: E501
            raise ValueError("Invalid value for parameter `limit` when calling `deletes_programs`, must be a value less than or equal to `500`")  # noqa: E501
        if self.api_client.client_side_validation and ('limit' in params and params['limit'] < 0):  # noqa: E501
            raise ValueError("Invalid value for parameter `limit` when calling `deletes_programs`, must be a value greater than or equal to `0`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'min_change_version' in params:
            query_params.append(('minChangeVersion', params['min_change_version']))  # noqa: E501
        if 'max_change_version' in params:
            query_params.append(('maxChangeVersion', params['max_change_version']))  # noqa: E501

        header_params = {}
        if 'snapshot_identifier' in params:
            header_params['Snapshot-Identifier'] = params['snapshot_identifier']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth2_client_credentials']  # noqa: E501

        return self.api_client.call_api(
            '/ed-fi/programs/deletes', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[DeletedResource]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_programs(self, **kwargs):  # noqa: E501
        """Retrieves specific resources using the resource's property values (using the \"Get\" pattern).  # noqa: E501

        This GET operation provides access to resources using the \"Get\" search pattern.  The values of any properties of the resource that are specified will be used to return all matching results (if it exists).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_programs(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int offset: Indicates how many items should be skipped before returning results.
        :param int limit: Indicates the maximum number of items that should be returned in the results.
        :param int min_change_version: Used in synchronization to set sequence minimum ChangeVersion
        :param int max_change_version: Used in synchronization to set sequence maximum ChangeVersion
        :param bool total_count: Indicates if the total number of items available should be returned in the 'Total-Count' header of the response.  If set to false, 'Total-Count' header will not be provided.
        :param str program_type_descriptor: The type of program.
        :param str program_name: The formal name of the Program of instruction, training, services, or benefits available through federal, state, or local agencies.
        :param int education_organization_id: The identifier assigned to an education organization.
        :param str id: 
        :param str program_id: A unique number or alphanumeric code assigned to a program by a school, school system, a state, or other agency or entity.
        :param str snapshot_identifier: Indicates the Snapshot-Identifier that should be used.
        :return: list[EdFiProgram]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_programs_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_programs_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_programs_with_http_info(self, **kwargs):  # noqa: E501
        """Retrieves specific resources using the resource's property values (using the \"Get\" pattern).  # noqa: E501

        This GET operation provides access to resources using the \"Get\" search pattern.  The values of any properties of the resource that are specified will be used to return all matching results (if it exists).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_programs_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int offset: Indicates how many items should be skipped before returning results.
        :param int limit: Indicates the maximum number of items that should be returned in the results.
        :param int min_change_version: Used in synchronization to set sequence minimum ChangeVersion
        :param int max_change_version: Used in synchronization to set sequence maximum ChangeVersion
        :param bool total_count: Indicates if the total number of items available should be returned in the 'Total-Count' header of the response.  If set to false, 'Total-Count' header will not be provided.
        :param str program_type_descriptor: The type of program.
        :param str program_name: The formal name of the Program of instruction, training, services, or benefits available through federal, state, or local agencies.
        :param int education_organization_id: The identifier assigned to an education organization.
        :param str id: 
        :param str program_id: A unique number or alphanumeric code assigned to a program by a school, school system, a state, or other agency or entity.
        :param str snapshot_identifier: Indicates the Snapshot-Identifier that should be used.
        :return: list[EdFiProgram]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['offset', 'limit', 'min_change_version', 'max_change_version', 'total_count', 'program_type_descriptor', 'program_name', 'education_organization_id', 'id', 'program_id', 'snapshot_identifier']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_programs" % key
                )
            params[key] = val
        del params['kwargs']

        if self.api_client.client_side_validation and ('limit' in params and params['limit'] > 5000):  # noqa: E501
            raise ValueError("Invalid value for parameter `limit` when calling `get_programs`, must be a value less than or equal to `500`")  # noqa: E501
        if self.api_client.client_side_validation and ('limit' in params and params['limit'] < 0):  # noqa: E501
            raise ValueError("Invalid value for parameter `limit` when calling `get_programs`, must be a value greater than or equal to `0`")  # noqa: E501
        if self.api_client.client_side_validation and ('program_type_descriptor' in params and
                                                       len(params['program_type_descriptor']) > 306):
            raise ValueError("Invalid value for parameter `program_type_descriptor` when calling `get_programs`, length must be less than or equal to `306`")  # noqa: E501
        if self.api_client.client_side_validation and ('program_name' in params and
                                                       len(params['program_name']) > 60):
            raise ValueError("Invalid value for parameter `program_name` when calling `get_programs`, length must be less than or equal to `60`")  # noqa: E501
        if self.api_client.client_side_validation and ('program_id' in params and
                                                       len(params['program_id']) > 20):
            raise ValueError("Invalid value for parameter `program_id` when calling `get_programs`, length must be less than or equal to `20`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'min_change_version' in params:
            query_params.append(('minChangeVersion', params['min_change_version']))  # noqa: E501
        if 'max_change_version' in params:
            query_params.append(('maxChangeVersion', params['max_change_version']))  # noqa: E501
        if 'total_count' in params:
            query_params.append(('totalCount', params['total_count']))  # noqa: E501
        if 'program_type_descriptor' in params:
            query_params.append(('programTypeDescriptor', params['program_type_descriptor']))  # noqa: E501
        if 'program_name' in params:
            query_params.append(('programName', params['program_name']))  # noqa: E501
        if 'education_organization_id' in params:
            query_params.append(('educationOrganizationId', params['education_organization_id']))  # noqa: E501
        if 'id' in params:
            query_params.append(('id', params['id']))  # noqa: E501
        if 'program_id' in params:
            query_params.append(('programId', params['program_id']))  # noqa: E501

        header_params = {}
        if 'snapshot_identifier' in params:
            header_params['Snapshot-Identifier'] = params['snapshot_identifier']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth2_client_credentials']  # noqa: E501

        return self.api_client.call_api(
            '/ed-fi/programs', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[EdFiProgram]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_programs_by_id(self, id, **kwargs):  # noqa: E501
        """Retrieves a specific resource using the resource's identifier (using the \"Get By Id\" pattern).  # noqa: E501

        This GET operation retrieves a resource by the specified resource identifier.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_programs_by_id(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: A resource identifier that uniquely identifies the resource. (required)
        :param str if_none_match: The previously returned ETag header value, used here to prevent the unnecessary data transfer of an unchanged resource.
        :param str snapshot_identifier: Indicates the Snapshot-Identifier that should be used.
        :return: EdFiProgram
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_programs_by_id_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_programs_by_id_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def get_programs_by_id_with_http_info(self, id, **kwargs):  # noqa: E501
        """Retrieves a specific resource using the resource's identifier (using the \"Get By Id\" pattern).  # noqa: E501

        This GET operation retrieves a resource by the specified resource identifier.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_programs_by_id_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: A resource identifier that uniquely identifies the resource. (required)
        :param str if_none_match: The previously returned ETag header value, used here to prevent the unnecessary data transfer of an unchanged resource.
        :param str snapshot_identifier: Indicates the Snapshot-Identifier that should be used.
        :return: EdFiProgram
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'if_none_match', 'snapshot_identifier']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_programs_by_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and ('id' not in params or
                                                       params['id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `id` when calling `get_programs_by_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'if_none_match' in params:
            header_params['If-None-Match'] = params['if_none_match']  # noqa: E501
        if 'snapshot_identifier' in params:
            header_params['Snapshot-Identifier'] = params['snapshot_identifier']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth2_client_credentials']  # noqa: E501

        return self.api_client.call_api(
            '/ed-fi/programs/{id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='EdFiProgram',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def post_program(self, program, **kwargs):  # noqa: E501
        """Creates or updates resources based on the natural key values of the supplied resource.  # noqa: E501

        The POST operation can be used to create or update resources. In database terms, this is often referred to as an \"upsert\" operation (insert + update). Clients should NOT include the resource \"id\" in the JSON body because it will result in an error. The web service will identify whether the resource already exists based on the natural key values provided, and update or create the resource appropriately. It is recommended to use POST for both create and update except while updating natural key of a resource in which case PUT operation must be used.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_program(program, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param EdFiProgram program: The JSON representation of the \"program\" resource to be created or updated. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.post_program_with_http_info(program, **kwargs)  # noqa: E501
        else:
            (data) = self.post_program_with_http_info(program, **kwargs)  # noqa: E501
            return data

    def post_program_with_http_info(self, program, **kwargs):  # noqa: E501
        """Creates or updates resources based on the natural key values of the supplied resource.  # noqa: E501

        The POST operation can be used to create or update resources. In database terms, this is often referred to as an \"upsert\" operation (insert + update). Clients should NOT include the resource \"id\" in the JSON body because it will result in an error. The web service will identify whether the resource already exists based on the natural key values provided, and update or create the resource appropriately. It is recommended to use POST for both create and update except while updating natural key of a resource in which case PUT operation must be used.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_program_with_http_info(program, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param EdFiProgram program: The JSON representation of the \"program\" resource to be created or updated. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['program']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_program" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'program' is set
        if self.api_client.client_side_validation and ('program' not in params or
                                                       params['program'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `program` when calling `post_program`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'program' in params:
            body_params = params['program']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth2_client_credentials']  # noqa: E501

        return self.api_client.call_api(
            '/ed-fi/programs', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def put_program(self, id, program, **kwargs):  # noqa: E501
        """Updates a resource based on the resource identifier.  # noqa: E501

        The PUT operation is used to update a resource by identifier. If the resource identifier (\"id\") is provided in the JSON body, it will be ignored. Additionally, this API resource is not configured for cascading natural key updates. Natural key values for this resource cannot be changed using PUT operation and will not be modified in the database, and so recommendation is to use POST as that supports upsert behavior.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.put_program(id, program, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: A resource identifier that uniquely identifies the resource. (required)
        :param EdFiProgram program: The JSON representation of the \"program\" resource to be created or updated. (required)
        :param str if_match: The ETag header value used to prevent the PUT from updating a resource modified by another consumer.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.put_program_with_http_info(id, program, **kwargs)  # noqa: E501
        else:
            (data) = self.put_program_with_http_info(id, program, **kwargs)  # noqa: E501
            return data

    def put_program_with_http_info(self, id, program, **kwargs):  # noqa: E501
        """Updates a resource based on the resource identifier.  # noqa: E501

        The PUT operation is used to update a resource by identifier. If the resource identifier (\"id\") is provided in the JSON body, it will be ignored. Additionally, this API resource is not configured for cascading natural key updates. Natural key values for this resource cannot be changed using PUT operation and will not be modified in the database, and so recommendation is to use POST as that supports upsert behavior.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.put_program_with_http_info(id, program, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: A resource identifier that uniquely identifies the resource. (required)
        :param EdFiProgram program: The JSON representation of the \"program\" resource to be created or updated. (required)
        :param str if_match: The ETag header value used to prevent the PUT from updating a resource modified by another consumer.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'program', 'if_match']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method put_program" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and ('id' not in params or
                                                       params['id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `id` when calling `put_program`")  # noqa: E501
        # verify the required parameter 'program' is set
        if self.api_client.client_side_validation and ('program' not in params or
                                                       params['program'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `program` when calling `put_program`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'if_match' in params:
            header_params['If-Match'] = params['if_match']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'program' in params:
            body_params = params['program']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth2_client_credentials']  # noqa: E501

        return self.api_client.call_api(
            '/ed-fi/programs/{id}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
