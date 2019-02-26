import os

from sheep.files import read_yaml_file


def test_read_yaml_file():
    config_file_path = os.getenv('SHEEP_CONFIG_FILE_PATH')
    data = read_yaml_file(config_file_path)
    assert isinstance(data, dict)
    assert data.get('compose_projects')
