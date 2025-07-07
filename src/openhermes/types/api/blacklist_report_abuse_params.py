# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["BlacklistReportAbuseParams"]


class BlacklistReportAbuseParams(TypedDict, total=False):
    reason: Required[str]

    reason_type: Required[str]

    record_id: Required[str]
