# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel
from .flow_item_output import FlowItemOutput

__all__ = ["FlowUpdateResponse", "Result"]


class Result(BaseModel):
    flow: Optional[FlowItemOutput] = None
    """请求/响应中的流变量类"""


class FlowUpdateResponse(BaseModel):
    code: int

    message: str

    result: Result
    """PUT /api/flow result"""
