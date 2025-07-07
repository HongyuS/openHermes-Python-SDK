# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from openhermes import OpenHermes, AsyncOpenHermes
from tests.utils import assert_matches_type
from openhermes.types.api.auth import KeyCheckResponse, KeyManageResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestKey:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_check(self, client: OpenHermes) -> None:
        key = client.api.auth.key.check()
        assert_matches_type(KeyCheckResponse, key, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_check(self, client: OpenHermes) -> None:
        response = client.api.auth.key.with_raw_response.check()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        key = response.parse()
        assert_matches_type(KeyCheckResponse, key, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_check(self, client: OpenHermes) -> None:
        with client.api.auth.key.with_streaming_response.check() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            key = response.parse()
            assert_matches_type(KeyCheckResponse, key, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_manage(self, client: OpenHermes) -> None:
        key = client.api.auth.key.manage(
            action="action",
        )
        assert_matches_type(KeyManageResponse, key, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_manage(self, client: OpenHermes) -> None:
        response = client.api.auth.key.with_raw_response.manage(
            action="action",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        key = response.parse()
        assert_matches_type(KeyManageResponse, key, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_manage(self, client: OpenHermes) -> None:
        with client.api.auth.key.with_streaming_response.manage(
            action="action",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            key = response.parse()
            assert_matches_type(KeyManageResponse, key, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncKey:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip()
    @parametrize
    async def test_method_check(self, async_client: AsyncOpenHermes) -> None:
        key = await async_client.api.auth.key.check()
        assert_matches_type(KeyCheckResponse, key, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_check(self, async_client: AsyncOpenHermes) -> None:
        response = await async_client.api.auth.key.with_raw_response.check()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        key = await response.parse()
        assert_matches_type(KeyCheckResponse, key, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_check(self, async_client: AsyncOpenHermes) -> None:
        async with async_client.api.auth.key.with_streaming_response.check() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            key = await response.parse()
            assert_matches_type(KeyCheckResponse, key, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_manage(self, async_client: AsyncOpenHermes) -> None:
        key = await async_client.api.auth.key.manage(
            action="action",
        )
        assert_matches_type(KeyManageResponse, key, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_manage(self, async_client: AsyncOpenHermes) -> None:
        response = await async_client.api.auth.key.with_raw_response.manage(
            action="action",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        key = await response.parse()
        assert_matches_type(KeyManageResponse, key, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_manage(self, async_client: AsyncOpenHermes) -> None:
        async with async_client.api.auth.key.with_streaming_response.manage(
            action="action",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            key = await response.parse()
            assert_matches_type(KeyManageResponse, key, path=["response"])

        assert cast(Any, response.is_closed) is True
