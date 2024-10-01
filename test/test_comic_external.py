# coding: utf-8

"""
    ComicKing

    PHP Symfony-based comic catalog full-stack.

    The version of the OpenAPI document: 0.0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from comicking_openapi.models.comic_external import ComicExternal

class TestComicExternal(unittest.TestCase):
    """ComicExternal unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ComicExternal:
        """Test ComicExternal
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ComicExternal`
        """
        model = ComicExternal()
        if include_optional:
            return ComicExternal(
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                ulid = '',
                link_website_host = '',
                link_website_name = '',
                link_relative_reference = '',
                is_official = True,
                is_community = True
            )
        else:
            return ComicExternal(
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                ulid = '',
                link_website_host = '',
                link_website_name = '',
        )
        """

    def testComicExternal(self):
        """Test ComicExternal"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
