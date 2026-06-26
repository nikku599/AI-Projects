# AI-Projects
A collection of AI projects by nikku599 — compact, practical demos and agent templates.

## Projects

### Professionally_You
A concise conversational AI that represents a professional profile on a personal site. It uses your LinkedIn PDF and a short summary to craft context-aware responses.
- Key features: LinkedIn-based persona, contact capture tools, unknown-question logging, Pushover notifications, Gradio UI, response evaluation.
- See the code and configuration in the repository root.

### Todos Agent Loop
A simple agent that plans with a todo list, executes steps via tool calls, and returns a final answer.
- Key features: todo-based planning, function-calling tools (create/mark todos), sequential execution loop, Rich-formatted console output.
- Runs as a script/notebook using OpenAI function-calling APIs.

### Coder Crew (CrewAI)
Multi-agent coder template powered by crewAI. Agents collaborate on coding and research tasks.
- Key features: configurable agents/tasks (src/coder/config), CLI: `crewai run` creates a report (e.g., report.md).
- Requirements: Python 3.10–3.13, crewAI/uv, set `OPENAI_API_KEY` in `.env`.
- See: `CrewAI Projects/coder/README.md` for full setup and usage.

### Debate Crew (CrewAI)
Multi-agent debate template powered by crewAI for structured argumentation and research workflows.
- Key features: configurable agents/tasks (src/debate/config), CLI: `crewai run` to execute example scenarios.
- Requirements: Python 3.10–3.13, crewAI/uv, set `OPENAI_API_KEY` in `.env`.
- See: `CrewAI Projects/debate/README.md` for full setup and usage.

## Quick start
1. Add your OpenAI API key to `.env` (OPENAI_API_KEY).
2. For CrewAI projects: install crewAI/uv and run `crewai install` then `crewai run` inside the project folder.
3. For the root projects: follow the inline comments and run the Python scripts/notebooks.

Contributions and issues welcome — open a GitHub issue if you find bugs or want improvements.
