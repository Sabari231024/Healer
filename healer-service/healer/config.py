import os
GIT_REPO_URL = os.getenv("GIT_REPO_URL")
GIT_MAIN_BRANCH = os.getenv("GIT_MAIN_BRANCH", "main")
GIT_CLONE_PATH = os.getenv("GIT_CLONE_PATH", "/repo")
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
GITHUB_API_URL = "https://api.github.com"
GITHUB_REPO_FULL = os.getenv("GITHUB_REPO_FULL")
LLM_SERVICE_URL = os.getenv("LLM_SERVICE_URL")
