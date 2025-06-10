import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.document_version_base import DocumentVersionBase
    from ..models.user_base import UserBase


T = TypeVar("T", bound="Comment")


@_attrs_define
class Comment:
    """
    Attributes:
        id (Union[Unset, int]): Unique identifier for the *Comment*
        etag (Union[Unset, str]): ETag for the *Comment*
        message (Union[Unset, str]): The content of the Comment
        created_at (Union[Unset, datetime.datetime]): The time the *Comment* was created (as a ISO-8601 timestamp)
        updated_at (Union[Unset, datetime.datetime]): The time the *Comment* was last updated (as a ISO-8601 timestamp)
        creator (Union[Unset, UserBase]):
        document_version (Union[Unset, DocumentVersionBase]):
    """

    id: Union[Unset, int] = UNSET
    etag: Union[Unset, str] = UNSET
    message: Union[Unset, str] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    creator: Union[Unset, "UserBase"] = UNSET
    document_version: Union[Unset, "DocumentVersionBase"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        etag = self.etag

        message = self.message

        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        creator: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.creator, Unset):
            creator = self.creator.to_dict()

        document_version: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.document_version, Unset):
            document_version = self.document_version.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if etag is not UNSET:
            field_dict["etag"] = etag
        if message is not UNSET:
            field_dict["message"] = message
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if creator is not UNSET:
            field_dict["creator"] = creator
        if document_version is not UNSET:
            field_dict["document_version"] = document_version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.document_version_base import DocumentVersionBase
        from ..models.user_base import UserBase

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        etag = d.pop("etag", UNSET)

        message = d.pop("message", UNSET)

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

        _creator = d.pop("creator", UNSET)
        creator: Union[Unset, UserBase]
        if isinstance(_creator, Unset):
            creator = UNSET
        else:
            creator = UserBase.from_dict(_creator)

        _document_version = d.pop("document_version", UNSET)
        document_version: Union[Unset, DocumentVersionBase]
        if isinstance(_document_version, Unset):
            document_version = UNSET
        else:
            document_version = DocumentVersionBase.from_dict(_document_version)

        comment = cls(
            id=id,
            etag=etag,
            message=message,
            created_at=created_at,
            updated_at=updated_at,
            creator=creator,
            document_version=document_version,
        )

        comment.additional_properties = d
        return comment

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
