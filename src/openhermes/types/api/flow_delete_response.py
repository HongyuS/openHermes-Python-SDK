# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["FlowDeleteResponse", "Result"]


class Result(BaseModel):
    flow_id: Optional[str] = FieldInfo(alias="flowId", default=None)


class FlowDeleteResponse(BaseModel):
    code: int

    message: str

    result: Result
    """DELETE /api/flow/ result"""
