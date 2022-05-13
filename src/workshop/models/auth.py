from pydantic import BaseModel


class BaseUser(BaseModel):
    """ Базовая модель юзера """

    email: str
    username: str


class UserCreate(BaseUser):
    """ Создание пользователя """

    password: str


class User(BaseUser):
    """ Модель юзера (наследуется от базовой) """

    id: int

    class Config:
        orm_mode = True


class Token(BaseModel):
    """ Модель токена """

    access_token: str
    token_type: str = "bearer"


