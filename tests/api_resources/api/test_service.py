# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from openhermes import OpenHermes, AsyncOpenHermes
from tests.utils import assert_matches_type
from openhermes.types.api import (
    ServiceListResponse,
    ServiceDeleteResponse,
    ServiceUpdateResponse,
    ServiceRetrieveResponse,
    ServiceModifyFavoriteResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestService:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve(self, client: OpenHermes) -> None:
        service = client.api.service.retrieve(
            service_id="",
        )
        assert_matches_type(ServiceRetrieveResponse, service, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve_with_all_params(self, client: OpenHermes) -> None:
        service = client.api.service.retrieve(
            service_id="",
            edit=True,
        )
        assert_matches_type(ServiceRetrieveResponse, service, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retrieve(self, client: OpenHermes) -> None:
        response = client.api.service.with_raw_response.retrieve(
            service_id="",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        service = response.parse()
        assert_matches_type(ServiceRetrieveResponse, service, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_retrieve(self, client: OpenHermes) -> None:
        with client.api.service.with_streaming_response.retrieve(
            service_id="",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            service = response.parse()
            assert_matches_type(ServiceRetrieveResponse, service, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_retrieve(self, client: OpenHermes) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `service_id` but received ''"):
            client.api.service.with_raw_response.retrieve(
                service_id="",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_update(self, client: OpenHermes) -> None:
        service = client.api.service.update(
            data={},
        )
        assert_matches_type(ServiceUpdateResponse, service, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update_with_all_params(self, client: OpenHermes) -> None:
        service = client.api.service.update(
            data={},
            service_id="serviceId",
        )
        assert_matches_type(ServiceUpdateResponse, service, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update(self, client: OpenHermes) -> None:
        response = client.api.service.with_raw_response.update(
            data={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        service = response.parse()
        assert_matches_type(ServiceUpdateResponse, service, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update(self, client: OpenHermes) -> None:
        with client.api.service.with_streaming_response.update(
            data={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            service = response.parse()
            assert_matches_type(ServiceUpdateResponse, service, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: OpenHermes) -> None:
        service = client.api.service.list()
        assert_matches_type(ServiceListResponse, service, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list_with_all_params(self, client: OpenHermes) -> None:
        service = client.api.service.list(
            created_by_me=True,
            favorited=True,
            keyword="keyword",
            page=1,
            page_size=1,
            search_type="all",
        )
        assert_matches_type(ServiceListResponse, service, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: OpenHermes) -> None:
        response = client.api.service.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        service = response.parse()
        assert_matches_type(ServiceListResponse, service, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: OpenHermes) -> None:
        with client.api.service.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            service = response.parse()
            assert_matches_type(ServiceListResponse, service, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: OpenHermes) -> None:
        service = client.api.service.delete(
            "serviceId",
        )
        assert_matches_type(ServiceDeleteResponse, service, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: OpenHermes) -> None:
        response = client.api.service.with_raw_response.delete(
            "serviceId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        service = response.parse()
        assert_matches_type(ServiceDeleteResponse, service, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: OpenHermes) -> None:
        with client.api.service.with_streaming_response.delete(
            "serviceId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            service = response.parse()
            assert_matches_type(ServiceDeleteResponse, service, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_delete(self, client: OpenHermes) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `service_id` but received ''"):
            client.api.service.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_modify_favorite(self, client: OpenHermes) -> None:
        service = client.api.service.modify_favorite(
            service_id="",
            favorited=True,
        )
        assert_matches_type(ServiceModifyFavoriteResponse, service, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_modify_favorite(self, client: OpenHermes) -> None:
        response = client.api.service.with_raw_response.modify_favorite(
            service_id="",
            favorited=True,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        service = response.parse()
        assert_matches_type(ServiceModifyFavoriteResponse, service, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_modify_favorite(self, client: OpenHermes) -> None:
        with client.api.service.with_streaming_response.modify_favorite(
            service_id="",
            favorited=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            service = response.parse()
            assert_matches_type(ServiceModifyFavoriteResponse, service, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_modify_favorite(self, client: OpenHermes) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `service_id` but received ''"):
            client.api.service.with_raw_response.modify_favorite(
                service_id="",
                favorited=True,
            )


class TestAsyncService:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncOpenHermes) -> None:
        service = await async_client.api.service.retrieve(
            service_id="",
        )
        assert_matches_type(ServiceRetrieveResponse, service, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncOpenHermes) -> None:
        service = await async_client.api.service.retrieve(
            service_id="",
            edit=True,
        )
        assert_matches_type(ServiceRetrieveResponse, service, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncOpenHermes) -> None:
        response = await async_client.api.service.with_raw_response.retrieve(
            service_id="",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        service = await response.parse()
        assert_matches_type(ServiceRetrieveResponse, service, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncOpenHermes) -> None:
        async with async_client.api.service.with_streaming_response.retrieve(
            service_id="",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            service = await response.parse()
            assert_matches_type(ServiceRetrieveResponse, service, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncOpenHermes) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `service_id` but received ''"):
            await async_client.api.service.with_raw_response.retrieve(
                service_id="",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_update(self, async_client: AsyncOpenHermes) -> None:
        service = await async_client.api.service.update(
            data={},
        )
        assert_matches_type(ServiceUpdateResponse, service, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncOpenHermes) -> None:
        service = await async_client.api.service.update(
            data={},
            service_id="serviceId",
        )
        assert_matches_type(ServiceUpdateResponse, service, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncOpenHermes) -> None:
        response = await async_client.api.service.with_raw_response.update(
            data={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        service = await response.parse()
        assert_matches_type(ServiceUpdateResponse, service, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncOpenHermes) -> None:
        async with async_client.api.service.with_streaming_response.update(
            data={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            service = await response.parse()
            assert_matches_type(ServiceUpdateResponse, service, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncOpenHermes) -> None:
        service = await async_client.api.service.list()
        assert_matches_type(ServiceListResponse, service, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncOpenHermes) -> None:
        service = await async_client.api.service.list(
            created_by_me=True,
            favorited=True,
            keyword="keyword",
            page=1,
            page_size=1,
            search_type="all",
        )
        assert_matches_type(ServiceListResponse, service, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncOpenHermes) -> None:
        response = await async_client.api.service.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        service = await response.parse()
        assert_matches_type(ServiceListResponse, service, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncOpenHermes) -> None:
        async with async_client.api.service.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            service = await response.parse()
            assert_matches_type(ServiceListResponse, service, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncOpenHermes) -> None:
        service = await async_client.api.service.delete(
            "serviceId",
        )
        assert_matches_type(ServiceDeleteResponse, service, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncOpenHermes) -> None:
        response = await async_client.api.service.with_raw_response.delete(
            "serviceId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        service = await response.parse()
        assert_matches_type(ServiceDeleteResponse, service, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncOpenHermes) -> None:
        async with async_client.api.service.with_streaming_response.delete(
            "serviceId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            service = await response.parse()
            assert_matches_type(ServiceDeleteResponse, service, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncOpenHermes) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `service_id` but received ''"):
            await async_client.api.service.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_modify_favorite(self, async_client: AsyncOpenHermes) -> None:
        service = await async_client.api.service.modify_favorite(
            service_id="",
            favorited=True,
        )
        assert_matches_type(ServiceModifyFavoriteResponse, service, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_modify_favorite(self, async_client: AsyncOpenHermes) -> None:
        response = await async_client.api.service.with_raw_response.modify_favorite(
            service_id="",
            favorited=True,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        service = await response.parse()
        assert_matches_type(ServiceModifyFavoriteResponse, service, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_modify_favorite(self, async_client: AsyncOpenHermes) -> None:
        async with async_client.api.service.with_streaming_response.modify_favorite(
            service_id="",
            favorited=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            service = await response.parse()
            assert_matches_type(ServiceModifyFavoriteResponse, service, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_modify_favorite(self, async_client: AsyncOpenHermes) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `service_id` but received ''"):
            await async_client.api.service.with_raw_response.modify_favorite(
                service_id="",
                favorited=True,
            )
