
"""
    Clio API Documentation

    # Developer Support and Feedback * Clio takes the availability and stability of our API seriously; please report any **degradations** or **breakages** to Clio's API Support team at [api@clio.com](mailto:api@clio.com). * For business and partnership inquiries, contact our API Partnerships team at [api.partnerships@clio.com](mailto:api.partnerships@clio.com). * For best practices and tips from the Clio development community, join the conversation in the [Clio Developer Slack Channel](https://join.slack.com/t/clio-public/shared_invite/zt-1bd5nfbiv-WloZR3ZjepoUTv28SI1ezw).  A community-driven [Clio Developers Stack Overflow Group](https://stackoverflow.com/questions/tagged/clio-api) also exists where you can connect and ask questions from other Clio API users. # Getting Started > **Note:** The API is available in four distinct data regions: Australia (au.app.clio.com), Canada (ca.app.clio.com), EU (eu.app.clio.com) and US (app.clio.com). > > Likewise, the developer portal is available at region-specific links for the [Australia](https://au.developers.clio.com), [Canada](https://ca.developers.clio.com), [EU](https://eu.developers.clio.com), and [US](https://developers.clio.com) regions. > > This document assumes the US region is being used (app.clio.com). If you're building in one of the other regions, you should adapt the links and examples as necessary.  To start building on the Clio API, you’ll need a Clio account – you can review our [Developer Handbook](https://docs.developers.clio.com/) and follow the steps to sign up for an account.  Once you have an account, you can [create a developer application](https://docs.developers.clio.com/api-docs/applications) from the [Developer Portal](https://developers.clio.com) and start building! # Authorization with OAuth 2.0 See our [Authorization documentation →](https://docs.developers.clio.com/api-docs/authorization) # Permissions See our [Permissions documentation →](https://docs.developers.clio.com/api-docs/permissions) # Fields See our [Fields documentation →](https://docs.developers.clio.com/api-docs/fields) # Rate Limiting See our [Rate Limits documentation →](https://docs.developers.clio.com/api-docs/rate-limits) # Paging See our [Pagination documentation →](https://docs.developers.clio.com/api-docs/paging) # ETags See our [ETags documentation →](https://docs.developers.clio.com/api-docs/etags) # Minor Versions API v4 supports multiple minor versions. Versions are of the form '4.X.Y'. To request a specific version, you can use an `X-API-VERSION` header in your request, with the header value set to the API version you're requesting. If this header is omitted, it will be treated as a request for the default API version. If the header is present but invalid, it will return a `410 Gone` response. If the header is present and valid, but it is no longer supported, it will return a `410 Gone` response.  An `X-API-VERSION` will be included in all successful responses, with the value being set to the API version used.  You can find our [API Versioning Policy and Guidelines](https://docs.developers.clio.com/api-docs/api-versioning-policy) in our documentation hub.  The [API Changelog](https://docs.developers.clio.com/api-docs/api-changelog) explains each version's changes in further detail. - 4.0.4    Update `quantity` field to return values in seconds rather than hours for Activities  - 4.0.5    * Remove `matter_balances` field from Bills   * Standardize status/state enum values   * Add a Document association to completed DocumentAutomations   * Add rate visibility handling for Activity's price and total  - 4.0.6    Remove `document_versions` collection field from Documents  - 4.0.7    Change secure link format  - 4.0.8    * `Activity` hours are redacted in the response based on the activity hours visibility setting for the user   * Add `quantity_redacted` field to activities  - 4.0.9    **This is the default version**    Contacts are filtered and redacted in the response based on the new 'Contacts Visibility' user permission setting.  - 4.0.10    Fixed validation of `type` query parameter when querying Notes   

    The version of the OpenAPI document: v4
    Contact: api@clio.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations

import json
import pprint
import re  # noqa: F401
from datetime import date, datetime
from typing import Any, ClassVar, Dict, List, Optional, Set, Union

from clio_sdk.models.activity_calendar_entry_base import ActivityCalendarEntryBase
from clio_sdk.models.activity_description_base import ActivityDescriptionBase
from clio_sdk.models.activity_task_base import ActivityTaskBase
from clio_sdk.models.activity_text_message_conversation_base import ActivityTextMessageConversationBase
from clio_sdk.models.bill_base import BillBase
from clio_sdk.models.client_portal_base import ClientPortalBase
from clio_sdk.models.communication_base import CommunicationBase
from clio_sdk.models.contact_base import ContactBase
from clio_sdk.models.currency_base import CurrencyBase
from clio_sdk.models.document_version_base import DocumentVersionBase
from clio_sdk.models.expense_category_base import ExpenseCategoryBase
from clio_sdk.models.legal_aid_uk_activity_base import LegalAidUkActivityBase
from clio_sdk.models.matter_base import MatterBase
from clio_sdk.models.note_base import NoteBase
from clio_sdk.models.polymorphic_object_base import PolymorphicObjectBase
from clio_sdk.models.timer_base import TimerBase
from clio_sdk.models.user_base import UserBase
from clio_sdk.models.utbms_code_base import UtbmsCodeBase
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictFloat, StrictInt, StrictStr, field_validator
from typing_extensions import Self


class Activity(BaseModel):
    """
    Activity
    """ # noqa: E501
    id: Optional[StrictInt] = Field(default=None, description="Unique identifier for the *Activity*")
    etag: Optional[StrictStr] = Field(default=None, description="ETag for the *Activity*")
    type: Optional[StrictStr] = Field(default=None, description="The type of the *Activity*")
    var_date: Optional[date] = Field(default=None, description="The date the *Activity* was performed (as a ISO-8601 date)", alias="date")
    quantity_in_hours: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The number of hours the TimeEntry took.")
    rounded_quantity_in_hours: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The number of hours rounded accordingly to the billing settings. The rounded value is used to calculate the total. ")
    quantity: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The field is applicable to TimeEntry, ExpenseEntry, and SoftCostEntry.  **Version <= 4.0.3:** The number of hours the TimeEntry took.  **Latest version:** The number of seconds the TimeEntry took. ")
    rounded_quantity: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The field is applicable to time entries only.  **Version <= 4.0.3:** The number of hours rounded accordingly to the billing settings. The rounded value is used to calculate the total.  **Latest version:** The number of seconds rounded accordingly to the billing settings. The rounded value is used to calculate the total. ")
    quantity_redacted: Optional[StrictBool] = Field(default=None, description="Is `true` if any of the following fields are redacted: `quantity`, `rounded_quantity`, `rounded_quantity_in_hours`, `quantity_in_hours`, `total`, `non_billable_total` ")
    price: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The hourly or flat rate of the *Activity*")
    note: Optional[StrictStr] = Field(default=None, description="The details about the *Activity*")
    flat_rate: Optional[StrictBool] = Field(default=None, description="Whether the *Activity* is a flat rate")
    billed: Optional[StrictBool] = Field(default=None, description="Whether the *Activity* has been added to an active bill that is in the state of `awaiting_payment` or `paid`")
    on_bill: Optional[StrictBool] = Field(default=None, description="Whether the *Activity* has been added to an active bill that is in the state of `draft`, `awaiting_approval`, `awaiting_payment` or `paid`")
    total: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The total cost of draft, billable and billed items in the *Activity*")
    contingency_fee: Optional[StrictBool] = Field(default=None, description="Whether or not the *Activity* is a contingency fee")
    created_at: Optional[datetime] = Field(default=None, description="The time the *Activity* was created (as a ISO-8601 timestamp)")
    updated_at: Optional[datetime] = Field(default=None, description="The time the *Activity* was last updated (as a ISO-8601 timestamp)")
    reference: Optional[StrictStr] = Field(default=None, description="A check reference for a HardCostEntry.")
    non_billable: Optional[StrictBool] = Field(default=None, description="Whether the *Activity* is non-billable")
    non_billable_total: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The total cost of non-billable items in the *Activity*")
    no_charge: Optional[StrictBool] = Field(default=None, description="Whether the non-billable *Activity* is shown on the bill.")
    tax_setting: Optional[StrictStr] = Field(default=None, description="The option denoting whether primary tax, secondary tax, or both is applied to an expense entry.")
    currency: Optional[CurrencyBase] = None
    activity_description: Optional[ActivityDescriptionBase] = None
    expense_category: Optional[ExpenseCategoryBase] = None
    bill: Optional[BillBase] = None
    communication: Optional[CommunicationBase] = None
    client_portal: Optional[ClientPortalBase] = None
    matter: Optional[MatterBase] = None
    matter_note: Optional[NoteBase] = None
    contact_note: Optional[NoteBase] = None
    subject: Optional[PolymorphicObjectBase] = None
    timer: Optional[TimerBase] = None
    user: Optional[UserBase] = None
    utbms_expense: Optional[UtbmsCodeBase] = None
    vendor: Optional[ContactBase] = None
    calendar_entry: Optional[ActivityCalendarEntryBase] = None
    task: Optional[ActivityTaskBase] = None
    text_message_conversation: Optional[ActivityTextMessageConversationBase] = None
    document_version: Optional[DocumentVersionBase] = None
    legal_aid_uk_activity: Optional[LegalAidUkActivityBase] = None
    __properties: ClassVar[List[str]] = ["id", "etag", "type", "date", "quantity_in_hours", "rounded_quantity_in_hours", "quantity", "rounded_quantity", "quantity_redacted", "price", "note", "flat_rate", "billed", "on_bill", "total", "contingency_fee", "created_at", "updated_at", "reference", "non_billable", "non_billable_total", "no_charge", "tax_setting", "currency", "activity_description", "expense_category", "bill", "communication", "client_portal", "matter", "matter_note", "contact_note", "subject", "timer", "user", "utbms_expense", "vendor", "calendar_entry", "task", "text_message_conversation", "document_version", "legal_aid_uk_activity"]

    @field_validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['TimeEntry', 'ExpenseEntry', 'HardCostEntry', 'SoftCostEntry']):
            raise ValueError("must be one of enum values ('TimeEntry', 'ExpenseEntry', 'HardCostEntry', 'SoftCostEntry')")
        return value

    @field_validator('tax_setting')
    def tax_setting_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['no_tax', 'tax_1_only', 'tax_2_only', 'tax_1_and_tax_2']):
            raise ValueError("must be one of enum values ('no_tax', 'tax_1_only', 'tax_2_only', 'tax_1_and_tax_2')")
        return value

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
        """Create an instance of Activity from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of currency
        if self.currency:
            _dict['currency'] = self.currency.to_dict()
        # override the default output from pydantic by calling `to_dict()` of activity_description
        if self.activity_description:
            _dict['activity_description'] = self.activity_description.to_dict()
        # override the default output from pydantic by calling `to_dict()` of expense_category
        if self.expense_category:
            _dict['expense_category'] = self.expense_category.to_dict()
        # override the default output from pydantic by calling `to_dict()` of bill
        if self.bill:
            _dict['bill'] = self.bill.to_dict()
        # override the default output from pydantic by calling `to_dict()` of communication
        if self.communication:
            _dict['communication'] = self.communication.to_dict()
        # override the default output from pydantic by calling `to_dict()` of client_portal
        if self.client_portal:
            _dict['client_portal'] = self.client_portal.to_dict()
        # override the default output from pydantic by calling `to_dict()` of matter
        if self.matter:
            _dict['matter'] = self.matter.to_dict()
        # override the default output from pydantic by calling `to_dict()` of matter_note
        if self.matter_note:
            _dict['matter_note'] = self.matter_note.to_dict()
        # override the default output from pydantic by calling `to_dict()` of contact_note
        if self.contact_note:
            _dict['contact_note'] = self.contact_note.to_dict()
        # override the default output from pydantic by calling `to_dict()` of subject
        if self.subject:
            _dict['subject'] = self.subject.to_dict()
        # override the default output from pydantic by calling `to_dict()` of timer
        if self.timer:
            _dict['timer'] = self.timer.to_dict()
        # override the default output from pydantic by calling `to_dict()` of user
        if self.user:
            _dict['user'] = self.user.to_dict()
        # override the default output from pydantic by calling `to_dict()` of utbms_expense
        if self.utbms_expense:
            _dict['utbms_expense'] = self.utbms_expense.to_dict()
        # override the default output from pydantic by calling `to_dict()` of vendor
        if self.vendor:
            _dict['vendor'] = self.vendor.to_dict()
        # override the default output from pydantic by calling `to_dict()` of calendar_entry
        if self.calendar_entry:
            _dict['calendar_entry'] = self.calendar_entry.to_dict()
        # override the default output from pydantic by calling `to_dict()` of task
        if self.task:
            _dict['task'] = self.task.to_dict()
        # override the default output from pydantic by calling `to_dict()` of text_message_conversation
        if self.text_message_conversation:
            _dict['text_message_conversation'] = self.text_message_conversation.to_dict()
        # override the default output from pydantic by calling `to_dict()` of document_version
        if self.document_version:
            _dict['document_version'] = self.document_version.to_dict()
        # override the default output from pydantic by calling `to_dict()` of legal_aid_uk_activity
        if self.legal_aid_uk_activity:
            _dict['legal_aid_uk_activity'] = self.legal_aid_uk_activity.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Activity from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "etag": obj.get("etag"),
            "type": obj.get("type"),
            "date": obj.get("date"),
            "quantity_in_hours": obj.get("quantity_in_hours"),
            "rounded_quantity_in_hours": obj.get("rounded_quantity_in_hours"),
            "quantity": obj.get("quantity"),
            "rounded_quantity": obj.get("rounded_quantity"),
            "quantity_redacted": obj.get("quantity_redacted"),
            "price": obj.get("price"),
            "note": obj.get("note"),
            "flat_rate": obj.get("flat_rate"),
            "billed": obj.get("billed"),
            "on_bill": obj.get("on_bill"),
            "total": obj.get("total"),
            "contingency_fee": obj.get("contingency_fee"),
            "created_at": obj.get("created_at"),
            "updated_at": obj.get("updated_at"),
            "reference": obj.get("reference"),
            "non_billable": obj.get("non_billable"),
            "non_billable_total": obj.get("non_billable_total"),
            "no_charge": obj.get("no_charge"),
            "tax_setting": obj.get("tax_setting"),
            "currency": CurrencyBase.from_dict(obj["currency"]) if obj.get("currency") is not None else None,
            "activity_description": ActivityDescriptionBase.from_dict(obj["activity_description"]) if obj.get("activity_description") is not None else None,
            "expense_category": ExpenseCategoryBase.from_dict(obj["expense_category"]) if obj.get("expense_category") is not None else None,
            "bill": BillBase.from_dict(obj["bill"]) if obj.get("bill") is not None else None,
            "communication": CommunicationBase.from_dict(obj["communication"]) if obj.get("communication") is not None else None,
            "client_portal": ClientPortalBase.from_dict(obj["client_portal"]) if obj.get("client_portal") is not None else None,
            "matter": MatterBase.from_dict(obj["matter"]) if obj.get("matter") is not None else None,
            "matter_note": NoteBase.from_dict(obj["matter_note"]) if obj.get("matter_note") is not None else None,
            "contact_note": NoteBase.from_dict(obj["contact_note"]) if obj.get("contact_note") is not None else None,
            "subject": PolymorphicObjectBase.from_dict(obj["subject"]) if obj.get("subject") is not None else None,
            "timer": TimerBase.from_dict(obj["timer"]) if obj.get("timer") is not None else None,
            "user": UserBase.from_dict(obj["user"]) if obj.get("user") is not None else None,
            "utbms_expense": UtbmsCodeBase.from_dict(obj["utbms_expense"]) if obj.get("utbms_expense") is not None else None,
            "vendor": ContactBase.from_dict(obj["vendor"]) if obj.get("vendor") is not None else None,
            "calendar_entry": ActivityCalendarEntryBase.from_dict(obj["calendar_entry"]) if obj.get("calendar_entry") is not None else None,
            "task": ActivityTaskBase.from_dict(obj["task"]) if obj.get("task") is not None else None,
            "text_message_conversation": ActivityTextMessageConversationBase.from_dict(obj["text_message_conversation"]) if obj.get("text_message_conversation") is not None else None,
            "document_version": DocumentVersionBase.from_dict(obj["document_version"]) if obj.get("document_version") is not None else None,
            "legal_aid_uk_activity": LegalAidUkActivityBase.from_dict(obj["legal_aid_uk_activity"]) if obj.get("legal_aid_uk_activity") is not None else None
        })
        return _obj


