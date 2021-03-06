# coding: utf-8

"""
    Layar API Documentation

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import layar_api
from layar_api.api.clustered_query_api import ClusteredQueryApi  # noqa: E501
from layar_api.rest import ApiException


class TestClusteredQueryApi(unittest.TestCase):
    """ClusteredQueryApi unit test stubs"""

    def setUp(self):
        self.api = ClusteredQueryApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create(self):
        """Test case for create

        create a new clustered query request  # noqa: E501
        """
        pass

    def test_get(self):
        """Test case for get

        clustered query details  # noqa: E501
        """
        pass

    def test_get_by_query_string(self):
        """Test case for get_by_query_string

        find clustered query by query string  # noqa: E501
        """
        pass

    def test_get_clusters(self):
        """Test case for get_clusters

        getClusters  # noqa: E501
        """
        pass

    def test_update(self):
        """Test case for update

        update  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
