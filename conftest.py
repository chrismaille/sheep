import os

import pytest

from sheep.main import Sheep


def pytest_generate_tests(metafunc):
    """Tests Pre-Run."""
    os.environ['SHEEP_CONFIG_FILE_PATH'] = './example/sheep.yml'


@pytest.fixture
def sheep():
    config_file_path = os.getenv('SHEEP_CONFIG_FILE_PATH')
    sheep = Sheep(config_file_path)
    return sheep
