# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from openhermes import OpenHermes, AsyncOpenHermes
from tests.utils import assert_matches_type
from openhermes.types.api import ResponseData

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestLogout:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_get(self, client: OpenHermes) -> None:
        logout = client.api.auth.logout.get()
        assert_matches_type(ResponseData, logout, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get(self, client: OpenHermes) -> None:
        response = client.api.auth.logout.with_raw_response.get()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        logout = response.parse()
        assert_matches_type(ResponseData, logout, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get(self, client: OpenHermes) -> None:
        with client.api.auth.logout.with_streaming_response.get() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            logout = response.parse()
            assert_matches_type(ResponseData, logout, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_post(self, client: OpenHermes) -> None:
        logout = client.api.auth.logout.post(
            token="token",
        )
        assert_matches_type(ResponseData, logout, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_post(self, client: OpenHermes) -> None:
        response = client.api.auth.logout.with_raw_response.post(
            token="token",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        logout = response.parse()
        assert_matches_type(ResponseData, logout, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_post(self, client: OpenHermes) -> None:
        with client.api.auth.logout.with_streaming_response.post(
            token="token",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            logout = response.parse()
            assert_matches_type(ResponseData, logout, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncLogout:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip()
    @parametrize
    async def test_method_get(self, async_client: AsyncOpenHermes) -> None:
        logout = await async_client.api.auth.logout.get()
        assert_matches_type(ResponseData, logout, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncOpenHermes) -> None:
        response = await async_client.api.auth.logout.with_raw_response.get()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        logout = await response.parse()
        assert_matches_type(ResponseData, logout, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncOpenHermes) -> None:
        async with async_client.api.auth.logout.with_streaming_response.get() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            logout = await response.parse()
            assert_matches_type(ResponseData, logout, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_post(self, async_client: AsyncOpenHermes) -> None:
        logout = await async_client.api.auth.logout.post(
            token="token",
        )
        assert_matches_type(ResponseData, logout, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_post(self, async_client: AsyncOpenHermes) -> None:
        response = await async_client.api.auth.logout.with_raw_response.post(
            token="token",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        logout = await response.parse()
        assert_matches_type(ResponseData, logout, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_post(self, async_client: AsyncOpenHermes) -> None:
        async with async_client.api.auth.logout.with_streaming_response.post(
            token="token",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            logout = await response.parse()
            assert_matches_type(ResponseData, logout, path=["response"])

        assert cast(Any, response.is_closed) is True
