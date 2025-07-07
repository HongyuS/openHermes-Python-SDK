# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["AuthRedirectResponse", "Result"]


class Result(BaseModel):
    url: str


class AuthRedirectResponse(BaseModel):
    code: int

    message: str

    result: Result
    """GET /api/auth/redirect Result 数据结构"""
