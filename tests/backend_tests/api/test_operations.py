import pytest
from httpx import AsyncClient

JWT_TOKEN = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE2NTI0NTI0MzYsIm5iZiI6MTY1MjQ1MjQzNiwiZXhwIjoxNjUyNDU2MDM2LCJzdWIiOiIxIiwidXNlciI6eyJlbWFpbCI6InR5bGVyYmxhY2tvdXQxN0BnbWFpbC5jb20iLCJ1c2VybmFtZSI6InNlY2RldDE3IiwiaWQiOjF9fQ.KB7g0VVQ0QPI1fmrdKkLXfokKUcfofUbSKqOMDLhGTk'

HEADERS = {'Content-Type': 'multipart/form-data', 'Authorization': f'Bearer {JWT_TOKEN}'}


@pytest.mark.anyio
async def test_get_operations():
    """ Тест на получение всех транзакций """

    async with AsyncClient(headers=HEADERS) as operation:
        response = await operation.get("http://127.0.0.1:666/operations/")
    assert response.status_code == 200


@pytest.mark.anyio
async def test_get_operation():
    """
        Тест на получение конкретной транзакции
        в response.json() проверяются данные, которые должны вернуться
    """

    async with AsyncClient(headers=HEADERS) as operation:
        response = await operation.get("http://127.0.0.1:666/operations/1/")
    assert response.status_code == 200
    assert response.json() == {
        "date": "2022-05-12",
        "kind": "income",
        "amount": 12000,
        "description": "operation updated in the pytest",
        "id": 1
    }


@pytest.mark.anyio
async def test_get_type_operations():
    """
        Тест на получение транзакций по фильтру /?kind=
        фильтры по типам: income (доход) и outcome (расход)
    """

    async with AsyncClient(headers=HEADERS) as ac:
        response = await ac.get("http://127.0.0.1:666/operations/?kind=outcome")
    assert response.status_code == 200


@pytest.mark.anyio
async def test_create_operation():
    """ Тест на создание транзакции """

    headers = {'Content-Type': 'application/json', 'Authorization': f'Bearer {JWT_TOKEN}'}
    json = {
        "date": "2022-05-12",
        "kind": "income",
        "amount": 777,
        "description": "operation created in the pytest"
    }

    async with AsyncClient(headers=headers) as ac:
        response = await ac.post("http://127.0.0.1:666/operations/", headers=headers, json=json)
    assert response.status_code == 200


@pytest.mark.anyio
async def test_update_operation():
    """ Тест на обновление транзакции """

    headers = {'Content-Type': 'application/json', 'Authorization': f'Bearer {JWT_TOKEN}'}
    json = {
        "date": "2022-05-12",
        "kind": "income",
        "amount": 12000,
        "description": "operation updated in the pytest"
    }

    async with AsyncClient(headers=headers) as ac:
        operation_id: int = 2
        response = await ac.put(f"http://127.0.0.1:666/operations/{operation_id}/", headers=headers, json=json)
    assert response.status_code == 200


@pytest.mark.anyio
async def test_delete_operation():
    """ Тест на удаление транзакции """

    headers = {'Content-Type': 'application/json', 'Authorization': f'Bearer {JWT_TOKEN}'}

    async with AsyncClient(headers=headers) as ac:
        response = await ac.delete("http://127.0.0.1:666/operations/18/", headers=headers)
    assert response.status_code == 204

