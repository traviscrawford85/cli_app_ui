import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.folder_base_type import FolderBaseType
from ..types import UNSET, Unset

T = TypeVar("T", bound="FolderBase")


@_attrs_define
class FolderBase:
    """
    Attributes:
        id (Union[Unset, int]): Unique identifier for the *Folder*
        etag (Union[Unset, str]): ETag for the *Folder*
        created_at (Union[Unset, datetime.datetime]): The time the *Folder* was created (as a ISO-8601 timestamp)
        updated_at (Union[Unset, datetime.datetime]): The time the *Folder* was last updated (as a ISO-8601 timestamp)
        deleted_at (Union[Unset, datetime.datetime]): The time the *Folder* was deleted (as a ISO-8601 timestamp)
        type_ (Union[Unset, FolderBaseType]): The type of the *Folder*
        locked (Union[Unset, bool]): Whether or not the Folder is locked. Locked Folder cannot be modified
        name (Union[Unset, str]): The name of the Folder
        root (Union[Unset, bool]): Whether or not the Folder is the root folder. There is only one root folder per
            account
    """

    id: Union[Unset, int] = UNSET
    etag: Union[Unset, str] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    deleted_at: Union[Unset, datetime.datetime] = UNSET
    type_: Union[Unset, FolderBaseType] = UNSET
    locked: Union[Unset, bool] = UNSET
    name: Union[Unset, str] = UNSET
    root: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        etag = self.etag

        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        deleted_at: Union[Unset, str] = UNSET
        if not isinstance(self.deleted_at, Unset):
            deleted_at = self.deleted_at.isoformat()

        type_: Union[Unset, str] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        locked = self.locked

        name = self.name

        root = self.root

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if etag is not UNSET:
            field_dict["etag"] = etag
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if deleted_at is not UNSET:
            field_dict["deleted_at"] = deleted_at
        if type_ is not UNSET:
            field_dict["type"] = type_
        if locked is not UNSET:
            field_dict["locked"] = locked
        if name is not UNSET:
            field_dict["name"] = name
        if root is not UNSET:
            field_dict["root"] = root

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        etag = d.pop("etag", UNSET)

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

        _deleted_at = d.pop("deleted_at", UNSET)
        deleted_at: Union[Unset, datetime.datetime]
        if isinstance(_deleted_at, Unset):
            deleted_at = UNSET
        else:
            deleted_at = isoparse(_deleted_at)

        _type_ = d.pop("type", UNSET)
        type_: Union[Unset, FolderBaseType]
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = FolderBaseType(_type_)

        locked = d.pop("locked", UNSET)

        name = d.pop("name", UNSET)

        root = d.pop("root", UNSET)

        folder_base = cls(
            id=id,
            etag=etag,
            created_at=created_at,
            updated_at=updated_at,
            deleted_at=deleted_at,
            type_=type_,
            locked=locked,
            name=name,
            root=root,
        )

        folder_base.additional_properties = d
        return folder_base

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
