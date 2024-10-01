# coding: utf-8

"""
    ComicKing

    PHP Symfony-based comic catalog full-stack.

    The version of the OpenAPI document: 0.0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class NewCategory(BaseModel):
    """
    NewCategory
    """ # noqa: E501
    type_code: StrictStr = Field(alias="typeCode")
    code: StrictStr
    name: StrictStr
    link_website_host: Optional[StrictStr] = Field(default=None, alias="linkWebsiteHost")
    link_relative_reference: Optional[StrictStr] = Field(default=None, alias="linkRelativeReference")
    parent_code: Optional[StrictStr] = Field(default=None, alias="parentCode")
    __properties: ClassVar[List[str]] = ["typeCode", "code", "name", "linkWebsiteHost", "linkRelativeReference", "parentCode"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of NewCategory from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # set to None if link_website_host (nullable) is None
        # and model_fields_set contains the field
        if self.link_website_host is None and "link_website_host" in self.model_fields_set:
            _dict['linkWebsiteHost'] = None

        # set to None if link_relative_reference (nullable) is None
        # and model_fields_set contains the field
        if self.link_relative_reference is None and "link_relative_reference" in self.model_fields_set:
            _dict['linkRelativeReference'] = None

        # set to None if parent_code (nullable) is None
        # and model_fields_set contains the field
        if self.parent_code is None and "parent_code" in self.model_fields_set:
            _dict['parentCode'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of NewCategory from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "typeCode": obj.get("typeCode"),
            "code": obj.get("code"),
            "name": obj.get("name"),
            "linkWebsiteHost": obj.get("linkWebsiteHost"),
            "linkRelativeReference": obj.get("linkRelativeReference"),
            "parentCode": obj.get("parentCode")
        })
        return _obj


