# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import TypeAlias

from .response_data import ResponseData
from .base_app_operation_rsp import BaseAppOperationRsp

__all__ = ["AppDeleteResponse"]

AppDeleteResponse: TypeAlias = Union[BaseAppOperationRsp, ResponseData]
