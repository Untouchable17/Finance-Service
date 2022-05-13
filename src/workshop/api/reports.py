from fastapi import APIRouter, UploadFile, File, Depends, BackgroundTasks
from fastapi.responses import StreamingResponse

from workshop.models.auth import User
from workshop.services.auth import get_current_user
from workshop.services.reports import ReportsService


router = APIRouter(
    prefix="/reports",
    tags=["reports"],

)


@router.post("/import")
async def csv_import(
        background_tasks: BackgroundTasks,
        file: UploadFile = File(...),
        user: User = Depends(get_current_user),
        reports_service: ReportsService = Depends(),
):
    """ Импорт транзакций из csv файла """

    background_tasks.add_task(
        reports_service.csv_import,
        user.id, file.file
    )


@router.get("/export")
async def export_csv(
        user: User = Depends(get_current_user),
        reports_service: ReportsService = Depends()
):
    """ Экспорт транзакицй в csv файл """
    report = await reports_service.export_csv(user.id)
    return StreamingResponse(
        report, media_type="text/csv",
        headers={
            "Content-Disposition": "attachment; filename=report.csv"
        }
    )