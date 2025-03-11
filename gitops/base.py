import os

from ruamel.yaml import YAML

yaml = YAML()


REPOS_DIR_PATH = "data/repos"

def read_repos():
    items = []
    for filename in os.listdir(REPOS_DIR_PATH):
        with open(os.path.join(REPOS_DIR_PATH, filename), "r") as f:
            items.append(yaml.load(f.read()))

    repos = {}
    for item in items:
        item_key = item["key"]
        if item_key in repos:
            raise ValueError(f"Duplicate key value found: {item_key}")
        repos[item_key] = item

    return repos
