#  Self-Healing AI System
### AI-Driven Autonomous Bug Detection, Patch Generation & Git-Based Auto-Repair

This project implements a full **AI-augmented self-healing software pipeline** using:

- **Qwen2.5-Coder-1.5B (lightweight on-device LLM)**
- **FastAPI** for application & services
- **Automated Git branch creation**
- **Automated Pull-Request (PR) generation**
- **Developer-in-the-loop approval**
- **Automatic production updates after merge**

The system autonomously detects runtime failures in a running service, analyzes the root cause, generates an optimized fix using a local LLM, and submits the fix as a **Pull Request** for human review.  
Once merged, the system automatically pulls the latest code and updates the application.

---

#  Purpose

Software systems frequently crash due to:

- unhandled edge cases  
- incorrect inputs  
- library regressions  
- inconsistent environments  
- human mistakes  

Traditional debugging is:

- slow  
- manual  
- costly  
- dependent on availability  

This system aims to provide an **intelligent auto-repair pipeline** that:

1. Watches for runtime errors  
2. Generates a patch using an on-device LLM  
3. Creates a Git branch & Pull Request  
4. Allows developers to review and merge  
5. Automatically updates the live app  

This creates a **continuous self-healing feedback loop** with full human oversight.

---

#  Key Features

✔ Autonomous runtime error detection  
✔ AI-driven patch generation  
✔ Git-based workflow with PR automation  
✔ Human-in-the-loop safety  
✔ Automatic post-merge app updates  
✔ Fully local & secure  
✔ Works across multiple microservices  

---

#  Architecture Overview

```
               ┌──────────────────────┐
               │    App Service       │
               │ (FastAPI / Flask)    │
               └──────────┬───────────┘
                          │ Error Report
                          ▼
               ┌──────────────────────┐
               │   Healer Service     │
               │ AI Coordinator       │
               └──────────┬───────────┘
                          │ Prompt
                          ▼
             ┌──────────────────────────┐
             │     LLM Service          │
             │ Qwen2.5-Coder-1.5B API   │
             └──────────┬──────────────┘
                          │ Patch
                          ▼
               ┌──────────────────────┐
               │    Git Repository    │
               │ Pull Request Raised  │
               └──────────┬───────────┘
                          │ Merge
                          ▼
               ┌──────────────────────┐
               │  Healer Auto-Updates │
               │  App After Merge     │
               └──────────────────────┘
```

---

#  Advantages Over Traditional Approaches

###  1. Faster MTTR  
Repairs happen in minutes instead of hours/days.

###  2. AI understands context  
Reads source code + traceback + arguments.

###  3. PR-based workflow  
Ensures safety and human oversight.

###  4. Continuous improvement  
System evolves with each merge.

###  5. Secure and offline  
LLM runs locally inside a controlled environment.

---

#  Folder Structure

```
self-healing-system/
├── docker-compose.yml
├── app-service/
├── healer-service/
└── llm-service/
```

---

#  Installation & Setup

```
git clone <repo>
cd self-healing-system
docker-compose up --build
```

Ensure the Qwen model exists at:

```
models/qwen2.5-coder-1.5b-q4.gguf
```

---

#  How It Works

1. App triggers an exception  
2. Error sent to healer-service  
3. LLM generates patch  
4. Git branch created  
5. PR is opened  
6. Developer approves  
7. Healer pulls & updates code  

---

#  Early Development Disclaimer

This system is **in early stages**.  
Multiple components such as:

- sandboxed testing  
- AST-level patching  
- multi-language support  
- CI/CD integration  

…are still under active development.

The current version is **experimental** and not production-ready.

---

# License
MIT License
