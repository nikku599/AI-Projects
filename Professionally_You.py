# %%
from dotenv import load_dotenv
from openai import OpenAI
import os
import requests
import json
from pypdf import PdfReader
import gradio as gr


load_dotenv(override=True)
openai = OpenAI()


# %%
# For pushover

pushover_user = os.getenv("PUSHOVER_USER")
pushover_token = os.getenv("PUSHOVER_TOKEN")
pushover_url = "https://api.pushover.net/1/messages.json"

if pushover_user:
    print(f"Pushover user found and starts with {pushover_user[0]}")
else:
    print("Pushover user not found")

if pushover_token:
    print(f"Pushover token found and starts with {pushover_token[0]}")
else:
    print("Pushover token not found")

# %%

def push(message):
    data = {
        "token": pushover_token,
        "user": pushover_user,
        "message": message
    }
    requests.post(pushover_url, data=data)

# %%
def record_user_details(email, name="Name not provided", notes="not provided"):
    push(f"Recording interest from {name} with email {email} and notes {notes}")
    return {"recorded" : "ok"}

def record_unknown_question(question):
    push(f"Recording unknown question: {question}")
    return {"recorded" : "ok"}


# %%
record_user_details_json = {
    "name": "record_user_details",
    "description": "Use this tool to record that a user is interested in being in touch and provided an email address",
    "parameters": {
        "type": "object",
        "properties": {
            "email": {
                "type": "string",
                "description": "The email address of this user"
            },
            "name": {
                "type": "string",
                "description": "The user's name, if they provided it"
            }
            ,
            "notes": {
                "type": "string",
                "description": "Any additional information about the conversation that's worth recording to give context"
            }
        },
        "required": ["email"],
        "additionalProperties": False
    }
}

# %%
record_unknown_question_json = {
    "name": "record_unknown_question",
    "description": "Use this tool to record that a user asked an unknown question",
    "parameters": {
        "type": "object",
        "properties": {
            "question": {
                "type": "string",
                "description": "The question that the user asked"
            }
        },
        "required": ["question"],
        "additionalProperties": False
    }
}

# %%
tools = [{"type": "function", "function": record_user_details_json}, {"type": "function", "function": record_unknown_question_json}]

# %%
tools

# %%
def handle_tool_calls(tool_calls):
    results = []
    for tool_call in tool_calls:
        tool_name = tool_call.function.name
        tool_args = json.loads(tool_call.function.arguments)
        tool = globals().get(tool_name)
        result = tool(**tool_args) if tool else {}
        results.append({"role": "tool", "content": json.dumps(result), "tool_call_id": tool_call.id})
    return results


# %%
reader = PdfReader("me/linkedin.pdf")
linkedin = ""
for page in reader.pages:
    text = page.extract_text()
    if text:
        linkedin += text

with open("me/summary.txt", "r", encoding="utf-8") as f:
    summary = f.read()

name = "Nikhil Sharma"

# %%
system_prompt = f"You are acting as {name}. You are answering questions on {name}'s website, \
particularly questions related to {name}'s career, background, skills and experience. \
Your responsibility is to represent {name} for interactions on the website as faithfully as possible. \
You are given a summary of {name}'s background and LinkedIn profile which you can use to answer questions. \
Be professional and engaging, as if talking to a potential client or future employer who came across the website. \
If you don't know the answer to any question, use your record_unknown_question tool to record the question that you couldn't answer, even if it's about something trivial or unrelated to career. \
If the user is engaging in discussion, try to steer them towards getting in touch via email; ask for their email and record it using your record_user_details tool. "

system_prompt += f"\n\n## Summary:\n{summary}\n\n## LinkedIn Profile:\n{linkedin}\n\n"
system_prompt += f"With this context, please chat with the user, always staying in character as {name}."


# %%
def chat(message, history):
    messages = [{"role": "system", "content": system_prompt}] + history + [{"role": "user", "content": message}]
    done = False
    while not done:
        response = openai.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages,
            tools=tools,
            tool_choice="auto",
            max_tokens=1000
        )
        finish_reason = response.choices[0].finish_reason
        if finish_reason == "tool_calls":
            tool_calls = response.choices[0].message.tool_calls
            results = handle_tool_calls(tool_calls)
            messages.append(response.choices[0].message)
            messages.extend(results)
        else:
            done = True
    return response.choices[0].message.content

# %%
messages=[{"role": "system", "content": system_prompt}] + [{"role": "system", "content": "Make sure to ask the email id to get in touch as well"}]
initial_response = openai.chat.completions.create(
    model="gpt-4o-mini",
    messages=messages,
    max_tokens=1000
)
initial_content = initial_response.choices[0].message.content
chatbot = gr.Chatbot(value=[{"role":"assistant", "content":initial_content}], type="messages")
gr.ChatInterface(chat, chatbot=chatbot, type="messages").launch()

# %%



