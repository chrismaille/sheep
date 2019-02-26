from sheep.main import Sheep


def test_read_yaml_file(sheep: Sheep):
    sheep.read_config_file()
    compose_data = sheep.config
    assert isinstance(compose_data, dict)
    assert compose_data.get('compose_projects')


def test_read_compose_data(sheep: Sheep):
    sheep.read_config_file()
    project = sheep.config['compose_projects'].keys()[0]
    data = sheep.read_compose_file(project)
    assert isinstance(data, dict)
