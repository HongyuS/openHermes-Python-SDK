# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["ConversationUpdateParams"]


class ConversationUpdateParams(TypedDict, total=False):
    conversation_id: Required[Annotated[str, PropertyInfo(alias="conversationId")]]

    title: Required[str]
