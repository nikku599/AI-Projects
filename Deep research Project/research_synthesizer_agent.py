from pydantic import BaseModel, Field
from agents import Agent


INSTRUCTIONS = """
You are an expert Research Synthesizer Agent.

Your responsibility is to transform verified research findings into a
well-organized knowledge structure that can be directly consumed by a
Report Writer Agent.

You are NOT responsible for writing the final report.

Given a collection of verified findings:

1. Group related findings into logical themes and sections.
2. Remove duplicate information while preserving important details.
3. Merge evidence from multiple sources into cohesive insights.
4. Highlight important trends, patterns, relationships, and causal factors.
5. Preserve supporting evidence that may be useful to the report writer.
6. Clearly identify contradictions, disagreements, and alternative viewpoints.
7. Distinguish between:
   - Verified facts
   - Expert opinions
   - Estimates
   - Uncertainties
8. Identify research gaps or areas where evidence is weak.
9. Organize information in a way that makes report generation easy.
10. Do not invent information or draw unsupported conclusions.

The output should be highly structured, information-dense, and optimized
for downstream report generation.

Do NOT write introductions, conclusions, executive summaries, or
recommendations. Focus on organizing and synthesizing knowledge.
"""


class ResearchInsight(BaseModel):
    title: str = Field(
        description="Short title summarizing the insight."
    )
    summary: str = Field(
        description="Detailed synthesized explanation of the insight."
    )
    supporting_evidence: list[str] = Field(
        description="Evidence supporting the insight."
    )


class ResearchSection(BaseModel):
    section_title: str = Field(
        description="Logical section name."
    )
    key_points: list[str] = Field(
        description="Important findings in this section."
    )
    insights: list[ResearchInsight] = Field(
        description="Synthesized insights for this section."
    )


class ContradictoryView(BaseModel):
    topic: str = Field(
        description="Topic where disagreement exists."
    )
    viewpoints: list[str] = Field(
        description="Different competing viewpoints."
    )
    explanation: str = Field(
        description="Explanation of why disagreement exists."
    )


class SynthesizedResearch(BaseModel):
    research_topic: str = Field(
        description="Original research topic."
    )
    sections: list[ResearchSection] = Field(
        description="Organized research sections."
    )
    contradictions: list[ContradictoryView] = Field(
        description="Conflicting findings and viewpoints."
    )
    research_gaps: list[str] = Field(
        description="Areas requiring additional research."
    )
    important_takeaways: list[str] = Field(
        description="Most important verified findings."
    )


research_synthesizer_agent = Agent(
    name="ResearchSynthesizerAgent",
    instructions=INSTRUCTIONS,
    model="gpt-5.5",
    output_type=SynthesizedResearch,
)