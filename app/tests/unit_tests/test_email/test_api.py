import pytest
from httpx import AsyncClient
from pydantic import EmailStr


@pytest.mark.parametrize(
    "email, subject, message, status_code",
    [
        ("example@example.com", "Test subject", "Test message", 200),
        ("wrongemail", "Test subject", "Test message", 422),
    ],
)
async def test_send_email(
    email: EmailStr,
    subject: str,
    message: str,
    status_code: int,
    async_client: AsyncClient,
):
    response = await async_client.post(
        "/email/send_email",
        json={"email": email, "subject": subject, "message": message},
    )

    assert response.status_code == status_code
