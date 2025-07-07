# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import TypeAlias

from .response_data import ResponseData
from .base_app_operation import BaseAppOperation

__all__ = ["AppCreateOrUpdateResponse"]

AppCreateOrUpdateResponse: TypeAlias = Union[BaseAppOperation, ResponseData]
