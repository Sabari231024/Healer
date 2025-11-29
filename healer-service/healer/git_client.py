import os, subprocess, requests
from .config import GIT_REPO_URL, GIT_CLONE_PATH, GIT_MAIN_BRANCH, GITHUB_TOKEN, GITHUB_API_URL, GITHUB_REPO_FULL

def run(cmd, cwd=None):
    p = subprocess.run(cmd, shell=True, cwd=cwd, capture_output=True, text=True)
    if p.returncode != 0:
        raise RuntimeError(p.stderr)
    return p.stdout

def ensure_repo_cloned():
    if not os.path.exists(GIT_CLONE_PATH):
        run(f"git clone {GIT_REPO_URL} {GIT_CLONE_PATH}")
    else:
        run("git fetch origin", cwd=GIT_CLONE_PATH)
        run(f"git checkout {GIT_MAIN_BRANCH}", cwd=GIT_CLONE_PATH)
        run(f"git pull origin {GIT_MAIN_BRANCH}", cwd=GIT_CLONE_PATH)

def create_branch(branch):
    run(f"git checkout -b {branch}", cwd=GIT_CLONE_PATH)

def commit_and_push(branch, msg):
    run("git add .", cwd=GIT_CLONE_PATH)
    run(f"git commit -m "{msg}"", cwd=GIT_CLONE_PATH)
    run(f"git push origin {branch}", cwd=GIT_CLONE_PATH)

def create_github_pr(branch, title, body):
    url = f"{GITHUB_API_URL}/repos/{GITHUB_REPO_FULL}/pulls"
    headers = {"Authorization": f"token {GITHUB_TOKEN}"}
    payload = {"title": title, "head": branch, "base": GIT_MAIN_BRANCH, "body": body}
    r = requests.post(url, json=payload, headers=headers)
    if r.status_code not in (200,201):
        raise RuntimeError(r.text)
    return r.json()
