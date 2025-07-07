# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["KnowledgeUpdateParams"]


class KnowledgeUpdateParams(TypedDict, total=False):
    conversation_id: Required[Annotated[str, PropertyInfo(alias="conversationId")]]

    kb_ids: Annotated[List[str], PropertyInfo(alias="kbIds")]
    """知识库 ID 列表"""
