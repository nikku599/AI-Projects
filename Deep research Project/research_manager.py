from agents import Runner, trace, gen_trace_id
from search_agent import search_agent
from planner_agent import planner_agent, WebSearchItem, WebSearchPlan
from fact_verification_agent import fact_verification_agent
from research_synthesizer_agent import research_synthesizer_agent
from writer_agent import writer_agent, ReportData
import asyncio


class ResearchManager:

    async def run(self, query: str):
        """
        Full deep research pipeline:
        planning → searching → verification → synthesis → writing
        """
        trace_id = gen_trace_id()

        with trace("Deep Research Pipeline", trace_id=trace_id):

            trace_url = f"https://platform.openai.com/traces/trace?trace_id={trace_id}"
            print(f"Trace: {trace_url}")
            yield f"Trace link: {trace_url}"

            # 1. Planning
            yield "Step 1/5: Planning search strategy..."
            search_plan = await self.plan_searches(query)

            # 2. Searching
            yield f"Step 2/5: Running {len(search_plan.searches)} searches..."
            search_results = await self.perform_searches(search_plan)

            # 3. Fact Verification
            yield "Step 3/5: Verifying facts..."
            verified_data = await self.verify_facts(query, search_results)

            # 4. Synthesis
            yield "Step 4/5: Synthesizing research..."
            synthesized_data = await self.synthesize_research(query, verified_data)

            # 5. Writing Report
            yield "Step 5/5: Writing final report..."
            report = await self.write_report(query, synthesized_data)

            yield "Completed successfully."
            yield report.markdown_report

    # -----------------------
    # 1. PLANNING
    # -----------------------
    async def plan_searches(self, query: str) -> WebSearchPlan:
        result = await Runner.run(
            planner_agent,
            f"User Query: {query}",
        )
        return result.final_output_as(WebSearchPlan)

    # -----------------------
    # 2. SEARCHING
    # -----------------------
    async def perform_searches(self, search_plan: WebSearchPlan) -> list[str]:
        tasks = [
            asyncio.create_task(self.search(item))
            for item in search_plan.searches
        ]

        results = []
        for task in asyncio.as_completed(tasks):
            res = await task
            if res:
                results.append(res)

        return results

    async def search(self, item: WebSearchItem) -> str | None:
        try:
            result = await Runner.run(
                search_agent,
                f"Search Query: {item.query}\nReason: {item.reason}",
            )
            return str(result.final_output)
        except Exception as e:
            print(f"Search failed: {e}")
            return None

    # -----------------------
    # 3. FACT VERIFICATION
    # -----------------------
    async def verify_facts(self, query: str, search_results: list[str]):
        """
        Send raw search results to verification agent
        for claim-level validation.
        """
        input_text = f"""
Original Query:
{query}

Collected Search Results:
{search_results}
"""

        result = await Runner.run(
            fact_verification_agent,
            input_text,
        )

        return result.final_output

    # -----------------------
    # 4. SYNTHESIS
    # -----------------------
    async def synthesize_research(self, query: str, verified_data):
        """
        Convert verified facts into structured research knowledge.
        """
        input_text = f"""
Original Query:
{query}

Verified Research Data:
{verified_data}
"""

        result = await Runner.run(
            research_synthesizer_agent,
            input_text,
        )

        return result.final_output

    # -----------------------
    # 5. WRITING
    # -----------------------
    async def write_report(self, query: str, synthesized_data: str) -> ReportData:
        """
        Generate final report from structured synthesis.
        """
        input_text = f"""
Original Query:
{query}

Synthesized Research:
{synthesized_data}
"""

        result = await Runner.run(
            writer_agent,
            input_text,
        )

        return result.final_output_as(ReportData)