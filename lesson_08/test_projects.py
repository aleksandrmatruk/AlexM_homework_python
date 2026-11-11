import os
import requests
from dotenv import load_dotenv

load_dotenv()

BASE_URL = "https://ru.yougile.com/api-v2"
TOKEN = os.getenv("YOUGILE_TOKEN")
HEADERS = {
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/json"
}


def test_create_project_positive():
    payload = {"title": "Мой тестовый проект"}
    response = requests.post(
        f"{BASE_URL}/projects", json=payload, headers=HEADERS
    )
    assert response.status_code == 201
    project_id = response.json()["id"]

    try:
        assert project_id is not None
    finally:
        requests.delete(f"{BASE_URL}/projects/{project_id}", headers=HEADERS)


def test_create_project_negative():
    payload = {}
    response = requests.post(
        f"{BASE_URL}/projects", json=payload, headers=HEADERS
    )
    assert response.status_code in (400, 422)
    assert "message" in response.json() or "error" in response.json()


def test_get_project_positive():
    payload = {"title": "Проект для GET-теста"}
    create_response = requests.post(
        f"{BASE_URL}/projects", json=payload, headers=HEADERS
    )
    assert create_response.status_code == 201
    project_id = create_response.json()["id"]

    try:
        get_response = requests.get(
            f"{BASE_URL}/projects/{project_id}", headers=HEADERS
        )
        assert get_response.status_code == 200
        assert get_response.json()["id"] == project_id
        assert "Проект для GET-теста" in get_response.json()["title"]
    finally:
        requests.delete(f"{BASE_URL}/projects/{project_id}", headers=HEADERS)


def test_get_project_negative():
    fake_id = "00000000-0000-0000-0000-000000000000"
    response = requests.get(
        f"{BASE_URL}/projects/{fake_id}", headers=HEADERS
    )
    assert response.status_code == 404


def test_update_project_positive():
    payload = {"title": "Старое название"}
    create_response = requests.post(
        f"{BASE_URL}/projects", json=payload, headers=HEADERS
    )
    assert create_response.status_code == 201
    project_id = create_response.json()["id"]

    try:
        update_payload = {"title": "Новое название"}
        update_response = requests.put(
            f"{BASE_URL}/projects/{project_id}",
            json=update_payload,
            headers=HEADERS
        )
        assert update_response.status_code == 200

        check_response = requests.get(
            f"{BASE_URL}/projects/{project_id}", headers=HEADERS
        )
        assert "Новое название" in check_response.json()["title"]
    finally:
        requests.delete(f"{BASE_URL}/projects/{project_id}", headers=HEADERS)


def test_update_project_negative():
    fake_id = "00000000-0000-0000-0000-000000000000"
    payload = {"title": "Попытка изменить несуществующий проект"}
    response = requests.put(
        f"{BASE_URL}/projects/{fake_id}",
        json=payload,
        headers=HEADERS
    )
    assert response.status_code == 404
