# coding: utf-8

"""
    ComicKing

    PHP Symfony-based comic catalog full-stack.

    The version of the OpenAPI document: 0.0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from comicking_openapi.models.new_comic_volume import NewComicVolume

class TestNewComicVolume(unittest.TestCase):
    """NewComicVolume unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> NewComicVolume:
        """Test NewComicVolume
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `NewComicVolume`
        """
        model = NewComicVolume()
        if include_optional:
            return NewComicVolume(
                number = 1.337,
                released_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
            )
        else:
            return NewComicVolume(
                number = 1.337,
        )
        """

    def testNewComicVolume(self):
        """Test NewComicVolume"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
