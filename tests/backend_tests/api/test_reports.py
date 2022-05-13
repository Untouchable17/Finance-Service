import pytest
from httpx import AsyncClient

JWT_TOKEN = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE2NTI0NTI0MzYsIm5iZiI6MTY1MjQ1MjQzNiwiZXhwIjoxNjUyNDU2MDM2LCJzdWIiOiIxIiwidXNlciI6eyJlbWFpbCI6InR5bGVyYmxhY2tvdXQxN0BnbWFpbC5jb20iLCJ1c2VybmFtZSI6InNlY2RldDE3IiwiaWQiOjF9fQ.KB7g0VVQ0QPI1fmrdKkLXfokKUcfofUbSKqOMDLhGTk'

HEADERS = {'Content-Type': 'application/json', 'Authorization': f'Bearer {JWT_TOKEN}'}


@pytest.mark.anyio
async def test_export_file():
    """ Импорт транзакций в файл """

    async with AsyncClient(headers=HEADERS) as ac:
        response = await ac.get("http://127.0.0.1:666/reports/export")
    assert response.status_code == 200
