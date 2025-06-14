# generated by datamodel-codegen:
#   filename:  openapi_sdk.yaml

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Field


class ClientPortalBase(BaseModel):
    created_at: Optional[str] = Field(
        None,
        description="The time the *ClientPortal* was created (as a ISO-8601 timestamp)",
    )
    etag: Optional[str] = Field(None, description="ETag for the *ClientPortal*")
    id: Optional[int] = Field(
        None, description="Unique identifier for the *ClientPortal*"
    )
    unread_count: Optional[int] = Field(
        None, description="The number of unread count messages for the current user."
    )
    unread_notifiable_count: Optional[int] = Field(
        None,
        description="The number of unread messages for the current user once their notification settings have been applied.",
    )
    updated_at: Optional[str] = Field(
        None,
        description="The time the *ClientPortal* was last updated (as a ISO-8601 timestamp)",
    )
