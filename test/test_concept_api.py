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
from layar_api.api.concept_api import ConceptApi  # noqa: E501
from layar_api.rest import ApiException


class TestConceptApi(unittest.TestCase):
    """ConceptApi unit test stubs"""

    def setUp(self):
        self.api = ConceptApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_assign_from_column(self):
        """Test case for assign_from_column

        start an async process to create concepts from a column in an uploaded spreadsheet  # noqa: E501
        """
        pass

    def test_assign_from_term(self):
        """Test case for assign_from_term

        create a concept from an arbitrary text string  # noqa: E501
        """
        pass

    def test_create(self):
        """Test case for create

        save a new concept  # noqa: E501
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

    def test_demote(self):
        """Test case for demote

        demote concept  # noqa: E501
        """
        pass

    def test_get(self):
        """Test case for get

        concept details  # noqa: E501
        """
        pass

    def test_get_external_concepts(self):
        """Test case for get_external_concepts

        find concepts by external id  # noqa: E501
        """
        pass

    def test_get_related_concepts(self):
        """Test case for get_related_concepts

        find related concepts  # noqa: E501
        """
        pass

    def test_get_statement_counts_over_time(self):
        """Test case for get_statement_counts_over_time

        statement counts over time for concept id  # noqa: E501
        """
        pass

    def test_make_primary_synonym(self):
        """Test case for make_primary_synonym

        Make Primary Synonym  # noqa: E501
        """
        pass

    def test_make_synonyms(self):
        """Test case for make_synonyms

        set all the concept ids as synonyms of each other  # noqa: E501
        """
        pass

    def test_patch(self):
        """Test case for patch

        patch  # noqa: E501
        """
        pass

    def test_remove_synonym(self):
        """Test case for remove_synonym

        Remove As Synonym  # noqa: E501
        """
        pass

    def test_search(self):
        """Test case for search

        search for concepts  # noqa: E501
        """
        pass

    def test_update(self):
        """Test case for update

        update  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
