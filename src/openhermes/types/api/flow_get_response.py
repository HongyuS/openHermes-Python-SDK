# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel
from .flow_item_output import FlowItemOutput

__all__ = ["FlowGetResponse", "Result"]


class Result(BaseModel):
    flow: Optional[FlowItemOutput] = None
    """请求/响应中的流变量类"""


class FlowGetResponse(BaseModel):
    code: int

    message: str

    result: Result
    """GET /api/flow result"""
