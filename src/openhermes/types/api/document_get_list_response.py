# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["DocumentGetListResponse", "Result", "ResultDocument"]


class ResultDocument(BaseModel):
    name: str

    size: float

    status: Literal["used", "unused", "processing", "failed"]
    """文档状态"""

    type: str

    api_id: Optional[str] = FieldInfo(alias="_id", default=None)

    conversation_id: None = None

    created_at: Optional[float] = None

    user_sub: None = None


class Result(BaseModel):
    documents: Optional[List[ResultDocument]] = None


class DocumentGetListResponse(BaseModel):
    code: int

    message: str

    result: Result
    """GET /api/document/{conversation_id} Result 数据结构"""
