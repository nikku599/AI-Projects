# AI-Projects
This repo contains AI projects built by me, including a professional chatbot and a todo-based agent loop.

## Professionally_You

A conversational AI chatbot that represents a professional on their personal website. This project uses OpenAI's GPT-4 API to create an intelligent assistant that can answer questions about a person.

### Features

- **Professional Representation**: The chatbot acts as you, answering questions based on your LinkedIn profile and personal summary
- **Tool Integration**: Equipped with custom tools to:
  - Record user contact information (email, name, notes) for follow-up
  - Log unknown questions for continuous improvement
- **Pushover Notifications**: Real-time notifications when users interact with the chatbot
- **Gradio Interface**: User-friendly chat interface for seamless conversations
- **Context-Aware Responses**: Uses your LinkedIn profile and summary to provide accurate, personalized responses
- **Response Evaluation System**: Integrated Pydantic-based evaluation system to assess response quality and provide structured feedback

### How It Works

1. Loads your LinkedIn profile (PDF) and professional summary (text file)
2. Creates a system prompt that represents you professionally
3. Uses GPT-4 Mini for intelligent, natural conversations
4. Evaluates response quality using a structured evaluation system
5. Attempts to collect user contact information through conversation
6. Sends notifications via Pushover when important interactions occur

### Requirements

- OpenAI API key
- Pushover account (for notifications)
- PDF of LinkedIn profile (`me/linkedin.pdf`)
- Text file with professional summary (`me/summary.txt`)
- Pydantic (for response evaluation)

### Usage

The chatbot launches with an initial greeting and handles multi-turn conversations, automatically processing tool calls for recording user details and questions. Response quality is evaluated using the integrated evaluation system with Pydantic models for structured feedback.

## Todos Agent Loop

An AI agent that solves problems by planning with a todo list, executing each step via tool calls, and returning a final answer. Built with OpenAI's function-calling API and a simple agent loop.

### Features

- **Todo-Based Planning**: The agent creates a step-by-step todo list before solving a problem
- **Tool Integration**: Custom tools to:
  - Create todos from a list of step descriptions
  - Mark todos complete with completion notes
- **Agent Loop**: Runs until the model finishes without further tool calls
- **Rich Console Output**: Formatted todo lists and completion notes using Rich markup
- **Structured Problem Solving**: Breaks down problems (including estimating missing values) and works through them sequentially

### How It Works

1. Receives a user problem via a system + user message
2. Uses GPT-5.2 with function-calling tools (`create_todos`, `mark_complete`)
3. Plans steps, executes them one by one, and marks each todo complete
4. Returns the final solution in Rich console markup

### Requirements

- OpenAI API key (via `.env`)
- `openai`
- `python-dotenv`
- `rich`

### Usage

Run the script (e.g. as a notebook-style Python file). The agent will plan todos, execute them through the loop, and print the solution. Customize `user_message` and `system_message` to change the problem or behavior.
