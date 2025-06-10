import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.activity_base import ActivityBase


T = TypeVar("T", bound="Timer")


@_attrs_define
class Timer:
    """
    Attributes:
        id (Union[Unset, int]): Unique identifier for the *Timer*
        etag (Union[Unset, str]): ETag for the *Timer*
        start_time (Union[Unset, datetime.datetime]): The time the *Timer* was started (as ISO-8601 timestamp)
        elapsed_time (Union[Unset, float]): How much time has elapsed, in hours, since the timer was started
        created_at (Union[Unset, datetime.datetime]): The time the *Timer* was created (as a ISO-8601 timestamp)
        updated_at (Union[Unset, datetime.datetime]): The time the *Timer* was last updated (as a ISO-8601 timestamp)
        activity (Union[Unset, ActivityBase]):
    """

    id: Union[Unset, int] = UNSET
    etag: Union[Unset, str] = UNSET
    start_time: Union[Unset, datetime.datetime] = UNSET
    elapsed_time: Union[Unset, float] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    activity: Union[Unset, "ActivityBase"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        etag = self.etag

        start_time: Union[Unset, str] = UNSET
        if not isinstance(self.start_time, Unset):
            start_time = self.start_time.isoformat()

        elapsed_time = self.elapsed_time

        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        activity: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.activity, Unset):
            activity = self.activity.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if etag is not UNSET:
            field_dict["etag"] = etag
        if start_time is not UNSET:
            field_dict["start_time"] = start_time
        if elapsed_time is not UNSET:
            field_dict["elapsed_time"] = elapsed_time
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if activity is not UNSET:
            field_dict["activity"] = activity

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.activity_base import ActivityBase

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        etag = d.pop("etag", UNSET)

        _start_time = d.pop("start_time", UNSET)
        start_time: Union[Unset, datetime.datetime]
        if isinstance(_start_time, Unset):
            start_time = UNSET
        else:
            start_time = isoparse(_start_time)

        elapsed_time = d.pop("elapsed_time", UNSET)

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

        _activity = d.pop("activity", UNSET)
        activity: Union[Unset, ActivityBase]
        if isinstance(_activity, Unset):
            activity = UNSET
        else:
            activity = ActivityBase.from_dict(_activity)

        timer = cls(
            id=id,
            etag=etag,
            start_time=start_time,
            elapsed_time=elapsed_time,
            created_at=created_at,
            updated_at=updated_at,
            activity=activity,
        )

        timer.additional_properties = d
        return timer

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
