# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel

__all__ = ["KeyManageResponse", "Result"]


class Result(BaseModel):
    api_key: str


class KeyManageResponse(BaseModel):
    code: int

    message: str

    result: Result
    """POST /api/auth/key Result 数据结构"""
