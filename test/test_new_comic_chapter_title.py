# coding: utf-8

"""
    ComicKing

    PHP Symfony-based comic catalog full-stack.

    The version of the OpenAPI document: 0.0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from comicking_openapi.models.new_comic_chapter_title import NewComicChapterTitle

class TestNewComicChapterTitle(unittest.TestCase):
    """NewComicChapterTitle unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> NewComicChapterTitle:
        """Test NewComicChapterTitle
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `NewComicChapterTitle`
        """
        model = NewComicChapterTitle()
        if include_optional:
            return NewComicChapterTitle(
                language_lang = '',
                content = '',
                is_synonym = True,
                is_latinized = True
            )
        else:
            return NewComicChapterTitle(
                language_lang = '',
                content = '',
        )
        """

    def testNewComicChapterTitle(self):
        """Test NewComicChapterTitle"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
