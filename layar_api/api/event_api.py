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


class EventApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_event(self, id, **kwargs):  # noqa: E501
        """Get event details  # noqa: E501

        Get information provided in a specific Event object.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_event(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: (required)
        :return: Event
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_event_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_event_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def get_event_with_http_info(self, id, **kwargs):  # noqa: E501
        """Get event details  # noqa: E501

        Get information provided in a specific Event object.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_event_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: (required)
        :return: Event
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
                    " to method get_event" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_event`")  # noqa: E501

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
            '/layar/event/{id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Event',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def search_events(self, **kwargs):  # noqa: E501
        """Search for events  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.search_events(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int start: the start offset for the row
        :param int rows: the number of rows to return
        :param str q: the query string to search for
        :param str sort: sort results by the given property
        :param str order: what order to return sorted results
        :param date from_date: beginning of date range to return
        :param date to_date: end of date range to return
        :param str subject_id: limit results to those tagged with the given subject ID
        :param str project_id: limit results to those tagged with the given project ID
        :return: list[Event]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.search_events_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.search_events_with_http_info(**kwargs)  # noqa: E501
            return data

    def search_events_with_http_info(self, **kwargs):  # noqa: E501
        """Search for events  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.search_events_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int start: the start offset for the row
        :param int rows: the number of rows to return
        :param str q: the query string to search for
        :param str sort: sort results by the given property
        :param str order: what order to return sorted results
        :param date from_date: beginning of date range to return
        :param date to_date: end of date range to return
        :param str subject_id: limit results to those tagged with the given subject ID
        :param str project_id: limit results to those tagged with the given project ID
        :return: list[Event]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['start', 'rows', 'q', 'sort', 'order', 'from_date', 'to_date', 'subject_id', 'project_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method search_events" % key
                )
            params[key] = val
        del params['kwargs']

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
        if 'subject_id' in params:
            query_params.append(('subjectId', params['subject_id']))  # noqa: E501
        if 'project_id' in params:
            query_params.append(('projectId', params['project_id']))  # noqa: E501

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
            '/layar/event', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[Event]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
