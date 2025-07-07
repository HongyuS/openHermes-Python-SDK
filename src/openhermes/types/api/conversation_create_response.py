# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ConversationCreateResponse", "Result"]


class Result(BaseModel):
    conversation_id: str = FieldInfo(alias="conversationId")


class ConversationCreateResponse(BaseModel):
    code: int

    message: str

    result: Result
    """POST /api/conversation Result 数据结构"""
