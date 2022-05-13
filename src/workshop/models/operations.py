from datetime import date
from decimal import Decimal
from typing import Optional
from enum import Enum

from pydantic import BaseModel


class OperationKind(str, Enum):
    """ Тип транзакции (доход/расход) """

    INCOME = "income"
    OUTCOME = "outcome"


class OperationBase(BaseModel):
    """ Базовая модель транзакций """

    date: Optional[date]
    kind: Optional[OperationKind]
    amount: Optional[Decimal]
    description: Optional[str]


class Operation(OperationBase):
    """ Сериализатор транзакций """

    id: int

    class Config:
        orm_mode = True


class OperationCreate(OperationBase):
    """ Сериализатор создания транзакции """
    pass


class OperationUpdate(OperationBase):
    """ Сериализатор для обновления транзакции """
    pass