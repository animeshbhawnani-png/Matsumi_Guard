from fastapi import APIRouter, HTTPException

from schemas.requests import AnalyzeTransactionRequest
from schemas.responses import AnalyzeTransactionResponse
from services.risk_engine import analyze_transaction


router = APIRouter(tags=["Transactions"])


@router.post("/analyzeTransaction", response_model=AnalyzeTransactionResponse)
async def analyze_transaction_route(payload: AnalyzeTransactionRequest):
    """
    Analyze a Cardano transaction for risk & compliance.
    """
    try:
        result = await analyze_transaction(
            tx_hash=payload.txHash,
            wallet_address=payload.walletAddress,
            metadata=payload.metadata or {},
        )
        return result
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error analyzing transaction: {str(e)}"
        )


