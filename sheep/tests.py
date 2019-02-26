from sheep.main import Sheep


def test_read_yaml_file(sheep: Sheep):
    sheep.read_config_file()
    compose_data = sheep.config
    assert isinstance(compose_data, dict)
    assert compose_data.get('compose_projects')
