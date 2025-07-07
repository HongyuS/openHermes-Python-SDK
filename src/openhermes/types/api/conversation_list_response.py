# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from .conversation_list_item import ConversationListItem

__all__ = ["ConversationListResponse", "Result"]


class Result(BaseModel):
    conversations: List[ConversationListItem]


class ConversationListResponse(BaseModel):
    code: int

    message: str

    result: Result
    """GET /api/conversation Result 数据结构"""
