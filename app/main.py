from fastapi import FastAPI

from app.email.router import router as email_router

app = FastAPI(title="Сервис по рассылке email")

app.include_router(email_router)
