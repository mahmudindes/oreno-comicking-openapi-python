# coding: utf-8

"""
    ComicKing

    PHP Symfony-based comic catalog full-stack.

    The version of the OpenAPI document: 0.0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from comicking_openapi.models.set_comic_external import SetComicExternal

class TestSetComicExternal(unittest.TestCase):
    """SetComicExternal unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SetComicExternal:
        """Test SetComicExternal
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SetComicExternal`
        """
        model = SetComicExternal()
        if include_optional:
            return SetComicExternal(
                link_website_host = '',
                link_relative_reference = '',
                is_official = True,
                is_community = True
            )
        else:
            return SetComicExternal(
        )
        """

    def testSetComicExternal(self):
        """Test SetComicExternal"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
