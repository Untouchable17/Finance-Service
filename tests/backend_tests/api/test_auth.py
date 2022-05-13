import pytest
import requests
from httpx import AsyncClient

JWT_TOKEN = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE2NTI0NTI0MzYsIm5iZiI6MTY1MjQ1MjQzNiwiZXhwIjoxNjUyNDU2MDM2LCJzdWIiOiIxIiwidXNlciI6eyJlbWFpbCI6InR5bGVyYmxhY2tvdXQxN0BnbWFpbC5jb20iLCJ1c2VybmFtZSI6InNlY2RldDE3IiwiaWQiOjF9fQ.KB7g0VVQ0QPI1fmrdKkLXfokKUcfofUbSKqOMDLhGTk'


@pytest.mark.anyio
async def test_auth_validate_token():
    """ Тест на валидацию токена и получение информации о юзере """

    headers = {'Content-Type': 'application/json', 'Token': f'{JWT_TOKEN}'}

    async with AsyncClient(headers=headers) as ce:
        response = await ce.get("http://127.0.0.1:666/auth/validate")
    assert response.status_code == 200
    assert response.json() == {
        "iat": 1652452436,
        "nbf": 1652452436,
        "exp": 1652456036,
        "sub": "1",
        "user": {
            "email": "tylerblackout17@gmail.com",
            "username": "secdet17",
            "id": 1
        }
    }


@pytest.mark.anyio
def test_sign_in():
    """ Тест авторизации и получение jwt токена """

    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    data = {
        "username": "secdet17",
        "password": "qwerty1234"
    }

    response = requests.post("http://127.0.0.1:666/auth/sign-in", headers=headers, data=data)
    assert response.status_code == 200


@pytest.mark.anyio
def test_sign_up():
    """ Тест регистрации """

    headers = {'Content-Type': 'application/json'}
    json = {
        "email": "test1@gmail.com",
        "username": "testuser1",
        "password": "testuser1"
    }

    response = requests.post("http://127.0.0.1:666/auth/sign-up", headers=headers, json=json)
    assert response.status_code == 200
