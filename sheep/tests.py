from sheep.main import Sheep


def test_read_yaml_file(sheep: Sheep):
    compose_data = sheep.read_config_file()
    assert isinstance(compose_data, dict)
    assert compose_data.get('compose_projects')
