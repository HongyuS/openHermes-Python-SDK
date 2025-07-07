# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from openhermes import Openhermes, AsyncOpenhermes
from tests.utils import assert_matches_type
from openhermes.types.api import (
    FlowGetResponse,
    FlowDeleteResponse,
    FlowUpdateResponse,
    FlowGetServicesResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFlow:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update(self, client: Openhermes) -> None:
        flow = client.api.flow.update(
            app_id="appId",
            flow_id="flowId",
            flow={},
        )
        assert_matches_type(FlowUpdateResponse, flow, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update_with_all_params(self, client: Openhermes) -> None:
        flow = client.api.flow.update(
            app_id="appId",
            flow_id="flowId",
            flow={
                "connectivity": True,
                "created_at": 0,
                "debug": True,
                "description": "description",
                "edges": [
                    {
                        "branch_id": "branchId",
                        "edge_id": "edgeId",
                        "source_node": "sourceNode",
                        "target_node": "targetNode",
                        "type": "type",
                    }
                ],
                "editable": True,
                "enable": True,
                "flow_id": "flowId",
                "focus_point": {
                    "x": 0,
                    "y": 0,
                },
                "name": "name",
                "nodes": [
                    {
                        "call_id": "callId",
                        "depedency": {
                            "node_id": "nodeId",
                            "type": "type",
                        },
                        "description": "description",
                        "editable": True,
                        "enable": True,
                        "name": "name",
                        "node_id": "nodeId",
                        "parameters": {},
                        "position": {
                            "x": 0,
                            "y": 0,
                        },
                        "service_id": "serviceId",
                        "step_id": "stepId",
                    }
                ],
            },
        )
        assert_matches_type(FlowUpdateResponse, flow, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update(self, client: Openhermes) -> None:
        response = client.api.flow.with_raw_response.update(
            app_id="appId",
            flow_id="flowId",
            flow={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        flow = response.parse()
        assert_matches_type(FlowUpdateResponse, flow, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update(self, client: Openhermes) -> None:
        with client.api.flow.with_streaming_response.update(
            app_id="appId",
            flow_id="flowId",
            flow={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            flow = response.parse()
            assert_matches_type(FlowUpdateResponse, flow, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: Openhermes) -> None:
        flow = client.api.flow.delete(
            app_id="appId",
            flow_id="flowId",
        )
        assert_matches_type(FlowDeleteResponse, flow, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: Openhermes) -> None:
        response = client.api.flow.with_raw_response.delete(
            app_id="appId",
            flow_id="flowId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        flow = response.parse()
        assert_matches_type(FlowDeleteResponse, flow, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: Openhermes) -> None:
        with client.api.flow.with_streaming_response.delete(
            app_id="appId",
            flow_id="flowId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            flow = response.parse()
            assert_matches_type(FlowDeleteResponse, flow, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_get(self, client: Openhermes) -> None:
        flow = client.api.flow.get(
            app_id="appId",
            flow_id="flowId",
        )
        assert_matches_type(FlowGetResponse, flow, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get(self, client: Openhermes) -> None:
        response = client.api.flow.with_raw_response.get(
            app_id="appId",
            flow_id="flowId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        flow = response.parse()
        assert_matches_type(FlowGetResponse, flow, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get(self, client: Openhermes) -> None:
        with client.api.flow.with_streaming_response.get(
            app_id="appId",
            flow_id="flowId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            flow = response.parse()
            assert_matches_type(FlowGetResponse, flow, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_get_services(self, client: Openhermes) -> None:
        flow = client.api.flow.get_services()
        assert_matches_type(FlowGetServicesResponse, flow, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get_services(self, client: Openhermes) -> None:
        response = client.api.flow.with_raw_response.get_services()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        flow = response.parse()
        assert_matches_type(FlowGetServicesResponse, flow, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get_services(self, client: Openhermes) -> None:
        with client.api.flow.with_streaming_response.get_services() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            flow = response.parse()
            assert_matches_type(FlowGetServicesResponse, flow, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncFlow:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip()
    @parametrize
    async def test_method_update(self, async_client: AsyncOpenhermes) -> None:
        flow = await async_client.api.flow.update(
            app_id="appId",
            flow_id="flowId",
            flow={},
        )
        assert_matches_type(FlowUpdateResponse, flow, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncOpenhermes) -> None:
        flow = await async_client.api.flow.update(
            app_id="appId",
            flow_id="flowId",
            flow={
                "connectivity": True,
                "created_at": 0,
                "debug": True,
                "description": "description",
                "edges": [
                    {
                        "branch_id": "branchId",
                        "edge_id": "edgeId",
                        "source_node": "sourceNode",
                        "target_node": "targetNode",
                        "type": "type",
                    }
                ],
                "editable": True,
                "enable": True,
                "flow_id": "flowId",
                "focus_point": {
                    "x": 0,
                    "y": 0,
                },
                "name": "name",
                "nodes": [
                    {
                        "call_id": "callId",
                        "depedency": {
                            "node_id": "nodeId",
                            "type": "type",
                        },
                        "description": "description",
                        "editable": True,
                        "enable": True,
                        "name": "name",
                        "node_id": "nodeId",
                        "parameters": {},
                        "position": {
                            "x": 0,
                            "y": 0,
                        },
                        "service_id": "serviceId",
                        "step_id": "stepId",
                    }
                ],
            },
        )
        assert_matches_type(FlowUpdateResponse, flow, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncOpenhermes) -> None:
        response = await async_client.api.flow.with_raw_response.update(
            app_id="appId",
            flow_id="flowId",
            flow={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        flow = await response.parse()
        assert_matches_type(FlowUpdateResponse, flow, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncOpenhermes) -> None:
        async with async_client.api.flow.with_streaming_response.update(
            app_id="appId",
            flow_id="flowId",
            flow={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            flow = await response.parse()
            assert_matches_type(FlowUpdateResponse, flow, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncOpenhermes) -> None:
        flow = await async_client.api.flow.delete(
            app_id="appId",
            flow_id="flowId",
        )
        assert_matches_type(FlowDeleteResponse, flow, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncOpenhermes) -> None:
        response = await async_client.api.flow.with_raw_response.delete(
            app_id="appId",
            flow_id="flowId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        flow = await response.parse()
        assert_matches_type(FlowDeleteResponse, flow, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncOpenhermes) -> None:
        async with async_client.api.flow.with_streaming_response.delete(
            app_id="appId",
            flow_id="flowId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            flow = await response.parse()
            assert_matches_type(FlowDeleteResponse, flow, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_get(self, async_client: AsyncOpenhermes) -> None:
        flow = await async_client.api.flow.get(
            app_id="appId",
            flow_id="flowId",
        )
        assert_matches_type(FlowGetResponse, flow, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncOpenhermes) -> None:
        response = await async_client.api.flow.with_raw_response.get(
            app_id="appId",
            flow_id="flowId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        flow = await response.parse()
        assert_matches_type(FlowGetResponse, flow, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncOpenhermes) -> None:
        async with async_client.api.flow.with_streaming_response.get(
            app_id="appId",
            flow_id="flowId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            flow = await response.parse()
            assert_matches_type(FlowGetResponse, flow, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_services(self, async_client: AsyncOpenhermes) -> None:
        flow = await async_client.api.flow.get_services()
        assert_matches_type(FlowGetServicesResponse, flow, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get_services(self, async_client: AsyncOpenhermes) -> None:
        response = await async_client.api.flow.with_raw_response.get_services()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        flow = await response.parse()
        assert_matches_type(FlowGetServicesResponse, flow, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get_services(self, async_client: AsyncOpenhermes) -> None:
        async with async_client.api.flow.with_streaming_response.get_services() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            flow = await response.parse()
            assert_matches_type(FlowGetServicesResponse, flow, path=["response"])

        assert cast(Any, response.is_closed) is True
