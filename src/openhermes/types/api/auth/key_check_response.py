# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel

__all__ = ["KeyCheckResponse", "Result"]


class Result(BaseModel):
    api_key_exists: bool


class KeyCheckResponse(BaseModel):
    code: int

    message: str

    result: Result
    """GET /api/auth/key Result 数据结构"""
