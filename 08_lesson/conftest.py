import os
import pytest


@pytest.fixture(scope="session")
def base_url():
    return "https://ru.yougile.com/api-v2"


@pytest.fixture(scope="session")
def headers():
    token = os.getenv("YOUGILE_TOKEN")
    if not token:
        raise RuntimeError(
            "Не задана переменная окружения YOUGILE_TOKEN"
        )

    return {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
    }
