import os
from datetime import datetime
from .llm_client import generate_completion
from .git_client import ensure_repo_cloned, create_branch, commit_and_push, create_github_pr
from .config import GIT_CLONE_PATH
from .models import ErrorReport

PATCH_FILE = "app/logic.py"

async def process_error_and_create_pr(err: ErrorReport):
    ensure_repo_cloned()
    prompt = f"Fix this Python function:\nError: {err.exception_type}\nSource:\n{err.source_code}\n```python"
    patched = (await generate_completion(prompt)).strip()

    target = os.path.join(GIT_CLONE_PATH, PATCH_FILE)
    old = open(target).read()
    new = old.replace(err.source_code, patched) if err.source_code in old else old + "\n\n" + patched
    open(target, "w").write(new)

    branch = f"ai-fix-{err.function_name}-{datetime.utcnow().strftime('%Y%m%d%H%M%S')}"
    create_branch(branch)
    commit_and_push(branch, f"AI patch {err.function_name}")
    return create_github_pr(branch, f"AI Fix {err.function_name}", "Auto patch.")
