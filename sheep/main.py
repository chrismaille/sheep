from pathlib import Path

import yaml


class Sheep:
    def __init__(self, config_file_path):
        self.config_file_path = config_file_path

    def read_yaml_file(self):
        file_path = Path(self.config_file_path).resolve()
        with open(file_path) as file:
            data = yaml.safe_load(file)
        return data
