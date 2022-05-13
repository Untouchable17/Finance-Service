from typing import List, Optional

from fastapi import APIRouter
from fastapi import Depends
from fastapi import Response, status

from workshop.models.operations import (
    Operation, OperationKind, OperationCreate, OperationUpdate
)
from workshop.services.auth import get_current_user
from workshop.services.operations import OperationServices
from workshop.models.auth import User

router = APIRouter(
    prefix="/operations",
    tags=["operations"],

)


@router.get("/", response_model=List[Operation])
async def get_operations(
        kind: Optional[OperationKind] = None,
        user: User = Depends(get_current_user),
        service: OperationServices = Depends(),
):
    """ Получение всех транзакций """

    return await service.get_list(user_id=user.id, kind=kind)


@router.post("/", response_model=Operation)
async def create_operation(
        operation_data: OperationCreate,
        user: User = Depends(get_current_user),
        service: OperationServices = Depends()
):
    """ Создание транзакции """

    return await service.create(user_id=user.id, operation_data=operation_data)


@router.get("/{operation_id}/", response_model=Operation)
async def get_operation(
        operation_id: int,
        user: User = Depends(get_current_user),
        service: OperationServices = Depends()
):
    """ Получение одной транзакции """

    return await service.get(user_id=user.id, operation_id=operation_id)


@router.put("/{operation_id}/", response_model=Operation)
async def update_operation(
        operation_id: int,
        operation_data: OperationUpdate,
        user: User = Depends(get_current_user),
        service: OperationServices = Depends()
):
    """ Обновление транзакции """

    return await service.update(
        operation_id=operation_id,
        operation_data=operation_data,
        user_id=user.id
    )


@router.delete("/{operation_id}/")
async def delete_operation(
    operation_id: int,
    user: User = Depends(get_current_user),
    service: OperationServices = Depends()
):
    """ Удаление транзакции """

    await service.delete(user_id=user.id, operation_id=operation_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
