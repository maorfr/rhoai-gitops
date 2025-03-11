import os

from github import Github


def init_github():
    return Github(os.environ["GITHUB_TOKEN"])
