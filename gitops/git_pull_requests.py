import json

from gitops.base import read_repos
from gitops.utils.github import init_github


def main():
    gh = init_github()
    repos = read_repos()

    pr_data = []
    for key, repo in repos.items():
        gh_repo = gh.get_repo(key)
        prs = gh_repo.get_pulls(state="open")

        for pr in prs:
            item = {
                "component": key,
                "title": pr.title,
                "target": pr.base.ref,
                "url": pr.html_url,
                "author": pr.user.login,
            }
            pr_data.append(item)

    with open("reports/pull_requests.json", "w") as json_file:
        json_file.write(json.dumps(pr_data))


if __name__ == "__main__":
    main()
