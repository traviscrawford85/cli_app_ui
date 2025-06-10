import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bank_account_base import BankAccountBase
    from ..models.contact_base import ContactBase
    from ..models.matter_base import MatterBase


T = TypeVar("T", bound="BankTransfer")


@_attrs_define
class BankTransfer:
    """
    Attributes:
        id (Union[Unset, int]): Unique identifier for the *BankTransfer*
        etag (Union[Unset, str]): ETag for the *BankTransfer*
        amount (Union[Unset, float]): The amount of the transfer.
        date (Union[Unset, datetime.datetime]): The date of the transfer.
        description (Union[Unset, str]): The description of the transfer.
        primary_authorizer (Union[Unset, str]): The primary authorizer of the transfer.
        secondary_authorizer (Union[Unset, str]): The secondary authorizer of the transfer.
        created_at (Union[Unset, datetime.datetime]): The time the *BankTransfer* was created (as a ISO-8601 timestamp)
        updated_at (Union[Unset, datetime.datetime]): The time the *BankTransfer* was last updated (as a ISO-8601
            timestamp)
        client (Union[Unset, ContactBase]):
        destination_account (Union[Unset, BankAccountBase]):
        matter (Union[Unset, MatterBase]):
        source_account (Union[Unset, BankAccountBase]):
    """

    id: Union[Unset, int] = UNSET
    etag: Union[Unset, str] = UNSET
    amount: Union[Unset, float] = UNSET
    date: Union[Unset, datetime.datetime] = UNSET
    description: Union[Unset, str] = UNSET
    primary_authorizer: Union[Unset, str] = UNSET
    secondary_authorizer: Union[Unset, str] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    client: Union[Unset, "ContactBase"] = UNSET
    destination_account: Union[Unset, "BankAccountBase"] = UNSET
    matter: Union[Unset, "MatterBase"] = UNSET
    source_account: Union[Unset, "BankAccountBase"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        etag = self.etag

        amount = self.amount

        date: Union[Unset, str] = UNSET
        if not isinstance(self.date, Unset):
            date = self.date.isoformat()

        description = self.description

        primary_authorizer = self.primary_authorizer

        secondary_authorizer = self.secondary_authorizer

        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        client: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.client, Unset):
            client = self.client.to_dict()

        destination_account: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.destination_account, Unset):
            destination_account = self.destination_account.to_dict()

        matter: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.matter, Unset):
            matter = self.matter.to_dict()

        source_account: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.source_account, Unset):
            source_account = self.source_account.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if etag is not UNSET:
            field_dict["etag"] = etag
        if amount is not UNSET:
            field_dict["amount"] = amount
        if date is not UNSET:
            field_dict["date"] = date
        if description is not UNSET:
            field_dict["description"] = description
        if primary_authorizer is not UNSET:
            field_dict["primary_authorizer"] = primary_authorizer
        if secondary_authorizer is not UNSET:
            field_dict["secondary_authorizer"] = secondary_authorizer
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if client is not UNSET:
            field_dict["client"] = client
        if destination_account is not UNSET:
            field_dict["destination_account"] = destination_account
        if matter is not UNSET:
            field_dict["matter"] = matter
        if source_account is not UNSET:
            field_dict["source_account"] = source_account

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bank_account_base import BankAccountBase
        from ..models.contact_base import ContactBase
        from ..models.matter_base import MatterBase

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        etag = d.pop("etag", UNSET)

        amount = d.pop("amount", UNSET)

        _date = d.pop("date", UNSET)
        date: Union[Unset, datetime.datetime]
        if isinstance(_date, Unset):
            date = UNSET
        else:
            date = isoparse(_date)

        description = d.pop("description", UNSET)

        primary_authorizer = d.pop("primary_authorizer", UNSET)

        secondary_authorizer = d.pop("secondary_authorizer", UNSET)

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

        _client = d.pop("client", UNSET)
        client: Union[Unset, ContactBase]
        if isinstance(_client, Unset):
            client = UNSET
        else:
            client = ContactBase.from_dict(_client)

        _destination_account = d.pop("destination_account", UNSET)
        destination_account: Union[Unset, BankAccountBase]
        if isinstance(_destination_account, Unset):
            destination_account = UNSET
        else:
            destination_account = BankAccountBase.from_dict(_destination_account)

        _matter = d.pop("matter", UNSET)
        matter: Union[Unset, MatterBase]
        if isinstance(_matter, Unset):
            matter = UNSET
        else:
            matter = MatterBase.from_dict(_matter)

        _source_account = d.pop("source_account", UNSET)
        source_account: Union[Unset, BankAccountBase]
        if isinstance(_source_account, Unset):
            source_account = UNSET
        else:
            source_account = BankAccountBase.from_dict(_source_account)

        bank_transfer = cls(
            id=id,
            etag=etag,
            amount=amount,
            date=date,
            description=description,
            primary_authorizer=primary_authorizer,
            secondary_authorizer=secondary_authorizer,
            created_at=created_at,
            updated_at=updated_at,
            client=client,
            destination_account=destination_account,
            matter=matter,
            source_account=source_account,
        )

        bank_transfer.additional_properties = d
        return bank_transfer

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
