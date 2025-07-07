# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from openhermes import OpenHermes, AsyncOpenHermes
from tests.utils import assert_matches_type
from openhermes.types.api import ResponseData
from openhermes.types.api.blacklist import UserGetResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestUser:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_change(self, client: OpenHermes) -> None:
        user = client.api.blacklist.user.change(
            is_ban=0,
            user_sub="user_sub",
        )
        assert_matches_type(ResponseData, user, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_change(self, client: OpenHermes) -> None:
        response = client.api.blacklist.user.with_raw_response.change(
            is_ban=0,
            user_sub="user_sub",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(ResponseData, user, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_change(self, client: OpenHermes) -> None:
        with client.api.blacklist.user.with_streaming_response.change(
            is_ban=0,
            user_sub="user_sub",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(ResponseData, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_get(self, client: OpenHermes) -> None:
        user = client.api.blacklist.user.get()
        assert_matches_type(UserGetResponse, user, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_get_with_all_params(self, client: OpenHermes) -> None:
        user = client.api.blacklist.user.get(
            page=0,
        )
        assert_matches_type(UserGetResponse, user, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get(self, client: OpenHermes) -> None:
        response = client.api.blacklist.user.with_raw_response.get()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(UserGetResponse, user, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get(self, client: OpenHermes) -> None:
        with client.api.blacklist.user.with_streaming_response.get() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(UserGetResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncUser:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip()
    @parametrize
    async def test_method_change(self, async_client: AsyncOpenHermes) -> None:
        user = await async_client.api.blacklist.user.change(
            is_ban=0,
            user_sub="user_sub",
        )
        assert_matches_type(ResponseData, user, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_change(self, async_client: AsyncOpenHermes) -> None:
        response = await async_client.api.blacklist.user.with_raw_response.change(
            is_ban=0,
            user_sub="user_sub",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(ResponseData, user, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_change(self, async_client: AsyncOpenHermes) -> None:
        async with async_client.api.blacklist.user.with_streaming_response.change(
            is_ban=0,
            user_sub="user_sub",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(ResponseData, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_get(self, async_client: AsyncOpenHermes) -> None:
        user = await async_client.api.blacklist.user.get()
        assert_matches_type(UserGetResponse, user, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncOpenHermes) -> None:
        user = await async_client.api.blacklist.user.get(
            page=0,
        )
        assert_matches_type(UserGetResponse, user, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncOpenHermes) -> None:
        response = await async_client.api.blacklist.user.with_raw_response.get()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(UserGetResponse, user, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncOpenHermes) -> None:
        async with async_client.api.blacklist.user.with_streaming_response.get() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(UserGetResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True
