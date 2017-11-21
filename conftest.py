import json
import os.path
import pytest
from fixture.application import Application


def pytest_addoption(parser):
    parser.addoption("--config", action="store", default="config.json")

@pytest.fixture()
def config(request):
    file_name = request.config.getoption("--config")
    file_name = os.path.join(os.path.dirname(os.path.abspath(__file__)), file_name)
    with open(file_name) as f:
        return json.loads(f)

@pytest.fixture(scope="session")
def app():
    fixture = Application()
    return fixture
