from typing import List, Optional

from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException
from starlette import status

from workshop import tables
from workshop.database import get_session
from workshop.models.operations import (
    OperationKind, OperationCreate, OperationUpdate
)


class OperationServices:

    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    async def _get(self, user_id: int, operation_id: int) -> tables.Operation:
        """ Обработчик для получения одной транзакции  """

        operation = (self.session.query(tables.Operation).filter_by(
            id=operation_id, user_id=user_id).first())
        if not operation:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
        return operation

    async def get_list(
            self,
            user_id: int,
            kind: Optional[OperationKind] = None) -> List[tables.Operation]:
        """ Получение списка транзакций """

        query = self.session.query(tables.Operation).filter_by(user_id=user_id)
        if kind:
            query = query.filter_by(kind=kind)
        operations = query.all()

        return operations

    async def get(self, user_id: int, operation_id: int) -> tables.Operation:
        """ Получение одной транзакции из обработчика ._get """

        return await self._get(user_id, operation_id)

    async def create_many(
            self,
            user_id: int,
            operations_data: List[OperationCreate]
    ) -> List[tables.Operation]:
        """ Создание сразу нескольких транзакций """

        operations = [
            tables.Operation(**operation_data.dict(), user_id=user_id)
            for operation_data in operations_data
        ]
        self.session.add_all(operations)
        self.session.commit()
        return operations

    async def create(
            self,
            user_id: int,
            operation_data: OperationCreate
    ) -> tables.Operation:
        """ Создание одной транзакции """

        operation = tables.Operation(**operation_data.dict(), user_id=user_id)
        self.session.add(operation)
        self.session.commit()

        return operation

    async def update(
            self,
            user_id: int,
            operation_id: int,
            operation_data: OperationUpdate
    ) -> tables.Operation:
        """ Обновление данных в одной транзакции """

        operation = await self._get(user_id, operation_id)
        for field, value in operation_data:
            setattr(operation, field, value)
        self.session.commit()
        return operation

    async def delete(self, user_id: int, operation_id: int):
        """ Удаление транзакции """

        operation = await self._get(user_id, operation_id)
        self.session.delete(operation)
        self.session.commit()
