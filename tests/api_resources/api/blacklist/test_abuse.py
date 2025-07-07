# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from openhermes import Openhermes, AsyncOpenhermes
from tests.utils import assert_matches_type
from openhermes.types.api import ResponseData
from openhermes.types.api.blacklist import GetBlacklistQuestionRsp

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAbuse:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_change(self, client: Openhermes) -> None:
        abuse = client.api.blacklist.abuse.change(
            id="id",
            is_deletion=0,
        )
        assert_matches_type(ResponseData, abuse, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_change(self, client: Openhermes) -> None:
        response = client.api.blacklist.abuse.with_raw_response.change(
            id="id",
            is_deletion=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        abuse = response.parse()
        assert_matches_type(ResponseData, abuse, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_change(self, client: Openhermes) -> None:
        with client.api.blacklist.abuse.with_streaming_response.change(
            id="id",
            is_deletion=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            abuse = response.parse()
            assert_matches_type(ResponseData, abuse, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_get(self, client: Openhermes) -> None:
        abuse = client.api.blacklist.abuse.get()
        assert_matches_type(GetBlacklistQuestionRsp, abuse, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_get_with_all_params(self, client: Openhermes) -> None:
        abuse = client.api.blacklist.abuse.get(
            page=0,
        )
        assert_matches_type(GetBlacklistQuestionRsp, abuse, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get(self, client: Openhermes) -> None:
        response = client.api.blacklist.abuse.with_raw_response.get()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        abuse = response.parse()
        assert_matches_type(GetBlacklistQuestionRsp, abuse, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get(self, client: Openhermes) -> None:
        with client.api.blacklist.abuse.with_streaming_response.get() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            abuse = response.parse()
            assert_matches_type(GetBlacklistQuestionRsp, abuse, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAbuse:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip()
    @parametrize
    async def test_method_change(self, async_client: AsyncOpenhermes) -> None:
        abuse = await async_client.api.blacklist.abuse.change(
            id="id",
            is_deletion=0,
        )
        assert_matches_type(ResponseData, abuse, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_change(self, async_client: AsyncOpenhermes) -> None:
        response = await async_client.api.blacklist.abuse.with_raw_response.change(
            id="id",
            is_deletion=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        abuse = await response.parse()
        assert_matches_type(ResponseData, abuse, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_change(self, async_client: AsyncOpenhermes) -> None:
        async with async_client.api.blacklist.abuse.with_streaming_response.change(
            id="id",
            is_deletion=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            abuse = await response.parse()
            assert_matches_type(ResponseData, abuse, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_get(self, async_client: AsyncOpenhermes) -> None:
        abuse = await async_client.api.blacklist.abuse.get()
        assert_matches_type(GetBlacklistQuestionRsp, abuse, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncOpenhermes) -> None:
        abuse = await async_client.api.blacklist.abuse.get(
            page=0,
        )
        assert_matches_type(GetBlacklistQuestionRsp, abuse, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncOpenhermes) -> None:
        response = await async_client.api.blacklist.abuse.with_raw_response.get()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        abuse = await response.parse()
        assert_matches_type(GetBlacklistQuestionRsp, abuse, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncOpenhermes) -> None:
        async with async_client.api.blacklist.abuse.with_streaming_response.get() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            abuse = await response.parse()
            assert_matches_type(GetBlacklistQuestionRsp, abuse, path=["response"])

        assert cast(Any, response.is_closed) is True
