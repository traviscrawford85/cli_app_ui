import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.web_site_base_name import WebSiteBaseName
from ..types import UNSET, Unset

T = TypeVar("T", bound="WebSiteBase")


@_attrs_define
class WebSiteBase:
    """
    Attributes:
        id (Union[Unset, int]): Unique identifier for the *WebSite*
        etag (Union[Unset, str]): ETag for the *WebSite*
        address (Union[Unset, str]): The address of the *WebSite*
        name (Union[Unset, WebSiteBaseName]): The type of *WebSite* it is
        default_web_site (Union[Unset, bool]): Whether it is the default for this contact
        created_at (Union[Unset, datetime.datetime]): The time the *WebSite* was created (as a ISO-8601 timestamp)
        updated_at (Union[Unset, datetime.datetime]): The time the *WebSite* was last updated (as a ISO-8601 timestamp)
    """

    id: Union[Unset, int] = UNSET
    etag: Union[Unset, str] = UNSET
    address: Union[Unset, str] = UNSET
    name: Union[Unset, WebSiteBaseName] = UNSET
    default_web_site: Union[Unset, bool] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        etag = self.etag

        address = self.address

        name: Union[Unset, str] = UNSET
        if not isinstance(self.name, Unset):
            name = self.name.value

        default_web_site = self.default_web_site

        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if etag is not UNSET:
            field_dict["etag"] = etag
        if address is not UNSET:
            field_dict["address"] = address
        if name is not UNSET:
            field_dict["name"] = name
        if default_web_site is not UNSET:
            field_dict["default_web_site"] = default_web_site
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        etag = d.pop("etag", UNSET)

        address = d.pop("address", UNSET)

        _name = d.pop("name", UNSET)
        name: Union[Unset, WebSiteBaseName]
        if isinstance(_name, Unset):
            name = UNSET
        else:
            name = WebSiteBaseName(_name)

        default_web_site = d.pop("default_web_site", UNSET)

        _created_at = d.pop("created_at", UNSET)
        created_at: Union[Unset, datetime.datetime]
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        _updated_at = d.pop("updated_at", UNSET)
        updated_at: Union[Unset, datetime.datetime]
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)

        web_site_base = cls(
            id=id,
            etag=etag,
            address=address,
            name=name,
            default_web_site=default_web_site,
            created_at=created_at,
            updated_at=updated_at,
        )

        web_site_base.additional_properties = d
        return web_site_base

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
