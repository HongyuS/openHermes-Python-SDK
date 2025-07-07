# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["UserChangeParams"]


class UserChangeParams(TypedDict, total=False):
    is_ban: Required[int]

    user_sub: Required[str]
