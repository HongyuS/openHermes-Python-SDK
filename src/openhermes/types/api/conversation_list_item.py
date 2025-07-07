# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ConversationListItem", "KBList", "Llm"]


class KBList(BaseModel):
    kb_id: str = FieldInfo(alias="kbId")

    kb_name: str = FieldInfo(alias="kbName")


class Llm(BaseModel):
    icon: Optional[str] = None

    llm_id: Optional[str] = FieldInfo(alias="llmId", default=None)

    api_model_name: Optional[str] = FieldInfo(alias="modelName", default=None)


class ConversationListItem(BaseModel):
    app_id: str = FieldInfo(alias="appId")

    conversation_id: str = FieldInfo(alias="conversationId")

    created_time: str = FieldInfo(alias="createdTime")

    debug: bool

    doc_count: int = FieldInfo(alias="docCount")

    title: str

    kb_list: Optional[List[KBList]] = FieldInfo(alias="kbList", default=None)

    llm: Optional[Llm] = None
    """GET /api/conversation Result 数据结构"""
