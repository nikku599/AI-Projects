# AI-Projects
A collection of AI projects by nikku599 — compact, practical demos and agent templates.

## Projects (Overview)
A short index of projects in this repository. Expand each section for: what the project does, skills & concepts used, and how it works.

### Professionally_You
What it does
- A conversational AI assistant that emulates a professional's tone and knowledge based on a LinkedIn PDF and a short personal summary. Designed for embedding on a personal site to answer visitor questions and capture leads.

Skills & concepts
- Prompt engineering and persona design
- Document ingestion and retrieval (PDF parsing, embeddings)
- Context management across multi-turn conversations
- Tooling via function calls to capture contact info and log unknowns
- Notification integration (Pushover)

How it works (high level)
1. Loads `me/linkedin.pdf` and `me/summary.txt` and extracts relevant text.
2. Creates a system prompt that frames the assistant as the professional.
3. Uses the OpenAI API to generate responses, leveraging retrieved context for accuracy.
4. When user intent indicates contact info, invokes tools to store details and sends Pushover notifications for follow-up.
5. Unknown or out-of-scope questions are logged for later fine-tuning.

Requirements & files
- OpenAI API key
- Pushover account (optional for notifications)
- `me/linkedin.pdf` and `me/summary.txt`
- See project files in the repository root for runnable scripts and evaluation logic.

---

### Todos Agent Loop
What it does
- A simple problem-solving agent that plans by creating a todo list, executes tasks step-by-step (via tool calls), and returns a consolidated answer. Useful as a template for structured agent workflows.

Skills & concepts
- Agent design and loop control
- OpenAI function-calling API for structured tool interactions
- Task decomposition and state tracking
- Console output formatting with Rich

How it works (high level)
1. Receives a user problem and system instructions.
2. Requests a plan from the model and converts the plan into todos.
3. Executes each todo by calling helper functions/tools and appending completion notes.
4. Continues the loop until the model signals completion, then prints the final answer with Rich formatting.

Requirements & files
- OpenAI API key (via `.env`)
- Python packages: `openai`, `python-dotenv`, `rich`
- Run as a script or notebook — customize `user_message`/`system_message` to adapt the scenario.

---

### Coder Crew (CrewAI)
What it does
- A multi-agent template for coding and research tasks. Agents collaborate to research, draft, and produce artifacts (e.g., `report.md`) according to configured tasks.

Skills & concepts
- Multi-agent coordination and role definition
- Configuration-driven workflows (YAML for agents/tasks)
- CLI orchestration with crewAI
- Environment, dependency, and secret management

How it works (high level)
1. Define agents and tasks in `src/coder/config/agents.yaml` and `src/coder/config/tasks.yaml`.
2. Start the crew with `crewai run` — the crew orchestrator spawns agents, assigns tasks, and manages tool use and handoffs.
3. Agents use configured tools and prompts to research and generate outputs. The example creates a `report.md` in the project root.

Requirements & files
- Python 3.10–3.13
- `uv` (or pip-managed crewAI) and crewAI installed
- `OPENAI_API_KEY` set in `.env`
- See `CrewAI Projects/coder/README.md` for full setup and examples.

---

### Debate Crew (CrewAI)
What it does
- A multi-agent debate and analysis template that runs structured argumentation workflows and produces research or position outputs.

Skills & concepts
- Structured debate and role-based argument generation
- Multi-agent coordination and conflict-resolution strategies
- Prompt engineering for differing viewpoints
- Configuration-driven task orchestration

How it works (high level)
1. Configure debate roles and debate tasks in `src/debate/config/`.
2. Run `crewai run` to start the debate crew; agents assume roles (pro/con/moderator) and exchange arguments.
3. The crew compiles the debate into a final document or report (example: `report.md`).

Requirements & files
- Python 3.10–3.13
- `uv` and crewAI
- `OPENAI_API_KEY` in `.env`
- See `CrewAI Projects/debate/README.md` for full setup and examples.

---

## Quick start
1. Add your OpenAI API key to `.env` (OPENAI_API_KEY).
2. For CrewAI projects: install crewAI/uv and run `crewai install` then `crewai run` inside the project folder.
3. For the root projects: open the Python scripts or notebooks and run them after setting the required environment variables.

Contributions and issues welcome — open a GitHub issue if you find bugs or want improvements.
