# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from openhermes import OpenHermes, AsyncOpenHermes
from tests.utils import assert_matches_type
from openhermes.types.api import ResponseData, DocumentGetListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDocument:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: OpenHermes) -> None:
        document = client.api.document.delete(
            "document_id",
        )
        assert_matches_type(ResponseData, document, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: OpenHermes) -> None:
        response = client.api.document.with_raw_response.delete(
            "document_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = response.parse()
        assert_matches_type(ResponseData, document, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: OpenHermes) -> None:
        with client.api.document.with_streaming_response.delete(
            "document_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document = response.parse()
            assert_matches_type(ResponseData, document, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_delete(self, client: OpenHermes) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `document_id` but received ''"):
            client.api.document.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_get_list(self, client: OpenHermes) -> None:
        document = client.api.document.get_list(
            conversation_id="",
        )
        assert_matches_type(DocumentGetListResponse, document, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_get_list_with_all_params(self, client: OpenHermes) -> None:
        document = client.api.document.get_list(
            conversation_id="",
            unused=True,
            used=True,
        )
        assert_matches_type(DocumentGetListResponse, document, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get_list(self, client: OpenHermes) -> None:
        response = client.api.document.with_raw_response.get_list(
            conversation_id="",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = response.parse()
        assert_matches_type(DocumentGetListResponse, document, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get_list(self, client: OpenHermes) -> None:
        with client.api.document.with_streaming_response.get_list(
            conversation_id="",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document = response.parse()
            assert_matches_type(DocumentGetListResponse, document, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_get_list(self, client: OpenHermes) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `conversation_id` but received ''"):
            client.api.document.with_raw_response.get_list(
                conversation_id="",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_upload(self, client: OpenHermes) -> None:
        document = client.api.document.upload(
            conversation_id="",
            documents=[b"raw file contents"],
        )
        assert_matches_type(object, document, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_upload(self, client: OpenHermes) -> None:
        response = client.api.document.with_raw_response.upload(
            conversation_id="",
            documents=[b"raw file contents"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = response.parse()
        assert_matches_type(object, document, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_upload(self, client: OpenHermes) -> None:
        with client.api.document.with_streaming_response.upload(
            conversation_id="",
            documents=[b"raw file contents"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document = response.parse()
            assert_matches_type(object, document, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_upload(self, client: OpenHermes) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `conversation_id` but received ''"):
            client.api.document.with_raw_response.upload(
                conversation_id="",
                documents=[b"raw file contents"],
            )


class TestAsyncDocument:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncOpenHermes) -> None:
        document = await async_client.api.document.delete(
            "document_id",
        )
        assert_matches_type(ResponseData, document, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncOpenHermes) -> None:
        response = await async_client.api.document.with_raw_response.delete(
            "document_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = await response.parse()
        assert_matches_type(ResponseData, document, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncOpenHermes) -> None:
        async with async_client.api.document.with_streaming_response.delete(
            "document_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document = await response.parse()
            assert_matches_type(ResponseData, document, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncOpenHermes) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `document_id` but received ''"):
            await async_client.api.document.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_list(self, async_client: AsyncOpenHermes) -> None:
        document = await async_client.api.document.get_list(
            conversation_id="",
        )
        assert_matches_type(DocumentGetListResponse, document, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_list_with_all_params(self, async_client: AsyncOpenHermes) -> None:
        document = await async_client.api.document.get_list(
            conversation_id="",
            unused=True,
            used=True,
        )
        assert_matches_type(DocumentGetListResponse, document, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get_list(self, async_client: AsyncOpenHermes) -> None:
        response = await async_client.api.document.with_raw_response.get_list(
            conversation_id="",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = await response.parse()
        assert_matches_type(DocumentGetListResponse, document, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get_list(self, async_client: AsyncOpenHermes) -> None:
        async with async_client.api.document.with_streaming_response.get_list(
            conversation_id="",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document = await response.parse()
            assert_matches_type(DocumentGetListResponse, document, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_get_list(self, async_client: AsyncOpenHermes) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `conversation_id` but received ''"):
            await async_client.api.document.with_raw_response.get_list(
                conversation_id="",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_upload(self, async_client: AsyncOpenHermes) -> None:
        document = await async_client.api.document.upload(
            conversation_id="",
            documents=[b"raw file contents"],
        )
        assert_matches_type(object, document, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_upload(self, async_client: AsyncOpenHermes) -> None:
        response = await async_client.api.document.with_raw_response.upload(
            conversation_id="",
            documents=[b"raw file contents"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = await response.parse()
        assert_matches_type(object, document, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_upload(self, async_client: AsyncOpenHermes) -> None:
        async with async_client.api.document.with_streaming_response.upload(
            conversation_id="",
            documents=[b"raw file contents"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document = await response.parse()
            assert_matches_type(object, document, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_upload(self, async_client: AsyncOpenHermes) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `conversation_id` but received ''"):
            await async_client.api.document.with_raw_response.upload(
                conversation_id="",
                documents=[b"raw file contents"],
            )
