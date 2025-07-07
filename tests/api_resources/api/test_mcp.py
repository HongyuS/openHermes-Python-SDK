# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from openhermes import Openhermes, AsyncOpenhermes
from tests.utils import assert_matches_type
from openhermes.types.api import (
    McpDeleteResponse,
    McpGetListResponse,
    McpGetDetailResponse,
    McpCreateOrUpdateResponse,
    McpActivateOrDeactivateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMcp:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: Openhermes) -> None:
        mcp = client.api.mcp.delete(
            "serviceId",
        )
        assert_matches_type(McpDeleteResponse, mcp, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: Openhermes) -> None:
        response = client.api.mcp.with_raw_response.delete(
            "serviceId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mcp = response.parse()
        assert_matches_type(McpDeleteResponse, mcp, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: Openhermes) -> None:
        with client.api.mcp.with_streaming_response.delete(
            "serviceId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mcp = response.parse()
            assert_matches_type(McpDeleteResponse, mcp, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_delete(self, client: Openhermes) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `service_id` but received ''"):
            client.api.mcp.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_activate_or_deactivate(self, client: Openhermes) -> None:
        mcp = client.api.mcp.activate_or_deactivate(
            service_id="",
            active=True,
        )
        assert_matches_type(McpActivateOrDeactivateResponse, mcp, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_activate_or_deactivate(self, client: Openhermes) -> None:
        response = client.api.mcp.with_raw_response.activate_or_deactivate(
            service_id="",
            active=True,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mcp = response.parse()
        assert_matches_type(McpActivateOrDeactivateResponse, mcp, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_activate_or_deactivate(self, client: Openhermes) -> None:
        with client.api.mcp.with_streaming_response.activate_or_deactivate(
            service_id="",
            active=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mcp = response.parse()
            assert_matches_type(McpActivateOrDeactivateResponse, mcp, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_activate_or_deactivate(self, client: Openhermes) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `service_id` but received ''"):
            client.api.mcp.with_raw_response.activate_or_deactivate(
                service_id="",
                active=True,
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_create_or_update(self, client: Openhermes) -> None:
        mcp = client.api.mcp.create_or_update(
            config="config",
            description="description",
            name="name",
        )
        assert_matches_type(McpCreateOrUpdateResponse, mcp, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_or_update_with_all_params(self, client: Openhermes) -> None:
        mcp = client.api.mcp.create_or_update(
            config="config",
            description="description",
            name="name",
            icon="icon",
            mcp_type="sse",
            service_id="serviceId",
        )
        assert_matches_type(McpCreateOrUpdateResponse, mcp, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create_or_update(self, client: Openhermes) -> None:
        response = client.api.mcp.with_raw_response.create_or_update(
            config="config",
            description="description",
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mcp = response.parse()
        assert_matches_type(McpCreateOrUpdateResponse, mcp, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create_or_update(self, client: Openhermes) -> None:
        with client.api.mcp.with_streaming_response.create_or_update(
            config="config",
            description="description",
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mcp = response.parse()
            assert_matches_type(McpCreateOrUpdateResponse, mcp, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_get_detail(self, client: Openhermes) -> None:
        mcp = client.api.mcp.get_detail(
            service_id="",
        )
        assert_matches_type(McpGetDetailResponse, mcp, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_get_detail_with_all_params(self, client: Openhermes) -> None:
        mcp = client.api.mcp.get_detail(
            service_id="",
            edit=True,
        )
        assert_matches_type(McpGetDetailResponse, mcp, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get_detail(self, client: Openhermes) -> None:
        response = client.api.mcp.with_raw_response.get_detail(
            service_id="",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mcp = response.parse()
        assert_matches_type(McpGetDetailResponse, mcp, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get_detail(self, client: Openhermes) -> None:
        with client.api.mcp.with_streaming_response.get_detail(
            service_id="",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mcp = response.parse()
            assert_matches_type(McpGetDetailResponse, mcp, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_get_detail(self, client: Openhermes) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `service_id` but received ''"):
            client.api.mcp.with_raw_response.get_detail(
                service_id="",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_get_list(self, client: Openhermes) -> None:
        mcp = client.api.mcp.get_list()
        assert_matches_type(McpGetListResponse, mcp, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_get_list_with_all_params(self, client: Openhermes) -> None:
        mcp = client.api.mcp.get_list(
            is_active=True,
            keyword="keyword",
            page=1,
            page_size=1,
            search_type="all",
        )
        assert_matches_type(McpGetListResponse, mcp, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get_list(self, client: Openhermes) -> None:
        response = client.api.mcp.with_raw_response.get_list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mcp = response.parse()
        assert_matches_type(McpGetListResponse, mcp, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get_list(self, client: Openhermes) -> None:
        with client.api.mcp.with_streaming_response.get_list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mcp = response.parse()
            assert_matches_type(McpGetListResponse, mcp, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncMcp:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncOpenhermes) -> None:
        mcp = await async_client.api.mcp.delete(
            "serviceId",
        )
        assert_matches_type(McpDeleteResponse, mcp, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncOpenhermes) -> None:
        response = await async_client.api.mcp.with_raw_response.delete(
            "serviceId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mcp = await response.parse()
        assert_matches_type(McpDeleteResponse, mcp, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncOpenhermes) -> None:
        async with async_client.api.mcp.with_streaming_response.delete(
            "serviceId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mcp = await response.parse()
            assert_matches_type(McpDeleteResponse, mcp, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncOpenhermes) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `service_id` but received ''"):
            await async_client.api.mcp.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_activate_or_deactivate(self, async_client: AsyncOpenhermes) -> None:
        mcp = await async_client.api.mcp.activate_or_deactivate(
            service_id="",
            active=True,
        )
        assert_matches_type(McpActivateOrDeactivateResponse, mcp, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_activate_or_deactivate(self, async_client: AsyncOpenhermes) -> None:
        response = await async_client.api.mcp.with_raw_response.activate_or_deactivate(
            service_id="",
            active=True,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mcp = await response.parse()
        assert_matches_type(McpActivateOrDeactivateResponse, mcp, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_activate_or_deactivate(self, async_client: AsyncOpenhermes) -> None:
        async with async_client.api.mcp.with_streaming_response.activate_or_deactivate(
            service_id="",
            active=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mcp = await response.parse()
            assert_matches_type(McpActivateOrDeactivateResponse, mcp, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_activate_or_deactivate(self, async_client: AsyncOpenhermes) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `service_id` but received ''"):
            await async_client.api.mcp.with_raw_response.activate_or_deactivate(
                service_id="",
                active=True,
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_or_update(self, async_client: AsyncOpenhermes) -> None:
        mcp = await async_client.api.mcp.create_or_update(
            config="config",
            description="description",
            name="name",
        )
        assert_matches_type(McpCreateOrUpdateResponse, mcp, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_or_update_with_all_params(self, async_client: AsyncOpenhermes) -> None:
        mcp = await async_client.api.mcp.create_or_update(
            config="config",
            description="description",
            name="name",
            icon="icon",
            mcp_type="sse",
            service_id="serviceId",
        )
        assert_matches_type(McpCreateOrUpdateResponse, mcp, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create_or_update(self, async_client: AsyncOpenhermes) -> None:
        response = await async_client.api.mcp.with_raw_response.create_or_update(
            config="config",
            description="description",
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mcp = await response.parse()
        assert_matches_type(McpCreateOrUpdateResponse, mcp, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create_or_update(self, async_client: AsyncOpenhermes) -> None:
        async with async_client.api.mcp.with_streaming_response.create_or_update(
            config="config",
            description="description",
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mcp = await response.parse()
            assert_matches_type(McpCreateOrUpdateResponse, mcp, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_detail(self, async_client: AsyncOpenhermes) -> None:
        mcp = await async_client.api.mcp.get_detail(
            service_id="",
        )
        assert_matches_type(McpGetDetailResponse, mcp, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_detail_with_all_params(self, async_client: AsyncOpenhermes) -> None:
        mcp = await async_client.api.mcp.get_detail(
            service_id="",
            edit=True,
        )
        assert_matches_type(McpGetDetailResponse, mcp, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get_detail(self, async_client: AsyncOpenhermes) -> None:
        response = await async_client.api.mcp.with_raw_response.get_detail(
            service_id="",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mcp = await response.parse()
        assert_matches_type(McpGetDetailResponse, mcp, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get_detail(self, async_client: AsyncOpenhermes) -> None:
        async with async_client.api.mcp.with_streaming_response.get_detail(
            service_id="",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mcp = await response.parse()
            assert_matches_type(McpGetDetailResponse, mcp, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_get_detail(self, async_client: AsyncOpenhermes) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `service_id` but received ''"):
            await async_client.api.mcp.with_raw_response.get_detail(
                service_id="",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_list(self, async_client: AsyncOpenhermes) -> None:
        mcp = await async_client.api.mcp.get_list()
        assert_matches_type(McpGetListResponse, mcp, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_list_with_all_params(self, async_client: AsyncOpenhermes) -> None:
        mcp = await async_client.api.mcp.get_list(
            is_active=True,
            keyword="keyword",
            page=1,
            page_size=1,
            search_type="all",
        )
        assert_matches_type(McpGetListResponse, mcp, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get_list(self, async_client: AsyncOpenhermes) -> None:
        response = await async_client.api.mcp.with_raw_response.get_list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mcp = await response.parse()
        assert_matches_type(McpGetListResponse, mcp, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get_list(self, async_client: AsyncOpenhermes) -> None:
        async with async_client.api.mcp.with_streaming_response.get_list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mcp = await response.parse()
            assert_matches_type(McpGetListResponse, mcp, path=["response"])

        assert cast(Any, response.is_closed) is True
