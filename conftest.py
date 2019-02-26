import os


def pytest_generate_tests(metafunc):
    """Tests Pre-Run."""
    os.environ['SHEEP_CONFIG_FILE_PATH'] = './example/sheep.yml'
