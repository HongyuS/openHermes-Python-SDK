# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["BaseAppOperationRsp", "Result"]


class Result(BaseModel):
    app_id: str = FieldInfo(alias="appId")
    """应用 ID"""


class BaseAppOperationRsp(BaseModel):
    code: int

    message: str

    result: Result
    """基础应用操作 Result 数据结构"""
