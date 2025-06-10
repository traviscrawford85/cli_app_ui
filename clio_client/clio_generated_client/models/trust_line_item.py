import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bill_base import BillBase
    from ..models.contact_base import ContactBase
    from ..models.matter_base import MatterBase


T = TypeVar("T", bound="TrustLineItem")


@_attrs_define
class TrustLineItem:
    """
    Attributes:
        id (Union[Unset, int]): Unique identifier for the *TrustLineItem*
        etag (Union[Unset, str]): ETag for the *TrustLineItem*
        date (Union[Unset, datetime.date]): The date of the *TrustLineItem* (as a ISO-8601 date)
        total (Union[Unset, float]): The total amount for the *TrustLineItem*
        note (Union[Unset, str]): Note for the *TrustLineItem*
        created_at (Union[Unset, datetime.datetime]): The time the *TrustLineItem* was created (as a ISO-8601 timestamp)
        updated_at (Union[Unset, datetime.datetime]): The time the *TrustLineItem* was last updated (as a ISO-8601
            timestamp)
        bill (Union[Unset, BillBase]):
        matter (Union[Unset, MatterBase]):
        client (Union[Unset, ContactBase]):
    """

    id: Union[Unset, int] = UNSET
    etag: Union[Unset, str] = UNSET
    date: Union[Unset, datetime.date] = UNSET
    total: Union[Unset, float] = UNSET
    note: Union[Unset, str] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    bill: Union[Unset, "BillBase"] = UNSET
    matter: Union[Unset, "MatterBase"] = UNSET
    client: Union[Unset, "ContactBase"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        etag = self.etag

        date: Union[Unset, str] = UNSET
        if not isinstance(self.date, Unset):
            date = self.date.isoformat()

        total = self.total

        note = self.note

        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        bill: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.bill, Unset):
            bill = self.bill.to_dict()

        matter: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.matter, Unset):
            matter = self.matter.to_dict()

        client: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.client, Unset):
            client = self.client.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if etag is not UNSET:
            field_dict["etag"] = etag
        if date is not UNSET:
            field_dict["date"] = date
        if total is not UNSET:
            field_dict["total"] = total
        if note is not UNSET:
            field_dict["note"] = note
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if bill is not UNSET:
            field_dict["bill"] = bill
        if matter is not UNSET:
            field_dict["matter"] = matter
        if client is not UNSET:
            field_dict["client"] = client

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bill_base import BillBase
        from ..models.contact_base import ContactBase
        from ..models.matter_base import MatterBase

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        etag = d.pop("etag", UNSET)

        _date = d.pop("date", UNSET)
        date: Union[Unset, datetime.date]
        if isinstance(_date, Unset):
            date = UNSET
        else:
            date = isoparse(_date).date()

        total = d.pop("total", UNSET)

        note = d.pop("note", UNSET)

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

        _bill = d.pop("bill", UNSET)
        bill: Union[Unset, BillBase]
        if isinstance(_bill, Unset):
            bill = UNSET
        else:
            bill = BillBase.from_dict(_bill)

        _matter = d.pop("matter", UNSET)
        matter: Union[Unset, MatterBase]
        if isinstance(_matter, Unset):
            matter = UNSET
        else:
            matter = MatterBase.from_dict(_matter)

        _client = d.pop("client", UNSET)
        client: Union[Unset, ContactBase]
        if isinstance(_client, Unset):
            client = UNSET
        else:
            client = ContactBase.from_dict(_client)

        trust_line_item = cls(
            id=id,
            etag=etag,
            date=date,
            total=total,
            note=note,
            created_at=created_at,
            updated_at=updated_at,
            bill=bill,
            matter=matter,
            client=client,
        )

        trust_line_item.additional_properties = d
        return trust_line_item

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
