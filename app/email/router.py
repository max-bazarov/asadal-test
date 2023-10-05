from fastapi import APIRouter, Depends, status

from app.email.dependencies import email_service_factory
from app.email.schemas import EmailSchema
from app.email.service import EmailService

router = APIRouter(prefix="/email", tags=["Email"])


@router.post("/send_email", status_code=status.HTTP_200_OK)
async def send_email(
    email_data: EmailSchema,
    email_service: EmailService = Depends(email_service_factory),
) -> EmailSchema:
    email_service.send_email(email_data)

    return EmailSchema(**email_data.model_dump())
