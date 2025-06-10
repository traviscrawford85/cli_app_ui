from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.mattercreate_files_body_data_relationships_item_contact import (
        MattercreateFilesBodyDataRelationshipsItemContact,
    )


T = TypeVar("T", bound="MattercreateFilesBodyDataRelationshipsItem")


@_attrs_define
class MattercreateFilesBodyDataRelationshipsItem:
    """
    Attributes:
        description (str): Describe the relationship between a Contact and a Matter.
        contact (MattercreateFilesBodyDataRelationshipsItemContact):
    """

    description: str
    contact: "MattercreateFilesBodyDataRelationshipsItemContact"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        description = self.description

        contact = self.contact.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "description": description,
                "contact": contact,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.mattercreate_files_body_data_relationships_item_contact import (
            MattercreateFilesBodyDataRelationshipsItemContact,
        )

        d = dict(src_dict)
        description = d.pop("description")

        contact = MattercreateFilesBodyDataRelationshipsItemContact.from_dict(d.pop("contact"))

        mattercreate_files_body_data_relationships_item = cls(
            description=description,
            contact=contact,
        )

        mattercreate_files_body_data_relationships_item.additional_properties = d
        return mattercreate_files_body_data_relationships_item

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
