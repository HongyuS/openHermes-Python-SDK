# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from openhermes import OpenHermes, AsyncOpenHermes
from tests.utils import assert_matches_type
from openhermes.types import APIGetRecordResponse
from openhermes.types.api import ResponseData

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAPI:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_add_comment(self, client: OpenHermes) -> None:
        api = client.api.add_comment(
            comment="liked",
            group_id="group_id",
            record_id="record_id",
        )
        assert_matches_type(ResponseData, api, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_add_comment_with_all_params(self, client: OpenHermes) -> None:
        api = client.api.add_comment(
            comment="liked",
            group_id="group_id",
            record_id="record_id",
            dislike_reason="dislike_reason",
            reason_description="reason_description",
            reason_link="reason_link",
        )
        assert_matches_type(ResponseData, api, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_add_comment(self, client: OpenHermes) -> None:
        response = client.api.with_raw_response.add_comment(
            comment="liked",
            group_id="group_id",
            record_id="record_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        api = response.parse()
        assert_matches_type(ResponseData, api, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_add_comment(self, client: OpenHermes) -> None:
        with client.api.with_streaming_response.add_comment(
            comment="liked",
            group_id="group_id",
            record_id="record_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            api = response.parse()
            assert_matches_type(ResponseData, api, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_chat(self, client: OpenHermes) -> None:
        api = client.api.chat(
            question="question",
        )
        assert_matches_type(object, api, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_chat_with_all_params(self, client: OpenHermes) -> None:
        api = client.api.chat(
            question="question",
            app={
                "app_id": "appId",
                "flow_id": "flowId",
                "params": {},
            },
            conversation_id="conversationId",
            debug=True,
            files=["string"],
            group_id="groupId",
            language="language",
        )
        assert_matches_type(object, api, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_chat(self, client: OpenHermes) -> None:
        response = client.api.with_raw_response.chat(
            question="question",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        api = response.parse()
        assert_matches_type(object, api, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_chat(self, client: OpenHermes) -> None:
        with client.api.with_streaming_response.chat(
            question="question",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            api = response.parse()
            assert_matches_type(object, api, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_get_record(self, client: OpenHermes) -> None:
        api = client.api.get_record(
            "conversation_id",
        )
        assert_matches_type(APIGetRecordResponse, api, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get_record(self, client: OpenHermes) -> None:
        response = client.api.with_raw_response.get_record(
            "conversation_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        api = response.parse()
        assert_matches_type(APIGetRecordResponse, api, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get_record(self, client: OpenHermes) -> None:
        with client.api.with_streaming_response.get_record(
            "conversation_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            api = response.parse()
            assert_matches_type(APIGetRecordResponse, api, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_get_record(self, client: OpenHermes) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `conversation_id` but received ''"):
            client.api.with_raw_response.get_record(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_list_users(self, client: OpenHermes) -> None:
        api = client.api.list_users()
        assert_matches_type(object, api, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list_users(self, client: OpenHermes) -> None:
        response = client.api.with_raw_response.list_users()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        api = response.parse()
        assert_matches_type(object, api, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list_users(self, client: OpenHermes) -> None:
        with client.api.with_streaming_response.list_users() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            api = response.parse()
            assert_matches_type(object, api, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_stop_generation(self, client: OpenHermes) -> None:
        api = client.api.stop_generation()
        assert_matches_type(ResponseData, api, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_stop_generation(self, client: OpenHermes) -> None:
        response = client.api.with_raw_response.stop_generation()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        api = response.parse()
        assert_matches_type(ResponseData, api, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_stop_generation(self, client: OpenHermes) -> None:
        with client.api.with_streaming_response.stop_generation() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            api = response.parse()
            assert_matches_type(ResponseData, api, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAPI:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip()
    @parametrize
    async def test_method_add_comment(self, async_client: AsyncOpenHermes) -> None:
        api = await async_client.api.add_comment(
            comment="liked",
            group_id="group_id",
            record_id="record_id",
        )
        assert_matches_type(ResponseData, api, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_add_comment_with_all_params(self, async_client: AsyncOpenHermes) -> None:
        api = await async_client.api.add_comment(
            comment="liked",
            group_id="group_id",
            record_id="record_id",
            dislike_reason="dislike_reason",
            reason_description="reason_description",
            reason_link="reason_link",
        )
        assert_matches_type(ResponseData, api, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_add_comment(self, async_client: AsyncOpenHermes) -> None:
        response = await async_client.api.with_raw_response.add_comment(
            comment="liked",
            group_id="group_id",
            record_id="record_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        api = await response.parse()
        assert_matches_type(ResponseData, api, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_add_comment(self, async_client: AsyncOpenHermes) -> None:
        async with async_client.api.with_streaming_response.add_comment(
            comment="liked",
            group_id="group_id",
            record_id="record_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            api = await response.parse()
            assert_matches_type(ResponseData, api, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_chat(self, async_client: AsyncOpenHermes) -> None:
        api = await async_client.api.chat(
            question="question",
        )
        assert_matches_type(object, api, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_chat_with_all_params(self, async_client: AsyncOpenHermes) -> None:
        api = await async_client.api.chat(
            question="question",
            app={
                "app_id": "appId",
                "flow_id": "flowId",
                "params": {},
            },
            conversation_id="conversationId",
            debug=True,
            files=["string"],
            group_id="groupId",
            language="language",
        )
        assert_matches_type(object, api, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_chat(self, async_client: AsyncOpenHermes) -> None:
        response = await async_client.api.with_raw_response.chat(
            question="question",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        api = await response.parse()
        assert_matches_type(object, api, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_chat(self, async_client: AsyncOpenHermes) -> None:
        async with async_client.api.with_streaming_response.chat(
            question="question",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            api = await response.parse()
            assert_matches_type(object, api, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_record(self, async_client: AsyncOpenHermes) -> None:
        api = await async_client.api.get_record(
            "conversation_id",
        )
        assert_matches_type(APIGetRecordResponse, api, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get_record(self, async_client: AsyncOpenHermes) -> None:
        response = await async_client.api.with_raw_response.get_record(
            "conversation_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        api = await response.parse()
        assert_matches_type(APIGetRecordResponse, api, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get_record(self, async_client: AsyncOpenHermes) -> None:
        async with async_client.api.with_streaming_response.get_record(
            "conversation_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            api = await response.parse()
            assert_matches_type(APIGetRecordResponse, api, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_get_record(self, async_client: AsyncOpenHermes) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `conversation_id` but received ''"):
            await async_client.api.with_raw_response.get_record(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_users(self, async_client: AsyncOpenHermes) -> None:
        api = await async_client.api.list_users()
        assert_matches_type(object, api, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list_users(self, async_client: AsyncOpenHermes) -> None:
        response = await async_client.api.with_raw_response.list_users()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        api = await response.parse()
        assert_matches_type(object, api, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list_users(self, async_client: AsyncOpenHermes) -> None:
        async with async_client.api.with_streaming_response.list_users() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            api = await response.parse()
            assert_matches_type(object, api, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_stop_generation(self, async_client: AsyncOpenHermes) -> None:
        api = await async_client.api.stop_generation()
        assert_matches_type(ResponseData, api, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_stop_generation(self, async_client: AsyncOpenHermes) -> None:
        response = await async_client.api.with_raw_response.stop_generation()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        api = await response.parse()
        assert_matches_type(ResponseData, api, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_stop_generation(self, async_client: AsyncOpenHermes) -> None:
        async with async_client.api.with_streaming_response.stop_generation() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            api = await response.parse()
            assert_matches_type(ResponseData, api, path=["response"])

        assert cast(Any, response.is_closed) is True
