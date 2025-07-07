# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["LlmListResponse", "Result"]


class Result(BaseModel):
    llm_id: str = FieldInfo(alias="llmId")
    """LLM ID"""

    api_model_name: str = FieldInfo(alias="modelName")
    """模型名称"""

    icon: Optional[str] = None
    """LLM 图标"""

    is_editable: Optional[bool] = FieldInfo(alias="isEditable", default=None)
    """是否可编辑"""

    max_tokens: Optional[int] = FieldInfo(alias="maxTokens", default=None)
    """最大 token 数"""

    openai_api_key: Optional[str] = FieldInfo(alias="openaiApiKey", default=None)
    """OpenAI API Key"""

    openai_base_url: Optional[str] = FieldInfo(alias="openaiBaseUrl", default=None)
    """OpenAI API Base URL"""


class LlmListResponse(BaseModel):
    code: int

    message: str

    result: Optional[List[Result]] = None
