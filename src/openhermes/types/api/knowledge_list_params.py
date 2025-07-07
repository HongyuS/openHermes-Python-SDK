# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["KnowledgeListParams"]


class KnowledgeListParams(TypedDict, total=False):
    conversation_id: Required[Annotated[str, PropertyInfo(alias="conversationId")]]

    kb_id: Annotated[str, PropertyInfo(alias="kbId")]

    kb_name: Annotated[str, PropertyInfo(alias="kbName")]
