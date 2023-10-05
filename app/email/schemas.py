from pydantic import BaseModel, EmailStr, field_validator

from app.email.validators import validate_email


class EmailSchema(BaseModel):
    email: EmailStr
    subject: str
    message: str

    @field_validator("email")
    def validate_email(cls, email: str) -> str:
        validate_email(email)

        return email
