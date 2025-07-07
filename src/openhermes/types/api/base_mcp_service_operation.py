# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["BaseMcpServiceOperation"]


class BaseMcpServiceOperation(BaseModel):
    service_id: str = FieldInfo(alias="serviceId")
    """服务 ID"""
