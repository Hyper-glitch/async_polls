import pathlib

import yaml

BASE_DIR = pathlib.Path(__file__).parent.parent
config_path = BASE_DIR / 'config' / 'polls.yaml'


def get_config(path):
    with open(path) as file:
        return yaml.safe_load(file)


postgres_config = get_config(config_path)
