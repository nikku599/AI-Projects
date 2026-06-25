from pydantic import BaseModel, Field
from agents import Agent


INSTRUCTIONS = """
You are an expert Fact Verification Agent.

Your job is to verify research findings produced by other agents.

Given a collection of claims, evidence, and sources:

1. Determine whether each claim is:
   - Verified
   - Partially Verified
   - Contradicted
   - Insufficient Evidence

2. Evaluate the quality and credibility of the supporting evidence.

3. Look for:
   - Missing evidence
   - Unsupported assumptions
   - Contradictory information
   - Outdated information
   - Potential hallucinations

4. Assign a confidence score:
   - High
   - Medium
   - Low

5. Explain your reasoning briefly and clearly.

6. Be conservative.
   If evidence is weak, conflicting, or insufficient,
   do not mark the claim as verified.

7. Focus on factual accuracy rather than writing quality.

Return only structured verification results.
"""


class VerificationResult(BaseModel):
    claim: str = Field(
        description="The claim being verified."
    )
    verdict: str = Field(
        description="One of: Verified, Partially Verified, Contradicted, Insufficient Evidence."
    )
    confidence: str = Field(
        description="One of: High, Medium, Low."
    )
    reasoning: str = Field(
        description="Explanation for the verdict."
    )
    supporting_evidence: list[str] = Field(
        description="Evidence supporting the verdict."
    )
    issues_found: list[str] = Field(
        description="Potential issues, contradictions, or missing evidence."
    )


class VerificationReport(BaseModel):
    results: list[VerificationResult] = Field(
        description="Verification results for all claims."
    )


fact_verification_agent = Agent(
    name="FactVerificationAgent",
    instructions=INSTRUCTIONS,
    model="gpt-5.5",
    output_type=VerificationReport,
)