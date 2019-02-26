import os
from pathlib import Path

import yaml


class Sheep:
    def __init__(self, config_file_path):
        self.config_file_path = config_file_path
        self.sheep_config = {}

    def read_config_file(self):
        file_path = Path(self.config_file_path).resolve()
        with open(file_path) as file:
            self.sheep_config = yaml.safe_load(file)
        return self.sheep_config

    def read_compose_file(self, project):
        compose_file_path = self.config_sheep['compose_projects'][project]['path']
        compose_file_list = self.config_sheep['compose_projects'][project]['files']
        for file in compose_file_list:
            file_path = Path(os.path.join(compose_file_path, file)).resolve()
