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
from layar_api.api.gpt_api import GptApi  # noqa: E501
from layar_api.rest import ApiException


class TestGptApi(unittest.TestCase):
    """GptApi unit test stubs"""

    def setUp(self):
        self.api = GptApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_generate(self):
        """Test case for generate

        Call Vyasa LLM to generate a system message and return the corresponding sources used  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()