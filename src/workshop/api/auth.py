from typing import Union, Any

from fastapi import APIRouter, Depends, status
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.responses import JSONResponse

from workshop.models.auth import UserCreate, Token
from workshop.services.auth import AuthService, check_jwt_token

router = APIRouter(
    prefix="/auth",
    tags=["auth"],
)


@router.get("/validate", response_model=Token)
async def get_user_info(
        token_data: Union[str, Any] = Depends(check_jwt_token)
) -> Any:
    """ УРЛ для получения информации о юзере """

    return JSONResponse(status_code=status.HTTP_200_OK, content=token_data)


@router.post("/sign-up", response_model=Token)
async def sign_up(user_data: UserCreate, service: AuthService = Depends()):
    """ УРЛ для регистрации """

    return await service.register_new_user(user_data)


@router.post("/sign-in", response_model=Token)
async def sing_in(
        form_data: OAuth2PasswordRequestForm = Depends(),
        service: AuthService = Depends()
):
    """ УРЛ для авторизации """
    return await service.authenticate_user(form_data.username, form_data.password)


