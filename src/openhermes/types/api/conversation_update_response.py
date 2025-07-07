# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel
from .conversation_list_item import ConversationListItem

__all__ = ["ConversationUpdateResponse"]


class ConversationUpdateResponse(BaseModel):
    code: int

    message: str

    result: ConversationListItem
    """GET /api/conversation Result 数据结构"""
