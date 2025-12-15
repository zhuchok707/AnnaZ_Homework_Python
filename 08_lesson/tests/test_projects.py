import uuid
import pytest
from api.projects_api import ProjectsAPI


@pytest.fixture
def projects_api(base_url, headers):
    return ProjectsAPI(base_url, headers)


@pytest.fixture
def created_project(projects_api):
    title = f"Test project {uuid.uuid4()}"
    response = projects_api.create_project(title)

    assert response.status_code == 201, response.text
    project_id = response.json()["id"]

    yield project_id
    # DELETE нет в API — данные остаются


# ---------- POST /projects ----------

def test_create_project_positive(projects_api):
    title = f"Positive project {uuid.uuid4()}"
    response = projects_api.create_project(title)

    assert response.status_code == 201, response.text
    assert "id" in response.json()


def test_create_project_negative(projects_api):
    response = projects_api.create_project("")

    assert response.status_code == 400


# ---------- PUT /projects/{id} ----------

def test_update_project_positive(projects_api, created_project):
    new_title = f"Updated project {uuid.uuid4()}"
    response = projects_api.update_project(created_project, new_title)

    assert response.status_code == 200, response.text
    assert "id" in response.json()


def test_update_project_negative(projects_api):
    response = projects_api.update_project("invalid_id", "Name")

    assert response.status_code == 404


# ---------- GET /projects/{id} ----------

def test_get_project_positive(projects_api, created_project):
    response = projects_api.get_project(created_project)

    assert response.status_code == 200, response.text
    assert response.json()["id"] == created_project


def test_get_project_negative(projects_api):
    response = projects_api.get_project("invalid_id")

    assert response.status_code == 404
