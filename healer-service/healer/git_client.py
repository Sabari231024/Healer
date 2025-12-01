import os
import subprocess
import requests
import shutil
from .config import (
    GIT_REPO_URL,
    GIT_CLONE_PATH,
    GIT_MAIN_BRANCH,
    GITHUB_TOKEN,
    GITHUB_API_URL,
    GITHUB_REPO_FULL
)

def run(cmd, cwd=None):
    p = subprocess.run(cmd, shell=True, cwd=cwd, capture_output=True, text=True)
    if p.returncode != 0:
        raise RuntimeError(f"Command failed: {cmd}\n{p.stderr}")
    return p.stdout


def ensure_repo_cloned():
    """
    Safely ensures the repo is cloned.
    Handles all cases:
    - /repo does not exist
    - /repo exists but empty
    - /repo exists but not a git repo
    - /repo exists and is a git repo
    """

    # CASE 1 — folder does not exist
    if not os.path.exists(GIT_CLONE_PATH):
        os.makedirs(os.path.dirname(GIT_CLONE_PATH), exist_ok=True)
        run(f"git clone {GIT_REPO_URL} {GIT_CLONE_PATH}")
        return

    # CASE 2 — folder exists but empty
    if len(os.listdir(GIT_CLONE_PATH)) == 0:
        run(f"git clone {GIT_REPO_URL} {GIT_CLONE_PATH}")
        return

    # CASE 3 — folder exists but no .git directory
    if not os.path.exists(os.path.join(GIT_CLONE_PATH, ".git")):
        # wipe folder and clone fresh
        shutil.rmtree(GIT_CLONE_PATH)
        run(f"git clone {GIT_REPO_URL} {GIT_CLONE_PATH}")
        return

    # CASE 4 — valid repo → fetch and sync with remote
    run("git fetch origin", cwd=GIT_CLONE_PATH)
    run(f"git checkout {GIT_MAIN_BRANCH}", cwd=GIT_CLONE_PATH)
    run(f"git reset --hard origin/{GIT_MAIN_BRANCH}", cwd=GIT_CLONE_PATH)


def create_branch(branch):
    run(f"git checkout -b {branch}", cwd=GIT_CLONE_PATH)


def commit_and_push(branch, msg):
    run("git add .", cwd=GIT_CLONE_PATH)

    # avoid failure when there is nothing to commit
    try:
        run(f'git commit -m "{msg}"', cwd=GIT_CLONE_PATH)
    except RuntimeError as e:
        if "nothing to commit" not in str(e).lower():
            raise e

    run(f"git push origin {branch}", cwd=GIT_CLONE_PATH)


def create_github_pr(branch, title, body):
    url = f"{GITHUB_API_URL}/repos/{GITHUB_REPO_FULL}/pulls"
    headers = {"Authorization": f"token {GITHUB_TOKEN}"}
    payload = {"title": title, "head": branch, "base": GIT_MAIN_BRANCH, "body": body}

    r = requests.post(url, json=payload, headers=headers)

    if r.status_code not in (200, 201):
        raise RuntimeError(f"GitHub PR creation failed:\n{r.text}")

    return r.json()
