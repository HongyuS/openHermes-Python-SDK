# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["AuthUserRsp", "Result"]


class Result(BaseModel):
    is_admin: bool

    revision: bool

    user_sub: str


class AuthUserRsp(BaseModel):
    code: int

    message: str

    result: Result
    """GET /api/auth/user Result 数据结构"""
