# coding: utf-8

"""
    ComicKing

    PHP Symfony-based comic catalog full-stack.

    The version of the OpenAPI document: 0.0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from comicking_openapi.models.set_comic_cover import SetComicCover

class TestSetComicCover(unittest.TestCase):
    """SetComicCover unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SetComicCover:
        """Test SetComicCover
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SetComicCover`
        """
        model = SetComicCover()
        if include_optional:
            return SetComicCover(
                link_website_host = '',
                link_relative_reference = '',
                hint = ''
            )
        else:
            return SetComicCover(
        )
        """

    def testSetComicCover(self):
        """Test SetComicCover"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
