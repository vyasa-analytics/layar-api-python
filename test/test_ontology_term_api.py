# coding: utf-8

"""
    Layar API Documentation

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 2.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import layar_api
from layar_api.api.ontology_term_api import OntologyTermApi  # noqa: E501
from layar_api.rest import ApiException


class TestOntologyTermApi(unittest.TestCase):
    """OntologyTermApi unit test stubs"""

    def setUp(self):
        self.api = OntologyTermApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_ontology_term_get(self):
        """Test case for ontology_term_get

        search for ontology terms  # noqa: E501
        """
        pass

    def test_ontology_term_id_delete(self):
        """Test case for ontology_term_id_delete

        delete  # noqa: E501
        """
        pass

    def test_ontology_term_id_get(self):
        """Test case for ontology_term_id_get

        ontologyTerm details  # noqa: E501
        """
        pass

    def test_ontology_term_id_put(self):
        """Test case for ontology_term_id_put

        update  # noqa: E501
        """
        pass

    def test_ontology_term_post(self):
        """Test case for ontology_term_post

        save a new ontology term  # noqa: E501
        """
        pass

    def test_ontology_term_search_post(self):
        """Test case for ontology_term_search_post

        search for ontologyTerms  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
