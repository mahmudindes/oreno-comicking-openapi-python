# coding: utf-8

"""
    ComicKing

    PHP Symfony-based comic catalog full-stack.

    The version of the OpenAPI document: 0.0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from comicking_openapi.models.category import Category

class TestCategory(unittest.TestCase):
    """Category unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Category:
        """Test Category
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Category`
        """
        model = Category()
        if include_optional:
            return Category(
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                type_code = '',
                code = '',
                name = '',
                link_website_host = '',
                link_relative_reference = '',
                parent_code = '',
                child_count = 56
            )
        else:
            return Category(
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                type_code = '',
                code = '',
                name = '',
                child_count = 56,
        )
        """

    def testCategory(self):
        """Test Category"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
