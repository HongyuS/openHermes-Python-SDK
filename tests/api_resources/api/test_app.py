# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from openhermes import Openhermes, AsyncOpenhermes
from tests.utils import assert_matches_type
from openhermes.types.api import (
    AppListResponse,
    AppDeleteResponse,
    AppRetrieveResponse,
    BaseAppOperationRsp,
    AppGetRecentResponse,
    AppCreateOrUpdateResponse,
    AppModifyFavoriteResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestApp:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve(self, client: Openhermes) -> None:
        app = client.api.app.retrieve(
            "appId",
        )
        assert_matches_type(AppRetrieveResponse, app, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retrieve(self, client: Openhermes) -> None:
        response = client.api.app.with_raw_response.retrieve(
            "appId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        app = response.parse()
        assert_matches_type(AppRetrieveResponse, app, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_retrieve(self, client: Openhermes) -> None:
        with client.api.app.with_streaming_response.retrieve(
            "appId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            app = response.parse()
            assert_matches_type(AppRetrieveResponse, app, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_retrieve(self, client: Openhermes) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            client.api.app.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: Openhermes) -> None:
        app = client.api.app.list()
        assert_matches_type(AppListResponse, app, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list_with_all_params(self, client: Openhermes) -> None:
        app = client.api.app.list(
            app_type="flow",
            created_by_me=True,
            favorited=True,
            keyword="keyword",
            page=1,
        )
        assert_matches_type(AppListResponse, app, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: Openhermes) -> None:
        response = client.api.app.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        app = response.parse()
        assert_matches_type(AppListResponse, app, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: Openhermes) -> None:
        with client.api.app.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            app = response.parse()
            assert_matches_type(AppListResponse, app, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: Openhermes) -> None:
        app = client.api.app.delete(
            "appId",
        )
        assert_matches_type(AppDeleteResponse, app, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: Openhermes) -> None:
        response = client.api.app.with_raw_response.delete(
            "appId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        app = response.parse()
        assert_matches_type(AppDeleteResponse, app, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: Openhermes) -> None:
        with client.api.app.with_streaming_response.delete(
            "appId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            app = response.parse()
            assert_matches_type(AppDeleteResponse, app, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_delete(self, client: Openhermes) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            client.api.app.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_create_or_update(self, client: Openhermes) -> None:
        app = client.api.app.create_or_update(
            app_type="flow",
            description="description",
            name="name",
        )
        assert_matches_type(AppCreateOrUpdateResponse, app, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_or_update_with_all_params(self, client: Openhermes) -> None:
        app = client.api.app.create_or_update(
            app_type="flow",
            description="description",
            name="name",
            app_id="appId",
            dialog_rounds=1,
            icon="icon",
            links=[
                {
                    "title": "title",
                    "url": "http://JS!?Q",
                }
            ],
            mcp_service=["string"],
            permission={
                "authorized_users": ["string"],
                "visibility": "protected",
            },
            recommended_questions=["string"],
            workflows=[
                {
                    "id": "id",
                    "debug": True,
                    "description": "description",
                    "name": "name",
                }
            ],
        )
        assert_matches_type(AppCreateOrUpdateResponse, app, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create_or_update(self, client: Openhermes) -> None:
        response = client.api.app.with_raw_response.create_or_update(
            app_type="flow",
            description="description",
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        app = response.parse()
        assert_matches_type(AppCreateOrUpdateResponse, app, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create_or_update(self, client: Openhermes) -> None:
        with client.api.app.with_streaming_response.create_or_update(
            app_type="flow",
            description="description",
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            app = response.parse()
            assert_matches_type(AppCreateOrUpdateResponse, app, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_get_recent(self, client: Openhermes) -> None:
        app = client.api.app.get_recent()
        assert_matches_type(AppGetRecentResponse, app, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_get_recent_with_all_params(self, client: Openhermes) -> None:
        app = client.api.app.get_recent(
            count=1,
        )
        assert_matches_type(AppGetRecentResponse, app, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get_recent(self, client: Openhermes) -> None:
        response = client.api.app.with_raw_response.get_recent()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        app = response.parse()
        assert_matches_type(AppGetRecentResponse, app, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get_recent(self, client: Openhermes) -> None:
        with client.api.app.with_streaming_response.get_recent() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            app = response.parse()
            assert_matches_type(AppGetRecentResponse, app, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_modify_favorite(self, client: Openhermes) -> None:
        app = client.api.app.modify_favorite(
            app_id="",
            favorited=True,
        )
        assert_matches_type(AppModifyFavoriteResponse, app, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_modify_favorite(self, client: Openhermes) -> None:
        response = client.api.app.with_raw_response.modify_favorite(
            app_id="",
            favorited=True,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        app = response.parse()
        assert_matches_type(AppModifyFavoriteResponse, app, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_modify_favorite(self, client: Openhermes) -> None:
        with client.api.app.with_streaming_response.modify_favorite(
            app_id="",
            favorited=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            app = response.parse()
            assert_matches_type(AppModifyFavoriteResponse, app, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_modify_favorite(self, client: Openhermes) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            client.api.app.with_raw_response.modify_favorite(
                app_id="",
                favorited=True,
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_publish(self, client: Openhermes) -> None:
        app = client.api.app.publish(
            "appId",
        )
        assert_matches_type(BaseAppOperationRsp, app, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_publish(self, client: Openhermes) -> None:
        response = client.api.app.with_raw_response.publish(
            "appId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        app = response.parse()
        assert_matches_type(BaseAppOperationRsp, app, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_publish(self, client: Openhermes) -> None:
        with client.api.app.with_streaming_response.publish(
            "appId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            app = response.parse()
            assert_matches_type(BaseAppOperationRsp, app, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_publish(self, client: Openhermes) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            client.api.app.with_raw_response.publish(
                "",
            )


class TestAsyncApp:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncOpenhermes) -> None:
        app = await async_client.api.app.retrieve(
            "appId",
        )
        assert_matches_type(AppRetrieveResponse, app, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncOpenhermes) -> None:
        response = await async_client.api.app.with_raw_response.retrieve(
            "appId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        app = await response.parse()
        assert_matches_type(AppRetrieveResponse, app, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncOpenhermes) -> None:
        async with async_client.api.app.with_streaming_response.retrieve(
            "appId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            app = await response.parse()
            assert_matches_type(AppRetrieveResponse, app, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncOpenhermes) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            await async_client.api.app.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncOpenhermes) -> None:
        app = await async_client.api.app.list()
        assert_matches_type(AppListResponse, app, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncOpenhermes) -> None:
        app = await async_client.api.app.list(
            app_type="flow",
            created_by_me=True,
            favorited=True,
            keyword="keyword",
            page=1,
        )
        assert_matches_type(AppListResponse, app, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncOpenhermes) -> None:
        response = await async_client.api.app.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        app = await response.parse()
        assert_matches_type(AppListResponse, app, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncOpenhermes) -> None:
        async with async_client.api.app.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            app = await response.parse()
            assert_matches_type(AppListResponse, app, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncOpenhermes) -> None:
        app = await async_client.api.app.delete(
            "appId",
        )
        assert_matches_type(AppDeleteResponse, app, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncOpenhermes) -> None:
        response = await async_client.api.app.with_raw_response.delete(
            "appId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        app = await response.parse()
        assert_matches_type(AppDeleteResponse, app, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncOpenhermes) -> None:
        async with async_client.api.app.with_streaming_response.delete(
            "appId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            app = await response.parse()
            assert_matches_type(AppDeleteResponse, app, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncOpenhermes) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            await async_client.api.app.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_or_update(self, async_client: AsyncOpenhermes) -> None:
        app = await async_client.api.app.create_or_update(
            app_type="flow",
            description="description",
            name="name",
        )
        assert_matches_type(AppCreateOrUpdateResponse, app, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_or_update_with_all_params(self, async_client: AsyncOpenhermes) -> None:
        app = await async_client.api.app.create_or_update(
            app_type="flow",
            description="description",
            name="name",
            app_id="appId",
            dialog_rounds=1,
            icon="icon",
            links=[
                {
                    "title": "title",
                    "url": "http://JS!?Q",
                }
            ],
            mcp_service=["string"],
            permission={
                "authorized_users": ["string"],
                "visibility": "protected",
            },
            recommended_questions=["string"],
            workflows=[
                {
                    "id": "id",
                    "debug": True,
                    "description": "description",
                    "name": "name",
                }
            ],
        )
        assert_matches_type(AppCreateOrUpdateResponse, app, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create_or_update(self, async_client: AsyncOpenhermes) -> None:
        response = await async_client.api.app.with_raw_response.create_or_update(
            app_type="flow",
            description="description",
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        app = await response.parse()
        assert_matches_type(AppCreateOrUpdateResponse, app, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create_or_update(self, async_client: AsyncOpenhermes) -> None:
        async with async_client.api.app.with_streaming_response.create_or_update(
            app_type="flow",
            description="description",
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            app = await response.parse()
            assert_matches_type(AppCreateOrUpdateResponse, app, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_recent(self, async_client: AsyncOpenhermes) -> None:
        app = await async_client.api.app.get_recent()
        assert_matches_type(AppGetRecentResponse, app, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_recent_with_all_params(self, async_client: AsyncOpenhermes) -> None:
        app = await async_client.api.app.get_recent(
            count=1,
        )
        assert_matches_type(AppGetRecentResponse, app, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get_recent(self, async_client: AsyncOpenhermes) -> None:
        response = await async_client.api.app.with_raw_response.get_recent()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        app = await response.parse()
        assert_matches_type(AppGetRecentResponse, app, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get_recent(self, async_client: AsyncOpenhermes) -> None:
        async with async_client.api.app.with_streaming_response.get_recent() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            app = await response.parse()
            assert_matches_type(AppGetRecentResponse, app, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_modify_favorite(self, async_client: AsyncOpenhermes) -> None:
        app = await async_client.api.app.modify_favorite(
            app_id="",
            favorited=True,
        )
        assert_matches_type(AppModifyFavoriteResponse, app, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_modify_favorite(self, async_client: AsyncOpenhermes) -> None:
        response = await async_client.api.app.with_raw_response.modify_favorite(
            app_id="",
            favorited=True,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        app = await response.parse()
        assert_matches_type(AppModifyFavoriteResponse, app, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_modify_favorite(self, async_client: AsyncOpenhermes) -> None:
        async with async_client.api.app.with_streaming_response.modify_favorite(
            app_id="",
            favorited=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            app = await response.parse()
            assert_matches_type(AppModifyFavoriteResponse, app, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_modify_favorite(self, async_client: AsyncOpenhermes) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            await async_client.api.app.with_raw_response.modify_favorite(
                app_id="",
                favorited=True,
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_publish(self, async_client: AsyncOpenhermes) -> None:
        app = await async_client.api.app.publish(
            "appId",
        )
        assert_matches_type(BaseAppOperationRsp, app, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_publish(self, async_client: AsyncOpenhermes) -> None:
        response = await async_client.api.app.with_raw_response.publish(
            "appId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        app = await response.parse()
        assert_matches_type(BaseAppOperationRsp, app, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_publish(self, async_client: AsyncOpenhermes) -> None:
        async with async_client.api.app.with_streaming_response.publish(
            "appId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            app = await response.parse()
            assert_matches_type(BaseAppOperationRsp, app, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_publish(self, async_client: AsyncOpenhermes) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            await async_client.api.app.with_raw_response.publish(
                "",
            )
