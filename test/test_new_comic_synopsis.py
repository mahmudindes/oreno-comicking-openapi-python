# coding: utf-8

"""
    ComicKing

    PHP Symfony-based comic catalog full-stack.

    The version of the OpenAPI document: 0.0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from comicking_openapi.models.new_comic_synopsis import NewComicSynopsis

class TestNewComicSynopsis(unittest.TestCase):
    """NewComicSynopsis unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> NewComicSynopsis:
        """Test NewComicSynopsis
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `NewComicSynopsis`
        """
        model = NewComicSynopsis()
        if include_optional:
            return NewComicSynopsis(
                language_lang = '',
                content = '',
                source = ''
            )
        else:
            return NewComicSynopsis(
                language_lang = '',
                content = '',
        )
        """

    def testNewComicSynopsis(self):
        """Test NewComicSynopsis"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
