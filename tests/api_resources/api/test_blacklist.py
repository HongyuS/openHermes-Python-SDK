# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from openhermes import OpenHermes, AsyncOpenHermes
from tests.utils import assert_matches_type
from openhermes.types.api import ResponseData

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBlacklist:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_report_abuse(self, client: OpenHermes) -> None:
        blacklist = client.api.blacklist.report_abuse(
            reason="reason",
            reason_type="reason_type",
            record_id="record_id",
        )
        assert_matches_type(ResponseData, blacklist, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_report_abuse(self, client: OpenHermes) -> None:
        response = client.api.blacklist.with_raw_response.report_abuse(
            reason="reason",
            reason_type="reason_type",
            record_id="record_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        blacklist = response.parse()
        assert_matches_type(ResponseData, blacklist, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_report_abuse(self, client: OpenHermes) -> None:
        with client.api.blacklist.with_streaming_response.report_abuse(
            reason="reason",
            reason_type="reason_type",
            record_id="record_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            blacklist = response.parse()
            assert_matches_type(ResponseData, blacklist, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncBlacklist:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip()
    @parametrize
    async def test_method_report_abuse(self, async_client: AsyncOpenHermes) -> None:
        blacklist = await async_client.api.blacklist.report_abuse(
            reason="reason",
            reason_type="reason_type",
            record_id="record_id",
        )
        assert_matches_type(ResponseData, blacklist, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_report_abuse(self, async_client: AsyncOpenHermes) -> None:
        response = await async_client.api.blacklist.with_raw_response.report_abuse(
            reason="reason",
            reason_type="reason_type",
            record_id="record_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        blacklist = await response.parse()
        assert_matches_type(ResponseData, blacklist, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_report_abuse(self, async_client: AsyncOpenHermes) -> None:
        async with async_client.api.blacklist.with_streaming_response.report_abuse(
            reason="reason",
            reason_type="reason_type",
            record_id="record_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            blacklist = await response.parse()
            assert_matches_type(ResponseData, blacklist, path=["response"])

        assert cast(Any, response.is_closed) is True
