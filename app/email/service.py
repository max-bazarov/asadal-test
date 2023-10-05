from email.message import EmailMessage
from pathlib import Path

from celery.exceptions import CeleryError
from jinja2 import Environment, FileSystemLoader
from pydantic import EmailStr

from app.email.config import email_config
from app.email.schemas import EmailSchema
from app.logger import logger
from app.tasks.tasks import create_sending_email_task

env = Environment(loader=FileSystemLoader(Path(__file__).parent / "templates"))


class EmailService:
    def _create_email(
        self, email_address: EmailStr, subject: str, message: str
    ):
        body = {"message": message}

        template = env.get_template("email.html")
        rendered_content = template.render(**body)

        email = EmailMessage()
        email["Subject"] = subject
        email[
            "From"
        ] = f"{email_config.MAIL_FROM_NAME} <{email_config.MAIL_FROM}>"
        email["To"] = email_address
        email.set_content(rendered_content, subtype="html")

        return email

    def send_email(self, email_data: EmailSchema):
        email = self._create_email(
            email_address=email_data.email,
            subject=email_data.subject,
            message=email_data.message,
        )

        try:
            create_sending_email_task(email)
            extra = {**email_data.model_dump()}
            extra["email_message"] = extra.pop("message")
            logger.info("Email task was created", extra=extra)

        except (CeleryError, Exception) as e:
            if isinstance(e, CeleryError):
                msg = "Celery Exc: Cannot create task"
            elif isinstance(e, Exception):
                msg = "Uknown Exc: Cannot create task"

            extra = {**email_data.model_dump()}
            extra["email_message"] = extra.pop("message")
            logger.error(msg, extra=extra, exc_info=True)
