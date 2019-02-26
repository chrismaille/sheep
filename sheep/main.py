import os
from pathlib import Path

import yaml


class Sheep:
    def __init__(self, config_file_path):
        self.config_file_path = config_file_path
        self.config = {}

    def read_config_file(self):
        file_path = Path(self.config_file_path).resolve()
        with open(file_path) as file:
            self.config = yaml.safe_load(file)

    def read_compose_file(self, project):
        compose_file_path = self.config['compose_projects'][project]['path']
        compose_file_list = self.config['compose_projects'][project]['files']
        for file in compose_file_list:
            file_path = Path(os.path.join(compose_file_path, file)).resolve()
