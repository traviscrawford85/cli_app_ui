# generated by datamodel-codegen:
#   filename:  openapi_sdk.yaml

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Field


class CustomFieldMatterSelectionBase(BaseModel):
    display_number: Optional[str] = Field(
        None,
        description="The reference and label of the *CustomFieldMatterSelection*. Depending on the account's manual_matter_numbering setting, this is either read only (generated) or customizable.",
    )
    id: Optional[int] = Field(
        None, description="Unique identifier for the *CustomFieldMatterSelection*"
    )
