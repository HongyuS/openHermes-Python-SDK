# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["LlmCreateOrUpdateParams"]


class LlmCreateOrUpdateParams(TypedDict, total=False):
    llm_id: Annotated[Optional[str], PropertyInfo(alias="llmId")]
    """大模型 ID"""

    icon: str
    """图标"""

    max_tokens: Annotated[int, PropertyInfo(alias="maxTokens")]
    """最大 token 数"""

    model_name: Annotated[str, PropertyInfo(alias="modelName")]
    """模型名称"""

    openai_api_key: Annotated[str, PropertyInfo(alias="openaiApiKey")]
    """OpenAI API Key"""

    openai_base_url: Annotated[str, PropertyInfo(alias="openaiBaseUrl")]
    """OpenAI API Base URL"""
