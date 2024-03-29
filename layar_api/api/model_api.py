# coding: utf-8

"""
    Layar API Documentation

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: VERSION_PLACEHOLDER
    Contact: AI-Support@Certara.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from layar_api.api_client import ApiClient


class ModelApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def download_model(self, id, **kwargs):  # noqa: E501
        """Download a model by ID  # noqa: E501

        Download the original model file by its model ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.download_model(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.download_model_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.download_model_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def download_model_with_http_info(self, id, **kwargs):  # noqa: E501
        """Download a model by ID  # noqa: E501

        Download the original model file by its model ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.download_model_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method download_model" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `download_model`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/octet-stream'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oAuth2ClientCredentials']  # noqa: E501

        return self.api_client.call_api(
            '/layar/model/{id}/download', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='str',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def search_models_by_computation_id(self, id, **kwargs):  # noqa: E501
        """Find models by project computation ID  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.search_models_by_computation_id(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: (required)
        :param int start: the start offset for the row
        :param int rows: the number of rows to return
        :param str q: the query string to search for
        :return: list[DeepLearningModel]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.search_models_by_computation_id_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.search_models_by_computation_id_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def search_models_by_computation_id_with_http_info(self, id, **kwargs):  # noqa: E501
        """Find models by project computation ID  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.search_models_by_computation_id_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: (required)
        :param int start: the start offset for the row
        :param int rows: the number of rows to return
        :param str q: the query string to search for
        :return: list[DeepLearningModel]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'start', 'rows', 'q']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method search_models_by_computation_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `search_models_by_computation_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []
        if 'start' in params:
            query_params.append(('start', params['start']))  # noqa: E501
        if 'rows' in params:
            query_params.append(('rows', params['rows']))  # noqa: E501
        if 'q' in params:
            query_params.append(('q', params['q']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oAuth2ClientCredentials']  # noqa: E501

        return self.api_client.call_api(
            '/layar/projectComputation/{id}/models', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[DeepLearningModel]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def search_models_by_module_id(self, module_id, **kwargs):  # noqa: E501
        """Find models by module ID  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.search_models_by_module_id(module_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str module_id: (required)
        :param int start: the start offset for the row
        :param int rows: the number of rows to return
        :param str q: the query string to search for
        :return: list[DeepLearningModel]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.search_models_by_module_id_with_http_info(module_id, **kwargs)  # noqa: E501
        else:
            (data) = self.search_models_by_module_id_with_http_info(module_id, **kwargs)  # noqa: E501
            return data

    def search_models_by_module_id_with_http_info(self, module_id, **kwargs):  # noqa: E501
        """Find models by module ID  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.search_models_by_module_id_with_http_info(module_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str module_id: (required)
        :param int start: the start offset for the row
        :param int rows: the number of rows to return
        :param str q: the query string to search for
        :return: list[DeepLearningModel]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['module_id', 'start', 'rows', 'q']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method search_models_by_module_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'module_id' is set
        if ('module_id' not in params or
                params['module_id'] is None):
            raise ValueError("Missing the required parameter `module_id` when calling `search_models_by_module_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'module_id' in params:
            path_params['moduleId'] = params['module_id']  # noqa: E501

        query_params = []
        if 'start' in params:
            query_params.append(('start', params['start']))  # noqa: E501
        if 'rows' in params:
            query_params.append(('rows', params['rows']))  # noqa: E501
        if 'q' in params:
            query_params.append(('q', params['q']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oAuth2ClientCredentials']  # noqa: E501

        return self.api_client.call_api(
            '/layar/module/{moduleId}/models', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[DeepLearningModel]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def search_models_by_project_id(self, project_id, **kwargs):  # noqa: E501
        """Find models by project ID  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.search_models_by_project_id(project_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str project_id: (required)
        :param int start: the start offset for the row
        :param int rows: the number of rows to return
        :param str q: the query string to search for
        :return: list[DeepLearningModel]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.search_models_by_project_id_with_http_info(project_id, **kwargs)  # noqa: E501
        else:
            (data) = self.search_models_by_project_id_with_http_info(project_id, **kwargs)  # noqa: E501
            return data

    def search_models_by_project_id_with_http_info(self, project_id, **kwargs):  # noqa: E501
        """Find models by project ID  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.search_models_by_project_id_with_http_info(project_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str project_id: (required)
        :param int start: the start offset for the row
        :param int rows: the number of rows to return
        :param str q: the query string to search for
        :return: list[DeepLearningModel]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['project_id', 'start', 'rows', 'q']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method search_models_by_project_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'project_id' is set
        if ('project_id' not in params or
                params['project_id'] is None):
            raise ValueError("Missing the required parameter `project_id` when calling `search_models_by_project_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'project_id' in params:
            path_params['projectId'] = params['project_id']  # noqa: E501

        query_params = []
        if 'start' in params:
            query_params.append(('start', params['start']))  # noqa: E501
        if 'rows' in params:
            query_params.append(('rows', params['rows']))  # noqa: E501
        if 'q' in params:
            query_params.append(('q', params['q']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oAuth2ClientCredentials']  # noqa: E501

        return self.api_client.call_api(
            '/layar/project/{projectId}/models', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[DeepLearningModel]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
