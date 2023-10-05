import smtplib
from email.errors import MessageError
from email.message import EmailMessage

from app.email.config import email_config
from app.logger import logger
from app.tasks.celery import celery


@celery.task
def create_sending_email_task(
    email: EmailMessage,
):
    with smtplib.SMTP_SSL(
        email_config.MAIL_SERVER, email_config.MAIL_PORT
    ) as server:
        try:
            server.login(
                email_config.MAIL_USERNAME, email_config.MAIL_PASSWORD
            )
            server.send_message(email)
            logger.info(
                "Message was sent",
                exc_info=True,
            )

        except (MessageError, Exception) as e:
            if isinstance(e, MessageError):
                msg = "Email Exc: Cannot send message"
            elif isinstance(e, Exception):
                msg = "Uknown Exc: Cannot send message"

            logger.error(msg, exc_info=True)
