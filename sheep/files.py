from pathlib import Path

import yaml


def read_yaml_file(config_file_path):
    file_path = Path(config_file_path).resolve()
    with open(file_path) as file:
        data = yaml.safe_load(file)
    return data