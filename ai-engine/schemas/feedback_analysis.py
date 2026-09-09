from typing import List, Optional

from pydantic import BaseModel, Field


class FeedbackAnalysis(BaseModel):

    summary: str

    customer_problem: str

    affected_feature: str

    issue: str

    sentiment: str

    intent: str

    severity: str

    customer_impact: str

    business_impact: Optional[str] = None

    root_cause_hypothesis: Optional[str] = None

    evidence: List[str] = Field(default_factory=list)

    priority: str

    recommended_solution: str

    development_action: str

    product_action: Optional[str] = None

    engineering_action: Optional[str] = None

    support_action: Optional[str] = None

    expected_outcome: Optional[str] = None

    confidence: float