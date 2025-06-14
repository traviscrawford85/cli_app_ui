# generated by datamodel-codegen:
#   filename:  openapi_sdk.yaml

from __future__ import annotations

from decimal import Decimal
from typing import Optional

from pydantic import BaseModel, Field


class LaukCivilCertificatedRateBase(BaseModel):
    activity: Optional[str] = Field(
        None, description="Activity of the *LaukCivilCertificatedRate*"
    )
    activity_sub_category: Optional[str] = Field(
        None, description="Activity sub-category"
    )
    activity_type: Optional[str] = Field(None, description="Activity type")
    attended_several_hearings_for_multiple_clients: Optional[bool] = Field(
        None, description="Multiple hearings for multiple clients indicator"
    )
    category_of_law: Optional[str] = Field(None, description="Category of law")
    change_of_solicitor: Optional[bool] = Field(
        None, description="Change of solicitor indicator"
    )
    court: Optional[str] = Field(None, description="Court associated")
    created_at: Optional[str] = Field(
        None,
        description="The time the *LaukCivilCertificatedRate* was created (as a ISO-8601 timestamp)",
    )
    eligible_for_sqm: Optional[bool] = Field(
        None, description="SQM eligibility (Legal Aid England and Wales)"
    )
    etag: Optional[str] = Field(
        None, description="ETag for the *LaukCivilCertificatedRate*"
    )
    exceptional: Optional[Decimal] = Field(
        None, description="Fee applied for high activity count"
    )
    exceptional_warning: Optional[str] = Field(
        None, description="Warning for exceptional status"
    )
    fee: Optional[Decimal] = Field(None, description="Fee amount")
    fee_scheme: Optional[str] = Field(None, description="Fee scheme")
    first_conducting_solicitor: Optional[bool] = Field(
        None, description="First conducting solicitor indicator"
    )
    id: Optional[int] = Field(
        None, description="Unique identifier for the *LaukCivilCertificatedRate*"
    )
    key: Optional[str] = Field(None, description="Unique key")
    number_of_clients: Optional[str] = Field(None, description="Number of clients")
    party: Optional[str] = Field(None, description="Associated party")
    post_transfer_clients_represented: Optional[str] = Field(
        None, description="Post-transfer clients represented"
    )
    rate_type: Optional[str] = Field(None, description="Rate type")
    region: Optional[str] = Field(None, description="Region")
    session_type: Optional[str] = Field(None, description="Session type")
    updated_at: Optional[str] = Field(
        None,
        description="The time the *LaukCivilCertificatedRate* was last updated (as a ISO-8601 timestamp)",
    )
    user_type: Optional[str] = Field(None, description="User type")
