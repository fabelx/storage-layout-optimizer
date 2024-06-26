import json
from pathlib import Path

import pytest

TEST_DIR = Path(__file__).resolve().parent


def get_fixture_path(filename: str) -> Path:
    """Get path for a fixture file.

    Args:
        filename: Filename of file in fixtures/.

    Returns:
        str: Full path of file in fixtures/.
    """
    return TEST_DIR / "fixtures" / filename


def get_storage_layout(filename: str):
    filepath = get_fixture_path(filename=filename)
    with open(filepath) as f:
        storage_layout = json.load(f)

    return storage_layout


@pytest.fixture(scope="function")
def storage_layout(filename: str):
    return get_storage_layout(filename)


@pytest.fixture(scope="function")
def storage(storage_layout: dict):
    return storage_layout.get("storage")
