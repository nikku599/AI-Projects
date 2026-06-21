# AI-Projects
This repo is for AI projects build by me

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
