# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from openhermes import Openhermes, AsyncOpenhermes
from tests.utils import assert_matches_type
from openhermes.types.api import AuthUser, AuthRedirectResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAuth:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_login(self, client: Openhermes) -> None:
        auth = client.api.auth.login(
            code="code",
        )
        assert_matches_type(object, auth, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_login(self, client: Openhermes) -> None:
        response = client.api.auth.with_raw_response.login(
            code="code",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth = response.parse()
        assert_matches_type(object, auth, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_login(self, client: Openhermes) -> None:
        with client.api.auth.with_streaming_response.login(
            code="code",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            auth = response.parse()
            assert_matches_type(object, auth, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_redirect(self, client: Openhermes) -> None:
        auth = client.api.auth.redirect()
        assert_matches_type(AuthRedirectResponse, auth, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_redirect(self, client: Openhermes) -> None:
        response = client.api.auth.with_raw_response.redirect()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth = response.parse()
        assert_matches_type(AuthRedirectResponse, auth, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_redirect(self, client: Openhermes) -> None:
        with client.api.auth.with_streaming_response.redirect() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            auth = response.parse()
            assert_matches_type(AuthRedirectResponse, auth, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve_user(self, client: Openhermes) -> None:
        auth = client.api.auth.retrieve_user()
        assert_matches_type(AuthUser, auth, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retrieve_user(self, client: Openhermes) -> None:
        response = client.api.auth.with_raw_response.retrieve_user()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth = response.parse()
        assert_matches_type(AuthUser, auth, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_retrieve_user(self, client: Openhermes) -> None:
        with client.api.auth.with_streaming_response.retrieve_user() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            auth = response.parse()
            assert_matches_type(AuthUser, auth, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_update_revision(self, client: Openhermes) -> None:
        auth = client.api.auth.update_revision()
        assert_matches_type(AuthUser, auth, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update_revision(self, client: Openhermes) -> None:
        response = client.api.auth.with_raw_response.update_revision()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth = response.parse()
        assert_matches_type(AuthUser, auth, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update_revision(self, client: Openhermes) -> None:
        with client.api.auth.with_streaming_response.update_revision() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            auth = response.parse()
            assert_matches_type(AuthUser, auth, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAuth:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip()
    @parametrize
    async def test_method_login(self, async_client: AsyncOpenhermes) -> None:
        auth = await async_client.api.auth.login(
            code="code",
        )
        assert_matches_type(object, auth, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_login(self, async_client: AsyncOpenhermes) -> None:
        response = await async_client.api.auth.with_raw_response.login(
            code="code",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth = await response.parse()
        assert_matches_type(object, auth, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_login(self, async_client: AsyncOpenhermes) -> None:
        async with async_client.api.auth.with_streaming_response.login(
            code="code",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            auth = await response.parse()
            assert_matches_type(object, auth, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_redirect(self, async_client: AsyncOpenhermes) -> None:
        auth = await async_client.api.auth.redirect()
        assert_matches_type(AuthRedirectResponse, auth, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_redirect(self, async_client: AsyncOpenhermes) -> None:
        response = await async_client.api.auth.with_raw_response.redirect()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth = await response.parse()
        assert_matches_type(AuthRedirectResponse, auth, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_redirect(self, async_client: AsyncOpenhermes) -> None:
        async with async_client.api.auth.with_streaming_response.redirect() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            auth = await response.parse()
            assert_matches_type(AuthRedirectResponse, auth, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve_user(self, async_client: AsyncOpenhermes) -> None:
        auth = await async_client.api.auth.retrieve_user()
        assert_matches_type(AuthUser, auth, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retrieve_user(self, async_client: AsyncOpenhermes) -> None:
        response = await async_client.api.auth.with_raw_response.retrieve_user()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth = await response.parse()
        assert_matches_type(AuthUser, auth, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_retrieve_user(self, async_client: AsyncOpenhermes) -> None:
        async with async_client.api.auth.with_streaming_response.retrieve_user() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            auth = await response.parse()
            assert_matches_type(AuthUser, auth, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_revision(self, async_client: AsyncOpenhermes) -> None:
        auth = await async_client.api.auth.update_revision()
        assert_matches_type(AuthUser, auth, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update_revision(self, async_client: AsyncOpenhermes) -> None:
        response = await async_client.api.auth.with_raw_response.update_revision()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth = await response.parse()
        assert_matches_type(AuthUser, auth, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update_revision(self, async_client: AsyncOpenhermes) -> None:
        async with async_client.api.auth.with_streaming_response.update_revision() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            auth = await response.parse()
            assert_matches_type(AuthUser, auth, path=["response"])

        assert cast(Any, response.is_closed) is True
