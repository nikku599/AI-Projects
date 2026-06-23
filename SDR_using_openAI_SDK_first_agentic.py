# %%
from dotenv import load_dotenv
from agents import Agent, Runner, trace, function_tool
from openai.types.responses import ResponseTextDeltaEvent
from typing import Dict
import os
import asyncio

# %%
load_dotenv(override=True)

# %%
instructions1 = "You are a sales agent working for ComplAI, \
a company that provides a SaaS tool for ensuring SOC2 compliance and preparing for audits, powered by AI. \
You write professional, serious cold emails."

instructions2 = "You are a humorous, engaging sales agent working for ComplAI, \
a company that provides a SaaS tool for ensuring SOC2 compliance and preparing for audits, powered by AI. \
You write witty, engaging cold emails that are likely to get a response."

instructions3 = "You are a busy sales agent working for ComplAI, \
a company that provides a SaaS tool for ensuring SOC2 compliance and preparing for audits, powered by AI. \
You write concise, to the point cold emails."

# %%
sales_agent1 = Agent(
        name="Professional Sales Agent",
        instructions=instructions1,
        model="gpt-4o-mini"
)

sales_agent2 = Agent(
        name="Engaging Sales Agent",
        instructions=instructions2,
        model="gpt-4o-mini"
)

sales_agent3 = Agent(
        name="Busy Sales Agent",
        instructions=instructions3,
        model="gpt-4o-mini"
)

# %%
description = "Write a cold sales email"

tool1 = sales_agent1.as_tool(tool_name="sales_agent1", tool_description=description)
tool2 = sales_agent2.as_tool(tool_name="sales_agent2", tool_description=description)
tool3 = sales_agent3.as_tool(tool_name="sales_agent3", tool_description=description)

# %%
from IPython.display import Markdown

@function_tool
def show_the_best_email_tool(best_email : str):
    display(Markdown("Inside the show_best_email_tool\n\n"))
    display(Markdown(best_email))
    return {"status":"success"}


# %%
tools = [tool1, tool2, tool3, show_the_best_email_tool]

# %%
instructions = """
You are a Sales Manager at ComplAI. Your goal is to find the single best cold sales email using the sales_agent tools.
 
Follow these steps carefully:
1. Generate Drafts: Use all three sales_agent tools to generate three different email drafts. Do not proceed until all three drafts are ready.
 
2. Evaluate and Select: Review the drafts and choose the single best email using your judgment of which one is most effective.

3. use show_the_best_email_tool to show the best email you selected.

4. Do not call the tools more than once
 
Crucial Rules:
- You must use the sales agent tools to generate the drafts — do not write them yourself.
- you must return only one email and not more than one email
- Do not use show_the_best_email_tool if any output_guardrail tripwire
"""


# sales_manager = Agent(name="Sales Manager", instructions=instructions, tools=tools, model="gpt-4o-mini")

# message = "Send a cold sales email addressed to 'Dear CTO'"

# with trace("Sales manager"):
#     result = await Runner.run(sales_manager, message)

# %%
#putting guardrails

from agents import GuardrailFunctionOutput, output_guardrail
from pydantic import BaseModel

class no_placeholder_check(BaseModel):
    is_placeholder_in_email : bool
    placeholder : str

guardrail_agent = Agent(
    "placeholder check",
    instructions="Check if any placeholder (like [Your Name]) is present in email",
    output_type=no_placeholder_check,
    model="gpt-4o-mini"
)

@output_guardrail
async def guardrail_against_placeholder(ctx, agent, message):
    result = await Runner.run(guardrail_agent, message, context=ctx.context)
    is_placeholder_in_email = result.final_output.is_placeholder_in_email
    return GuardrailFunctionOutput(output_info={"found_placeholder": result.final_output}, tripwire_triggered=is_placeholder_in_email)


# %%
careful_sale_manager = Agent(
    "careful sales manager",
    instructions=instructions,
    tools=tools,
    output_guardrails=[guardrail_against_placeholder],
    model="gpt-4o-mini"
)

message = "Write a cold sales email addressed to CEO of google"

with trace("Automated SDR with output guardrail"):
    result = await Runner.run(careful_sale_manager, message)

# %%



