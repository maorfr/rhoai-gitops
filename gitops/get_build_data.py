import json

from gitops.base import read_repos
from gitops.utils.github import init_github


def main():
    gh = init_github()
    repos = read_repos()

    build_data = []
    for key, repo in repos.items():
        gh_repo = gh.get_repo(key)
        for b in repo["branches"]:
            ref = b["branch"]
            commit = gh_repo.get_commit(ref)
            runs = commit.get_check_runs()
            for r in runs:
                item = {
                    "component": key,
                    "branch": ref,
                    "commit": commit.sha,
                    "status": r.conclusion,
                    "url": r.details_url,
                }
                build_data.append(item)

    with open("reports/build_data.json", "w") as json_file:
        json_file.write(json.dumps(build_data))


if __name__ == "__main__":
    main()
