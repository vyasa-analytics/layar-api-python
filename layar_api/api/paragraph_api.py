# coding: utf-8

"""
    Layar API Documentation

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 2.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from layar_api.api_client import ApiClient


class ParagraphApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def paragraph_get(self, **kwargs):  # noqa: E501
        """search for paragraphs  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.paragraph_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str q: the query string to search for
        :param int rows: the number of rows to return
        :param int start: the start offset for the row
        :param str sort: sort results by the given property
        :param str order: what order to return sorted results
        :param date from_date: beginning of date range to return
        :param date to_date: end of date range to return
        :param list[str] ids: limit results to specific paragraphs
        :param list[str] document_ids: limit results to paragraphs from specific documents
        :param bool highlight: highlight the query results within the paragraphs
        :param list[str] similar_ids: find paragraphs that are similar to others (by their IDs)
        :param list[str] similar_text: find paragraphs that are similar to the supplied text
        :param list[str] sources: limit results to paragraphs from specific sources
        :return: list[Paragraph]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.paragraph_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.paragraph_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def paragraph_get_with_http_info(self, **kwargs):  # noqa: E501
        """search for paragraphs  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.paragraph_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str q: the query string to search for
        :param int rows: the number of rows to return
        :param int start: the start offset for the row
        :param str sort: sort results by the given property
        :param str order: what order to return sorted results
        :param date from_date: beginning of date range to return
        :param date to_date: end of date range to return
        :param list[str] ids: limit results to specific paragraphs
        :param list[str] document_ids: limit results to paragraphs from specific documents
        :param bool highlight: highlight the query results within the paragraphs
        :param list[str] similar_ids: find paragraphs that are similar to others (by their IDs)
        :param list[str] similar_text: find paragraphs that are similar to the supplied text
        :param list[str] sources: limit results to paragraphs from specific sources
        :return: list[Paragraph]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['q', 'rows', 'start', 'sort', 'order', 'from_date', 'to_date', 'ids', 'document_ids', 'highlight', 'similar_ids', 'similar_text', 'sources']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method paragraph_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'q' in params:
            query_params.append(('q', params['q']))  # noqa: E501
        if 'rows' in params:
            query_params.append(('rows', params['rows']))  # noqa: E501
        if 'start' in params:
            query_params.append(('start', params['start']))  # noqa: E501
        if 'sort' in params:
            query_params.append(('sort', params['sort']))  # noqa: E501
        if 'order' in params:
            query_params.append(('order', params['order']))  # noqa: E501
        if 'from_date' in params:
            query_params.append(('fromDate', params['from_date']))  # noqa: E501
        if 'to_date' in params:
            query_params.append(('toDate', params['to_date']))  # noqa: E501
        if 'ids' in params:
            query_params.append(('ids', params['ids']))  # noqa: E501
            collection_formats['ids'] = 'multi'  # noqa: E501
        if 'document_ids' in params:
            query_params.append(('documentIds', params['document_ids']))  # noqa: E501
            collection_formats['documentIds'] = 'multi'  # noqa: E501
        if 'highlight' in params:
            query_params.append(('highlight', params['highlight']))  # noqa: E501
        if 'similar_ids' in params:
            query_params.append(('similarIds', params['similar_ids']))  # noqa: E501
            collection_formats['similarIds'] = 'multi'  # noqa: E501
        if 'similar_text' in params:
            query_params.append(('similarText', params['similar_text']))  # noqa: E501
            collection_formats['similarText'] = 'multi'  # noqa: E501
        if 'sources' in params:
            query_params.append(('sources', params['sources']))  # noqa: E501
            collection_formats['sources'] = 'multi'  # noqa: E501

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
            '/paragraph', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[Paragraph]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def paragraph_id_get(self, id, **kwargs):  # noqa: E501
        """paragraph details  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.paragraph_id_get(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: (required)
        :return: Paragraph
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.paragraph_id_get_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.paragraph_id_get_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def paragraph_id_get_with_http_info(self, id, **kwargs):  # noqa: E501
        """paragraph details  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.paragraph_id_get_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: (required)
        :return: Paragraph
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
                    " to method paragraph_id_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `paragraph_id_get`")  # noqa: E501

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
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oAuth2ClientCredentials']  # noqa: E501

        return self.api_client.call_api(
            '/paragraph/{id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Paragraph',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def paragraph_search_post(self, **kwargs):  # noqa: E501
        """search for paragraphs  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.paragraph_search_post(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ParagraphSearchCommand body:
        :return: list[Paragraph]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.paragraph_search_post_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.paragraph_search_post_with_http_info(**kwargs)  # noqa: E501
            return data

    def paragraph_search_post_with_http_info(self, **kwargs):  # noqa: E501
        """search for paragraphs  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.paragraph_search_post_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ParagraphSearchCommand body:
        :return: list[Paragraph]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method paragraph_search_post" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oAuth2ClientCredentials']  # noqa: E501

        return self.api_client.call_api(
            '/paragraph/search', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[Paragraph]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def part_of_speech_parse_text_post(self, **kwargs):  # noqa: E501
        """parse text into part of speech components  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.part_of_speech_parse_text_post(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param PartOfSpeechCommand body:
        :return: list[PartOfSpeechResponse]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.part_of_speech_parse_text_post_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.part_of_speech_parse_text_post_with_http_info(**kwargs)  # noqa: E501
            return data

    def part_of_speech_parse_text_post_with_http_info(self, **kwargs):  # noqa: E501
        """parse text into part of speech components  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.part_of_speech_parse_text_post_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param PartOfSpeechCommand body:
        :return: list[PartOfSpeechResponse]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method part_of_speech_parse_text_post" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oAuth2ClientCredentials']  # noqa: E501

        return self.api_client.call_api(
            '/partOfSpeech/parseText', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[PartOfSpeechResponse]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
