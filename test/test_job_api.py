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
from layar_api.api.job_api import JobApi  # noqa: E501
from layar_api.rest import ApiException


class TestJobApi(unittest.TestCase):
    """JobApi unit test stubs"""

    def setUp(self):
        self.api = JobApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_job(self):
        """Test case for get_job

        Get job details  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
