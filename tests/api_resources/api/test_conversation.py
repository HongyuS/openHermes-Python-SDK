# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from openhermes import Openhermes, AsyncOpenhermes
from tests.utils import assert_matches_type
from openhermes.types.api import (
    ResponseData,
    ConversationListResponse,
    ConversationCreateResponse,
    ConversationUpdateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestConversation:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create(self, client: Openhermes) -> None:
        conversation = client.api.conversation.create()
        assert_matches_type(ConversationCreateResponse, conversation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_with_all_params(self, client: Openhermes) -> None:
        conversation = client.api.conversation.create(
            app_id="appId",
            debug=True,
            kb_ids=["string"],
            llm_id="llm_id",
        )
        assert_matches_type(ConversationCreateResponse, conversation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create(self, client: Openhermes) -> None:
        response = client.api.conversation.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        conversation = response.parse()
        assert_matches_type(ConversationCreateResponse, conversation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create(self, client: Openhermes) -> None:
        with client.api.conversation.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            conversation = response.parse()
            assert_matches_type(ConversationCreateResponse, conversation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_update(self, client: Openhermes) -> None:
        conversation = client.api.conversation.update(
            conversation_id="conversationId",
            title="x",
        )
        assert_matches_type(ConversationUpdateResponse, conversation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update(self, client: Openhermes) -> None:
        response = client.api.conversation.with_raw_response.update(
            conversation_id="conversationId",
            title="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        conversation = response.parse()
        assert_matches_type(ConversationUpdateResponse, conversation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update(self, client: Openhermes) -> None:
        with client.api.conversation.with_streaming_response.update(
            conversation_id="conversationId",
            title="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            conversation = response.parse()
            assert_matches_type(ConversationUpdateResponse, conversation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: Openhermes) -> None:
        conversation = client.api.conversation.list()
        assert_matches_type(ConversationListResponse, conversation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: Openhermes) -> None:
        response = client.api.conversation.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        conversation = response.parse()
        assert_matches_type(ConversationListResponse, conversation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: Openhermes) -> None:
        with client.api.conversation.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            conversation = response.parse()
            assert_matches_type(ConversationListResponse, conversation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: Openhermes) -> None:
        conversation = client.api.conversation.delete(
            conversation_list=["string"],
        )
        assert_matches_type(ResponseData, conversation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: Openhermes) -> None:
        response = client.api.conversation.with_raw_response.delete(
            conversation_list=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        conversation = response.parse()
        assert_matches_type(ResponseData, conversation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: Openhermes) -> None:
        with client.api.conversation.with_streaming_response.delete(
            conversation_list=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            conversation = response.parse()
            assert_matches_type(ResponseData, conversation, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncConversation:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip()
    @parametrize
    async def test_method_create(self, async_client: AsyncOpenhermes) -> None:
        conversation = await async_client.api.conversation.create()
        assert_matches_type(ConversationCreateResponse, conversation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncOpenhermes) -> None:
        conversation = await async_client.api.conversation.create(
            app_id="appId",
            debug=True,
            kb_ids=["string"],
            llm_id="llm_id",
        )
        assert_matches_type(ConversationCreateResponse, conversation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncOpenhermes) -> None:
        response = await async_client.api.conversation.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        conversation = await response.parse()
        assert_matches_type(ConversationCreateResponse, conversation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncOpenhermes) -> None:
        async with async_client.api.conversation.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            conversation = await response.parse()
            assert_matches_type(ConversationCreateResponse, conversation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_update(self, async_client: AsyncOpenhermes) -> None:
        conversation = await async_client.api.conversation.update(
            conversation_id="conversationId",
            title="x",
        )
        assert_matches_type(ConversationUpdateResponse, conversation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncOpenhermes) -> None:
        response = await async_client.api.conversation.with_raw_response.update(
            conversation_id="conversationId",
            title="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        conversation = await response.parse()
        assert_matches_type(ConversationUpdateResponse, conversation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncOpenhermes) -> None:
        async with async_client.api.conversation.with_streaming_response.update(
            conversation_id="conversationId",
            title="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            conversation = await response.parse()
            assert_matches_type(ConversationUpdateResponse, conversation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncOpenhermes) -> None:
        conversation = await async_client.api.conversation.list()
        assert_matches_type(ConversationListResponse, conversation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncOpenhermes) -> None:
        response = await async_client.api.conversation.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        conversation = await response.parse()
        assert_matches_type(ConversationListResponse, conversation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncOpenhermes) -> None:
        async with async_client.api.conversation.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            conversation = await response.parse()
            assert_matches_type(ConversationListResponse, conversation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncOpenhermes) -> None:
        conversation = await async_client.api.conversation.delete(
            conversation_list=["string"],
        )
        assert_matches_type(ResponseData, conversation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncOpenhermes) -> None:
        response = await async_client.api.conversation.with_raw_response.delete(
            conversation_list=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        conversation = await response.parse()
        assert_matches_type(ResponseData, conversation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncOpenhermes) -> None:
        async with async_client.api.conversation.with_streaming_response.delete(
            conversation_list=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            conversation = await response.parse()
            assert_matches_type(ResponseData, conversation, path=["response"])

        assert cast(Any, response.is_closed) is True
