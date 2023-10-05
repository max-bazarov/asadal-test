import asyncio

import pytest
from fastapi.testclient import TestClient  # noqa
from httpx import AsyncClient

from app.main import app as fastapi_app


# Взято из документации к pytest-asyncio
@pytest.fixture(scope="session")
def event_loop(request):
    """Create an instance of the default event loop for each test case."""
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest.fixture(scope="function")
async def async_client():
    async with AsyncClient(
        app=fastapi_app, base_url="http://test"
    ) as async_client:
        yield async_client
