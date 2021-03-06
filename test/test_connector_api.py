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
from layar_api.api.connector_api import ConnectorApi  # noqa: E501
from layar_api.rest import ApiException


class TestConnectorApi(unittest.TestCase):
    """ConnectorApi unit test stubs"""

    def setUp(self):
        self.api = ConnectorApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create(self):
        """Test case for create

        save  # noqa: E501
        """
        pass

    def test_delete(self):
        """Test case for delete

        delete  # noqa: E501
        """
        pass

    def test_delete_many(self):
        """Test case for delete_many

        delete all the records with the given IDs  # noqa: E501
        """
        pass

    def test_get(self):
        """Test case for get

        connector details  # noqa: E501
        """
        pass

    def test_patch(self):
        """Test case for patch

        patch  # noqa: E501
        """
        pass

    def test_search(self):
        """Test case for search

        """
        pass

    def test_update(self):
        """Test case for update

        update  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
