# coding: utf-8

"""
    ComicKing

    PHP Symfony-based comic catalog full-stack.

    The version of the OpenAPI document: 0.0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from comicking_openapi.models.set_comic_chapter import SetComicChapter

class TestSetComicChapter(unittest.TestCase):
    """SetComicChapter unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SetComicChapter:
        """Test SetComicChapter
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SetComicChapter`
        """
        model = SetComicChapter()
        if include_optional:
            return SetComicChapter(
                number = 1.337,
                version = '',
                released_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                thumbnail_link_website_host = '',
                thumbnail_link_relative_reference = '',
                volume_number = ''
            )
        else:
            return SetComicChapter(
        )
        """

    def testSetComicChapter(self):
        """Test SetComicChapter"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
