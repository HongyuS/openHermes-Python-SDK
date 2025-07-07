# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["LlmListProvidersResponse", "Result"]


class Result(BaseModel):
    description: str
    """LLM 提供商描述"""

    icon: str
    """LLM 提供商图标"""

    provider: str
    """LLM 提供商"""

    url: Optional[str] = None
    """LLM 提供商 URL"""


class LlmListProvidersResponse(BaseModel):
    code: int

    message: str

    result: Optional[List[Result]] = None
