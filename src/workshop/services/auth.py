from typing import Optional, Union, Any
from datetime import datetime, timedelta

from fastapi import Header
from fastapi import HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from passlib.hash import bcrypt
from pydantic import ValidationError
from sqlalchemy.orm import Session
from starlette import status

from workshop.database import get_session
from workshop.models.auth import User, Token, UserCreate
from workshop.settings import settings
from workshop import tables


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/sign-in")


async def get_current_user(token: str = Depends(oauth2_scheme)) -> User:
    return await AuthService.validate_token(token)


async def check_jwt_token(
        token: Optional[str] = Header(None)) -> Union[str, Any]:
    """ Проверка JWT токена на валидность """

    exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={
            "WWW-Authenticate": "Bearer"
        }
    )

    try:
        payload = jwt.decode(
            token, settings.jwt_secret, algorithms=[settings.jwt_algorithm]
        )
        return payload
    except (jwt.JWTError, jwt.ExpiredSignatureError, AttributeError):
        raise exception from None


class AuthService:

    @classmethod
    def verify_password(
            cls,
            plain_password: str,
            hashed_password: str) -> bool:
        """ Проверка пароля и хэша """
        return bcrypt.verify(plain_password, hashed_password)

    @classmethod
    def hash_password(cls, password: str) -> str:
        """ Хэширование пароля """
        return bcrypt.hash(password)

    @classmethod
    async def validate_token(cls, token: str) -> User:
        """ Валидация токена """
        exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={
                "WWW-Authenticate": "Bearer"
            }
        )
        try:
            # расшифровка токена и его подлинность
            payload = jwt.decode(
                token, settings.jwt_secret, algorithms=[settings.jwt_algorithm]
            )
        except JWTError:
            raise exception from None

        user_data = payload.get("user")  # достаем поле user из токена
        try:
            user = User.parse_obj(user_data)
        except ValidationError:
            raise exception from None
        return user

    @classmethod
    async def create_token(cls, user: tables.User) -> Token:
        """
            Создание токена и передача сериализованных полей таблицы user
            В токене будет вся необходимая информация о пользователе
        """

        user_data = User.from_orm(user)
        time_now = datetime.utcnow()

        payload = {
            "iat": time_now,
            "nbf": time_now,
            "exp": time_now + timedelta(seconds=settings.jwt_expiration),
            "sub": str(user_data.id),
            "user": user_data.dict(),
        }
        token = jwt.encode(
            payload,
            settings.jwt_secret,
            algorithm=settings.jwt_algorithm
        )
        return Token(access_token=token)

    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    async def register_new_user(self, user_data: UserCreate) -> Token:
        """ Авторизация токена сразу после регистрации """

        user = tables.User(
            email=user_data.email,
            username=user_data.username,
            password_hash=self.hash_password(user_data.password),
        )

        self.session.add(user)
        self.session.commit()

        return await self.create_token(user)  # возвращаем токен юзера

    async def authenticate_user(self, username: str, password: str):
        """ Авторизация пользователя """

        exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={
                "WWW-Authenticate": "Bearer",
            }
        )

        user = (
            self.session.query(tables.User).filter(
                tables.User.username == username).first()
        )

        if not user:
            raise exception

        if not self.verify_password(password, user.password_hash):
            raise exception

        return await self.create_token(user)
