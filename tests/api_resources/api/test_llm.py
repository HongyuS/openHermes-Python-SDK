# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from openhermes import OpenHermes, AsyncOpenHermes
from tests.utils import assert_matches_type
from openhermes.types.api import (
    LlmListResponse,
    LlmListProvidersResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestLlm:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: OpenHermes) -> None:
        llm = client.api.llm.list()
        assert_matches_type(LlmListResponse, llm, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list_with_all_params(self, client: OpenHermes) -> None:
        llm = client.api.llm.list(
            llm_id="llmId",
        )
        assert_matches_type(LlmListResponse, llm, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: OpenHermes) -> None:
        response = client.api.llm.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        llm = response.parse()
        assert_matches_type(LlmListResponse, llm, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: OpenHermes) -> None:
        with client.api.llm.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            llm = response.parse()
            assert_matches_type(LlmListResponse, llm, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: OpenHermes) -> None:
        llm = client.api.llm.delete(
            llm_id="llmId",
        )
        assert_matches_type(object, llm, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: OpenHermes) -> None:
        response = client.api.llm.with_raw_response.delete(
            llm_id="llmId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        llm = response.parse()
        assert_matches_type(object, llm, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: OpenHermes) -> None:
        with client.api.llm.with_streaming_response.delete(
            llm_id="llmId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            llm = response.parse()
            assert_matches_type(object, llm, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_create_or_update(self, client: OpenHermes) -> None:
        llm = client.api.llm.create_or_update()
        assert_matches_type(object, llm, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_or_update_with_all_params(self, client: OpenHermes) -> None:
        llm = client.api.llm.create_or_update(
            llm_id="llmId",
            icon="icon",
            max_tokens=0,
            model_name="modelName",
            openai_api_key="openaiApiKey",
            openai_base_url="openaiBaseUrl",
        )
        assert_matches_type(object, llm, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create_or_update(self, client: OpenHermes) -> None:
        response = client.api.llm.with_raw_response.create_or_update()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        llm = response.parse()
        assert_matches_type(object, llm, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create_or_update(self, client: OpenHermes) -> None:
        with client.api.llm.with_streaming_response.create_or_update() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            llm = response.parse()
            assert_matches_type(object, llm, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_list_providers(self, client: OpenHermes) -> None:
        llm = client.api.llm.list_providers()
        assert_matches_type(LlmListProvidersResponse, llm, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list_providers(self, client: OpenHermes) -> None:
        response = client.api.llm.with_raw_response.list_providers()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        llm = response.parse()
        assert_matches_type(LlmListProvidersResponse, llm, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list_providers(self, client: OpenHermes) -> None:
        with client.api.llm.with_streaming_response.list_providers() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            llm = response.parse()
            assert_matches_type(LlmListProvidersResponse, llm, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_update_conv(self, client: OpenHermes) -> None:
        llm = client.api.llm.update_conv(
            conversation_id="conversationId",
        )
        assert_matches_type(object, llm, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update_conv_with_all_params(self, client: OpenHermes) -> None:
        llm = client.api.llm.update_conv(
            conversation_id="conversationId",
            llm_id="llmId",
        )
        assert_matches_type(object, llm, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update_conv(self, client: OpenHermes) -> None:
        response = client.api.llm.with_raw_response.update_conv(
            conversation_id="conversationId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        llm = response.parse()
        assert_matches_type(object, llm, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update_conv(self, client: OpenHermes) -> None:
        with client.api.llm.with_streaming_response.update_conv(
            conversation_id="conversationId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            llm = response.parse()
            assert_matches_type(object, llm, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncLlm:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncOpenHermes) -> None:
        llm = await async_client.api.llm.list()
        assert_matches_type(LlmListResponse, llm, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncOpenHermes) -> None:
        llm = await async_client.api.llm.list(
            llm_id="llmId",
        )
        assert_matches_type(LlmListResponse, llm, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncOpenHermes) -> None:
        response = await async_client.api.llm.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        llm = await response.parse()
        assert_matches_type(LlmListResponse, llm, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncOpenHermes) -> None:
        async with async_client.api.llm.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            llm = await response.parse()
            assert_matches_type(LlmListResponse, llm, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncOpenHermes) -> None:
        llm = await async_client.api.llm.delete(
            llm_id="llmId",
        )
        assert_matches_type(object, llm, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncOpenHermes) -> None:
        response = await async_client.api.llm.with_raw_response.delete(
            llm_id="llmId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        llm = await response.parse()
        assert_matches_type(object, llm, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncOpenHermes) -> None:
        async with async_client.api.llm.with_streaming_response.delete(
            llm_id="llmId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            llm = await response.parse()
            assert_matches_type(object, llm, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_or_update(self, async_client: AsyncOpenHermes) -> None:
        llm = await async_client.api.llm.create_or_update()
        assert_matches_type(object, llm, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_or_update_with_all_params(self, async_client: AsyncOpenHermes) -> None:
        llm = await async_client.api.llm.create_or_update(
            llm_id="llmId",
            icon="icon",
            max_tokens=0,
            model_name="modelName",
            openai_api_key="openaiApiKey",
            openai_base_url="openaiBaseUrl",
        )
        assert_matches_type(object, llm, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create_or_update(self, async_client: AsyncOpenHermes) -> None:
        response = await async_client.api.llm.with_raw_response.create_or_update()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        llm = await response.parse()
        assert_matches_type(object, llm, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create_or_update(self, async_client: AsyncOpenHermes) -> None:
        async with async_client.api.llm.with_streaming_response.create_or_update() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            llm = await response.parse()
            assert_matches_type(object, llm, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_providers(self, async_client: AsyncOpenHermes) -> None:
        llm = await async_client.api.llm.list_providers()
        assert_matches_type(LlmListProvidersResponse, llm, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list_providers(self, async_client: AsyncOpenHermes) -> None:
        response = await async_client.api.llm.with_raw_response.list_providers()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        llm = await response.parse()
        assert_matches_type(LlmListProvidersResponse, llm, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list_providers(self, async_client: AsyncOpenHermes) -> None:
        async with async_client.api.llm.with_streaming_response.list_providers() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            llm = await response.parse()
            assert_matches_type(LlmListProvidersResponse, llm, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_conv(self, async_client: AsyncOpenHermes) -> None:
        llm = await async_client.api.llm.update_conv(
            conversation_id="conversationId",
        )
        assert_matches_type(object, llm, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_conv_with_all_params(self, async_client: AsyncOpenHermes) -> None:
        llm = await async_client.api.llm.update_conv(
            conversation_id="conversationId",
            llm_id="llmId",
        )
        assert_matches_type(object, llm, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update_conv(self, async_client: AsyncOpenHermes) -> None:
        response = await async_client.api.llm.with_raw_response.update_conv(
            conversation_id="conversationId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        llm = await response.parse()
        assert_matches_type(object, llm, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update_conv(self, async_client: AsyncOpenHermes) -> None:
        async with async_client.api.llm.with_streaming_response.update_conv(
            conversation_id="conversationId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            llm = await response.parse()
            assert_matches_type(object, llm, path=["response"])

        assert cast(Any, response.is_closed) is True
