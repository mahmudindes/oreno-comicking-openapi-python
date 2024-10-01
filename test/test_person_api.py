# coding: utf-8

"""
    ComicKing

    PHP Symfony-based comic catalog full-stack.

    The version of the OpenAPI document: 0.0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from comicking_openapi.api.person_api import PersonApi


class TestPersonApi(unittest.TestCase):
    """PersonApi unit test stubs"""

    def setUp(self) -> None:
        self.api = PersonApi()

    def tearDown(self) -> None:
        pass

    def test_add_person(self) -> None:
        """Test case for add_person

        Add person.
        """
        pass

    def test_delete_person(self) -> None:
        """Test case for delete_person

        Delete person.
        """
        pass

    def test_get_person(self) -> None:
        """Test case for get_person

        Get person.
        """
        pass

    def test_list_person(self) -> None:
        """Test case for list_person

        List person.
        """
        pass

    def test_update_person(self) -> None:
        """Test case for update_person

        Update person.
        """
        pass


if __name__ == '__main__':
    unittest.main()
