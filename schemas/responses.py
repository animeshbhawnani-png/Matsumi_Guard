from typing import Dict, List

from pydantic import BaseModel, Field


class AnalyzeTransactionResponse(BaseModel):
    txHash: str = Field(..., description="Cardano transaction hash")
    complianceScore: int = Field(..., ge=0, le=100, description="0-100 score")
    riskLevel: str = Field(..., description="Risk level: Low, Medium, High")
    issues: List[str] = Field(default_factory=list, description="List of detected issues")
    recommendations: List[str] = Field(
        default_factory=list, description="Recommended next actions"
    )
    riskBreakdown: Dict[str, int] = Field(
        default_factory=dict,
        description="Per-factor risk points contributing to the final score",
    )


class AnalyzeWalletResponse(BaseModel):
    walletAddress: str = Field(..., description="Cardano wallet address")
    complianceScore: int = Field(..., ge=0, le=100, description="0-100 score")
    riskLevel: str = Field(..., description="Risk level: Low, Medium, High")
    issues: List[str] = Field(default_factory=list, description="List of detected issues")
    recommendations: List[str] = Field(
        default_factory=list, description="Recommended next actions"
    )
    riskBreakdown: Dict[str, int] = Field(
        default_factory=dict,
        description="Per-factor risk points contributing to the final score",
    )


