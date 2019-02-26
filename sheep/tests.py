def test_read_yaml_file(sheep):
    data = sheep.read_yaml_file()
    assert isinstance(data, dict)
    assert data.get('compose_projects')
