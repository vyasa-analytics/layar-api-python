# coding: utf-8

"""
    Layar API Documentation

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: VERSION_PLACEHOLDER
    Contact: support@vyasa.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import layar_api
from layar_api.api.administration_api import AdministrationApi  # noqa: E501
from layar_api.rest import ApiException


class TestAdministrationApi(unittest.TestCase):
    """AdministrationApi unit test stubs"""

    def setUp(self):
        self.api = AdministrationApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_debug_logging(self):
        """Test case for debug_logging

        temporarily (15m) enable DEBUG level logging  # noqa: E501
        """
        pass

    def test_diagnostics(self):
        """Test case for diagnostics

        generate an encrypted diagnostics file  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
