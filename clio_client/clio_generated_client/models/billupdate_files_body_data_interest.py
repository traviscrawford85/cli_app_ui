from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.billupdate_files_body_data_interest_type import BillupdateFilesBodyDataInterestType
from ..types import UNSET, Unset

T = TypeVar("T", bound="BillupdateFilesBodyDataInterest")


@_attrs_define
class BillupdateFilesBodyDataInterest:
    """
    Attributes:
        rate (Union[Unset, float]): Interest amount for the Bill as percentage.
        type_ (Union[Unset, BillupdateFilesBodyDataInterestType]): The type of interest you are applying to your Bill
            with the `interest[rate]`.
        period (Union[Unset, int]): The interest period for how frequently your Bill will charge interest.
    """

    rate: Union[Unset, float] = UNSET
    type_: Union[Unset, BillupdateFilesBodyDataInterestType] = UNSET
    period: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        rate = self.rate

        type_: Union[Unset, str] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        period = self.period

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if rate is not UNSET:
            field_dict["rate"] = rate
        if type_ is not UNSET:
            field_dict["type"] = type_
        if period is not UNSET:
            field_dict["period"] = period

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        rate = d.pop("rate", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: Union[Unset, BillupdateFilesBodyDataInterestType]
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = BillupdateFilesBodyDataInterestType(_type_)

        period = d.pop("period", UNSET)

        billupdate_files_body_data_interest = cls(
            rate=rate,
            type_=type_,
            period=period,
        )

        billupdate_files_body_data_interest.additional_properties = d
        return billupdate_files_body_data_interest

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
