import csv
from typing import Any
from io import StringIO

from fastapi import Depends

from workshop.models.operations import OperationCreate, Operation
from workshop.services.operations import OperationServices


class ReportsService:

    def __init__(self, operation_service: OperationServices = Depends()):
        self.operation_service = operation_service

    async def csv_import(self, user_id: int, file: Any):
        """ Получение записей из csv файла """

        reader = csv.DictReader(
            (line.decode() for line in file),
            fieldnames=["date", "kind", "amount", "description"]
        )
        operations = []
        next(reader)    # пропускаем заголовок при импорте файла(csv)
        for row in reader:
            operation_data = OperationCreate.parse_obj(row)
            if operation_data.description == "":
                operation_data.description = None
            operations.append(operation_data)
        await self.operation_service.create_many(user_id, operations)

    async def export_csv(self, user_id: int) -> Any:

        output = StringIO()
        writer = csv.DictWriter(
             output,
             fieldnames=["date", "kind", "amount", "description"],
             extrasaction="ignore",
        )

        operations = await self.operation_service.get_list(user_id)
        writer.writeheader()
        for operation in operations:
            operation_data = Operation.from_orm(operation)
            writer.writerow(operation_data.dict())

        output.seek(0)
        return output
