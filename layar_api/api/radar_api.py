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


class RadarApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_nearest_neighbor_count(self, x_vyasa_data_providers, **kwargs):  # noqa: E501
        """Get nearest neighbor counts  # noqa: E501

        Return a count of nearest neighbor terms for an input query string  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_nearest_neighbor_count(x_vyasa_data_providers, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_vyasa_data_providers: remote data providers to query (required)
        :param str terms:
        :return: InlineResponse2004
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_nearest_neighbor_count_with_http_info(x_vyasa_data_providers, **kwargs)  # noqa: E501
        else:
            (data) = self.get_nearest_neighbor_count_with_http_info(x_vyasa_data_providers, **kwargs)  # noqa: E501
            return data

    def get_nearest_neighbor_count_with_http_info(self, x_vyasa_data_providers, **kwargs):  # noqa: E501
        """Get nearest neighbor counts  # noqa: E501

        Return a count of nearest neighbor terms for an input query string  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_nearest_neighbor_count_with_http_info(x_vyasa_data_providers, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_vyasa_data_providers: remote data providers to query (required)
        :param str terms:
        :return: InlineResponse2004
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['x_vyasa_data_providers', 'terms']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_nearest_neighbor_count" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'x_vyasa_data_providers' is set
        if ('x_vyasa_data_providers' not in params or
                params['x_vyasa_data_providers'] is None):
            raise ValueError("Missing the required parameter `x_vyasa_data_providers` when calling `get_nearest_neighbor_count`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'terms' in params:
            query_params.append(('terms', params['terms']))  # noqa: E501

        header_params = {}
        if 'x_vyasa_data_providers' in params:
            header_params['X-Vyasa-Data-Providers'] = params['x_vyasa_data_providers']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oAuth2ClientCredentials']  # noqa: E501

        return self.api_client.call_api(
            '/layar/radar/count', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2004',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_radar(self, x_vyasa_data_providers, **kwargs):  # noqa: E501
        """Get Radar results  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_radar(x_vyasa_data_providers, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_vyasa_data_providers: remote data providers to query (required)
        :param int start: the start offset for the row
        :param int rows: the number of rows to return
        :param str q: the query string to search for
        :param str sort: sort results by the given property
        :param str order: what order to return sorted results
        :param date from_date: beginning of date range to return
        :param date to_date: end of date range to return
        :param float minimum_similarity: threshold for term similarity
        :param list[str] terms: query terms (results will be similar to these terms)
        :param list[str] context_terms:
        :param list[str] live_source_ids: limit results to those found in a specific live source
        :param list[str] concept_type_ids: limit results to those of a specific concept type
        :param RadarExcludeSearchCommand excludes: limit results to those without these properties
        :return: list[Radar]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_radar_with_http_info(x_vyasa_data_providers, **kwargs)  # noqa: E501
        else:
            (data) = self.get_radar_with_http_info(x_vyasa_data_providers, **kwargs)  # noqa: E501
            return data

    def get_radar_with_http_info(self, x_vyasa_data_providers, **kwargs):  # noqa: E501
        """Get Radar results  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_radar_with_http_info(x_vyasa_data_providers, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_vyasa_data_providers: remote data providers to query (required)
        :param int start: the start offset for the row
        :param int rows: the number of rows to return
        :param str q: the query string to search for
        :param str sort: sort results by the given property
        :param str order: what order to return sorted results
        :param date from_date: beginning of date range to return
        :param date to_date: end of date range to return
        :param float minimum_similarity: threshold for term similarity
        :param list[str] terms: query terms (results will be similar to these terms)
        :param list[str] context_terms:
        :param list[str] live_source_ids: limit results to those found in a specific live source
        :param list[str] concept_type_ids: limit results to those of a specific concept type
        :param RadarExcludeSearchCommand excludes: limit results to those without these properties
        :return: list[Radar]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['x_vyasa_data_providers', 'start', 'rows', 'q', 'sort', 'order', 'from_date', 'to_date', 'minimum_similarity', 'terms', 'context_terms', 'live_source_ids', 'concept_type_ids', 'excludes']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_radar" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'x_vyasa_data_providers' is set
        if ('x_vyasa_data_providers' not in params or
                params['x_vyasa_data_providers'] is None):
            raise ValueError("Missing the required parameter `x_vyasa_data_providers` when calling `get_radar`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'start' in params:
            query_params.append(('start', params['start']))  # noqa: E501
        if 'rows' in params:
            query_params.append(('rows', params['rows']))  # noqa: E501
        if 'q' in params:
            query_params.append(('q', params['q']))  # noqa: E501
        if 'sort' in params:
            query_params.append(('sort', params['sort']))  # noqa: E501
        if 'order' in params:
            query_params.append(('order', params['order']))  # noqa: E501
        if 'from_date' in params:
            query_params.append(('fromDate', params['from_date']))  # noqa: E501
        if 'to_date' in params:
            query_params.append(('toDate', params['to_date']))  # noqa: E501
        if 'minimum_similarity' in params:
            query_params.append(('minimumSimilarity', params['minimum_similarity']))  # noqa: E501
        if 'terms' in params:
            query_params.append(('terms', params['terms']))  # noqa: E501
            collection_formats['terms'] = 'multi'  # noqa: E501
        if 'context_terms' in params:
            query_params.append(('contextTerms', params['context_terms']))  # noqa: E501
            collection_formats['contextTerms'] = 'multi'  # noqa: E501
        if 'live_source_ids' in params:
            query_params.append(('liveSourceIds', params['live_source_ids']))  # noqa: E501
            collection_formats['liveSourceIds'] = 'multi'  # noqa: E501
        if 'concept_type_ids' in params:
            query_params.append(('conceptTypeIds', params['concept_type_ids']))  # noqa: E501
            collection_formats['conceptTypeIds'] = 'multi'  # noqa: E501
        if 'excludes' in params:
            query_params.append(('excludes', params['excludes']))  # noqa: E501

        header_params = {}
        if 'x_vyasa_data_providers' in params:
            header_params['X-Vyasa-Data-Providers'] = params['x_vyasa_data_providers']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oAuth2ClientCredentials']  # noqa: E501

        return self.api_client.call_api(
            '/layar/radar', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[Radar]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_radar_by_concept_id(self, **kwargs):  # noqa: E501
        """Find semantically similar terms for a concept  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_radar_by_concept_id(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int size: the number of rows to return
        :param float minimum_similarity:
        :param str concept_id:
        :param str source:
        :return: list[Radar]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_radar_by_concept_id_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_radar_by_concept_id_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_radar_by_concept_id_with_http_info(self, **kwargs):  # noqa: E501
        """Find semantically similar terms for a concept  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_radar_by_concept_id_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int size: the number of rows to return
        :param float minimum_similarity:
        :param str concept_id:
        :param str source:
        :return: list[Radar]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['size', 'minimum_similarity', 'concept_id', 'source']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_radar_by_concept_id" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'size' in params:
            query_params.append(('size', params['size']))  # noqa: E501
        if 'minimum_similarity' in params:
            query_params.append(('minimumSimilarity', params['minimum_similarity']))  # noqa: E501
        if 'concept_id' in params:
            query_params.append(('conceptId', params['concept_id']))  # noqa: E501
        if 'source' in params:
            query_params.append(('source', params['source']))  # noqa: E501

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
            '/layar/radar/byConceptId', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[Radar]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_radar_by_query_string(self, x_vyasa_data_providers, **kwargs):  # noqa: E501
        """Find semantically similar terms for a string  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_radar_by_query_string(x_vyasa_data_providers, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_vyasa_data_providers: remote data providers to query (required)
        :param str q: the query string to search for
        :param int size: the number of rows to return
        :param float minimum_similarity:
        :param str source:
        :return: list[Radar]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_radar_by_query_string_with_http_info(x_vyasa_data_providers, **kwargs)  # noqa: E501
        else:
            (data) = self.get_radar_by_query_string_with_http_info(x_vyasa_data_providers, **kwargs)  # noqa: E501
            return data

    def get_radar_by_query_string_with_http_info(self, x_vyasa_data_providers, **kwargs):  # noqa: E501
        """Find semantically similar terms for a string  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_radar_by_query_string_with_http_info(x_vyasa_data_providers, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_vyasa_data_providers: remote data providers to query (required)
        :param str q: the query string to search for
        :param int size: the number of rows to return
        :param float minimum_similarity:
        :param str source:
        :return: list[Radar]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['x_vyasa_data_providers', 'q', 'size', 'minimum_similarity', 'source']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_radar_by_query_string" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'x_vyasa_data_providers' is set
        if ('x_vyasa_data_providers' not in params or
                params['x_vyasa_data_providers'] is None):
            raise ValueError("Missing the required parameter `x_vyasa_data_providers` when calling `get_radar_by_query_string`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'q' in params:
            query_params.append(('q', params['q']))  # noqa: E501
        if 'size' in params:
            query_params.append(('size', params['size']))  # noqa: E501
        if 'minimum_similarity' in params:
            query_params.append(('minimumSimilarity', params['minimum_similarity']))  # noqa: E501
        if 'source' in params:
            query_params.append(('source', params['source']))  # noqa: E501

        header_params = {}
        if 'x_vyasa_data_providers' in params:
            header_params['X-Vyasa-Data-Providers'] = params['x_vyasa_data_providers']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oAuth2ClientCredentials']  # noqa: E501

        return self.api_client.call_api(
            '/layar/radar/byQueryString', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[Radar]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
