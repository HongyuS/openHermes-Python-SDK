# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["ResponseData"]


class ResponseData(BaseModel):
    code: int

    message: str

    result: object
