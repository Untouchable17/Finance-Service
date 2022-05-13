from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from workshop.api import router

origins = ["*"]

tags_metadata = [
    {
        "name": "auth",
        "description": "Авторизация и регистрация"
    },
    {
        "name": "operations",
        "description": "CRUD для операций с финансами"
    },
    {
        "name": "reports",
        "description": "Экспорт и импорт отчетов в csv файл"
    },
]

app = FastAPI(
    title="Blackout",
    description="Сервис учета личных финансов",
    version="17",
    openapi_tags=tags_metadata
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(router)

