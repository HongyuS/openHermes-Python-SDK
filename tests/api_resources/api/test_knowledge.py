# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from openhermes import Openhermes, AsyncOpenhermes
from tests.utils import assert_matches_type
from openhermes.types.api import ResponseData, KnowledgeListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestKnowledge:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update(self, client: Openhermes) -> None:
        knowledge = client.api.knowledge.update(
            conversation_id="conversationId",
        )
        assert_matches_type(ResponseData, knowledge, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update_with_all_params(self, client: Openhermes) -> None:
        knowledge = client.api.knowledge.update(
            conversation_id="conversationId",
            kb_ids=["string"],
        )
        assert_matches_type(ResponseData, knowledge, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update(self, client: Openhermes) -> None:
        response = client.api.knowledge.with_raw_response.update(
            conversation_id="conversationId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        knowledge = response.parse()
        assert_matches_type(ResponseData, knowledge, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update(self, client: Openhermes) -> None:
        with client.api.knowledge.with_streaming_response.update(
            conversation_id="conversationId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            knowledge = response.parse()
            assert_matches_type(ResponseData, knowledge, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: Openhermes) -> None:
        knowledge = client.api.knowledge.list(
            conversation_id="conversationId",
        )
        assert_matches_type(KnowledgeListResponse, knowledge, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list_with_all_params(self, client: Openhermes) -> None:
        knowledge = client.api.knowledge.list(
            conversation_id="conversationId",
            kb_id="kbId",
            kb_name="kbName",
        )
        assert_matches_type(KnowledgeListResponse, knowledge, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: Openhermes) -> None:
        response = client.api.knowledge.with_raw_response.list(
            conversation_id="conversationId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        knowledge = response.parse()
        assert_matches_type(KnowledgeListResponse, knowledge, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: Openhermes) -> None:
        with client.api.knowledge.with_streaming_response.list(
            conversation_id="conversationId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            knowledge = response.parse()
            assert_matches_type(KnowledgeListResponse, knowledge, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncKnowledge:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip()
    @parametrize
    async def test_method_update(self, async_client: AsyncOpenhermes) -> None:
        knowledge = await async_client.api.knowledge.update(
            conversation_id="conversationId",
        )
        assert_matches_type(ResponseData, knowledge, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncOpenhermes) -> None:
        knowledge = await async_client.api.knowledge.update(
            conversation_id="conversationId",
            kb_ids=["string"],
        )
        assert_matches_type(ResponseData, knowledge, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncOpenhermes) -> None:
        response = await async_client.api.knowledge.with_raw_response.update(
            conversation_id="conversationId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        knowledge = await response.parse()
        assert_matches_type(ResponseData, knowledge, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncOpenhermes) -> None:
        async with async_client.api.knowledge.with_streaming_response.update(
            conversation_id="conversationId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            knowledge = await response.parse()
            assert_matches_type(ResponseData, knowledge, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncOpenhermes) -> None:
        knowledge = await async_client.api.knowledge.list(
            conversation_id="conversationId",
        )
        assert_matches_type(KnowledgeListResponse, knowledge, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncOpenhermes) -> None:
        knowledge = await async_client.api.knowledge.list(
            conversation_id="conversationId",
            kb_id="kbId",
            kb_name="kbName",
        )
        assert_matches_type(KnowledgeListResponse, knowledge, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncOpenhermes) -> None:
        response = await async_client.api.knowledge.with_raw_response.list(
            conversation_id="conversationId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        knowledge = await response.parse()
        assert_matches_type(KnowledgeListResponse, knowledge, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncOpenhermes) -> None:
        async with async_client.api.knowledge.with_streaming_response.list(
            conversation_id="conversationId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            knowledge = await response.parse()
            assert_matches_type(KnowledgeListResponse, knowledge, path=["response"])

        assert cast(Any, response.is_closed) is True
